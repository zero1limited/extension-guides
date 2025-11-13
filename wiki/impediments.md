# Impediments

## What are they? 
An impediment is something that is stopping you from progressing with the task in hand. 

## What to do if you have an impediment
1. Add a comment to the task fully detailing what is impeding you
2. Add an 'Impediment' tag to the task

## Automations

### 'Impediment' tag added
The automation 'Impediment tag added' will: 
- Add a task comment (which will notify all comment followers)
- Add the Project Manager as an assignee

 "We are currently impeded on this task, but rest assured that we are working hard to remove this 
 blocker."

 ### Impediment removed within 7 days
The automation 'Impediment removed within 7 days' will be triggered once the impediment tag has been removed, but only if the task is in any of the following columns: 
- Support
- Not Started
- In progress

 ### Impediment +7 days old (pulls it from the workload)
 The automation 'Impediment 7+ days old' will: 
- Add a task comment (which will notify all comment followers)
- Change the assignee to the Project Manager
- Add an Escalated tag
- Move the task to the prioritise column

 "Unfortunately we are still facing a blocker on this task. We are going to remove this from our current workload until we are able to progress. In the meantime your Project Manager will try to remove this impediment and will reschedule the work as soon as possible. "

 The project Manager should keep the task and take responsibiity for removing the blocker and rescheduling the work. If there is work on an instance the PM should ask the previous assignee to save any work to a git branch to free up the space for other work

 ### Impediment removed - needs re-prioritising and rescheduling
The automation 'Impediment removed - needs re-prioritising and rescheduling will be triggered once the impediment tag has been removed, but only if the task is in any of the following columns: 
- Prioritise
Which it should be, based on previous automations

Removing the tag will trigger the following comment to be added to the task (which the Product owner follows)

"Great news, the previous blocker has now been removed from this task. Unfortunately, as this task was previous pulled out of the workload, it will now need to be reprioritised and rescheduled. You can discuss this with your Project Manager on your next prioritisation call. 
If this is a business critical task please let your Project Manager know so it can be expedited."

The Project Manager can then assign the task back to the original assignee and discuss prioritisation with the client on the next call. 


 # AUTOMATIONS CURRENTLY IN TESTING
 See https://zero1.teamwork.com/app/tasks/38657053 for details