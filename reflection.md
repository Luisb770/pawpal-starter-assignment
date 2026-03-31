# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design included classes like Task, Pet, Owner, and Scheduler.
Each class had a clear role, where Task stored task info, and Scheduler handled building the daily plan.
**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---
Yes, my design changed during implementation to keep things simpler and easier to manage.
I reduced complexity by focusing mainly on Task and a scheduler function instead of over-engineering multiple classes.
## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
My scheduler considers time available, task duration, and task priority (high, medium, low).
I decided priority and time mattered most because they directly impact what can realistically be completed in a day.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---
The scheduler prioritizes high-priority tasks even if it skips several lower-priority ones.
This is reasonable because important pet care tasks should not be missed even if less important ones are delayed.

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI to help design the structure, improve the UI, and implement the scheduling logic.
The most helpful prompts were asking for cleaner designs, simpler logic, and step-by-step improvements.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

There were times I did not accept AI suggestions if they were too complex or unnecessary for the project.
I verified suggestions by testing the code myself and making sure it matched the project requirements.

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested that higher-priority tasks are selected first and that tasks do not exceed the available time.
These tests were important to ensure the scheduler behaves correctly and produces realistic plans.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---
I am fairly confident the scheduler works correctly for normal use cases.
If I had more time, I would test edge cases like empty task lists, equal priorities, and very limited time.

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with how clean and intuitive the UI turned out.
The app feels simple to use while still demonstrating meaningful logic.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would improve the scheduler by adding smarter ordering and user preferences.
I would also separate the logic into different files for better scalability

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One key thing I learned is that simple designs are often more effective than complex ones.
I also learned that AI is most useful when combined with your own judgment and testing.