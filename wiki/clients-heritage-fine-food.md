# Heritage Fine Food / 5 A Day Box

[TOC]

## Introduction

# Overview

## Subscriptions

### Testing a subscription that isn't due yet
**THIS IS ONLY TO BE DONE ON A DEV INSTANCE, DO NOT DO THIS ON PROD**

- get the subscription id
- in mysql helper run `update subscriptions set next_order_date = DATE_FORMAT(DATE_ADD(NOW(), INTERVAL 1 DAY), '%Y-%m-%d') where entity_id = XXXX;`
  where `XXXX` is the ID of the subscription
- on cli run `php bin/magento config:set -- payment/worldpay_futurepay/environment staging`
- on cli run `php bin/magento config:set -- payment/worldpay_futurepay/force_success 1`
- on cli run `php bin/magento cache:flush`
- on cli run `php bin/magento subscriptions:process --subscription-id=XXXX --force`
  where `XXXX` is the ID of the subscription
  

## WorldPay / Future Pay

Heritage have 2 worldpay accounts. One they refer to as new, and one as current.
At the time of writing the "new" one isn't in use on production, it is a target in future to move towards it.
All integration with worldpay is done against the current one.

The original developer of the worldpay integration was a guy called Pete (07802 481950)

Being able to capture a payment in the future without a users interation is called a "future pay" agreement.

### Current Worldpay
Within worlday the "integrations" are called installations, there can be numerous installations per account. They are akin to access credentials.
There have been a number of installations set up, not all are needed.

There needs to be seperate installations to setup a future pay agreement, and to charge/capture a payment from one.
The flow is: setup up future pay agreement (optionally capture payment at time of set up) > worldpay returns a future pay id > use the future pay agreement to capture an amount in the future.

**Admin Crentials**
- url: [https://secure.worldpay.com/sso/public/auth/login.html?serviceIdentifier=merchantadmin](https://secure.worldpay.com/sso/public/auth/login.html?serviceIdentifier=merchantadmin)
- username: `wp35305442`
- password: `nbQ8L%MJzQ`

**View Crendentials**
(cant change any details)
- url: [https://secure.worldpay.com/sso/public/auth/login.html?serviceIdentifier=merchantadmin](https://secure.worldpay.com/sso/public/auth/login.html?serviceIdentifier=merchantadmin)
- username: `adamc@wpcom99403`
- password: `7Qwf?sQ$tR44!!`


#### Setup Future Pay Agreement
This is currently done via: "1502037 (Select Junior - www.5adayboxdirect.com (Magento new))" (I'm not sure which one is used in production at the moment)  
**Current Configuration**

|Field|Test Value|Production Value|
|---|---|---|
|Installation ID:|`1502037`|`1502037`|
|Installation Reference:|`2FBF4D82C16A9B4E390CB5FC531`|`2FBF4D82C16A9B4E390CB5FC531`|
|Administration Code:|`WPCOM99403`|`WPCOM99403`|
|Company Name:|`5 A DAY BOX LIMITED`|`5 A DAY BOX LIMITED`|
|Environment|`TEST`|`Production`|
|Description|`www.5adayboxdirect.com (Magento new)`|`www.5adayboxdirect.com (Magento new)`|
|Customer description (for payment pages)|`5 A DAY BOX LIMITED`|`5 A DAY BOX LIMITED`|
|Integration type|`Select Junior(60)`|`Select Junior(60)`|
|Enforce Installation Reference|`no`|`no`|					
|Use 3D Secure Authentication?|`true`|`true`|
|Use Mastercard SPA?|`true`|`true`|
|Store-builder used|`Magento v2.x`|`Magento v2.x`|
|store-builder: if other - please specify|`Custom`|`Custom`|
|Payment Response URL|`https://staging-5adaybox-co-uk-20097.01.mdoq.io/worldpay/ipn`|`https://staging.5adaybox.co.uk/worldpay/ipn`|
|Payment Response enabled?|`yes`|`yes`|
|Shopper Redirect URL|`https://staging-5adaybox-co-uk-20097.01.mdoq.io/worldpay/ipn/success`|`https://staging.5adaybox.co.uk/worldpay/ipn/succes`|
|Shopper Redirect button enabled? (Note: If set to true, the "Shopper Redirect URL" field must also be supplied)|`no`|`no`|
|Enable Recurring Payment Response|`yes`|`yes`|
|Enable the Shopper Response|`yes`|`yes`|
|Suspension of Payment Response|`no`|`no`|
|Payment Response failure count|`0`|`0`|
|Payment Response failure email address|`adam.crossland@zero1.co.uk`|`adam.crossland@zero1.co.uk`|
|Attach HTTP(s) Payment Message to the failure email?|`yes`|`yes`|
|Merchant receipt email address (if set, overrides value at Merchant Code level)|`adam.crossland@zero1.co.uk`|`adam.crossland@zero1.co.uk`|
|Enable Mobile Pages?|`no`|`no`|
|No Worldpay Header enabled?|`no`|`no`|
|Remove Breadcrumb?|`no`|`no`|
|Info servlet password|`pg!1*&d6%TRu^3sYxfwa`|`nR%sCE&yWTtBVxHZv&6Y`|
|Payment Response password|`$S3^#wdKV&ZyRsV7DX%k`|`C4v1cYV^d5$Ekb5B1fN&`|
|MD5 secret for transactions|`$e6fD$%eF&jje8UDb9^B`|`xTkHbFVzk&TnJ@J!Fz8W`|
|SignatureFields|`instId:amount:currency:cartId`|`instId:amount:currency:cartId`|

**Original Production Configuration**
For the configuration pre ZERO1/Magento, there is file in the teamwork project called `Changes for Worldpay Installation.xlsx`. I have locked it, so it shouldn't get deleted.
**dont click anything on these, no idea what will happen**
https://www.5adaybox.co.uk/testcc.aspx
https://www.5adaybox.co.uk/test2.aspx
https://www.5adaybox.co.uk/test.aspx

https://www.5adaybox.co.uk/testfppayment.htm
https://www.5adaybox.co.uk/testfuture.aspx
https://www.5adaybox.co.uk/testfuture.htm

#### Capture Payment
This is currently done via: "141962 (Select Junior - remote admin only)"
**Current Configuration**
|Field|Value|
|-|-|
|Installation ID:|`141962`|
|Installation Reference:|`94C94D79BE96E51DD7599E3BF41`|
|Administration Code:|`WPCOM99403`|
|Auth Password:|`tiaVou4lAG`|


#### Testing

Test Card Details
https://developer.worldpay.com/products/access/card-payments/testing/
http://support.worldpay.com/support/kb/bg/testandgolive/tgl5103.html
http://support.worldpay.com/support/kb/bg/htmlredirect/Content/rhtml/Test_Card_Numbers.htm

Test url (may go in future)
https://staging-5adaybox-co-uk-20097.01.mdoq.io/worldpay/testpayment/index?888

#### Support
Contacting support is painful
Telephone: 0330 333 1233 Option 6.
You also need to know the following info
- Registered Contact Info
  GREENGATE HOUSE,87 PICKWICK ROAD,CORSHAM, SN13 9BY
  LOWERFIELDS FARM,BYSTONE LANE,COATE,DEVIZES, SN10 3LQ
- Bank Account:
  Name: Lloyds Bank PLC, 38 The Market Place, Devizes, Wiltshire SN10 1JD
  Sort Code: 30 92 63
  Account Number: 24209360
- Account Name: The Heritage Fine Food Company Limited
- Trading Name: 5 A Day Box
- Merchant ID: WPACC65140658
- Admin Code: WPCOM99403

If they agree to email you, they will only do it for the email on the account, this is Ken (kenmortimer@5adaybox.co.uk), he will need to forward the email on to you.

### New Worldpay
**Admin Credentials**
- url: [https://secure.worldpay.com/merchant/common/start.html?jlbz=WecX4WBnZuaBtXnJHeN6MfUJcYhIS5q5k50KuoKPS4](https://secure.worldpay.com/merchant/common/start.html?jlbz=WecX4WBnZuaBtXnJHeN6MfUJcYhIS5q5k50KuoKPS4)
- username: `admin@theheritagef`
- password: `Tt6EE(LD@@!`


### Dev Stuff
Documentation for this system is c**** to say the least
**Futurepay docs**
http://support.worldpay.com/support/kb/bg/recurringpayments/rpfp7105.html
http://support.worldpay.com/support/kb/bg/recurringpayments/rpfp7104.html
http://support.worldpay.com/support/kb/bg/recurringpayments/rpfp7100.html
http://support.worldpay.com/support/kb/bg/recurringpayments/rpfp8105.html

**Md5 / security hash**
http://support.worldpay.com/support/kb/bg/htmlredirect/Content/rhtml/Enhance_security_with_MD5.htm

**Forcing/Hacking a subscription in**
1. create customer
2. add address
3. add items
4. go through checkout, as soon as you're redirected to worldpay can stop.
5. In the MAP get the order ID (increment)
6. In the MAP make sure worldpay is in **Staging mode** and **Debug is enabled**
7. In postman, make a new env for the instance (just need the base url)
8. In postman, open the request Worldpay > POST ProcessIpnResponse
  Set `cartId` to order increment ID
9. Make the request, it will error.
  Go to map an look for a comment on the order like: `Worldpay IPN: Unable authorize the request.Was expecting MC_validation: "XXXXX", got: "YYYYY"`
10. In postman, set `MC_validation` to what ever was "expected" in the previous comment
11. Make the postman request again.

That should be it?


**Other Links**
http://support.worldpay.com/support/kb/bg/recurringpayments/rpfp8103.html
http://support.worldpay.com/support/kb/bg/recurringpayments/rpfp8105.html
http://support.worldpay.com/support/kb/bg/recurringpayments/rpfp8009.html
http://support.worldpay.com/support/kb/bg/htmlredirect/Content/rhtml/Integrate_your_website_with.htm
http://support.worldpay.com/support/kb/bg/htmlredirect/Content/rhtml/HTML_Redirect_parameters.htm#_Recurring_payments_(FuturePay)
http://support.worldpay.com/support/kb/bg/testandgolive/tgl5102.html
https://developerengine.fisglobal.com/apis/bg350
https://developerengine.fisglobal.com/apis/bg350/integratedeveloper


There is a postman collection in the "Team Workspace"
