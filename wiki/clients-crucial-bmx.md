# Crucial BMX

[TOC]


## Selling Supplier Stock - Back Ordering
Here's another one of Arron's pikey scripts - https://docs.google.com/spreadsheets/d/1uzLILVPETS4w35n32sMJX8I8ZUSgzXNfCAULA7XJVao/edit?gid=1184307188#gid=1184307188

The above script pulls feeds and pushes back-ordering to the Magento 2 Rest API all from the Apps Scripts attached to the above.

Seventies - because this is sat behind an FTP connection this is pulled to a local location with an MDOQ Cron job `curl -u "seventies.ftp@citruslime.com:B3sFuZkbbajY" ftp://ftp.citruslime.com/Seventies_stock.txt -O`


### Removing Back Order
If a product which was on back order (supplier stocked) and Crucial get this in stock, we have a simple extension which runs at 4am on Cron via MDOQ Cron config `cd ~/htdocs && php bin/magento zero1:disable-backorder >> var/log/disable_backorders.log 2>&1` 



## POS Integration
installing the modules

Add the POS API repository to your Magento composer configuration.
Run `composer config repositories.repo-name composer https://packages.ebizmarts.com`
Then run `composer config http-basic.pos.gitlab.ebizmarts.com apiuser zPMZ7EY6cyJDHTgshzSK`
