# Cron Health Check
This recommendation is applicable for all M2 sites.

## Pitch
The Magento cron is a task scheduler that runs tasks at specified internvals in the background. By running them in the background this allows the site to respond quicker and let the server deal with the task while the user does something else.
A good example is the Magento indexer, instead of indexing the product every time you save it in the admin (which could take a very long time), Magento does this in the background using the cron, allowing you to save products in seconds.
The benefits of running these tasks in the background, is balanced with a lack of visibility about any errors. There is no place in the Magento admin that gives you any detail about tasks that succeeded or failed.
Jobs may fail from time to time, but persistent failing can lead to critical issues such as payments not being processed.
This recommendation will:
- check your cron settings are inline with Magento's best practise 
- check for any jobs that are repeatidly failing
- check for any jobs that are taking an excessive amount of time

We will then generate a report, which may include further recommendations to fix any issues found.


## Process
### Who
Anyone with access to MDOQ

### Setup
This task requires a recent backup (within the last 24 hours). 
Ideally using test for the client, which may just involve recreating the DB.

1. Check they have a sanitized backup from the last 24 hours
2. If not run a sanitized backup
3. Change "Settings > Cron > Enabled" to "No" for the "TEST" instance
4. Synchonize "MySQL" for the instance.


### Instructions
1. Create a copy of this [file](https://docs.google.com/document/d/1d3Qn80Vkiy5wlh6cjQXov925OBceL_BSHESZcIK9J1I/edit?usp=sharing)

2. You will then need to log into the MAP and navigate to: stores > configuration > Advanced | System > Cron (Scheduled Tasks).
  Here you will see a list of groups starting with "Cron configuration options for group..."
  Please check the following values, for the groups Index, Default and Consumer you only need to check that specific value. For the group "3rd Party" you must check all the other values, the test can only pass if all meet the requirements.
   - group: the index group to check
   - setting: the name of the setting
   - check: checks to carry out to make sure the current value passes
   - check name: the name of the test/check to update in the report
   
|Group|Setting|Check|Check Name|
|:-|:-|:-|:-|
|Index|Generate Schedules Every|< 30|Cron Job Generation Interval|
|Index|Schedule Ahead for|< 30 and at least 2x "Generate Schedules Every"|Cron Job Schedule Ahead By|
|Index|Missed if Not Run Within|< 30|Cron Job Lifetime|
|Index|History Cleanup Every|>= 120 && < 14400|Cron History Clean Up|
|Index|Success History Lifetime|> 30|Cron Success History|
|Index|Failure History Lifetime|> 30 and at least 2 x "Success History Lifetime"|Cron Fail History|
|Default|Generate Schedules Every|< 30|Cron Job Generation Interval|
|Default|Schedule Ahead for|< 30 and at least 2x "Generate Schedules Every"|Cron Job Schedule Ahead By|
|Default|Missed if Not Run Within|< 30|Cron Job Lifetime|
|Default|History Cleanup Every|>= 120 && < 14400|Cron History Clean Up|
|Default|Success History Lifetime|> 30|Cron Success History|
|Default|Failure History Lifetime|> 30 and at least 2 x "Success History Lifetime"|Cron Fail History|
|Consumers|Generate Schedules Every|< 30|Cron Job Generation Interval|
|Consumers|Schedule Ahead for|< 30 and at least 2x "Generate Schedules Every"|Cron Job Schedule Ahead By|
|Consumers|Missed if Not Run Within|< 30|Cron Job Lifetime|
|Consumers|History Cleanup Every|>= 120 && < 14400|Cron History Clean Up|
|Consumers|Success History Lifetime|> 30|Cron Success History|
|Consumers|Failure History Lifetime|> 30 and at least 2 x "Success History Lifetime"|Cron Fail History|
|3rd Party|Generate Schedules Every|< 30|Cron Job Generation Interval|
|3rd Party|Schedule Ahead for|< 30 and at least 2x "Generate Schedules Every"|Cron Job Schedule Ahead By|
|3rd Party|Missed if Not Run Within|< 30|Cron Job Lifetime|
|3rd Party|History Cleanup Every|>= 120 && < 14400|Cron History Clean Up|
|3rd Party|Success History Lifetime|> 30|Cron Success History|
|3rd Party|Failure History Lifetime|> 30 and at least 2 x "Success History Lifetime"|Cron Fail History|

  **N.B** for any checks that fail, the extra column should include what the current value is. (**If it is a 3rd party index, please include the name**) You should also add to the recommendation list that we change that setting to be inline with recommended settings.
  > We recommend bringing the “JOB NAME” setting inline with best practise, this can be carried out by our second line support team.
  
3. "Check Cron Is Running"
  In the mysql helper for the instance run the following:
  `select DATE_FORMAT(executed_at, '%Y-%m-%d %H:%i') as ran_at, count(*) as 'count' from cron_schedule group by DATE_FORMAT(executed_at, '%Y-%m-%d %H:%i') order by ran_at desc;`
  Ensure the top row is a timestamp from within 1 hour of when the backup was taken.
  Ensure that they look to be being run regularly, this doesn't have to be every minute but would expect to see at least 1 every 30 mins.
  
  `select DATE_FORMAT(scheduled_at, '%Y-%m-%d %H:%i') as ran_at, count(*) as 'count' from cron_schedule group by DATE_FORMAT(scheduled_at, '%Y-%m-%d %H:%i') order by ran_at desc;`
  Ensure the top row is a timestamp from within 1 hour of when the backup was taken.
  Ensure that they look to be being run regularly, this should be ~1 row per minute, however up 1 row per 5 mins should be okay.
  
  If any of these checks fail the check(s) which failed should be added to the extra column as well as raising the following as a recommendation
  
  > We recommend that an investigation be carried out by our third line team to ensure that cron is running on your production site. If your cron is failing this could lead to failed payments or orders.
  
4. "Check Cleanup Is Running"
  `select created_at from cron_schedule order by created_at asc limit 1;`
  Ensure returned timestamp is within 30 days of when the backup was taken
  If check fails add the detail to the extra colum and add the following to recommendations
  > We recommend that further investigation be carried out to determine why your cron logs are not being auomatically cleaned up.
  
5. "Check only healthy jobs"
  `select status, count(*) from cron_schedule where status not in ('pending', 'running', 'success') group by status;`
  We would expected an empty set or less than 100 total entries (add up the `count(*)` column).
  
  If this check fails add the totals to the extra info, e.g: 10 missed, 100 errored
  
>**^This check does not need to raise a recommendation as they will be raised from the below.**
  
6. "Check for errored jobs"
  `select count(*) from cron_schedule where status = 'error';`
  Ensure 0
  if this check fails run the following:
  `select job_code, count(*) as 'count' from cron_schedule where status = 'error' group by job_code order by count(*) desc;`
  
  For every row in this respose the following recommendation should be added to the list.
  > We recommend investigating why the job "JOB CODE" has errored. 
  If the job code looks like it is from a payment module then this should be noted a "High Priority"
  
7. "Check for missed jobs"
  `select count(*) from cron_schedule where status = 'missed';`
  Ensure 0
  if this check fails run the following:
  The following should recommendation should be added to the list
  > We recommend investigating why jobs are being missed, most commonly this is because a job or multiple jobs are taking to long to process, or they run so frequently they stop others from running. Our third line team should be able to investigate to determine if this can be improved.
  
8. "Check for Zombie jobs"
  `select * from cron_schedule where executed_at is not null and finished_at is null and status not in ('error');`
  Ensure this returns an empty set
  If this check fails, for each row the following recommendation should be added to the list. 
  > The following job "JOB CODE" looks to run for an extensive amount of time. This can cause, amongst other things, a gradual reduction in server performance as well as to cause other jobs to be missed. We recommed investigating to determine why this job is taking so long.

9. Make sure you have add a recommendation for all checks that failed where applicable.

10. Update the `??` at the top of the page to reflect the number of checks that passed.

11. Change "Settings" => "Cron" => "Enabled" to yes for the "TEST" instance. (You do not need to sync anything)

12. Once you have updated report, you should download as a PDF (File > Download > PDF) an attach to a new comment.
  If everything has passed the coment should read
  > We have completed your cron health checks, we are pleased to say that your site has passed all checks and no further investigation is neccesarry.
  We have attached a copy of your report.
  
  You should then close the task
  
  If there are some checks that have failed, the comment should read
  > We have completed our cron health checks unfortuntaley some of the checks haven't passed. Please could you review the attached report and let us know if you are happy for us to proceed with all recommendations or the specific ones your would like.

  Once they respond see [handling accepted recommendations](#handling-accepted-recommendations)

## Handling Accepted Recommendations

**Please hand the task to the recommendation owner**

- TODO: document 3rd line raising process

Any follow up tasks raised should contain:
- a link to the original task
- a copy of the report

- For any accepted recommendations relating to step 2 checks, these can be grouped together into a single task. Anyone with access to production can implement.
  **TODO** - confirm if we are going to lock these settings.
  
- If an accepted recommendation comes back for step 3, this needs to go to third line. [notes](#investigating-check-cron-is-running)

- If an accepted recommendation comes back for step 4, this should be progress as a job fail for "cron cleanup" to 3rd line [notes](#investigating-check-cleanup-is-running)

- For any accepted recommendations relating to step 6 or 8, a task needs raising for each one. This task can initially be investigated by 1st line. See [notes](#investigating-broken-jobs)

- If an accepted recommendation comes back for step 7, this needs to be raised as a task to 3rd line [notes](#investigating-missed-jobs)

### Investigating Check Cron Is Running


### Investigating Check Cleanup Is Running


### Investigating Broken Jobs


### Investigating Missed Jobs
