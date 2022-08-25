# Cheat Sheet Tech Lead

> A team Lead is not about being on the top in term of hierarchy, but at the front of the team,  like a leader of adventure, when there is a blocker, you need to jump in and unblock the, and direct the team to the right direction.

> Act as a shepherd, looking after the team and steer them loosely in the right direction, rather than enforcing all my idea.
> -- Jon Pither, Talking With Tech Leads

It's not about the end goal, it is all about the journey, so enjoy the day.

Tech Lead brings value by

1. enabling everyone on the team to contribute code as much as possible
1. by avoiding rewrites due to people working in different ways
1. by managing tech debt to make it easier to add code
1. by promoting relationships between the development group and business colleagues to ensure the code addresses business goals and delivers true value

## How to run stand up?

1. open jira
1. yesterday
1. meetings for today
1. today
1. going through the tickets in the jira board person by person
   1. keep jira board up to date
   1. discuss progress
   1. identify blockers
1. anything else that's not in jira, but try our best to capture all works in jira tickets

## PLANNING sprint planning checklist

- [ ] announce public holidays
- [ ] ask if anyone has holiday plan
- [ ] open jira
- [ ] going through current sprint person by person
- [ ] pull in tickets from groomed tickets in backlog
- [ ] plan for next sprint by BE, iOS, Android, Data Science, QA...
  - [ ] estimate tickets
  - [ ] pull in tickets for the next sprint
- [ ] write down sprint goal
  - [ ] goal for each BE
  - [ ] goal for iOS
  - [ ] goal for Android
  - [ ] goal for Data Science
  - [ ] goal for QA
  - [ ] goal for Product
  - [ ] cutoff for release date
  - [ ] release date

**Reminder**

- count **Estimates** to have realistic goal for sprint

## REFINEMENT refinement checklist

- [ ] optional - designer explain upcoming project
- [ ] groom/explain ticket in the grooming section of backlog
  - the idea for refinement is for all of us to understand the tickets
- [ ] ask for bug tickets and tech debt tickets from developers want to do next sprint
- [ ] ask if there will be other tickets not in grooming yet from products, QA ...
- [ ] anything else?

Notes:

- No need to come up with estimate during refinements, estimates are required during planning

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

- A/B test required

h1. Analytics

h1. Design

h1. How To QA

Frontend Ticket: BDD
Backend Ticket: Endpoint + Expected Response

h1. Tech Notes

h1. Questions
```

## Estimates

- Number of days for one engineers, assuming no meetings

## Meetings

- Standup at 10:20 everyday
- Weekly Metrics Sync at 10:40 on Thursday
- Two Week Sprint
  - Week 1: Retrospective at 10:00 on Tuesday
  - Week 1: Refinement at 10:00 on Thursday
  - Week 2: Sprint Planning at 15:00 on Thursday

## API work flow

1. API Design Doc first
1. iOS & Android tickets
1. BE tickets

## ideals - tech

- 100% code coverage
- documentations
- strict typing
- comprehensible tickets

## ideals - behaviour

- jira
  - all ongoing tasks should be in Jira
  - breakdown large tasks into subtasks in Jira board
  - initial estimates needs to be accurate, spend time thinking about estimates after refinement and before planning
- Before Standup
  - 🔎 Focus on 3 most important things on each day
  - 🎉 Prepare at least one celebration
- My role is to remove obstacles, manage the stakeholders, and clear a path to incrementally improve the system. In return I expected everyone to be professional, speak out when they felt things weren't right, and respect the ideas of shared ownership.
- If I am doing my job right, you should not feel my existence.
- I consider myself a facilitator instead of a leader.
- Only needs to do 3 things:
  1. Provide (training, motivation, resources, opportunities, etc.)
  1. Remove (blockers, confusion, politics)
  1. Get Out Of The Way.
- Bring Positive Energy! Celebrate wins!
- Need to be realistic on deliverables
- to tell the team in stand-up
  - `Thursday: planning today, spend sometime to understand the tickets from backlog or refinement and think about the estimate before planning`
  - `Friendly Reminder: We have refinement today, have a think about any tech debt and bug tickets that you want to discuss and bring into next sprint.`
- Ticket Template
  - Description
  - Acceptance Criteria
    - A/B test required
  - Analytics
  - Design
  - How To QA
    - Frontend Ticket: BDD
    - Backend Ticket: Endpoint + Expected Response
  - Tech Notes
  - Questions

## PRODUCT_MANAGER Topics for 1 on 1 with Product Manager

- [ ] What tickets / work are coming up in the sprint planning ?
  - so that I can prepare the tickets for the next sprint and not be surprised if the priority suddenly changed
- [ ] What tickets / work are coming up in the refinement?
- Team delivery / performance
- Feedbacks
- Blockers
- Ongoing Issues
- Ongoing Experiments A/B tests

## Estimates

We changed the estimate to original estimate because he suggest not to change estimate to remaining estimate

- the estimate should the estimate of the entire work even if it spanned multiple sprints
- it averages out into an average *velocity*
- we can use comments on ticket if needed to indicate whats left or just team understanding even if it says 8 there's not 8 left to do but leave JIRA as 8

*Some comments regarding velocity*

We are not using velocity in the squad but it is average amount of story points we can do per sprint in the squad.

For example in the following sprint we agree 32 number of story points and during the week the remaining story points should slowly drop down to zero, in burndown chart.

Then if for the next 3 sprints, we are completing 30, 33, 31 story points the we can say our (average) velocity is 32.
Velocity is useful to know what's the realistic amount of tickets / work we can do per sprint.

## NEW_EPIC_TICKETS Required tickets for each project

- [ ] Add Epic ticket for project
- [ ] QA: BDD senarios
- [ ] BE, iOS, Android: Heimdall
- [ ] Spike BE, iOS, Android: Breakdown tickets with estimates
- [ ] BE, iOS, Android: spikes for uncertainties

## IN_OFFICE

- [ ] check if all meetings has meeting room
- [ ] print checklist

## STANDUP - Standup template

- Standup - Yesterday

### TODOs - tickets <leader>ij

- 🔍 1 -
- 🔍 2 -
- 🔍 3 -

### Meetings - <leader>ia

### Others

## SCRUM_OF_SCRUMS - scrum of scrums template

### SoS - Update of the sprint that affects other teams

### Are there new obstacle / Blockers?

### Things that might affect our teams
