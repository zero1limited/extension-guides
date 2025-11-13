# Google Analytics 4

[TOC]



We are using Yireo `yireo/magento2-googletagmanager2`
https://github.com/yireo/Yireo_GoogleTagManager2/blob/master/USAGE.md

### Pitch

As part of the prepation for the migration from Google Universal Analytics to Google Analytics 4, we are raising this recommendation so that we can begin to track basic traffic inforamtion and also Ecommerce data. 

Google Analytics 4 is drastically different from Universal Analytics. The functionality covered includes the following:

• view_item, view_item_list
• select_item
• add_to_cart, remove_from_cart
• login, logout
• view_promotion, select_promotion
• add_to_wishlist
• add_to_cart, remove_from_cart, view_cart
• begin_checkout, add_shipping_info, add_payment_info, purchase


Requirements: 
You already have a functional Google Tag Manager Account
We must have administrative acess to GTM and Google Analytics


### Installation Instructions


With the MDOQ instance please login to SSH then `composer require yireo/magento2-googletagmanager2`



### Setup & Configuration - Marketing
You must have access to Google Tag Manager and the relevant GA4 account before you can install this.

Download the file [gtm-wd64xt2_v9.json](/gtm-wd64xt2_v9.json) and import it into GTM, ensuring you Merge (don't Replace)

### Keywords

#### yireo ga4 analytics google gtm google tag manager