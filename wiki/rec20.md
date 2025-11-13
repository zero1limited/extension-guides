<!--

As a Developer, I want to generate a report of logged errors so that I can provide a client with a list of proactive fixes to carry out.




Hi __________,

Errors on your site, though not always fatal, may be having an effect on performance and sales

We would like to proactively spend time monitoring logs on your production site, looking in to any errors being thrown. We will then generate a report for you highlighting any issues.

Most errors are caused by 3rd party modules so we may end up advising you that some need upgrading or replacing.

-->


# Instructions
This work must be carried out on a fresh instance to reduce the chance of false positive, this means:
- recreating TEST right before carrying the process out
- creating a fresh instance.

Demo video: https://watch.screencastify.com/v/Pme8OPvyMdCbYQebUISH

1. Open code editor for intance
2. run the following in the terminal `curl -s https://gist.githubusercontent.com/adamzero1/f652f5b7bacfa5b66594c11a057f36e3/raw/dbba844863834e6d230b928be3ba0cfcf0ba4c98/analyse_magento_var_directory.php | php`
3. Copy & paste the content into the current task.
4. If any of the results are "FAIL" go to "Recommending error cleanup"
5. If all of the results go to "Result Success"


## Recommending error cleanup
Add the following above the report in the comment.
```
Hi @productOwner,
Following a review of all your log and exception files (report below) we have found some potential issues that need action.
We would like to recommend a task capped at 2 hours to fix as many of the issues found as possible.

Please could you confirm if you are happy for us to proceed with this work.

Many thanks
[REPORT CONTENT]
```
submit comment.
If client declines close task.
If client accepts please ask Suz to send this to second line.

## Result Success
Add the following above the report in the comment.
```
Hi @productOwner,

We have completed a review of all your log and exception files and are happy to confirm all is in working order.
The report generated is below, however no further action is required.

Many thanks
[REPORT CONTENT]
```
Submit the comment and close the task.







# YOU DONT NEED TO GO BELOW HERE





# Stuff from previous wikis
**Introduction**
The exceptions and logs health check is a set of tests/tasks that can be carried out to check if there are any obvious errors. At the moment this task is a manual process, the end goal being an MDOQ job, so the process can be deskilled.


**Peforming the task**
As the process for this task is still in its infancy this will be added/updated everytime the task is performed.
The process is the same regardless of platform.

- check system.log is under 100M
  `ls -lath system.log`
- check last written to date `var/log/system.log`
  `tail -n 1 system.log`
- check for any warnings in `var/log/system.log` in last thousand lines
  count = `tail -n 1000 system.log | grep "Warning: " | wc -l`
  error percentage: count / 10
  _aiming for <10%_
- check exception.log under 100M
  `ls -lath exception.log`
- check last written to date `var/log/exception.log`
  confirm greater than 30 days 
  check not written to in last 30 days
- check for any recent reports in `var/report`
- check for any reports older than 30 days
  `find ./report -type f -mtime +30 -exec echo {} \; | wc -l`
  removing them: `find ./report -type f -mtime +30 -exec rm {} \;`
  
**Report Output**
```
## Logs & Exceptions Healthcheck
| Name | Description | Result | Extra |
|:-:|:-:|:-:|:-:|
| System.log Size | Confirm system.log is under 100M | PASS |   |
| System.log Last Written To | Check when system.log was last written to | FAIL | I have raise two tasks (see below) to reduce this. |
| System.log warning rate | A check to confirm, that the number of warnings written to system.log is less than 10% of output. | FAIL | 71% the tasks raised below should lower this |
| Exception.log size | Confirm exeception.log is under 100M | FAIL | I have truncated this file. (emptying it) |
| Exceptions.log Last written to | Check exception.log hasn't been written to in the last 30days | FAIL | I haven't raised a task for this yet, as I would like to resolve the other two issues first to see if they contribute. If this issue is still occuring in the review after they have been resolved I will raise a task for it. |
| Recent Reports | Check for any recent reports. (last 30 days) | FAIL | Again I will raise a task after the other two issues have been resolved. |
| Old Reports | Check for reports older than 30 days that need cleaning up | FAIL | 101 reports older than 30 days, I have removed them. |

### Tasks raised to resolve issues found
- https://zero1.teamwork.com/#/tasks/19732271
- https://zero1.teamwork.com/#/tasks/19732259
