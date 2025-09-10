# British Hardwood

[TOC]

## Growmaster
Orders are pushed into Growmaster as they are placed

Product updates are pulled into Magento every 2 hours from the this [import.php](https://github.com/zero1limited/treesandhedging.co.uk/blob/master/app/code/local/Webby/Growmaster/Model/Product/Import.php)

### Web Testing
#### [All Customers](view-source:http://portal.greenfieldsoftware.co.uk/GrowMaster/growmasterapi.svc/get_all_customers?siteid=21&username=BHT21&password=Britw00d)


In order to test this on UAT (as an example)
In MySQL Helper container do
```
truncate mghk_cron_schedule;
INSERT INTO `mghk_cron_schedule` (`job_code`,`status`,`messages`,`scheduled_at`,`executed_at`,`finished_at`) VALUES ('growmaster_execute','pending',NULL,NOW(),NULL,NULL);
```

SSH in
```
cd ~/htdocs && rm var/log/gromaster-product.log 
php cron.php
tail -f var/log/gromaster-product.log
```


Logs are available here
https://www.treesandhedging.co.uk/growmaster-log.php?pass=v8u8dH1Cs7Drhhv9fHCNUPQ8a

## Middleware v2

This middleware currenlty lives on the ZERO1 middleware server.
```
Host zero1_middleware
    User zero1
    Hostname 54.36.166.28
    Port 22
    IdentityFile ~/.ssh/zero1_middleware
    IdentitiesOnly yes
```
(currently accessible from the MDOQ bastion)

It's running the docker compose stack specified in the repo.
Repo: https://github.com/zero1limited/bht-growmaster-middleware

Docs on what functions are available are in the repo.

Frontend: http://54.36.166.28:82/
(not much there but useful when pulling files down)

**Owners**: ZERO1 - we are responsible for debug and dev
**Source**: Custom module, ZERO1 ported from a module to a middleware
**Logs**: download from server, laravel storage dir

## Commercial Extensions
| Name | Version | Who purchased? | Login details for vendor |
|-|-|-|-|
