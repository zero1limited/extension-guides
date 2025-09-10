# Roys Client Support Wiki
[TOC]
All relevant wiki's for Roys and Highways should be linked to from here. Please also include any other related items / notes that might help 1st line support

## Events
(**N.B** If you know better please update this)

Roys host a few events at different locations.
- [Shoe Fittings](#shoe-fittings)
- [Santas Grotto](#santas-grotto)
- [Afternoon Tea](#afternoon-tea)
- [Afternoon Tea With Santa](#afternoon-tea-with-santa)

Initially all these events had their own behaviours, however these differences are now unknown.
At the point of writing the only event I could get working was grotto event.
The events "system" is currently heavily reliant on `Aheadworks_AjaxCartPro`, if this module changes there is a strong chance it will break events.
The events "system" is also reliant on `Zero1_TrueBasket`

At the moment because Santas Grotto is the underlying theme, this means they can only run 1 event at a time.

### Shoe Fittings

#### Description
Allow a customer to select a location and date, they will then be able to pick an available time to "book".
- This is only implemented for Roys (i think)
- There is no price

#### Setup / Configuration

**Category Setup**
**FOR SOME REASON THIS CONFIGURATION HAS BEEN DONE AT STORE VIEW**
1. Enable category (Roys > Events > Show Fittings)
2. (Optionaly) "Include in Menu"
3. Display Settings > Layered Navigation Filters
    Event Location should be pinned at the top, and display mode should be "Always displayed"
    Event Date should be pinned second, and display mode should be "Always displayed"
4. Theme should be set to "Events"
5. Layout should be set to "No layout updates"

**Product Setup**
It looks like they type of product matters, they must be virtual, otherwise checkout gets a bit wonky.
Before creating products ensure all the Event Dates and Event Times are present in the attributes `event_date` and `event_time`

1. Create a vritual product
  - **Name** the name of the product doesnt matter functionally though convension is `Shoe Fittings 2024-050-27/07/2024-09:00`
  - **Attribute Set** Events
  - **Categroy** ensure the product is in the event category
  - **Visibility** ensure the product is visibile in `catalog`
  - **Event Location** set the location
  - **Event Date** set the event date
  - **Event Time** set the event time
  - Assign stock source and give it some stock, ideally should match **Event Location** but technically doesn't have to.

2. Reindex and flush cache


**CMS Block Setup**
On the category page for each filter there is a top and bottom cms block. see `app/design/frontend/z1/events/Smile_ElasticsuiteCatalog/templates/layer/view.phtml` for the logic.
Once of the most important bits, is the blocks that are active. At present the block tree looks like
- event_shoefittings_filter_eventlocation_content_top
  - event_shoefittings_landing_page_content_top
    - shoe-fitting-active
    - shoe-fitting-inactive
  
When enabling a shoes event:
- `shoe-fitting-active` cms block needs enabling
- `shoe-fitting-inactive` cms block needs disabling
When disabling a shoes event:
- `shoe-fitting-active` cms block needs disabling
- `shoe-fitting-inactive` cms block needs enabling


**Misc Setup**
- **Calendar Year** - The year the calendar loads when viewing the category. This is configured via the _plain_ value of the variable `all_events_year`. The value should be in `YYYY` format.
  **N.B** this variable affects _all_ events.
- **Calendar Month** - The start and end month for the event. This is configured with the variable `roys_events_start_and_end_months`. The _html_ value is the _start_ month. The _plain_ value is the _end_month. The value(s) should be the number of the month. For example if the event is just for May, the _plain_ value would be `5` and the _html_ value would be `5`. If the event is for April -> June, the _html_ value would be `4` and the _plain_ value would be `6`.

#### Testing


### Santas Grotto

#### Description

#### Setup / Configuration

#### Testing


### Afternoon Tea
#### Description
Allow a customer to sign up X adults and Y children for an afternoon teas slot.
- specify the age of each child
- have different price for adult and child
- This is for Highways

The event is implemented by creating a product for each timeslot with an available qty.

#### Setup / Configuration

**Category Setup**
1. Enable or create a category
2. Ensure category is in `GROTTO_CATEGORIES` at `app/code/Zero1/SantasGrotto/Helper/Config.php`
3. Ensure the theme is set to `HGL Events - Breakfast/Tea with Santa`

**Product Setup**
It doesn't look like they type of product matters, but for semantic probably better to make each slot a virtual product.
Before creating products ensure all the Event Dates and Event Times are present in the attributes `event_date` and `event_time`

1. Create a vritual product
  - **name** the name of the product doesnt matter functionally though convension is `Easter Bunny Afternoon Tea-085-28-05-2024-15-00`
  - **Categroy** ensure the product is in the event category
  - **Visibility** ensure the product is visibile in `catalog`
  - **Event Date** set the event date
  - **Customizable Options** The ticket type (ie Adult or Child)
    Create an Option with the title `Ticket Type`, option type: `Checkbox`, require: `yes`
    Add Values:
    - title `Adult`, price: xxxx, price type: `fixed`, sku: `AD`
    - title `Child`, price: xxxx, price type: `fixed`, sku: `CH`
  - Assign stock source `highway` and give it some stock

2. Reindex and flush cache


**Misc Setup**
- **Calendar Year** - The year the calendar loads when viewing the category. This is configured via the _plain_ value of the variable `all_events_year`. The value should be in `YYYY` format.
  **N.B** this variable affects _all_ events.
- **Calendar Month** - The start and end month for the event. This is configured with the variable `hgl_events_santa_grotto_start_and_end_months`. The _html_ value is the _start_ month. The _plain_ value is the _end_month. The value(s) should be the number of the month. For example if the event is just for May, the _plain_ value would be `5` and the _html_ value would be `5`. If the event is for April -> June, the _html_ value would be `4` and the _plain_ value would be `6`.

#### Testing
Create Products With
```bash
curl --location 'https://admin-roys-co-uk-20051.30.mdoq.io//rest/all/V1/products' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJ1aWQiOjQzLCJ1dHlwaWQiOjIsImlhdCI6MTcxODg4NDYxMSwiZXhwIjoxNzE4ODg4MjExfQ.-AuZxa8AGoJRkCGAc4S6zGEub6D20R2_HkB8fxoAMVQ' \
--header 'Cookie: PHPSESSID=ie0488inj7fsqptf0bt03a2lei' \
--data '{
    "product": {
        "id": 0,
        "sku": "Easter Bunny Afternoon Tea-085-30/05/2024-14:00",
        "name": "Easter Bunny Afternoon Tea-085-30/05/2024-14:00",
        "attribute_set_id": 4,
        "price": 0,
        "status": 1,
        "visibility": 2,
        "type_id": "virtual",
        "extension_attributes": {
            "website_ids": [
                2
            ],
            "category_links": [
                {
                    "position": 0,
                    "category_id": "2942"
                }
            ]
        },
        "product_links": [],
        "options": [
            {
                "product_sku": "Easter Bunny Afternoon Tea-085-30/05/2024-12:00",
                "title": "Ticket Type",
                "type": "checkbox",
                "sort_order": 1,
                "is_require": true,
                "max_characters": 0,
                "image_size_x": 0,
                "image_size_y": 0,
                "values": [
                    {
                        "title": "Adult",
                        "sort_order": 1,
                        "price": 12.99,
                        "price_type": "fixed",
                        "sku": "AD"
                    },
                    {
                        "title": "Child",
                        "sort_order": 2,
                        "price": 8.99,
                        "price_type": "fixed",
                        "sku": "CH"
                    }
                ]
            }
        ],
        "custom_attributes": [
            {
                "attribute_code": "category_ids",
                "value": [
                    "2942"
                ]
            },
            {
                "attribute_code": "event_date",
                "value": "13383"
            },
            {
                "attribute_code": "event_time",
                "value": "11616"
            }
        ]
    },
    "saveOptions": true
}'
```
(This is in ZERO1 postman as Roys > Create Afternoon Tea Product)


### Afternoon Tea With Santa

#### Description

#### Setup / Configuration

#### Testing


## Commercial Extensions
| Name | Version | Who purchased? | Login details for vendor |
|-|-|-|-|
Aheadworks_Ajaxcartpro |
Aheadworks_Rma |
Amasty_BannersLite |
Amasty_Base |
Amasty_Conditions |
Amasty_CommonTests |
Amasty_CommonRules |
Amasty_InvisibleCaptcha |
Amasty_Rgrid |
Amasty_Rules |
Amasty_RulesPro |
Amasty_ShippingArea |
Amasty_ShippingTableRates |
Amasty_Shiprestriction |
Ebizmarts_MailChimp |
Ebizmarts_SagePaySuite |
Ebizmarts_SagePaySuiteFormCrypt |
Ebizmarts_SagePaySuiteLogger |
Expert_EditorPdf |
Facebook_BusinessExtension |
Magefan_AdminUserGuide |
Magefan_Community |
Magefan_LazyLoad |
Mageplaza_Core |
Mageplaza_Smtp |
MarkShust_DisableTwoFactorAuth |
Mdoq_Connector |
PayPal_Braintree |
PayPal_BraintreeGraphQl |
Reviewscouk_Reviews |
Roys_StoreLocator |
Smile_ElasticsuiteAdminNotification |
Smile_ElasticsuiteCore |
Smile_ElasticsuiteCatalog |
Smile_ElasticsuiteCatalogGraphQl |
Smile_ElasticsuiteCatalogRule |
Smile_ElasticsuiteCatalogOptimizer |
Smile_ElasticsuiteTracker |
Smile_ElasticsuiteThesaurus |
Smile_ElasticsuiteSwatches |
Smile_ElasticsuiteIndices |
Smile_ElasticsuiteAnalytics |
Smile_ElasticsuiteVirtualCategory |
Temando_ShippingRemover |
Wyomind_Core |
Wyomind_CronScheduler |
Wyomind_Framework |
Wyomind_SimpleGoogleShopping |
Wyomind_Watchlog |
Zero1_AttributeSetup |
Zero1_BuyXForY |
Zero1_CheckoutStockLocations |
Zero1_ClickAndCollectShippingMethod |
Zero1_Csp |
Zero1_EventSystem |
Zero1_FixCategoryImages |
Zero1_GCR |
Zero1_GDPR |
Zero1_PDPStockLocations |
Zero1_Patches |
Zero1_RYTheme |
Zero1_Release |
Zero1_SantasGrotto |
Zero1_Splats |
Zero1_StockAtLocations |
Zero1_TrueBasket |

### Ebizmarts
Email: `itdevelopment@roys.co.uk`
Password: `R0y5Adm1n`

## Santas Grotto

Stuff about the Santas Grotto stuff.

It's main page is a category: 2502 (highways > events > breakfast with santa). It needs to be enabled to show.

There are a few key files:
- app/code/Zero1/SantasGrotto/view/frontend/web/js/view/booking.js
- app/design/frontend/z1/hgl_events_santa/Aheadworks_Ajaxcartpro/

It is also very important to name the product options correctly. For some reason the IDs appear to change per product, no idea why.
When the popup is loaded if goes through the config on the page to work out the correct options.
For this to work the options must have the names:
- `Age`
- `Special Instructions`
- The must be a drop down option, that have values with the name/labels: `Adult`, `Child`
- The must be a drop down option, that have values with the name/labels: `Male`, `Female`

If these aren't found, stuff will likely break
