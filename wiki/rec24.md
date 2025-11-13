# Instructions

1. Open up the file `composer.json` in the code editor and look for (Ctrl + F) "patches/zero1_static_maintenance_page.patch"
  If this line exist please remove for example it may look something like:
  ```json
  "magento/magento2-base": {
    "Static maintenance pages": "patches/zero1_static_maintenance_page.patch"
},
  ```
  You will then need to remove the full line to make it
  ```json
  "magento/magento2-base": {
},
  ```
  Save the file once a change is made
2. From Web SSH on the instance run each of the following one after another.
```
composer require zero1limited/magento2-patches:dev-master
php bin/magento module:enable Zero1_Patches
php bin/magento setup:upgrade --keep-generated
php bin/magento cache:flush
php bin/magento patch:add --patch=ZERO1-STATIC-MAINTENANCE-PAGE
composer install --no-dev
curl -s https://raw.githubusercontent.com/zero1limited/gitignore/master/updater.php | php
curl -s https://raw.githubusercontent.com/MDOQ-UK/Templates/main/gitignore/updater.php | php
```
> Pay attention to the output, if one looks to have failed stop and seek assitance.
{.is-warning}

3. Install the default file.
```
mkdir -p var/maintenance; wget -O var/maintenance/default_maintenance.html https://raw.githubusercontent.com/zero1limited/magento2-static-maintenance-page/master/default_maintenance.html
```

4. In the code editor, open the file `var/maintenance/default_maintenance.html`
You need to find and replace the following in this file:
- `{{LOGO_URL}}`
  This needs to be replaced with the logo url for the site, you can do this by visiting the production homepage of the production site.
  Right click > "view page source"
  Then "Ctrl" + "F" and search for logo
  ![capture.png](/recommendations/rec24/capture.png)
  Here the url we want is: `https://www.roys.co.uk/static/version1635400061/frontend/z1/ry/en_GB/images/logo.svg`
  
- `{{DOMAIN}}`
  This needs to be replaced with the domain name of the site, for example `www.roys.co.uk`
  
- `{{COMPANY_NAME}}`
  This needs to be replaced with the comany name
  
5. If the client has supplied their own mockups for specific stores.
You need to log into the admin of the instance and navigate to Stores > Stores 
You can then use the store view codes in the next step
![storeview_codes.png](/recommendations/rec24/storeview_codes.png)

6. You then need to use the code editor to make a maintenance file for each storecode. For the example above this would mean making the files:
`var/maintenance/highwaygardenandleisure.html`
`var/maintenance/default.html`
Then copy the content for each store into the mockups.

7. Once all maintenance pages have been created, go back to the cli and run
```
php bin/magento maintenance:enable
```

8. Test you should then be able to test the maintenance pages by visiting the frontend of each site.

9. If all is well run git push
The files you will likely need to add are:
- `composer.json`
- `var/maintenance/*`
- `pub/index.php`
- `.gitignore` (optional)
- `composer.lock` (optional)
- `app/etc/config.php` (optional)
If any of the none optional files aren't "addable" please stop and seek developer assistance.

10. Leaving maintenance mode enabled, pass the links to client for testing


## Checking if a site has a static maintenance page
1. go to the TEST instance for the client
2. open the code editor
3. look for the file `var/maintenance/default_maintenance.html`

If this file exists the client has static maintenance page
If this file doesn't exist the client doesn't have static maintenance page


## Releasing this work
This should be a downtime deployment
