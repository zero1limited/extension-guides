# Instructions

<!--
[Module on GitHub](https://github.com/zero1limited/magento2-improved-checkout-success-page)

[Module on Packagist](https://packagist.org/packages/zero1/module-improved-checkout-success-page)

## Pitch Email

Demonstration video for Improved Checkout Success Page - https://share.vidyard.com/watch/3HTsyPopBXvfDw1ZTGjVbj

The checkout success page is the final step in the customers journey on your site. 
It's very easy to lose sight of the checkout success page and it may seem like it's one of the least important parts of the customer's journey, but it's actually very important. It’s make or break when it comes to turning first-time shoppers into occasional and loyal customers.

Imagine inviting a friend over at your house on a Friday night. You make sure your house is warm & inviting, and you have a lovely sit down meal over some great conversation. You spend the night having a great time... Then, just when it’s time for your friend to leave, you suddenly disappear. You expect him/her to find their own way out, and close the door behind themselves. No matter how great of an evening you've both had, they probably won’t be coming over again any time soon... Now imagine that same scenario, but instead of disappearing you politely see your friend out. You tell them what a great time you had, and that you would love to get together again soon. Sounds much better than the first scenario doesn’t it?

This is exactly what we should be doing with your online customers at the checkout success page to convince them to come back for more.

A lot of time, effort and money is spent aquiring new customers, but it's easy to forget that customer retention is most profitable. In fact, your revenue would double if only 10% more of your current customers came back for a second purchase!

Magento's core checkout success page is poor and we strongly recommend using this Improved Checkout Success Page to gain all of the benfits mentioned above with the following features:

- Fully customisable "Thank You" message
- Ability to address customers by their name
- Ability to address guest customers by their checkout name
- More detailed and attractive order information
- Ability to add retention offers and promotions such as "Get X% off your next order"
- Showcase a list of related products
- Showcase Newsletter Signup to help increase email subscriptions
- Ability to change the display order of all features

As mentioned above, one feature of the improved checkout success page is the ability to add retention offers and promotions via static blocks. If you would like to implement the same method shown in the video, please supply us with the static block's name or ID when approving this task.
-->

Create an MDOQ dev instance for the relevant client
ssh onto the new instance then run the following commands...

```
cd htdocs
```
```
composer config repositories.zero1-magento2 git "https://github.com/zero1limited/magento2-improved-checkout-success-page"
```
```
composer require zero1/module-improved-checkout-success-page
```
```
php bin/magento module:enable Zero1_ImprovedCheckoutSuccessPage
```
```
php bin/magento setup:upgrade
```
```
php bin/magento cache:flush
```

> Before proceeding, please check on the Teamwork ticket whether the client has mentioned which static block they'd like to use.
{.is-danger}

If they DID provide a static block name or ID, please take note of this as it can be configured within QA. 
If they DID NOT provide a name or ID, don't worry about it...

---

To make configuration that bit faster on the frontend, enable the Bank Transfer payment method if it isn't already...
- Go to MAP > Stores > Config > Sales | Payment Methods
- Scroll down to Bank Transfer Payment and enable it

---

### Configure the module

Go to Stores > Config > Sales | Improved Success Page

Set "Use checkout name for guest customers" to Yes
Add the following text in the "Intro text" field...
```
Your order has been received and we're currently processing it now. You'll soon receive an email with your order details. 

If you have any questions at all, please don't hesitate to get in touch!
```

If the client provided a block name or ID, please complete the step below; otherwise, just save config and you're done

**Block provided:**
Scroll down to CMS Static Block Row
Set "Show static block row" to yes
Now select the name of the block the client asked for

Save config

### Completion

Now the configuration and testing is finished, go to your MDOQ instance and open the Github GUI
Git push, then select the following files...

```
composer.json
composer.lock
app/etc/config.php
```

Once the push is successful, please leave the instance where it is and pass to QA

# QA

- Go to the frontend and find a product (preferably one with related products assigned but this isn't a huge issue if you can't fine one)
- Add it to basket and go through checkout using Bank Transfer
- Place the order

(Please screenshot the success page to attach to the ticket later on)

When the success page loads, you should see 3 boxes with the order information on there. Underneath this you'll see the block you've just assigned (if there was one to assign), related products (if the product has related products) and then the newsletter signup button.

If you're still not 100% whether the module is present; right click > view page source > find "zero1-advanced-success" and if it's there, it will be working as expected

> **Important:** When passing the ticket back to the Zero1 owner, please copy the note below onto the ticket before assigning it back to the owner. Please also attach the screenshot you got from earlier. Thanks!
{.is-danger}


> // TODO - Pre-production check for frontend developer
> 
> Before we can go into production with this module, we need to check whether the client in question has any custom code changes applied to their (old) checkout success page (success.phtml) that will result in losing or affecting the client's analytics / conversion data once the new success page is live.
{.is-info}
