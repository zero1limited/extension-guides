# Professional Books

[TOC]

## Introduction

## Overview

## 3rd Party Extensions Purchased

All details here >>>>> 


## Emails


## Common Issues

### Orders failing to get to Linnworks
If an order is placed using Rvvup "Pay by Bank", the invoice can fail to generate. If the client raises an issue because the order did not reach linnworks then you can simply locate the order and 'Invoice' it using the invoice button. If the invoice does not progress to 'Processing' please escalate to 3rd line.

3rd line execute the SQL `UPDATE sales_order SET state='processing', status='processing' WHERE entity_id=22237`
