# Magento Security Patches
[TOC]

[THIS ARTICLE NOW LIVES HERE](https://zero1commerce.atlassian.net/wiki/x/x4CHAg)


## Security Patch Only Magento Upgrades
For security only patches this process should involve only the updating of Magento to the same version with a suffix Eg `-p1` 

Example scenario
From the CLI run `bin/magento -V` and if this returns something like `2.4.4-p1` then you would run the following


```
cd ~/htdocs
php bin/magento deploy:mode:set developer
php bin/magento cache:disable

composer require magento/product-community-edition:2.4.4-p14 -W
# OR
composer require magento/product-community-edition:2.4.5-p13 -W
# OR
composer require magento/product-community-edition:2.4.6-p11 -W
# OR
composer require magento/product-community-edition:2.4.7-p6 -W
# OR
composer require magento/product-community-edition:2.4.8-p1 -W

rm -Rf generated
php bin/magento setup:upgrade --keep-generated
php bin/magento deploy:mode:set production
php bin/magento cache:enable
```



If running `bin/magento -V` then returns the expected version `2.4.4-p13` then you can push your changes to git (composer.json & composer.lock) then follow the 'Im Done' process and pass to Acceptance.
**N.B** if there are changes to `.gitignore` please review or get a developer to review.

This marks the end of the process for Security Patch updates. If there is no version matching the clients Magento version with a -p version then please escalate this task to your manager.

More complex upgrades are covered below.

## Specific Upgrade Nuances


### Magento 2.4.7-p5 / 2.4.6-p10 / 2.4.5-p12 / 2.4.4-p13

Run these steps first
```
cd ~/htdocs
php bin/magento module:enable Magento_Elasticsearch
rm -Rf ./vendor

```

