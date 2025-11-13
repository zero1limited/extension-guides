# Composer - installing, updating, patching Magento extensions
Everything related to our use of composer should go here. 

[TOC]


## Updating Composer Itself
Latest Composer versions updated 19 September 2023 from https://getcomposer.org/download/


Up to and including Magento 2.4.4 Composer 1 is required. 

From Magento 2.4.4 up to 2.4.4-p2 Composer 2.1 is required.
```bash
composer self-update 2.1.14
```



From Magento 2.4.4-p3 up to 2.4.6-p2 Composer 2.2 is required
```bash
composer self-update 2.2.21
```

From Magento 2.4.7 onwards Composer 2.5 is required

```bash
composer self-update 2.5.8
```


## Checking for dependencies which are upgradable
run `composer show -o` - this will return the installed and the latest versions available.

Since the above will return all dependencies including many core ones, you might want to check just a single vendor extension.
run `composer show -o m2epro/magento2-extension | grep 'latest\|versions'` 

## Installing new extensions via composer

Login to the instance SSH. If you need to setup SSH go to: https://wiki.zero1.co.uk/docs/main/dept-operations/SSH

`cd htdocs`

`composer require amasty/module-mass-order-actions`

`bin/magento setup:upgrade`

`bin/magento deploy:mode:set production`

If this fails, escalate to a dev


## Upgrading Magento Modules
This guide relates specifically to modules declared in the composer.json
This does not relate to extensions in app/code/

Login to the instance SSH. If you need to setup SSH go to: https://wiki.zero1.co.uk/docs/main/dept-operations/SSH

This example is for the specific extension `amasty/module-mass-order-actions`

enter the project root: `cd htdocs`

list available upgrades: `composer show -a amasty/module-mass-order-actions`

show currently installed version: `composer show amasty/module-mass-order-actions`

update a module: `composer update --with-all-dependencies -- amasty/module-mass-order-actions`

post upgrade command: `bin/magento setup:upgrade`

post upgrade command: `bin/magento deploy:mode:set production`

If this fails, escalate to a dev


## Upgrading Magento 
Major upgrades Ie 2.3.x to 2.4.x will have major complexities with platform/stack requirements and also tend to have differences in the composer.json file. This guide is not for such operations.

If a minor Ie 2.4.5 to 2.4.6 or security Ie. -p3 security upgrade, you can do the following

1. Check the availability and current version
`composer show -a magento/product-community-edition`

2. If the task dictates just an emergency security update, then ideally you should be updating the current version with security patches.
Ie. from 2.4.4 to 2.4.4-p5 NOT from 2.4.4 to 2.4.5-p4

   
`composer require --with-all-dependencies magento/product-community-edition:2.4.4-p5`


## Updating Hyvä Themes to the latest version

```bash
composer update --with-all-dependencies hyva-themes/magento2-default-theme hyva-themes/magento2-theme-module
```



## Installing extensions which are not contained in vendor/supplier repositories
Working with composer dependencies which are not available from either public or private packagist responsitories, can be complex. 
More information can be found here.
