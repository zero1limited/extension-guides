# Deployment Process

[TOC]

This is a guide on the deployment process for work on Mdoq instances

### Prerequisites 
- Make sure all your/the developers work is committed to git.
- Make sure the developer that did the work has given you an explanation of the work and confirmation if the work requires downtime in their handover comment on the ticket.

### Regression Testing

First step is to put the instance into regression testing.
1. Click the blue "I'm done" button in the bottom right corner of your instance.
2. Select a target branch. This will always be ```master```.
3. Wait for your commits to load. If it says your branch is behind master you'll have to git merge first and retry from step 1. If the git merge fails, follow: [Resolving Merge Conflicts](https://docs.mdoq.io/hc/en-gb/articles/9832737324561-Resolving-Merge-Conflicts)
4. Select which setting you want the instance to run. Normally you should leave it as Skip regression testing - **no**, Allow DB recreation - **yes**, Allow Code recreation - **yes**, Delete instance after merging - **yes**.
5. Select **yes** to "Ignore Uncommitted Work" if the option appears.
6. Click the "Proceed To Regression Testing" button.
7. Let the regression testing run. If it passes it will automatically continue to preparing for client approval. If it fails follow: https://wiki2.zero1.co.uk/docs/main/dept-quality-assurance#content-automated-regression-testing

### Manual QA Testing
This step is to test the work that was carried out.
1. Follow: https://wiki2.zero1.co.uk/docs/main/dept-quality-assurance#content-manual-qa
2. Remember to get client signoff on the ticket before moving the the next stage.

### Accept Approval

Once automated and manual QA is complete you can move onto accept approval to merge the work to master.
1. Click the blue "Accept Approval" button. This will open up the tag menu. It will give a list of commits and the tags.
2. Choose a tag to merge to master. Normally we go by 3.year.week.release-amount-in-week. So an example would be 3.2025.27.00, the next one in that week would be 3.2025.27.01 then 3.2025.27.02 etc. Then on a new week it would change to 3.2025.28.00
3. Click the blue "Create Deployment" button.
4. Watch it in the logs do the accept approval stage. Once this finishes your work will be tagged in master and your instance will start deleting.

### Deployment

Now you need to release the work to the live site.
1. Confirm if the work is downtime or zero downtime (this should be in the developer's handover comment).
2a. If its zero downtime you can do the release anytime before 3pm. Just let the client know in the task, then go to the production instance, click "perform release", select you tag, tick the zero downtime box and click the "release" button.
2b. If its downtime you'll have to organise a release time with the client. Standard downtime is 3 minutes. Once a time is organised, go to the production instance, click "perform release", select your tag and click the "release" button.
4. Monitor the release till completion, then check the live site to confirm your work is present. If the release fails notify developers in Slack via the client's Slack channel.
5. Once the release is complete, update the client in your task and then close the task. Tell them to raise a new ticket if they notice any issues.
6. The deployment process is now complete.

### Known Bugs
- If a release fails Mdoq will leave cache off. This needs to be double checked post-release to confirm the cache status is correct.
