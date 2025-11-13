# Media Domain in use
To make sure you are getting the most out of your CDNs (These cache content for your users which means they get a faster response and your server doesn't need to serve the request) we would like to carry out an audit of key pages of your site to ensure they are using the correct domain for media assets.


## Prerequisites
- The client must be using a CDN for media images, this is typicall seen as a media.example.com

## Instructions
The idea of this task is to identify images that aren't being pull from the CDN. 
We can then detail these images to 2nd line / design team to change to use the CDN.

watch this: https://watch.screencastify.com/v/hnia8Gvv7pOPFjfpC4OE

The filter you need is: `domain:DOMAIN` for example, if I am looking at www.paddockspares.com, the filter would be: `domain:www.paddockspares.com`

Please carry out this task for:
- The homepage of the site
- Every top level category page

The output format should be the following:
```
PAGE_URL
	IMAGE_URL
  IMAGE_URL
  IMAGE_URL

PAGE_URL
  IMAGE_URL
  IMAGE_URL
```
For example for paddocks this would like something like:
```
https://www.paddockspares.com/
  https://www.paddockspares.com/media/wysiwyg/superpro.jpg
	https://www.paddockspares.com/media/wysiwyg/kandn_1.jpg
  
https://www.paddockspares.com/parts-and-accessories.html
  https://www.paddockspares.com/media/wysiwyg/landy.jpg
  
```

If you have carried this out and not found any images coming from the www. domain, please speak to Adam.

This task then needs to go to a 2nd liner / designer to confirm how we can pull these images from the media domain.

### Additional Notes
Please blag Adam, this is related to: https://zero1.teamwork.com/#/tasks/27230405
