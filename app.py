import streamlit as st
from dataclasses import dataclass
from typing import List


# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered",
)


# -----------------------------
# Simple data model
# -----------------------------
@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    category: str


PRIORITY_SCORE = {
    "high": 3,
    "medium": 2,
    "low": 1,
}


def build_schedule(tasks: List[Task], time_available: int) -> List[Task]:
    """
    Very simple scheduler:
    - Sort by priority first
    - Then shorter tasks first
    - Add tasks until time runs out
    """
    sorted_tasks = sorted(
        tasks,
        key=lambda task: (-PRIORITY_SCORE[task.priority], task.duration_minutes, task.title.lower())
    )

    plan = []
    used_time = 0

    for task in sorted_tasks:
        if used_time + task.duration_minutes <= time_available:
            plan.append(task)
            used_time += task.duration_minutes

    return plan


def explain_plan(plan: List[Task], total_time: int) -> List[str]:
    explanations = []
    running_time = 0

    for task in plan:
        running_time += task.duration_minutes
        explanations.append(
            f"**{task.title}** was chosen because it is a **{task.priority} priority** "
            f"{task.category} task and fits within today's available time. "
            f"Time used after this task: **{running_time}/{total_time} min**."
        )

    return explanations


# -----------------------------
# Session state
# -----------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "generated_plan" not in st.session_state:
    st.session_state.generated_plan = []


# -----------------------------
# Custom styling
# -----------------------------
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 780px;
        }

        h1, h2, h3 {
            letter-spacing: -0.02em;
        }

        .hero-card {
            padding: 1.4rem 1.4rem 1rem 1.4rem;
            border-radius: 22px;
            background: linear-gradient(135deg, #ffffff 0%, #f7f9fc 100%);
            border: 1px solid rgba(0,0,0,0.06);
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            margin-bottom: 1.2rem;
        }

        .mini-label {
            font-size: 0.85rem;
            color: #6b7280;
            margin-bottom: 0.25rem;
        }

        .stat-card {
            padding: 1rem 1.1rem;
            border-radius: 18px;
            background: #fafafa;
            border: 1px solid rgba(0,0,0,0.06);
            text-align: center;
        }

        .task-card {
            padding: 0.95rem 1rem;
            border-radius: 18px;
            background: white;
            border: 1px solid rgba(0,0,0,0.06);
            box-shadow: 0 6px 18px rgba(0,0,0,0.04);
            margin-bottom: 0.7rem;
        }

        .section-space {
            margin-top: 1.2rem;
            margin-bottom: 0.6rem;
        }

        div.stButton > button {
            width: 100%;
            border-radius: 14px;
            padding: 0.65rem 1rem;
            font-weight: 600;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Header / hero
# -----------------------------
st.markdown(
    """
    <div class="hero-card">
        <div class="mini-label">Daily pet care planning</div>
        <h1 style="margin:0;">🐾 PawPal+</h1>
        <p style="margin-top:0.55rem; color:#4b5563; font-size:1rem;">
            A simple assistant that helps pet owners choose the most important care tasks
            for the day based on priority and available time.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Owner + pet info
# -----------------------------
st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
st.subheader("Owner & Pet")

col1, col2 = st.columns(2)
with col1:
    owner_name = st.text_input("Owner name", value="Jordan")
    pet_name = st.text_input("Pet name", value="Mochi")
with col2:
    species = st.selectbox("Species", ["dog", "cat", "other"])
    time_available = st.slider("Time available today (minutes)", 15, 240, 60, step=15)


# -----------------------------
# Add tasks
# -----------------------------
st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
st.subheader("Add Tasks")

task_col1, task_col2 = st.columns(2)
with task_col1:
    task_title = st.text_input("Task title", value="Morning walk")
    task_category = st.selectbox(
        "Category",
        ["Walk", "Feeding", "Medication", "Enrichment", "Grooming", "Training", "Other"]
    )
with task_col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    priority = st.selectbox("Priority", ["high", "medium", "low"])

add_col1, add_col2 = st.columns([2, 1])
with add_col1:
    if st.button("Add task"):
        clean_title = task_title.strip()
        if clean_title:
            st.session_state.tasks.append(
                Task(
                    title=clean_title,
                    duration_minutes=int(duration),
                    priority=priority,
                    category=task_category,
                )
            )
            st.success(f"Added '{clean_title}'")
        else:
            st.error("Task title cannot be empty.")
with add_col2:
    if st.button("Clear all"):
        st.session_state.tasks = []
        st.session_state.generated_plan = []
        st.success("All tasks cleared.")


# -----------------------------
# Current tasks
# -----------------------------
st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
st.subheader("Today’s Task List")

if st.session_state.tasks:
    total_task_time = sum(task.duration_minutes for task in st.session_state.tasks)

    stat1, stat2, stat3 = st.columns(3)
    with stat1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="mini-label">Tasks</div>
                <div style="font-size:1.6rem; font-weight:700;">{len(st.session_state.tasks)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with stat2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="mini-label">Total minutes</div>
                <div style="font-size:1.6rem; font-weight:700;">{total_task_time}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with stat3:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="mini-label">Available today</div>
                <div style="font-size:1.6rem; font-weight:700;">{time_available}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")

    for i, task in enumerate(st.session_state.tasks, start=1):
        st.markdown(
            f"""
            <div class="task-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <div style="font-weight:700; font-size:1rem;">{i}. {task.title}</div>
                        <div style="color:#6b7280; font-size:0.92rem;">
                            {task.category} • {task.duration_minutes} min • {task.priority.capitalize()} priority
                        </div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.info("No tasks yet. Add a few to build today’s plan.")


# -----------------------------
# Generate schedule
# -----------------------------
st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
st.subheader("Generate Daily Plan")

if st.button("Create today’s plan"):
    if not st.session_state.tasks:
        st.warning("Add at least one task first.")
    else:
        plan = build_schedule(st.session_state.tasks, time_available)
        st.session_state.generated_plan = plan


# -----------------------------
# Display generated plan
# -----------------------------
if st.session_state.generated_plan:
    st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
    st.subheader(f"{pet_name}’s Plan for Today")

    used_time = 0
    for idx, task in enumerate(st.session_state.generated_plan, start=1):
        start_time = used_time
        end_time = used_time + task.duration_minutes
        used_time = end_time

        st.markdown(
            f"""
            <div class="task-card">
                <div style="font-weight:700; font-size:1rem;">{idx}. {task.title}</div>
                <div style="color:#6b7280; font-size:0.92rem; margin-top:0.2rem;">
                    {task.category} • {task.duration_minutes} min • {task.priority.capitalize()} priority
                </div>
                <div style="margin-top:0.45rem; font-size:0.95rem;">
                    Scheduled from <strong>{start_time} min</strong> to <strong>{end_time} min</strong>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Why this plan?")
    for reason in explain_plan(st.session_state.generated_plan, time_available):
        st.markdown(f"- {reason}")

    skipped_tasks = [
        task for task in st.session_state.tasks
        if task not in st.session_state.generated_plan
    ]

    if skipped_tasks:
        st.markdown("### Tasks not included today")
        for task in skipped_tasks:
            st.markdown(
                f"- **{task.title}** was skipped because there was not enough time after higher-priority tasks were scheduled."
            )