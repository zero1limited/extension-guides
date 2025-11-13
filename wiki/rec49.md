# Optimised Domain Sharding & CDN for static & media assets


## Email / Pitch
This recommendation is aimed at improving the technical performance of your website and infrastructure. Migrating static assets and media to alternative (sub) domains provides the ability for improved page load times but also optimised cache expiry headers for assets using the Content Delivery Network.

This estimation assumes you have a single store/domain on Magento. If you have multiple domains/websites then the estimation will be adjusted accordingly.
In order to proceed with this you will need an active Stackpath account. 



# Instructions
https://docs.mdoq.io/en/tutorials/mdoq/static-assets-subdomain



## Stackpath

You can setup 1 CDN with 2 URLs, this is the best way to save your site quota in Stackpath Eg. One Site with

- static.abakhan.co.uk pointing/using Host header www.abakhan.co.uk
- media.abakhan.co.uk pointing/using Host header www.abakhan.co.uk

Because these are using the Host Header of the main www site then your `cors_shared.conf`  can look like this


  ```
map $http_origin $cors_allow_origin {
  https://www.woolbox.co.uk https://www.woolbox.co.uk;
  default https://www.abakhan.co.uk;
}

  
  ```
  
  

When the above is completed you can proceed to QA

# QA



# Handover
Arron to complete this

Test before reconfiguring in MAP
```
curl -H "Origin: https://www.woolbox.co.uk" --verbose \
  https://static.woolbox.co.uk/static/version7672f1515f47c9701d0c84b89e9487fa55ce86b6/frontend/z1/ab/en_GB/Magento_Ui/templates/tooltip/tooltip.html 
  

```
Also ensure Cache CDN is cleared after the Nginx stuff has gone live and been restarted
