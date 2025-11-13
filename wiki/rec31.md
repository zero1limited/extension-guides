<!-- 
# Pitch 

PWA Kick Start

https://share.vidyard.com/watch/zCnQR9JjL4wPWTCoPLB4JZ?

Progressive Web Apps provide major improvements to the customer experience compared to traditional websites. They're like a hybrid between mobile apps and  websites. PWAs have the ability to continue functioning when the user doesnt have an internet connection. This gives your customers a positive experience compared with your competitors. 

A complete PWA is one where your whole website experience is available offline, including the checkout process. This option can come at significant investment.

This recommendation is a simplified PWA kickstart. It doesnt include a full PWA experience but a simplified offline experience where the customer is still presented with a branded, customisable page if their connection drops, with the additional benefit that this is also recognised by Google Lighthouse tests. It's also widely recognised that there is a relationship between Lighthouse scores and Google rankings.
-->

# Pre-recommendation check

Some clients may already have a PWA stub in place. If they do, this ticket obviously won't be necessary so please check the live site before recommending this to the client.

To check if the client already has this, please follow the steps below...

- Go to the client's live site in Chrome
- Right click on the page (doesn't matter where) and "Inspect Element"
- When the developer tools open up, you'll see a "Lighthouse" tab in the top right of the panel; click it
- Click "Generate Report"

Once the report has been generated, you'll see 5 sections:
```Performance | Accessibility | Best Practices | SEO | Progressive Web App```
The one we care about is Progressive Web App

If the PWA (Progressive Web App) section is greyed out and doesn't generate a tick, then the client DOES NOT have a PWA stub and this task can be recommended to them. 
If the PWA section DOES generate a score, the client has already got a PWA stub and this recommendation isn't neccessary

# Instructions

Before we're able to crack on with this one, we'll need to get some stuff off a frontend developer. Please ask a frontend dev for...

1. The client's logo as a transparent png saved as 'logo.png' at 512px X 512px
1. offline.html file - (Instructions for FED here - https://wiki.zero1.co.uk/en/pwa-stub-frontend)

Once you've been provided the assets, you can crack on...

## Crack on... 

Before you start with any instructions, please create two new folders on your desktop:
"Instance" and "Assets". Creating these folders now will save us a headache later on when trying to find files that we need to upload to the instance.

## Add frontend assets

The frontend developer should have provided you with 2 things:

1. offline.html
1. logo.png

- Copy 1 into your "Instance" folder
- Copy 2 into your "Assets" folder

## Generate the favicon package

- Go to https://realfavicongenerator.net/
- Click "Select Your Favicon Image"
- Upload the logo.png file from your "Assets" folder
- When the image has been uploaded, you'll be able to scroll down the page and view what the logo will look like on certain devices / platforms. Change the settings (if needed) to make sure the logo will look good on all devices / platforms
- Click "Generate your Favicons and HTML code"

## Create your admin.html file

- Open your text editor and create a new file
- Copy the tags that the realfavicongenerator generates in step 3 and paste them into the new file you created
- Copy the code below and paste this underneath the tags you just pasted into your file

`<script src="/upup.min.js" type="text/javascript"></script>`
`<script async type="text/javascript">// <![CDATA[`
`    UpUp.start({`
`      'content-url': '/pwa/offline.html'`
`    });`
`// ]]></script>`

All together you should have something that looks like this...

`<link rel="apple-touch-icon" sizes="180x180" href="/pub/pwa/apple-touch-icon.png">`
`<link rel="icon" type="image/png" sizes="32x32" href="/pub/pwa/favicon-32x32.png">`
`<link rel="icon" type="image/png" sizes="16x16" href="/pub/pwa/favicon-16x16.png">`
`<link rel="manifest" href="/pub/pwa/site.webmanifest">`
`<link rel="mask-icon" href="/pub/pwa/safari-pinned-tab.svg" color="#5bbad5">`
`<meta name="msapplication-TileColor" content="#2d89ef">`
`<meta name="theme-color" content="#ffffff">`
`<script src="/upup.min.js" type="text/javascript"></script>`
`<script async type="text/javascript">// <![CDATA[`
`    UpUp.start({`
`      'content-url': '/pwa/offline.html'`
`    });`
`// ]]></script>`

The top 5 links have href tags and we now need to update all of them to include `/pub/pwa` at the start

`<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">`
becomes...
`<link rel="apple-touch-icon" sizes="180x180" href="/pub/pwa/apple-touch-icon.png">`

Do this for all 5 href tags and you should end up with something like this...

`<link rel="apple-touch-icon" sizes="180x180" href="/pub/pwa/apple-touch-icon.png">`
`<link rel="icon" type="image/png" sizes="32x32" href="/pub/pwa/favicon-32x32.png">`
`<link rel="icon" type="image/png" sizes="16x16" href="/pub/pwa/favicon-16x16.png">`
`<link rel="manifest" href="/pub/pwa/site.webmanifest">`
`<link rel="mask-icon" href="/pub/pwa/safari-pinned-tab.svg" color="#5bbad5">`
`<meta name="msapplication-TileColor" content="#2d89ef">`
`<meta name="theme-color" content="#ffffff">`
`<script src="/upup.min.js" type="text/javascript"></script>`
`<script async type="text/javascript">// <![CDATA[`
`    UpUp.start({`
`      'content-url': '/pwa/offline.html'`
`    });`
`// ]]></script>`

- Save the file as admin.html to your "Assets" folder

## Get the client's meta description

- Go to the frontend of the client's live site
- Right click anywhere on the page and "View Page Source"
- When the source loads, you should see the site's meta description. It will look like this...


`<meta name="description" content="Roys is an independent department store, it has a great range of homewares, electricals, toys, gardening, DIY,  fashion and groceries all at great prices."/>
`
- The content bit is what we'll need later on

## Download the package

- Go to realfavicongenerator and download the package it generated (step 1)
- Copy ALL of the files from the package into your "Instance" folder

## Update your site.webmanifest

- Open your "Instance" folder and locate the `site.webmanifest` file
- Open that file in your text editor. It will look like this...

```
{
    "name": "",
    "short_name": "",
    "icons": [
        {
            "src": "/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ],
    "theme_color": "#ffffff",
    "background_color": "#ffffff",
    "display": "standalone"
}
```

- Add the client's name into the name and short_name sections. Should look like this...

```
"name": "Roys",
"short_name": "Roys",
```
- Copy the code below and paste this onto a new line underneath the short_name

```
"description": "",
```
- Copy the client's meta description and paste it into the quotes

All together you should have something that looks like this...

```
{
    "name": "Roys",
    "short_name": "Roys",
    "description": "Roys is an independent department store, it has a great range of homewares, electricals, toys, gardening, DIY,  fashion and groceries all at great prices",
    "icons": [
        {
            "src": "/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ],
    "theme_color": "#ffffff",
    "background_color": "#ffffff",
    "display": "standalone"
}
```

- Copy the code below and paste it just above the `theme_colour` line
```
"start_url": "/pwa/offline.html",
```
Now we need to update the src URLs. You will see 2 src references in your site.webmanifest file...
```
"src": "/android-chrome-192x192.png",
```
```
"src": "/android-chrome-512x512.png",
```
We need to update both of these to include /pwa at the start. These src links should now look like this...
```
"src": "/pwa/android-chrome-192x192.png",
```
```
"src": "/pwa/android-chrome-512x512.png",
```

Your final site.webmanifest file should look like this...

```
{
    "name": "Roys",
    "short_name": "Roys",
    "description": "Roys is an independent department store, it has a great range of homewares, electricals, toys, gardening, DIY,  fashion and groceries all at great prices",
    "icons": [
        {
            "src": "/pwa/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/pwa/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ],
    "start_url": "/pwa/offline.html",
    "theme_color": "#ffffff",
    "background_color": "#ffffff",
    "display": "standalone"
}
```
- Save the file

We now need to generate a maskable icon and add this to the site.webmanifest file...

- Go to http://maskable.app/editor
- At the top right of the screen you'll see an `Upload` option. Click it
- Upload the logo.png file from your `Assets` folder
> If the logo is not sized in the box correctly, select the logo layer on the right and increase / decrease the padding until the logo fits nicely
{.is-info}

- Change the background colour to white (or any colour that matches the company branding)
- Once happy, click export (just above the logo)
- Select max size and export
- This will download `maskable_icon.png`
- Add that image to your `Instance` folder

Now copy the following code and paste it into your `site.webmanifest` file just underneath the icons section...

```
{
	"src": "/pwa/maskable_icon.png",
	"sizes": "196x196",
	"type": "image/png",
	"purpose": "any maskable"
},
```

Now add the following line to the manifest...

```
"prefer_related_applications": true
```

Your site.webmanifest file should now look like this...

```
{
    "name": "Roys",
    "short_name": "Roys",
    "description": "Roys is an independent department store, it has a great range of homewares, electricals, toys, gardening, DIY,  fashion and groceries all at great prices",
    "icons": [
        {
            "src": "/pwa/maskable_icon.png",
            "sizes": "196x196",
            "type": "image/png",
            "purpose": "any maskable"
        },        
        {
            "src": "/pwa/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/pwa/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ],
    "start_url": "/pwa/offline.html",
    "theme_color": "#ffffff",
    "background_color": "#ffffff",
    "display": "standalone",
    "prefer_related_applications": true
}
```

**Important Final Test**

Please make sure that each line has a comma at the end. For example, description, short_name, display etc.
The "prefer_related_applications": true doesn't need a comma at the end

Once you've checked this, save it


## Download UpUp

- Go to https://www.talater.com/upup/getting-started-with-offline-first.html
- Scroll to the very bottom and click "Download UpUp"
- It will download a folder with two files in it

## Changes to the instance

- Go to your instance on MDOQ and open the code editor
- Locate the `pub` folder
- Get the two upup files you just downloaded and drag them into the pub folder
- Now create a new folder inside the `pub` folder called `pwa`
- Select all of the files in your "Instance" folder and drag them into the new pwa folder you just created
- The /pub/pwa folder should now contain all of the files from your `Instance` folder and the /pub folder should contain the two upup files you downloaded
- Go to MDOQ > Git > Push
- Select all the files you've added and push

## Add your admin html

- Go to the instance's admin panel
- Go to Content > Design > Configuration
- Select "Edit" on the relevant store view
- Scroll down to HTML Head > Scripts & Stylesheets
- Open your Assets > admin.html file in your text editor and copy the content
- Paste it into the Scripts & Stylesheets text area
- Save configuration
- Go to System > Cache Management
- Flush all caches

## Update the ticket

Before passing to QA, please attach your admin.html file to the teamwork ticket. Once attached, feel free to pass to QA

# QA

- Open the frontend of the instance in a new incognito window in Chrome
- Right click on the page (doesn't matter where) and "Inspect Element"
- When the developer tools open up, you'll see a "Lighthouse" tab in the top right of the panel; click it
- Click "Generate Report"

Once the report has been generated, you'll see 5 sections:
```Performance | Accessibility | Best Practices | SEO | Progressive Web App```
The one we care about is Progressive Web App

If the PWA (Progressive Web App) section is greyed out and doesn't generate a score, then the QA has failed
If the PWA section DOES generate a score, QA has passed

Please copy and paste the relevant comment below into the task before passing back to the Zero1 Owner

> **QA Passed**
> Note for Zero1 owner - **Post Release Action**: Please copy the content from the admin.html file attached to this task and paste it into the client's live MAP in Miscellaneous Scripts
**Important:** When copying the admin.html file into the client's live admin panel, please remove the two script tags (and everything in them) and put these in the Footer Miscellaneous Scripts. This way, the script tags won't be render-blocking on the frontend. Speak to Sean if unsure.
{.is-success}


> **QA Failed**
> Note for Zero1 owner: QA has failed and needs looking at. Please be aware that the admin.html file attached to this ticket could be an issue. If it needs amending, please ensure the file attached to the task is also amended to make sure there's no issues when putting this into live MAP
{.is-danger}
