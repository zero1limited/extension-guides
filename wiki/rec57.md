# Transactional Emails



## Pitch Email

Sending transactional emails to customers is a no-brainer for any ecommerce store. Customers want to be informed, updated and reassured about their order. Providing this information is key to improving their overall customer experience and can also give your reputation a boost.

Even though these are transactional emails and might seem a little mundane, we can still add content to them to further increase sales. They're a goldmine for potential sales and here’s why:

- They have an open rate of over 70% compared to bulk emails of 17%
- They have a 3x higher engagement rate than bulk emails
- It cost 6-7x more to acquire a new customer than to retain an existing one
- Repeat customers tend to spend more than new customers – 67% more

Studies show that only 32% of customers will place the second order during their first year.

This is a massive drop after the first purchase, However, if we make a customer purchase for the second time, they will more likely come back to your store again – for the third, fourth, and even the fifth time. You could double your revenue if only 10% of customers returned to your site for a second purchase.

Knowing these facts, we can encourage customers to make a second purchase by offering them discounts and offers.

A few examples would be...

**X% Off your next order**
A very simple but very effective way of creating urgency amongst customers and influencing repeat purchases

**Free delivery on your next order**
Now who doesn't love free delivery? Free delivery motivates customers to take action just to qualify for free deilvery, so what could be more appealing than offering a free delivery code at checkout for a repeat purchase.

**Limited time offer discounts**
You can offer irresistible discounted offers that customers must take before time expires, creating urgency which can influence your customers to make that valuable second purchase.

**Value added offers**
You can offer your customers value-added items (Get a FREE Gift!) on their next purchase. The value-added items could be complimentary products or potentially surplus / slow moving stock in your inventory.

---

We propose that these marketing offers are added to your order confirmation emails along with your shipment confirmation emails to gain maximum impact on your customers.

You will have the ability to add different codes for registered users and guest users.

This would also work very easily for Magento installations with multiple stores.

One other (potentially huge) benefit that this would bring is the ability to very easily track the data. If the codes used within the emails are set to a strict naming convention, you could very easily track the usage of these codes and gain visibility of your most valuable and effective offers; therefore giving you very valuable data on your customers' behaviour and how you can then influence this even more to generate even more revenue.



## Instructions

In the following example, we will work on the basis that the client is a single store and would like...

1 marketing block in the GUEST order confirmation email

> Important: Make sure when dealing with clients that have multiple stores to check the store scope when configuring emails / editing emails / creating the blocks. We wouldn't want clients to suffer from sending customers the wrong voucher codes as this would be completely detrimental to what this is all about and create a very shitty CX
{.is-danger}

[This video](https://share.vidyard.com/watch/GUvaDSa9RjdQtVVxUGwuPN?) covers everything explained below but would probably be valuable to go through both the video and steps below

## The block template

The block that's shown in the transactional emails is very simple and just has a background colour and font colour. Looks like this...

<table style="margin: 30px 0;">
    <tr>
        <td>
            <div style="background: #ff7f01;padding: 30px;text-align: center;">
                <h2 style="color: #fff;margin: 0;letter-spacing: -0.4px; font-weight: bold;font-size: 20px;">Get 10% OFF your next order!</h2>
                <p style="color: #fff; margin: 20px 0; text-align: center;">We really do appreciate your custom and would like to say thank you by giving you 10% off your next order. Enter the code below the next time you checkout and your 10% OFF will be applied. <br/>Enjoy!</p>
                <div style="background: #fff;border-radius: 2px;padding: 20px;font-size: 20px;font-weight: bold;letter-spacing: -0.4px;">DTRETOC10</div>
            </div>
        </td>
    </tr>
</table>

We'll edit the HTML and then create our blocks in MAP

> If a client would like to display something fancy with imagery etc, please speak to Sean or Paul and we can get it sorted
{.is-info}


Copy the following HTML into your text editor and change the background colours, font colours as text as needed:

`<table style="margin: 30px 0;">`
`    <tr>`
`        <td>`
`            <div style="background: #ff7f01;padding: 30px;text-align: center;">`
`                <h2 style="color: #fff;margin: 0;letter-spacing: -0.4px; font-weight: bold;font-size: 20px;">Get 10% OFF your next order!</h2>`
`                <p style="color: #fff; margin: 20px 0; text-align: center;">We really do appreciate your custom and would like to say thank you by giving you 10% off your next order. Enter the code below the next time you checkout and your 10% OFF will be applied. <br/>Enjoy!</p>`
`                <div style="background: #fff;border-radius: 2px;padding: 20px;font-size: 20px;font-weight: bold;letter-spacing: -0.4px;">DTRETOC10</div>`
`            </div>`
`        </td>`
`    </tr>`
`</table>`


## Create the relevant block in MAP

Creating a strict naming convention for these blocks isn't necessary but helps massively for finding them in future

> Check if your client is multi-site and assign blocks as appropiate
{.is-warning}


- Go to MAP > Content > Blocks > Add New Block
- Give the block a name and id

Transactional Email - Order Confirmation Incentive (Guest)
transemail_orderconfirmationincentive_guest

Now I can paste in the HTML from the template above and save the block

## Find out what transactional emails are in use

Before we can insert the new blocks into the transactional emails, we need to find out what email templates are being used.

Go to MAP > Stores > Configuration > Sales > Sales Emails

> Check if your client is multi-site and if so check the store scope
{.is-warning}

Here you'll be able to see what template is being used for:
- New Order for Guest

If any of these values are set to use default templates e.g. ```New Order (Default)```, you will need to "create new templates" below.

### Create new templates from "(Default)"

In this example we'll say the **New Order** setting in Sales Emails is set to ```New Order (Default)```

- Go into Go to MAP > Marketing > Email Templates and click "Add New Template"
- The first option you get will be Load Default Template with a pull down.
- Select the relevant template. In this case I'll pick New Order
- Click load template
- Give the template and name (New Order Confirmation)
- Save
- Go back to Stores > Config > Sales > Sales Emails and change the New Order pulldown from the default one, to the one you've just created(New Order Confirmation)

Repeat this process for any / all email templates that are set to use default templates

## Insert the blocks into the emails

The block is inserted into the template using the following code. You will obviously need to change the block_id="" value to match the ID of the block you want to insert.

```
{{block class="Magento\\Cms\\Block\\Block" area='frontend' block_id="transemail_orderconfirmationincentive_guest"}}
```

- Go to MAP > Marketing > Email Templates
- Select the email template you want to edit (e.g. New Order Confirmation)
- Decide where you want to insert the new block (you can use preview to be sure)
- Insert the code
- Save the template

# QA

- Place a test order on the frontend and receive the order confirmation email
- Check that the block is displaying as intended

On completion, please pass the task back to the Zero1 owner. Thanks!
