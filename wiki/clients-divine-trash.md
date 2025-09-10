# Divine Trash

[TOC]


# Clients WIKI Overview

[TOC]

In progress

## Overview
How we won this client


## Roles & Responsibilities

### Our responsibilities
- Testing - We use automated tests, client does their own testing and signs off



## Key Stakeholder(s)

## Customisations

## Integrations (3rd Party)


### linnworks.net


### Royal Mail Click & Drop



## Payment Engines


## Links

MDOQ Org
Teamwork Project
Teamwork customer-facing WIKI






















# OLD STUFF

OCustomisation and Test Plan


The following are created upon instance creation

- Test Gift Card Code
- Leopard Mug U401119G / 70795 - 100 qty added

Test the connectivity to Magento from POS (from CLI on the instance)
```
tail -f var/log/pos-api.log
tail -f mdoq/var/log/nginx/www-divinetrash-co-uk-11515.00.mdoq.io.443.access.log
```


## Key Documents

[New DT Merchandiser](https://docs.google.com/spreadsheets/d/1iH0OlKyP6dnCsQYqAsKpPu5MNfDGLDHZy5qWjTKLZTo/edit#gid=0) used to create Purchase Orders which are then posted into Linnworks and Akekeo together

The above document also contains some automation including the processing/completing of Shop Orders via the script/function completeShopOrders (see below)



## Linnworks

**Processing/Completing Shop Orders automatically**
Function sdfsdfdsfdsf(https://script.google.com/d/1MqxF3TIJ2XzUfpG5rrOatMgkDpRI4OkAOmlcxv7yKBFbu9pXVTXzilMg/edit?mid=ACjPJvFOjKL4xdeRzS2-mSwAmy79pOPzUsOoEEzED4o-_oxaOoWXyxU78mFi6gkaMo0Z2SV8duxe8MSGjs6gfU-OrHsQjT_CSUbevXeUl4qDB-Rg8zNJz5Ks72mcRe2-_AkXvW6vazsHbZzc&uiv=2)

If the above script suddenly fails to stop working, the pairLinn function may need running/debugging manually again. I did this 13 May 2022 (after not touching it for years) and it resolved.

## Commercial Extensions
| Name | Version | Who purchased? | Login details for vendor |
|-|-|-|-|