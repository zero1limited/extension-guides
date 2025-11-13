# Remote IP Address correction

## Pitch Email
Magento now often logs the incorrect IP address for customers and orders. This is due to the changing complexities of server infrastructure and web application firewalls. 
We have developed a process whereby we can identify from a string of IPs supplied in the request, which is the originating customer IP and make a code correction in order to log this as the customers' real IP address in both your web logs and the Magento Orders





## Instructions - if using Cloudflare

This should be something we do in the Nginx config?
Arron thinks we have implemented this somewhere? 
https://support.stackpath.com/hc/en-us/articles/360021658292-All-About-X-Forwarded-For
We need to find out where.
Cloudflare https://www.cloudflare.com/ips-v4
https://docs.mdoq.io/hc/en-gb/articles/4408658823569-Nginx?auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoxMTM2MjUzNywidXNlcl9pZCI6bnVsbCwidGlja2V0X2lkIjpudWxsLCJkZWZsZWN0aW9uX2lkIjo5NTYzNTEwOTgxMTM3LCJhcnRpY2xlcyI6WzQ0MDg2NTg4MjM1NjksNDQxMDc4OTkzMjU2MV0sInRva2VuIjpudWxsLCJleHAiOjE2NjczNzQ3MTJ9.QzNunRv8mJgZcZOoVvEQ8HMwcHqvY1t-1Lcs3jaXvuI#examples


Create an instancce on MDOQ, then using Code Editor, and check for file `mdoq/nginx/templates/default_https.conf`

If the file exists, add the following to it

```
echo "#list of Cloudflare WAF IPs
set_real_ip_from 173.245.48.0/20;
set_real_ip_from 103.21.244.0/22;
set_real_ip_from 103.22.200.0/22;
set_real_ip_from 103.31.4.0/22;
set_real_ip_from 141.101.64.0/18
set_real_ip_from 108.162.192.0/18;
set_real_ip_from 190.93.240.0/20;
set_real_ip_from 188.114.96.0/20;
set_real_ip_from 197.234.240.0/22;
set_real_ip_from 198.41.128.0/17;
set_real_ip_from 162.158.0.0/15;
set_real_ip_from 104.16.0.0/13;
set_real_ip_from 104.24.0.0/14;
set_real_ip_from 172.64.0.0/13;
set_real_ip_from 131.0.72.0/22;

#To ignore the trusted IPs, and only use IPs not present on the list
real_ip_recursive on;

#To specify the header to use for the module
real_ip_header x-forwarded-for; 
" >> /home/magento/htdocs/mdoq/nginx/templates/default_https.conf
```


If the file does not exist, run this command

```
echo "#list of Cloudflare WAF IPs
set_real_ip_from 173.245.48.0/20;
set_real_ip_from 103.21.244.0/22;
set_real_ip_from 103.22.200.0/22;
set_real_ip_from 103.31.4.0/22;
set_real_ip_from 141.101.64.0/18;
set_real_ip_from 108.162.192.0/18;
set_real_ip_from 190.93.240.0/20;
set_real_ip_from 188.114.96.0/20;
set_real_ip_from 197.234.240.0/22;
set_real_ip_from 198.41.128.0/17;
set_real_ip_from 162.158.0.0/15;
set_real_ip_from 104.16.0.0/13;
set_real_ip_from 104.24.0.0/14;
set_real_ip_from 172.64.0.0/13;
set_real_ip_from 131.0.72.0/22;

#To ignore the trusted IPs, and only use IPs not present on the list
real_ip_recursive on;

#To specify the header to use for the module
real_ip_header x-forwarded-for; 
" > /home/magento/htdocs/mdoq/nginx/templates/default_https.conf
```

1, Do a Git Push via MDOQ
2. Recreate the instance


# OLD Instructions

In the CLI from MDOQ run


```XML
echo "<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:ObjectManager/etc/config.xsd">
    <type name="Magento\Framework\HTTP\PhpEnvironment\RemoteAddress">
        <arguments>
            <argument name="alternativeHeaders" xsi:type="array">
                <item name="stackpath" xsi:type="string">HTTP_X_SP_FORWARDED_IP</item>
                <item name="real_ip" xsi:type="string">HTTP_X_REAL_IP</item>
            </argument>
        </arguments>
    </type>
</config>" > /home/magento/htdocs/app/etc/custom/di.xml
```
