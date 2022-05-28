# Cheat Sheet Tech Lead

A team Lead is not about being on the top in term of hierarchy, but at the front of the team,  like a leader of adventure, when there is a blocker, you need to jump in and unblock the, and direct the team to the right direction.

It's not about the end goal, it is all about the journey, just enjoy the day.

Tech Lead brings value by

1. enabling everyone on the team to contribute code as much as possible
1. by avoiding rewrites due to people working in different ways
1. by managing tech debt to make it easier to add code
1. by promoting relationships between the development group and business colleagues to ensure the code addresses business goals and delivers true value

## How to run stand-up?

1. open jira
1. going through the tickets in the jira board person by person
   1. keep jira board up to date
   1. discuss progress
   1. identify blockers
1. anything else that's not in jira, but try our best to capture all works in jira tickets

## How to run sprint planning?

1. open jira
1. going through current sprint person by person
1. pull in tickets from groomed tickets in backlog
1. plan for next sprint by BE, Design, iOS, Android, BI...
   - estimate tickets
   - pull in tickets for the next sprint

## How to run backlog refinement?

1. groom/explain ticket in the grooming section of backlog
   - the idea for refinement is for all of us to understand the tickets
1. raise bug tickets and tech debt tickets that developers want to do next sprint

Notes:

- no need to come up with estimate during refinements, estimates are required during planning

## Jira setup

- columns:
  - TO DO - selected tasks for current sprint
  - IN PROGRESS - in progress tasks
  - CODE REVIEW - opened PR and waiting for review
  - QA
  - DESIGN REVIEW - ticket first goes to QA for checking both functional and design and then it goes to the design review for PM and designers for the final gate check
  - DONE - completed

## Jira Ticket Template

```
h1. Description

h1. Acceptance Criteria

h1. Analytics

h1. Design

h1. Tech Notes

h1. Questions
```

## Estimates

- Number of days for one engineers, assuming no meetings

## Meetings

- Standup at 10:20 everyday
- Retrospective at 10:00 on Tuesday biweekly
- Sprint Planning at 15:00 on Thursday biweekly

## API work flow

1. API Design Doc first
1. FE tickets iOS & Android
1. BE tickets

## reminders

- all ongoing tasks should be in Jira
- breakdown large tasks into subtasks in Jira board
- initial estimates needs to be accurate, spend time thinking about estimates after refinement and before planning

## ideals

- 100% code coverage
- documentations
- strict typing
- comprehensible tickets

## topics for 1 on 1 with Product Manager

- What tickets / work are coming up in the next sprint?
  - so that I can prepare the tickets for the next sprint and not be surprised if the priority suddenly changed
- Team delivery / performance
- Feedbacks
- Blockers
