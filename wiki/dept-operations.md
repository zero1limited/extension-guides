# Operations Department

[TOC]

Overview 

## Standard Development Process

This document explains the full end to end process of how we use MDOQ to carryout, approve and deploy work.

### Summary

This process can be broken down into 5 main steps:
- Creating an instance
- Carrying out development work
- Automated regression testing
- Manual QA
- Release / Deployment

## Creating an instance

At the moment there is no formal process around who should create an instance.
If you need an instance create one.

The instance location should be "MDOQ Cloud"
If there isn't space on the clients account, you must confirm with Arron / Suz before selecting "Crystal" (ZERO1's private server) as the location.

### Creating an instance on crystal
1. On MDOQ, click the "NEW INSTANCE" button in the top right corner.
2. Click the "Create A Development Instance" button.
3. Select the client you want to roll up the instance for from the "Project" dropdown.
4. Click the "Bill to a different organisation" link underneath the project dropdown.
5. Select "ZERO-1 Ltd." from the "Bill To" dropdown.
6. Select "Crystal" from the "Location" dropdown.
7. Fill out the "Decription" and "Ticket Number" fields as you normally would when rolling up an instance.
8. Click the "SAVE" button and the instance will roll up under the client you selected.

## Carrying out development work
Carry out all the developerment work required by the change request or bug fix on the instance.
#### Once you have completed your work:
1. Click I'm done.
2. Make sure the following options are set: [I'm done settings - step 4 & 5](https://wiki.zero1.co.uk/docs/main/guide-deployment-process#content-regression-testing)
3. Unless otherwise stated, the target branch should be `master` or `main`. It is up to you to decide if the instance needs to be deleted after a deployment is created.
4. Wait for the instance to complete regression testing,
5. If it passes wait till the instance has finished the client acceptance stage (there should be a "Client Accepted" and "Client Declined" button).
   5b. If the instance fails regression testing refer to [Automated Regression Testing](https://wiki2.zero1.co.uk/docs/main/dept-quality-assurance#content-automated-regression-testing).
6. You can then hand it over to the client for approval. If the client approves pass the task to the acceptance column for QA with a comment stating: the work carried out, that you've checked it and if the work will need a downtime or zero downtime release.

## Automated Regression Testing
If the instance fails regression testing, it is up to a memeber of the QA team to determine if this issue was caused by the development or if it was a false negative. (i.e an issue with the test).
- Alert the QA team that your instance has failed regression testing by sending them a message with the instance link in the clients Slack channel.

#### QA Review process for failed tests
**Visit https://wiki.zero1.co.uk/en/quality-assurance#qa-review-process-for-failed-tests for process.**
## Manual QA
Before accepting an instance, please ensure:
- the instance is in client acceptance state. (There should be a "Client Accepted" and "Client Declined" button).
- there is a comment from the developer stating they have tested and approved their work.
- there should be a response from the client that it is approved.
- there is a comment from the developer indicating if this work will require a downtime or zero downtime release.

If **any** of these criteria aren't met, bat it straight back to the dev.

**Visit https://wiki2.zero1.co.uk/docs/main/dept-quality-assurance#content-manual-qa for process.**

## Release / Deployment

- @channel slack update in the clients channel that you are about to do a release (specify if its downtime or zero downtime).
- Do the release
- Once the release is complete check cache status using the Mdoq toolbelt (enable the caches if they report disabled).
- Flush opcache using the Mdoq toolbelt.
- Get fresh code and sanitised database backups.
- Indicate the release completed successfuly in the channel. (doesn't need to be an @channel).
- Resync TEST with the fresh backups once they are complete.

### Force Git Checkout Releases

Below is a document listing all the releases where we've had to force git checkout.
[Force git checkout list](https://docs.google.com/document/d/1SQFEmEfgGvzg4cpAiEGAktQHBK0mCi_L-RRP8xtRwk4/edit?usp=sharing)

