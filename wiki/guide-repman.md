# Repman

Adding modules to our Repman system is typically for internal modules (initially) and also MIAMI projects.

Login to https://app.repman.io/login with the user credentials which you should already have  - if not contact Arron for an invite

## Adding New Packages 

If you have created a new module and want to make it privately available to a client project, simply add it from the [Packages Page](https://app.repman.io/organization/zero1/package)

Select Repository Type : GitHub - this will take 15-20 seconds to load
Then select the Repository pull-down and type some of the repo name in order to locate it, leave 'Keep last releases' as 0 and click 'Add'

If the repo does not show up https://app.repman.io/organization/zero1/package after about 5 minutes this indicates your composer.json file is invalid

Contact Arron to walk through the error so that he can improve this document with each use-case.

### Potential Issues
• Ensure your composer name is all lowercase Ie: zero1/diddly-tum-tum
