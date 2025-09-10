# Fierce PC - Punch Technology 

[TOC]

# Fierce PC

## Credentials

### SSH Access
Host: `45.131.139.182.srvlist.ukfast.net`
Port: `2020`
User: `fiercepc.co.uk`
Password: `cU9pg6nadr9Nt8`
SSH Command: `ssh fiercepc.co.uk@45.131.139.182.srvlist.ukfast.net -p 2020`

**OLD**
Host: `185.162.224.73`
Port: `2020`
User: `root`
Password: `f8xo425snGKJ`

## Release Proccess
This should describe how to do a release for this client whilst we wait on the MDOQ connector to be configured.
This process will require a developer

1. Commit work as normal.
2. Use the "I'm done" process to get to the client approval step.
3. Get approval from client
4. SSH into the instance and run
  ```
  cd /home/magento/htdocs; \
  foldersToZip="pub/static var/generation var/di var/view_preprocessed vendor generated"; \
  staticVersionPath="./pub/static/deployed_version.txt"; \
  deploymentPath="deployment.tgz"; \
  if [ -f ${deploymentPath} ]; then \
      rm -rf ${deploymentPath}; \
  fi; \
   zipString=""; \
   for folder in ${foldersToZip}; do \
       if [ -d ${folder} ]; then \
           zipString="${zipString}${folder} "; \
       fi; \
   done; \
   tar -cvhzf ${deploymentPath} ${zipString}; \
   mv ${deploymentPath} pub/${deploymentPath};
  ```
(This will put all the deployment files into `pub/deployment.tgz` this can then be downloaded by adding `deployment.tgz` to the instances base url)
5. You then need to merge your branch into master and tag it (this can be done via Github)
6. As `fiercepc.co.uk` on the server make the following file: `/var/www/vhosts/fiercepc.co.uk/zero1-preprelease`, if it already exist, empty it and add the content
  ```
  #!/bin/bash -e

if [ -z $1 ]; then
    echo "first argument must be the tag you are going to"
    exit 1;
fi

if [ -z $2 ]; then
    echo "second arument must be the url of an existing deployment"
    exit 1;
fi

# set up some variables
TAG=$1
DEPLOYMENT_URL=$2
MAGENTO=fiercepc.co.uk

echo "Deploying Tag: ${TAG}"
echo "Using deployment: ${DEPLOYMENT_URL}"

if [ $(whoami) != ${MAGENTO} ]; then 
    echo "this script must be ran as: ${MAGENTO}"
    exit 1
fi

# make a new dir for everything to go in and checkout tag in it
set -x
git clone --depth 1 --branch ${TAG} git@github.com:zero1limited/magento2-fiercepc.git /var/www/vhosts/fiercepc.co.uk/live_deployment/releases/${TAG}
cd /var/www/vhosts/fiercepc.co.uk/live_deployment/releases/${TAG}

# pull down and extract deployment from MDOQ
wget --no-check-certificate -O deployment.tgz ${DEPLOYMENT_URL}
tar -xf deployment.tgz 

# put the symlinks in
# var
cd /var/www/vhosts/fiercepc.co.uk/live_deployment/releases/${TAG}/var
ln -s ../../../shared/var/session session
ln -s ../../../shared/var/report report
ln -s ../../../shared/var/log log
ln -s ../../../shared/var/fishpig fishpig
ln -s ../../../shared/var/export export
ln -s ../../../shared/var/import_history import_history
ln -s ../../../shared/var/importexport importexport
ln -s ../../../shared/var/import import
ln -s ../../../shared/var/magefan magefan
ln -s ../../../shared/var/cert cert
ln -s ../../../shared/var/Mailchimp Mailchimp
ln -s ../../../shared/var/import_export import_export
ln -s ../../../shared/var/logging logging
ln -s ../../../shared/var/composer_home composer_home

# pub 
cd /var/www/vhosts/fiercepc.co.uk/live_deployment/releases/${TAG}/pub
ln -s ../../../shared/pub/sitemap.xml sitemap.xml
ln -s ../../../shared/pub/.user.ini .user.ini
ln -s ../../../shared/pub/media media

# wp
cd /var/www/vhosts/fiercepc.co.uk/live_deployment/releases/${TAG}
ln -s ../../shared/wordpress wp

# app
cd /var/www/vhosts/fiercepc.co.uk/live_deployment/releases/${TAG}/app/etc
ln -s ../../../../shared/app/etc/env.php env.php

set +x
echo "Release staged"
  ```
7. As `fiercepc.co.uk` run the script like this: `/var/www/vhosts/fiercepc.co.uk/zero1-preprelease TAG URL` for example
   `/var/www/vhosts/fiercepc.co.uk/zero1-preprelease 2022.50.00 https://www-fiercepc-co-uk-16627.36.mdoq.io/deployment.tgz`
   You should see "Release Staged", if you don't stop and seek assistance
   At this point the live site hasn't be touched and we can back off without any issues
8. **This is where the danger zone begins**
   Create the file `/var/www/vhosts/fiercepc.co.uk/zero1-release` with the following content
  ```
  #!/bin/bash -e

if [ -z $1 ]; then
    echo "first argument must be the tag you are going to"
    exit 1;
fi

# set up some variables
TAG=$1
MAGENTO=fiercepc.co.uk

echo "Deploying Tag: ${TAG}"

if [ ! -d /var/www/vhosts/fiercepc.co.uk/live_deployment/releases/${TAG} ]; then
    echo "unable to find the release: ${TAG}"
    exit 1
fi


if [ $(whoami) != "root" ]; then
    echo "You must be root to run this script"
    exit 1
fi

# enable maintenance mode (in current and in target)
cd /var/www/vhosts/fiercepc.co.uk/live_deployment/current;
su ${MAGENTO} -c "php bin/magento maintenance:enable"
su ${MAGENTO} -c "cp var/.maintenance.flag /var/www/vhosts/fiercepc.co.uk/live_deployment/releases/${TAG}/var/.maintenance.flag"
su ${MAGENTO} -c "cp var/.maintenance.ip /var/www/vhosts/fiercepc.co.uk/live_deployment/releases/${TAG}/var/.maintenance.ip"

# swap "current symlink"
cd /var/www/vhosts/fiercepc.co.uk/live_deployment
su ${MAGENTO} -c "ln -sfn releases/${TAG} current"

# setup upgrade
cd /var/www/vhosts/fiercepc.co.uk/live_deployment/current
su ${MAGENTO} -c "php bin/magento setup:upgrade --keep-generated"

# cache flush
su ${MAGENTO} -c "php bin/magento cache:flush"


# php restart (NEED TO BE ROOT)
service php-fpm restart

# varnish restart (NEED TO BE ROOT)
service varnish restart

# disable maintenance mode
su ${MAGENTO} -c "php bin/magento maintenance:disable"


echo "Release Complete"
  ```
9. As `root` run the script like this: `/var/www/vhosts/fiercepc.co.uk/zero1-release TAG` for example
   `/var/www/vhosts/fiercepc.co.uk/zero1-release TAG`
   If all goes well you should see the message "Release Complete". If not investigate.


## V12 Finance

To test V12 finance, you will need to enter the following keys:

| API Key                             | Enc Key                                                            |
| ------------------------------------| ------------------------------------------------------------------ |
| 011e722d44b84333131453b8abaedf75    | ae4765bdb4701919ee597e89940ff93ca1534af4e289efcd3e6631631b78bd08   |


<b>I will work on adding these to the PRA's so that this isn't necessary to do each time a dev instance rolls up</b>

Also, you will need to use a specific Last Name to simulate various scenarios/outcomes from the application:

| Last Names to simulate given outcome | Description                                                                                                  |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------|
| `Approve`                            | Using `Approve` will approve the application                                                                 |
| `Refer`                              | Using `Refer` will refer the application indefinitely                                                        |
| `Decline`                            | Using `Decline` will decline the application                                                                 | 
| `ReferApprove`                       | Using `ReferApprove` will refer the application and then approve it after a random delay of up to one hour   |
| `ReferDecline`                       | Using `ReferDecline` will refer the application and then decline it after a random delay of up to one hour   |


When filling out the application, ensure this text is visible throughout: `This is a test application and will not be credit checked.`

When you get to the bank account/sort code section, enter these to test with:

| Sort Code | Account Number  |
| --------- | --------------- |
| 200000    | 55779911        |


  
