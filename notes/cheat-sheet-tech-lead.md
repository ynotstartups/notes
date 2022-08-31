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

## RUNNING_STANDUP - How to run stand up?

1. open jira
1. yesterday
1. meetings for today
1. today
1. going through the tickets in the jira board person by person
   1. keep jira board up to date
   1. discuss progress
   1. identify blockers
1. anything else that's not in jira, but try our best to capture all works in jira tickets

## RUNNING_RETRO - How to run stand up?

1. open miro board
1. setup a 5 minutes timer for the team to add topics
1. group tickets in similar theme
1. discuss tickets in sections
1. setup vote for star of the sprint

## PLANNING sprint planning checklist

- planning check list
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

## TICKET_TEMPLATE_GENERIC_TICKET - Jira Ticket Template

```
h1. Description

h1. Acceptance Criteria

- A/B test required

h1. Analytics

h1. Design

- see link in Epic

h1. How To QA

Frontend Ticket: BDD
Backend Ticket: Endpoint + Expected Response

h1. Tech Notes
```

## TICKET_TEMPLATE_BDD - BDD Ticket Template

```
h1. Description

In order to effectively test the behaviour, we need to have a BDD test suite.

h1. Tech Notes

Please see repo `app-bdd-scenarios`
```

## TICKET_TEMPLATE_BE_EXPERIMENT_CLEAN_UP - Experiment Clean Up Ticket Template

```
h1. Description

Please see LystOS to check if we want to keep or remove this flag.

h1. Acceptance Criteria

- remove flag from configuration
- remove flag from LystOS
- remove relevant code
```

## TICKET_TEMPLATE_ANALYTICS_REQUIREMENT - Product Analytics Requirement Ticket Template

```
h1. Acceptance Criteria

- add analytics

h1. Example

When something happens, the app should send analytics event with *key* ?? and *value* ??
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

## API_WORKFLOW

1. Draft API Design Doc
1. setup meeting with FE to discuss API
1. iOS & Android ticket to agree on API

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

## PRODUCT_MANAGER - Topics for 1 on 1 with Product Manager

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

## NEW_PROJECT_TICKETS Required tickets for each project

- [ ] Add Epic Ticket for project
- [ ] QA: BDD senarios
- [ ] BE, iOS, Android: Heimdall
- [ ] BE, iOS, Android: Heimdall Cleanup
- [ ] BE, iOS, Android: Breakdown tickets with estimates
- [ ] BE, iOS, Android: spikes for uncertainties

## IN_OFFICE

- [ ] check if all meetings has meeting room
- [ ] print checklist

## STANDUP - Standup template

- 🎉 celebrate
- 🔍 1 focus on
- 🔍 2 focus on
- 🔍 3 focus on

## SCRUM_OF_SCRUMS - scrum of scrums template

- Scrum of Scrums
  - Update of the sprint that affects other teams
  - Are there new obstacle / Blockers?
  - Things that might affect our teams

## TECH_SYNC - tech sync template

- [ ] what are the technological unknowns that we have?
- [ ] what are the confusing flow that we have?
- [ ] reminder to break down tickets and add estimates

## LEAD_SYNC - product and tech lead sync template

- [ ] what is the priority for the next sprint?
- [ ] what are the tickets that we have for the next sprint?
- [ ] what are the priority for the sprint after next sprint?
- [ ] Any upcoming works we should be aware of?
