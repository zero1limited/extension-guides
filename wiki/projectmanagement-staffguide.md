



# Deployments
Suggestions from meeting on Fri 12th Sep (Arron, Suz & Cal)

We offer different levels of 'deployment options' based on the client monthly committment, which can form part of a tiered package offering. i.e

**10 hour retainers**
- 1 deployment per month, carried out during the hours of 9am - 12pm

**20 hour retainers**
- Bi-weekly deployments, carried out during the hours of 9am - 12pm

**50 hour retainer**
Get a more customised release process, which they help to build using Teamwork forms 'Client questionanire. The Forms functionality in Teamwork has logic built in so the form can expand on a question based off the answer the client provides. 

Potential questions to include in the form (in no order)
- Would you like a fixed deployment schedule?
- How frequently would you like deployments?
- What is your deployment window? (this should include zero downtime deployments)
- Do you want to auto approve critical security patches?
- 
To be continued...

Once the client has completed the questionnaire the PM needs to set up custom automations in Teamwork 

**Managing tasks for deployments**
We already have a custom field 'Delivery formats' in each task that assignees can use to indicate they type of deployment process each task should take:

Delivery formats:
1. Zero downtime deployments
2. Downtime deployment 
3. Configuration
4. Consultancy
5. Emergency release

Each delivery type selected can trigger an automation, for example

1. **Zero downtime deployments** (These must be performed within the projects release window)
- When this delivery format is selected the task gets automatically tagged with 'Zero downtime deployment'
- When the task moves into the 'Ready for release' column, a Comment is automatically added to the task 'This work is ready for release. We dont anticipate their being any downtime, so we will perform this during your next release window'
- QA can have a filter in Teamwork that they check daily. Any tasks tagged with ZERO downtime that are in the 'Ready for release' column should be released that day.
- QA checks there are no other tags
- If there arent any, a tag can be created and the work can be deployed
- If there is another tag, identify the tagged work, identify the delivery format of the other work, when the other work is planned to be released and let the client know that this work will be deployed with, or after the tagged work. 
- Once the work has been deployed, QA then move the task to the 'Done' column which adds a 'Complete' tag. This automates a task comment 'This task has now been deployed.

2. **Downtime deployment** (These must be performed within the projects release window)
- When this delivery format is selected the task gets automatically tagged with 'Downtime deployment'
- When the task moves into the acceptance column QA will be prompted to check the Client questionnaire for the agreed deployment process
- When the task moves into the 'Ready for release' column, a Comment is automatically added to the task 'This work is ready for release. Unless otherwise instructed you should expect approximately 15 minutes downtime, please ensure your team are aware of this interruption. 

 **Action points from 27th Sep**
 - Arron to review and refine this https://docs.google.com/spreadsheets/d/1ksozw8Au7ANS7OdcYHyVzSBJ39DgIt1FDjmo7adrkNg/edit?gid=0#gid=0
 - Suz to ask Dave questions https://zero1.teamwork.com/#tasks/37825877?c=14633697





