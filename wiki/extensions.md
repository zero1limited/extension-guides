# Extensions

[TOC]

Overview 

## Developing Extensions

### Configuring repo / module

1. Create the following:   
  `.github/workflows/check_module.yml`  
  ```yaml
  name: Check Module

  on:
    workflow_dispatch:
    push:
      branches: [ "master" ] 

  permissions:
    contents: read

  concurrency:
    group: module-checks-${{ github.ref_name }}
    cancel-in-progress: true

  jobs:
    check-module:
      uses: zero1limited/magento2-module-checks/.github/workflows/check_module.yml@master
      permissions:
        contents: read
      secrets: inherit
  ```
    
  
  `.github/workflows/send_releases_to_shop.yml`  
  ```yaml
  name: Update Release Notes In Shop

  on:
    workflow_dispatch:
    release:

  permissions:
    contents: write

  concurrency:
    group: module-checks-${{ github.ref_name }}
    cancel-in-progress: true

  jobs:
    update-release-notes:
      uses: zero1limited/magento2-module-checks/.github/workflows/update_shop_release_notes.yml@master
      permissions:
        contents: read
      secrets: inherit
  ```
  Commit these files to the `master` / `main` branch.

2. Run the workflow (needed for other bits of github to "see" it)
  Go to: _Actions_ > _Check Module_ > _Run workflow_ > select main branch > _Run workflow_ 
  wait for it to finish (doesn't matter if it fails)

3. Within Github, go to _Settings_ > _Branches_ > _Add classic branch protection rule_
  **Branch name pattern:** the same as the default branch `main` / `master`
  **Require a pull request before merging:** Yes
  **Dismiss stale pull request approvals when new commits are pushed:** yes
  **Require status checks to pass before merging:** yes
  **Require branches to be up to date before merging:** yes
  **Status checks that are required:** `check-module / All Valid`
  (**N.B** if option not here it should be blank / no / off)

4. Within Github, go to _Settings_ > _Rules_ > _Rulesets_ > _New ruleset_ > _New tag ruleset_  
  **Ruleset Name:** `All`  
  **Enforcement Status:** `Active`  
  **Tag Targets**  
    - include all tags  
    - exclude `*-dev`  
  **Restrict updates:** yes  
  **Restrict deletions:** yes  
  **Require status checks to pass:** yes  
  **Require branches to be up to date before merging:** yes  
  **Do not require status checks on creation:** yes  
  **Status checks that are required:** `check-module / All Valid`  
  **Block force pushes:** yes  
  (**N.B** if option not here it should be blank / no / off)  


### Release / Deploy Process
> Still a WIP suggestions welcome

1. do your changes in a branch
2. make a pr, this should kick off `module-checks`
3. approve PR, merge into `main`/`master`
4. make a release  
  make a tag
  click "generate release notes"
  -> publish release
  (this should kick off `send_releases_to_shop`)

### Module Checks
Common checks we want in place across all our modules

### Send Release To Shop
Does what it says

If you edit the release notes of previous releases, you can just run it again from the the actions tab to update the shop. (ie don't need to create a release everytime you want to update the notes)


## Main Adobe Marketplace Account
The ZERO-1 company account is used for the main Repo for testing and generic keys
This is accessible via sales@zero1.co.uk account MAG000005402

Public: 1f22870161917d69331b7ffa7110df28
Private: 30fa34567b94e077f050015ac0cff05c



## Adding Extensions To ZERO1 Store

Private packagist: https://packagist.com/orgs/zero1limited
Because of how permissions work, the ZERO1 user will need adding to this Github team
https://github.com/orgs/zero1limited/teams/private-packagist

Then go into private packagist teams (https://packagist.com/orgs/zero1limited/teams) and "resynchronize" 

Give it 10 mins and the user should be able to access stuff.

## ZERO1 - MC clients
All ZERO1 clients that have an MC have acess to all the ZERO1 packages.
This is done through the use of a "bundle"
https://packagist.com/orgs/zero1limited/vendor-bundles/142/edit

We can then create a customer (to represent the client) and assign the bundle to them
eg: https://packagist.com/orgs/zero1limited/customers/13819/vendor-bundles

Credentials can then be collected for the client
eg: https://packagist.com/orgs/zero1limited/customers/13819/composer


## LICENSE
@deprecated - have moved the license (and the check for it) into the module checks, this way we can keep it in one place that can be access by actions.
[HERE](/docs/main/extensions/LICENSE.TXT)
/docs/main/extensions/


## TODO
sort this link out: https://docs.google.com/spreadsheets/d/1g5EDMqkZMo9h_3O6uGL8056J4JOJTtzFCTHaFrohD6Y/edit?gid=0#gid=0