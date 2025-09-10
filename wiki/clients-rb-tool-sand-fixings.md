# RB Tools

[TOC]


## General Configuration

### Payment module
There is the module `BSS_Paymentshipping` this module hides/displays shipping and payment methods depending on the customer group.
(So if you enable checkmo on an instance and cant see it you will likely need to go to Stores > "Methods For Customer" > "Payment")
**N.B** this module also takes effect in the admin! ! ! ! !


## Merlin Integration
All stuff about the Merlin system.

### Access Credentials

http://18.169.208.165:8182/merlin.asmx (Training database)
Datasource: mbstrain
Company: 1
Depot: 01
Account: WEB001

http://18.169.208.165:8181/merlin.asmx (Live database)
Datasource: mbs01
Company: 1
Depot: 01
Account: WEB001

> Your IP needs to be whitelisted to access, to get added to the whitelist you need to email: support@merlinsw.co.uk
{.is-info}


### Magento Module

The module `Zero1_MerlinErp` located in `app/code` performs the following tasks:
- [Get Stock](#get-stock)
- [Send Orders](#send-orders)
- [Update Stock Mappings](#update-stock-mappings)

The module is configured at: Stores > Configuration > Services > Merlin ERP
The module logs to it's own log file: `var/log/zero1/merlin_erp.log`

#### Get Stock
This job runs `0 */2 * * *`. It pulls all stock values from Merlin and then updates Magento, if the stock value in Magento is different to that in Merlin.

It might be possible to run this job more frequntly when live, but at present the catalog only contains ~20 products, so I have been unable to test to get an accurate idea of performance.

This job can be ran manully.
```
magento@15177-php-fpm:~/htdocs$ php bin/magento zero1:merlin:get-stock --help
Description:
  Get stock from Merlin ERP and update product(s) within Magento

Usage:
  zero1:merlin:get-stock [options]

Options:
      --skus[=SKUS]     If supplied only process specific skus (comma separated list of skus)
  -h, --help            Display this help message
  -q, --quiet           Do not output any message
  -V, --version         Display this application version
      --ansi            Force ANSI output
      --no-ansi         Disable ANSI output
  -n, --no-interaction  Do not ask any interactive question
  -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug
```

#### Send Orders
This job runs `*/5 * * * *` . It gets all order from Magento that have been updated in the last 24 hours, are at state processing and dont have a comment starting with `ORDER SENT TO MERLIN`. It then sends these orders to Merlin and adds a comment to the order `ORDER SENT TO MERLIN: XXXXXXX` where `XXXXXXX` is the ID of the order in Merlin.

This job can be ran manually.
```
magento@15177-php-fpm:~/htdocs$ php bin/magento zero1:merlin:send-orders --help
Description:
  Send Magento Order to Merlin ERP

Usage:
  zero1:merlin:send-orders [options]

Options:
      --orders[=ORDERS]  If supplied process specific orders (comma separated list of order ids (entity or increment))
      --force            Force orders to be resent to Merlin
  -h, --help             Display this help message
  -q, --quiet            Do not output any message
  -V, --version          Display this application version
      --ansi             Force ANSI output
      --no-ansi          Disable ANSI output
  -n, --no-interaction   Do not ask any interactive question
  -v|vv|vvv, --verbose   Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug
```

#### Update Stock Mappings
This job runs `0 * * * *` it gets all stock ids from Merlin (with their associated `part`) and tries to match `part` to a `sku` within Magento. If a product with a matching sku is found it is added to the mapping data `var/merlin/stock_lookup.json`.
This lookup is used by other Merlin processes, so we don't have to keep calling Marlin when we need a stockid.

This job can be ran manually
```
magento@15177-php-fpm:~/htdocs$ php bin/magento zero1:merlin:update-stock-mappings --help
Description:
  Get stockid and part from Merlin ERP and store for future use.

Usage:
  zero1:merlin:update-stock-mappings [options]

Options:
      --skus[=SKUS]     If supplied only process specific skus (comma separated list of skus)
  -h, --help            Display this help message
  -q, --quiet           Do not output any message
  -V, --version         Display this application version
      --ansi            Force ANSI output
      --no-ansi         Disable ANSI output
  -n, --no-interaction  Do not ask any interactive question
  -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug
```

