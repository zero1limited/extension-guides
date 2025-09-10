# Testing Payments
Various payment options for our trusted/preferred methods

[TOC]


## Super Payments

https://business.test.superpayments.com/

arron.moss@zero1.co.uk
KEY PSK_E9VOOO7aMZLfSEECZBBdl8cntk-l0hm1qtrajpJc
PWH_lK4m4u81NdOviusO7mrugIAIynE9H-BS9To2X-X7







## PayPal

If you need to test end-to-end payments instance you need to carry out the configuration steps below.

Configuring your store for PayPal Express Checkout Sandbox

In order to implement this configuration create a file in your repo called `mdoq/env.sh` this can house all your MDOQ specific functions which will configure the instance to sandbox mode as required.


<!--

Username:
sales-facilitator_api1.zero1.co.uk

Password:
6HL7CUAK9V2J3FSE

Signature:
AiPeH78BLxB7YLrrYyi2Uj3xnq-eAgSvusMe5a4.2bCWEq5RvOAaPJ.y

```
php bin/magento config:set paypal/wpp/api_username sales-facilitator_api1.zero1.co.uk
php bin/magento config:set paypal/wpp/api_password 6HL7CUAK9V2J3FSE 
php bin/magento config:set paypal/wpp/api_signature AiPeH78BLxB7YLrrYyi2Uj3xnq-eAgSvusMe5a4.2bCWEq5RvOAaPJ.y 
php bin/magento config:set paypal/general/business_account arron.moss@zero1.co.uk
php bin/magento config:set paypal/wpp/sandbox_flag 1 

```
Once the file is in place then you can simply add this to your Post Release Actions in the main Connector in MDOQ Ie.

`/home/magento/htdocs/mdoq/env.sh` ensuring your file is executable



2) Enter the following details:

Placing Test Orders with PayPal Checkout Express
buyer_1340611261_per@zero1.co.uk / 340611237
testing+1234@zero1.co.uk / testing321 

Email Associated with PayPal Merchant Account: arron.moss@zero1.co.uk
API Authentication Methods: 'API Signature'
API Username: arron_1340611024_biz_api1.zero1.co.uk
API Password: 1340611051
API Signature: AFcWxV21C7fd0v3bYYYRCpSSRl31An0GU8SKVIlomACHV5aW22xQDJgn
Sandbox Mode: 'Yes'
Enable this Solution: 'Yes'
-->


> The values below dont work from the CLI, because they are stored encrypted, you need to set them, then extract the encrypted values from the DB in order to get the encrypted values
{.is-warning}


```
#paypal test
php bin/magento config:set paypal/wpp/api_username arron.moss+sandboxbusiness_api1.zero1.co.uk
php bin/magento config:set paypal/wpp/api_password JDDJ8PDDH6XATT2U
php bin/magento config:set paypal/wpp/api_signature AN7RYZQ.31bZqTgC8c9AIBbiy4tkA3-oEyYqgcMiCqDxuTpGl8M-7Q0Q
php bin/magento config:set paypal/general/business_account arron.moss@zero1.co.uk
php bin/magento config:set paypal/wpp/sandbox_flag 1
```
## Paypal sandbox account
All these details are accessible via Arron's account arron.moss@zero1.co.uk via https://developer.paypal.com/developer/accounts/

| When             | Message                                                    |
|------------------|------------------------------------------------------------|
| Seller Username  | arron.moss+sandboxbusiness_api1.zero1.co.uk                |
| Seller Password  | `JDDJ8PDDH6XATT2U`                                         |
| Seller Signature | `AN7RYZQ.31bZqTgC8c9AIBbiy4tkA3-oEyYqgcMiCqDxuTpGl8M-7Q0Q` |
| Buyer Email      | sb-o7uli4928386@personal.example.com                       |
| Buyer Password   | `8Z$sVKq[`                                                 |


Merchant Account ID (used for In-Context Checkout Experience): `CL2KZQ95NHDZW`


https://developer.apple.com/apple-pay/sandbox-testing/
login here with zero1commerce email https://appstoreconnect.apple.com/access/users/sandbox

sandboxtester@zero1.co.uk
QLK3J4KJQ34a

## Opayo
This test plan assumes you are testing a Magento Checkout which has SagePay Suite CE or Pro installed and in TEST mode (need to ensure that all integration options are set to TEST even if Disabled).

Using the details from the current SagePay Test Card details page simply checkout

For quick reference [refer to the Opayo test details](https://www.opayo.co.uk/support/15/36/test-card-details-for-your-test-transactions)

We are in the process of standardising the test process for Sagepay. All live sites, when taken and rolled up in UAT, will have SagePay account settings updated to TEST mode and set to zero1ltd vendor. You should get a notice at checkout informing you that the license is not valid, however on UAT this is expected and not considered an issue with the testing process. We do not request keys for UAT instances given they can change.

You can then use these details to check transactions in Sage Pay

License Key: XXXXXXXXXXXXX

https://test.sagepay.com/mysagepay/settings.msp

Vendor: zero1ltd

User: uat

Password: us3rAccept4nc3!

Integration Key OGkLlMTucMotVDlfYbH7ll73QQwXh6WhhtI7hYfmZSLjleMAJ1

Integration Password ilSjj2L3cnNpNpgK0kKZr4Zgl3TrexKtq7p82V5BHWM3PxQEQ0awcogOEHU0flxEb

```
bin/magento config:set sagepaysuite/global/reporting_user uat
bin/magento config:set sagepaysuite/global/reporting_password us3rAccept4nc3!
```

### Klarna Playground

**Manage keys [here](https://portal.playground.klarna.com/settings/api-keys)**

**Manage Clients [here](https://portal.playground.klarna.com/settings/client-identifier)**

#### Credentials (correct as of 28/07/2025):
- Username: testing@zero1.co.uk
- Password: 22XkaPB2usjhxn!

#### Modules:
- Klarna Payments: `composer require klarna/m2-klarna`
- Hyvä Compat: `composer require hyva-themes/magento2-klarna-kp`

### New Details for Sagepay PI
Accessing SagePay Test in order to authorise new IP addresses
https://test.sagepay.com/mysagepay/settings.msp

Merchant ID 43244643
zero1ltd / zero1ltd
Sd4#dkd33jjedRR



Environment: TEST
Vendor Name: zero1ltd

Integration Key: `OGkLlMTucMotVDlfYbH7ll73QQwXh6WhhtI7hYfmZSLjleMAJ1`

Integration Password: `ilSjj2L3cnNpNpgK0kKZr4Zgl3TrexKtq7p82V5BHWM3PxQEQ0awcogOEHU0flxEb`

In order to bake the above into ./mdoq/env.sh you need to run the below command and add the output to the env.sh alon with the other bin/magento command below.

```

m2db_host=$(php -r '$env = include "./app/etc/env.php"; echo $env["db"]["connection"]["default"]["host"].PHP_EOL;');
m2db_user=$(php -r '$env = include "./app/etc/env.php"; echo $env["db"]["connection"]["default"]["username"].PHP_EOL;');
m2db_password=$(php -r '$env = include "./app/etc/env.php"; echo $env["db"]["connection"]["default"]["password"].PHP_EOL;');
m2db_database=$(php -r '$env = include "./app/etc/env.php"; echo $env["db"]["connection"]["default"]["dbname"].PHP_EOL;');
echo "USE ${m2db_database}; select CONCAT('bin/magento config:set ',path,' ',value) as '' FROM core_config_data WHERE path ='payment/sagepaysuitepi/password';" | mysql -h ${m2db_host} -u ${m2db_user} -p${m2db_password};

```

add these to env.sh
```
bin/magento config:set payment/sagepaysuitepi/key OGkLlMTucMotVDlfYbH7ll73QQwXh6WhhtI7hYfmZSLjleMAJ1
value output from the above command
```



---





Testing transactions from New servers / Adding New IPs to SagePay Test

If we are configuring a new server for a client which will eventually be the live server, the mySagePay account will need updating with the IP address of the server.

Obtain the IP address of the server from the Project Manager
Login to the SagePay Test Portal (details above)
Navigate to the Valid IPs section
Add the IP address but in the following format, if there are LESS than 3 number between dots, always prefix with zeros to arrive at 3 digits.
Eg 12.1.56.456 should be entered as 012.001.056.456
Add the Subnet of 255.255.255.000
You need to make sure that all payment method types are set to Test (even if disabled)!!

Form Payment option

For Sage Pay Suite Form integration we have a slightly different setup

Form Integration Encryption Password J1zR167BRucTnGqG



## Braintree

https://sandbox.braintreegateway.com/login

arron.moss@zero1.co.uk / 24bAsiL54



Merchant Account ID: djkdx3qbb3yn8krq
Merchant ID: djkdx3qbb3yn8krq

Public Key: 86nxkd2z7yzmwgwg

Private Key: e089f0122e0cc2c3a0ae1f0576b031a3

**Testing details**

**Test Value	Card Type**

378282246310005	**American Express**
371449635398431	**American Express**
6011111111111117	**Discover**
3530111333300000	**JCB**
6304000000000000	**Maestro**
5555555555554444	**Mastercard**
4111111111111111	**Visa**
4005519200000004	**Visa**
4009348888881881	**Visa**
4012000033330026	**Visa**
4012000077777777	**Visa**
4012888888881881	**Visa**
4217651111111119	**Visa**
4500600000000061	**Visa**

### Tools Today Sandbox Braintree Details

Public key: 5rf9394gqsbxzk2w

Private key: ade4ace244eaf15135e6da2e950523fc

Merchant ID: 4j6xsm9fryj3q88m

Merchant Account ID: Tools_Today

**Login Details**

https://sandbox.braintreegateway.com/

ToolsToday / kQ%CB54Nhd



## Adyen
https://docs.adyen.com/development-resources/test-cards/test-card-numbers



## Stripe
Currently using Stripe we have mercyrobes.com

/mdoq/post_roll_up_actions
```bash
function testStripe(){
    bin/magento config:set payment/stripe_payments_basic/stripe_mode test
    bin/magento config:set payment/stripe_payments_basic/stripe_live_pk ''
    bin/magento config:set payment/stripe_payments_basic/stripe_live_sk ''
    bin/magento config:set payment/stripe_payments_subscriptions/active 0
}
```



https://stripe.com/docs/testing?locale=en-GB



## Mollie

All options can be found here: [https://docs.mollie.com/overview/testing](https://docs.mollie.com/overview/testing)

Quick details:  
**Card Number:** `2223 0000 1047 9399`  
**Expiry:** anything in the future
**CVV** anything

## Mollie ApplePay

If the mollie Applepay service hangs it maybe that the following request does not reach the server due to Cloudflare issues. This is a non-eu location request therefore (as with WOP) it was blocked from access to the site
```
162.158.6.96 - - [04/Aug/2024:06:53:27 +0000] "POST /mollie/applePay/shippingMethods HTTP/2.0" 200 5901 "https://www.sipuk.co.uk/checkout/cart/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
```


**Testing ApplePay**
Use a compatible device and ensure Mollie is in LIVE mode. To place an order use a real card. The order will land in the clients Mollie account - this can then be refunded from within the Mollie Dashboard.

**Raising a ticket with Mollie**
If you have access to the clients account you can click 'chat with us' to start a livechat with Mollie. Another method is to visit:
https://www.mollie.com/contact/merchants

**You will need to get the clients Mollie ID before contacting Mollie (You can find your Mollie ID in the top left of your Mollie Dashboard.)**



## Viva Smart Checkout
All these details are accessible via Arron's account: https://demo.vivapayments.com/selfcare/en/security/apiaccess

Phone Number: 7971217574

Password: X4rgfSu3p!nhL77

2FA Code: 111111

Test cards: https://developer.viva.com/integration-reference/test-cards-and-environments/

| Config Setting  | Value                                                 |
|-----------------|-------------------------------------------------------|
| MerchantID      | 1fd172c9-2245-450f-948b-0e70fda87482                  |
| API Key         | zG{cj!                                                |
| Source Code     | Default                                               |
| OrderCode URL   | https://demo.vivapayments.com/api/orders              |
| Gateway URL     | https://demo.vivapayments.com/web/newtransaction.aspx |
| Transaction URL | https://demo.vivapayments.com/api/transactions        |      




## Authorize.net

Create a sandbox account at https://developer.authorize.net/hello_world/sandbox.html, that should be about it.

This account is owned by auth.net.testing@zero1.co.uk which is a group list containing arron.moss@zero1.co.uk & callum.breeze@zero1.co.uk

zero1comllc
878u9tZ3N2x)fZb$

```
API Login ID:	7XGxg42dy
Current Transaction Key:	 69eZP9Q9h844x229

Current Signature Key:	
9795DA8DD7D74310D63A16580A9DD69E116621197CD189ABA0478A989542A2E3CCC075CFF0E8F18073AB2E72D41651B83D244CF0C8B6C138FF7DDBE73F89AA9D
```

### Old account - needs reviewing

https://developer.authorize.net/hello_world/testing_guide.html

authorise.net SANDBOX
Site: https://sandbox.authorize.net/
Username: zero1limited
Old Password: ASKDJFhk2j4h5
New Password: hb7t0ZoUU!xE$$6D@eFf

API LOGIN ID: 44ntu8KA6a9
TRANSACTION KEY: 6mW4G256p9SwQcrV
KEY: Simon

New Client Key: 9x7rddT2q5AG8Ex2hJ5m88vsdXQ4629gY8uxpceMVfLzNkm4JA4NPY77tcKd7zW5

Test Card Numbers

The following test credit card numbers will only work in the sandbox. Use any expiration date after today’s date. If the card code is required, please use any 3-digit combination for Visa, Mastercard, Discover, Diners Club, EnRoute, and JCB; use a 4-digit combination for American Express.



Test Card Brand	Number

**American Express** 	370000000000002
**Discover**	6011000000000012
**JCB**  	3088000000000017
**Diners Club/ Carte Blanche**	38000000000006
**Visa** :4007000000027
4012888818888
4111111111111111
**Mastercard** :	5424000000000015
2223000010309703
2223000010309711


