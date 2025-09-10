# Development Department

[TOC]

Overview 
WIP Aim to be a single source of truth for a set of standards we maintain whilst work on Magento projects.

## Module Locations

Within Magento there are 3 locations modules can be created/installed.

### app/code/
This location should be used if:
- This module is only applicable to this client (now and in the future)
- The module has no additional/external requiremtns e.g it doesn't require another composer package

### vendor
This should be the default location for all modules, 3rd party or provided by ourselves.

### extensions
This location should be used if:
- There isn't a vendor installable version of the package (license expired)
- The module is only for this client, but has external composer requirements
- We are currently working on the module (see [working on modules](#working-on-modules))


## Creating a new module
If you need to create a new module the following needs carrying out:
- create github repository in the format `magento2-extension-name` e.g `magento2-my-super-awesome-module`
- create the module skeletion `./vendor/bin/magentodev create:module` 
  (this will create the skeleton an push to gitubs for ya)
- add the github repository to repman

## Onboarding Tasks
- setup Zero1 Repman access
- setup `extensions` directory
- convert 3rd party extensions to from `app/code` to `vendor` or `extensions` install.
- install `zero1/magento-dev` module
- install web rest logger module
- install admin action logs module


## Working on modules
If we are working on one of our modules (installed via composer into vendor) then we can setup an environment to allow us to better work on the module.

### Prerequisites 
- ssh key added to the instance ([Adding SSH Key](#adding-ssh-key))
- git configured ([Configuring Git](#configuring-git))

### Steps
In this example we will be updating `zero1/example-module`

**Starting work on the module**
1. git clone [ssh url] extensions/zero1/example-module
2. in the composer.json add the top of the `repositories` section
  ```json
  "repositories": {
        "zero1/example-module": {
            "type": "path",
            "url": "extensions/zero1/example-module/",
            "canonical": true,
            "options": {
                "symlink": true
            }
        },
  ```
3. require dev version of module `composer require zero1/example-module:@dev`
4. you should now be able to work on the module
5. when done commit your work to the module, ie `cd extensions/zero1/example-module`, `git add . --dry-run`, if happy `git add .`, `git commit -m "task url / commit message"`, then tag the module `git tag x.x.x`, `git push --tags`
6. edit the `canonical` option of the repository to `false`, so you now have
  ```json
  "repositories": {
        "zero1/example-module": {
            "type": "path",
            "url": "extensions/zero1/example-module/",
            "canonical": false,
            "options": {
                "symlink": true
            }
        },
  ```
7.  pull in your new version (the tag you made) `composer require zero1/example-module:x.x.x`
8.  test
9.  if all okay remove the repository addition from `composer.json` then `rm -rf extensions/zero1/example-module`

### Adding SSH Key
WIP this could change in the future but for now (until MDOQ supports a better option)
This should only be done on your instance, dont do on UAT as commits will come from you
```bash
mv ~/.ssh/id_rsa ~/.ssh/id_rsa.moved || true
nano ~/.ssh/id_rsa
ADD YOUR PRIVATE GITHUB SSH KEY TO THE FILE
chmod 600 ~/.ssh/id_rsa
```

Once you are done on the instance
```bash
rm ~/.ssh/id_rsa
mv ~/.ssh/id_rsa.moved ~/.ssh/id_rsa || true
```

### Configuring Git
```bash
git config user.email "Your email"
git config user.name "your github username"
```
