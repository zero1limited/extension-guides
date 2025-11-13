# Magento Upgrades
[TOC]

compatibility matrix
https://devdocs.magento.com/guides/v2.4/install-gde/system-requirements.html

## Introduction
This is a working progress document which Arron/Adam are developing, this process is for all clients regardless of size.
  

```
composer update && composer install --no-dev
bin/magento setup:upgrade && bin/magento deploy:mode:set developer

```
to check you have upgraded properly please run `bin/magento -V`
If the above process fails you are likely going to need to carry out the more involved steps below.

ARRONS WORKING NOTES (NEW)
BASED ON https://experienceleague.adobe.com/en/docs/commerce-operations/upgrade-guide/implementation/perform-upgrade

```

cp composer.json composer.json.bak
composer remove magento/product-community-edition --no-update
composer require-commerce magento/product-community-edition 2.4.8 --no-update --interactive-root-conflicts --force-root-updates

composer update


NOTE FROM ARRON 
I do not personally know how to merge the require-dev and other changes in.

```





## Estimating Upgrade Difficulty
This is WIP

1. Create a new instance for the client (or use UAT)
2. Login via SSH, copy paste all of the below content into your terminal and hit ENTER
  ```sh
  cd ~/htdocs \
    && cp ~/htdocs/auth.json ~/.composer/ \
    && composer create-project magento/upgrade-compatibility-tool uct --repository https://repo.magento.com \
    && chmod a+x ./uct/bin/uct \
    && ./uct/bin/uct upgrade:check --coming-version=2.4.3 --html-output-path=pub/uct.html --ignore-current-version-compatibility-issues -- ./
  ```
  (This command will take a long time to run)
3. Once complete go to the frontend of the site and add the following to the end of the url `uct.html`
  For example if the site's url was https://www.example.com, you would go to: https://www.example.com/uct.html
4. Save the webpage as a PDF (print > save as pdf) and upload to your task.






## System Requirements (Pre-Upgrade)
Before upgrading a client to the next Magento version up (2.4.5-p2/2.4.6), check the system requirements page here: https://experienceleague.adobe.com/docs/commerce-operations/installation-guide/system-requirements.html

The requirements here are crucial to ensure everything is ready for the upgrade. Also, ensure that the correct prerequisite versions match the version that it is being upgraded to.

For example, if you are upgrading to 2.4.5-p2 or 2.4.6, Composer needs to **AT LEAST** be on Composer 2, otherwise it will cause issues.

The PRA commands for Composer to be set to Composer 2 are as follows: 
`mv /usr/bin/composer /usr/bin/composer1; mv /usr/bin/composer2 /usr/bin/composer`

What this essentially does, is swap around the composer versions and changes it over to Composer 2, which is now compatible with later versions of Magento
  











<div style="display:none">

-----


## OLD - just keeping for reference for now
## Adams instructions on running the CLI SAK job

When repeating this cycle always execute this then recreate and re-run
```
curl -H "x-mdoq-auth: va6vPPESVg2rlCICoEm=Jsu+iL6QkTyR3DjSpZIkdKNAjtaK8yJR=bPiVU8gKF7NgqDHni2D2Pblgn5oVNcX+1cWUk-C+gneI=V6hZJjNWG4hLrcwFfannyxHz9GSvXxvTDPQj8BdOEww5K3KTwmcWVWt2zixu=2ksQ_OVL1Knxerfg_8OxkIqd_rPs+gh1DMRNytitsV6Kjk1usP2Our2FVR8T7pUK_IuIs=eVUjGbGGI8tJWY0VC3MJWT8NAf" -X PATCH --data '{"instance":{"component_configuration":{"php-fpm":{"use_parent_version":1}}}}' https://api.mdoq.io/v1/instance/id/8394/
```

### These next steps could be done in GitHub and with environment changes therefore we could jump straight to the ssh commands below.

**Edit app/etc/env.php adding this as an additional encryption key to `Dd8IuLl2AziZ89JiLmbbQC9vw70J7b1p`**
**Run the following in the MySQL GUI Helper**
`set FOREIGN_KEY_CHECKS=0; truncate magento_logging_event; truncate magento_logging_event_changes; set FOREIGN_KEY_CHECKS=1;`
**Remove custom changes  `app/etc/config.php` *these will need to be restored at somepoint.**


ssh to the mdoq instance
```
screen
docker exec -ti mdoq-worker-php-cli bash
su www-data

php index.php mdoq:recreate --instance-id=8394 -v && \
php index.php sak:run --instance-id=8394 --job=upgrade -v --job-param-version=2.3.2 >> "upgrade_-$(date +%s).log"
CTRL A 
CTRL D
```
this exits screen and should output the process ID so you can re-enter

```
screen -r 5050.pts-5.server1
```

## Instructions
Task start
* Review the Report output document initially making a note of the 'Failed' entries - search for Failed and note the number in your task notes.
* Open the composer.lock.orig in your upgrade instance - this will have been created as part of the CLI SAK job once complete

Repeating Steps per Failed Entry
* Obtain the name of the dependency. The name will be the part after `diff:set:require/` in the 1st colum Eg. `ampersand/cms-navigation` 
* Search for the repo in [GitHub](https://github.com/dt-automotives/) by name. 
* View the composer.json file in GitHub and if you see a line in the require parenthesis containing 'magento/framework' remove it
* In the `composer.lock.orig` search for the module and make a note of the version


Go back to the master branch of the main repo and check the [Composer.Lock](https://github.com/dt-automotives/uberkids/blob/master/composer.lock) file
Check the version/branch in the lock file and compare this to master now you have just updated the composer.json file Eg https://github.com/dt-automotives/snowio-magento2-attribute-option-code/compare/v1.8.2...master
you hopefully will see the only difference being the composer updates in which case you are safe to install the dependency master branch?
Eg `composer require --update-no-dev -- snowio/magento2-attribute-option-code:dev-master`

do I run the above command on local PHPStorm, commit the changes to the upgrade branch and repeat?
</div>

### Sub Processes
- [Prerequisites](/magento2/upgrades/Prerequisites)
- [Elastic Upgrade](/magento2/upgrades/elasticsearch-upgrade)
- [Varnish Upgrade](/magento2/upgrades/varnish-upgrade)
- [PHP Upgrade](/magento2/upgrades/php-upgrade)
- [MySQL Upgrade](/magento2/upgrades/mysql-upgrade)
- [Redis Upgrade](/magento2/upgrades/redis)
