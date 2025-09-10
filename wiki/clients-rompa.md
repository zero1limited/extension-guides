# ROMPA

[TOC]

### Known Issues
They are still running composer 1 which will run out of memory on instances when using composer commands. Workaround: Switch your instance to composer 2 under Settings > PHP FPM > Composer.

## Corefinity
Corefinity docs: https://manage.corefinity.com/docs/1.0/

**Staging**
URL: https://m2-staging-rompa-com.cfstack.com/
Username : rompa.com-staging
Password: ogKWsC8CUAAXmiJ5

### Releases
Because this client is hosted on Corefinity we can't use the normal (MDOQ) process for releases.

**Prerequisites**
Make sure you have access to: https://manage.corefinity.com/resources/websites/1079579 (if not ask)


1. Create a deployment from a dev/uat instance as normal (creating a tag in the normal format etc..)
2. Once the merge into master and tag is complete you can continue
3. Go here: https://github.com/zero1limited/magento2-rompa/actions
4. On the left click "Deploy"
5. On the right click "Run workflow"
6. **Branch** will always be: `master`
  **Tag to deploy** wil be the tag created in #1
  **Pipeline** (pick appropriate)
  Then click "run workflow"
7. Watch the job in Github to ensure it completes. (If not seek assistance)
8. You then need to go the appropriate environment: https://manage.corefinity.com/resources/websites/1079579
  (the orange "production" or "staging")
9. Then select deployments
  You should see an active one in the list at the bottom, click the "view" icon to watch deployment
10. Wait for deployment to complete. You should see "Status: Succeeded" (if not seek assistance)

***Please note: Running the "Deploy" workflow within GitHub _will_ initiate the deployment on the environment set in the GitHub action. DO NOT run the workflow until you want the changes to go live***

