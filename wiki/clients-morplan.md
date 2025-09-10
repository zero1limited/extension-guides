# Morplan

[TOC]

## Overview
Quick overview of the client.

### Known Issues
They are still running composer 1 which will run out of memory on instances when using composer commands. Workaround: Switch your instance to composer 2 under Settings > PHP FPM > Composer.

## Roles & Responsibilities

### Responsibilities

## Key Stakeholder(s)

## Customisations

### Akeneo


#### Akeneo Cron Jobs
Jobs are
```
bin/magento akeneo_connector:import --code=family,attribute,option
bin/magento akeneo_connector:import --code=product 
```

Cron is
```
0 1 * * 0 /opt/php/php-8.3/bin/php /microcloud/domains/morliv/domains/morplan.com/http/bin/magento akeneo_connector:import --code=family,attribute,option >> /microcloud/domains/morliv/domains/morplan.com/http/var/log/akeneo_connector_import_type.cron.log
0 */2 * * * /opt/php/php-8.3/bin/php /microcloud/domains/morliv/domains/morplan.com/http/bin/magento akeneo_connector:import --code=product >> /microcloud/domains/morliv/domains/morplan.com/http/var/log/akeneo_connector_import_type.cron.log
```


#### Akeneo Configuration
```
bin/magento config:set akeneo_connector/akeneo_api/base_url https://morplan-test.cloud.akeneo.com/
bin/magento config:set akeneo_connector/akeneo_api/username magento2_staging_5146
bin/magento config:set akeneo_connector/akeneo_api/client_id 1_5tlgrorbdc844w4404s0kk4s4og0c0o8wkcssgs0gso8swcssg

# CANT DO THIS - these are the encrypted values - can do via SQL
bin/magento config:set akeneo_connector/akeneo_api/password 0:3:eNL8AVvBtmnhKHoGJnmEe3RcclkQuLPKcJtjd0Gbk7Ltc9P2LA==
bin/magento config:set akeneo_connector/akeneo_api/client_secret 0:3:kHTDr93DRNHL2vMfEYtMZLBltA20kTi2jrFrGvva4oh0CLxoj9o31Lkzwk2rtu95R8g+F/pRSk7W+OALXGtC8wGvRL8dZiQ7xhaeW1NI
```

### Logoprint
https://designo.morplan.com/ lives on production

#### Custom Shipping for LogoPrint Products



## Hosting
Hosted with Sonassi.
They have two stacks

**Production**: stack1.c720
**UAT**: stack2.c720

We currently utilize staging for testing their SAP integration (their program Vouager FTP uses legacy SSH version and is unable to connect to MDOQ SFTP, see [ticket](https://zero1.teamwork.com/app/tasks/36981651))

### Stack 1 - Production
Frontend: https://www.morplan.com/
Opcache Status: https://www.morplan.com/opcache_status.php
Opcache Refresh: https://www.morplan.com/opcache.php
Webroot Directory: `/microcloud/domains/morliv/domains/morplan.com/www`

### Stack 2 - UAT
- Frontend: [https://uat.morplan.com/](https://logicspot:l0gicsp0t@uat.morplan.com/)
  (basic auth: username: `logicspot`, password: `l0gicsp0t`)  
- Admin: [https://uat.morplan.com//moruat2020roefz  ](https://logicspot:l0gicsp0t@uat.morplan.com/moruat2020roefz)
  Admin Account: `arronm` | `arron.moss@zero1.co.uk` | `m0ss24_zero&`  
  ```bash
  php-7.4 bin/magento admin:user:create --admin-user=arronm --admin-password='m0ss24_zero&' --admin-email=arron.moss@zero1.co.uk --admin-firstname=Arron --admin-lastname=Moss
  ```
  (recreate for when it expires)
- Opcache Status: [https://uat.morplan.com/opcache_status.php](https://logicspot:l0gicsp0t@uat.morplan.com/opcache_status.php)
- Opcache Refresh: [https://uat.morplan.com/opcache.php](https://logicspot:l0gicsp0t@uat.morplan.com/opcache.php)

**Server Info**
- Webroot Directory: `/microcloud/domains/moruat/domains/uat.morplan.com/www`  


#### Logoprint
FE: https://logicspot:l0gicsp0t@biztech.morplan.com/gb_en/  
Demo Product: https://biztech.morplan.com/gb_en/57527  
BE: https://biztech.morplan.com/admin  
Username: ls-admin  
Password: Kc8ghav1$an4Lqg%o4  

## Designo
Third party system heavily integrated with Magento.

### Production Logins:  
DesignO Url : https://designo.morplan.com/app/login  
Email : Liam.Sheridan@morplan.com  
password : 12345678  

### DesignO UAT Logins:  
DesignO Url : https://designo-uat.morplan.com/app/login
Email : `adam.crossland@zero1.co.uk`
password : `fsa6^6LUHHH7FvJegLz`

### Making a product "LogoPrint"-able

**UAT**
In designo the store must:
- be enabled 
- have the store code of 1
- have the store domain of `https://uat.morplan.com/gb_en/` their api checks that the Magento store url is part of it, e.g `where like '%MAGENTO_URL%'`

In designo the product must:
- be enabled
- be in the uat store

**MDOQ Instances**
This is very much a work in progress, so far all we can do is get the button to show.

```bash
php bin/magento config:set -- base/designo_emulation/enable 1
php bin/magento config:set -- base/designo_emulation/store_code 1
php bin/magento config:set -- base/designo_emulation/domain uat.morplan.com
```
(This should be ran on instance creation)

**Dev Info**
On each product load page a request is made to the designo API, this then determine if the "Logo Print" button is visilble

```txt
url: https://designo-uat.morplan.com/api/studio/is-product-customized?SKU=F51764&id=73653&store_id=1&store_url=https://uat.morplan.com/gb_en/
result: {"success":true,"personalize_button_label":"LogoPrint","personalize_button_color":"#252525","personalize_button_text_color":"#ffffff","artwork_setup_charge_label":"Printing Charge","url":"https:\/\/designo-uat.morplan.com\/dnb\/index.html?template_id=0&id=58&ecom_prod_id=73653&qty=1&options=&form_key=eyJpdiI6ImJidlUrVkRTZ0NCRnlWQnRLMWc4Wmc9PSIsInZhbHVlIjoiV3lCTGVtRUJXZ3FVVDl3LzM0ZThaT1NEeFMxeEhCYlI4bUVleGZ1NVVWTGZPdUhLZElKZDVHZ3RvWUptZkdCS096WUE2c1FPRnB4N3NqVDNjS1NLWFZJZHBjNkZDSlRtcU1CdXQrUUNDQUE9IiwibWFjIjoiOWFhM2MwYWI1ZmQ5MzdhNjViOTQwYmExOGJhYzE1MTU3ZDlmNWZhNWQ4ZDRhOGNjYmVhZmU1ODI3NGRjODc1MiJ9&toolType=producttool&storeid=1&store_pk=14&tool_identifier=product"}
```
Magento file: `app/code/Designnbuy/W2p/Helper/Data.php:getIframeUrl` (overridden by: `extensions/zero1/design-buy-additions/Helper/Data.php`)
Designo file: `src/app/Http/Controllers/api/ProductController.php:isProductCustomized`









### Connecting to Designo on Sonassi UAT
1. Go to the "UAT" section of "Stack 2" on this wiki and login to the UAT admin using the details provided.
2. On the lefthand menu click "Designo".
3. Login to the dashboard with the "DesignO Logins" details.
4. Go to Stores > Configuration > Designo > General > Labels and set "Enable DESIGNO" to "yes".
5. Designo should now be working on Sonassi UAT.

## Deployment Process for uat.morplan.com

```
cd /domains/uat.morplan.com/___repository/releases/morplanm2-core
checkout branch / tag you want
composer install
# keeps getting uninstalled
curl -o - https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash && export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && [ -s "$NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion" && nvm install 12.20.1 && nvm use 12.20.1 && npm install --global gulp-cli && npm install --global yarn
# build theme
cd app/design/frontend/Unified/hyva/web/tailwind \
  && rm -rf node_modules && npm ci \
  && npm run build-prod \
  && cd /domains/uat.morplan.com/___repository/releases/morplanm2-core
  
php bin/magento deploy:mode:set production
php bin/magento setup:upgrade --keep-generated
php bin/magento cache:enable && php bin/magento cache:flush
```

- dont need to flush opcache


Original Release was: `current -> releases/20240705162834` (in `/domains/uat.morplan.com/___repository`)


## Integrations

### SAP TSW
Magento generates files into `var/integration/export/adrmas`
They then download these to their server and process them

#### Generating Order XML for SAP
```bash
ORDER_ID=8100295654; php bin/magento integration:order:export "${ORDER_ID}" && php bin/magento integration:job:run -- transport_order_export && ls -lath var/integration/export/order/*${ORDER_ID}*
```
Once an order xml has been generated the order status will be "sent to sap"




**Testing Orders On MDOQ**
When you make a customer you need to set "SAP Contact ID" and "SAP ID" under "Account Information" (it can be anything)
You then need to create an address for them, and get the ID.
You then need to run a db command: `insert into customer_address_entity_text (attribute_id, entity_id, value) values (230, ADDRESS_ID, 'SAP ID');`
eg: `insert into customer_address_entity_text (attribute_id, entity_id, value) values (230, 1, '321321');`
Otherwise you will get the error: "Exception: Cannot get Customer Primary Address"

#### Generating Customer Export
`php bin/magento integration:customer:export b@b.com`

#### Adrmas Export
This job is generated when a customer address is saved. (Can be triggered via the MAP)
Looks like `php bin/magento integration:customer:migrate` will generate, BUT this looks to be all customers with no way to select specific customer.

`php bin/magento integration:job:run -- transport_adrmas_export`
Outputs to: `var/integration/export/adrmas`

## Payment Testing
Cybersource test details: (https://developer.cybersource.com/hello-world/testing-guide-v1.html)[https://developer.cybersource.com/hello-world/testing-guide-v1.html]

## Ireland Store

For you're notes on EORI / XI Eori:
```
N.Ireland / UK: XI271262812000 / GB271262812000
DE: DE658374552092586
PL: PL521364994500000
N/Ireland: XI271262812000
IE: IE3570934SH
UK: GB271262812000
FR: FR81076176700039
SP: ESB75038000
```
**Rules for EORI / XI EORI**
- All non-mainland UK addresses will require a VALID EORI number.                                                    
- All Northern Ireland (BT Postcodes) addresses will require both a VALID EORI and XI EORI number.

