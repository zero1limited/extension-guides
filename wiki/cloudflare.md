# Cloudflare WAF

[TOC]


## Handling CORS configuration for static. sub-domains











## Rules

### Redirect Rules
For ensuring non-www traffic is directed
expression
(http.host eq "roys.co.uk")

result dynamic
concat("https://www.roys.co.uk", http.request.uri.path)


















### Settings

### CDN

### WAF

API URL Configuration = `/rest/V1`
Whitelist Magento admin logged-in users = ON

 
## Connecting to Cloudflare API
This is hopefully something we can develope to ensure certain services are set as we would need them

Eg Rocket Loader - causes hell with Hyvä

Example of simple utility PHP file which could be centrally managed to keep a check on things? could be a magento extension eventually?



```
<?php

// Cloudflare API token
$apiToken = 'YOUR_API_TOKEN_HERE';
// Cloudflare Zone ID (you can find this in the Cloudflare dashboard)
$zoneId = 'YOUR_ZONE_ID_HERE';

// Cloudflare API endpoint to get Rocket Loader status
$url = "https://api.cloudflare.com/client/v4/zones/$zoneId/settings/rocket_loader";

// Initialize cURL
$ch = curl_init();

// Set the cURL options
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Authorization: Bearer $apiToken",
    "Content-Type: application/json"
]);

// Execute the request
$response = curl_exec($ch);

// Check if the request was successful
if (curl_errno($ch)) {
    echo 'Request Error:' . curl_error($ch);
} else {
    // Decode the response from JSON to an associative array
    $data = json_decode($response, true);
    
    // Check if the Rocket Loader setting is returned
    if (isset($data['result']) && isset($data['result']['value'])) {
        $status = $data['result']['value'];
        if ($status === 'on') {
            echo "Rocket Loader is enabled.";
        } elseif ($status === 'off') {
            echo "Rocket Loader is disabled.";
        } else {
            echo "Rocket Loader is in automatic mode.";
        }
    } else {
        echo "Unable to retrieve Rocket Loader status.";
    }
}

// Close the cURL session
curl_close($ch);

?>
```

  

### Firewall

#### Allowed IPs
- MDOQ `91.121.169.206` `51.89.218.69` `51.195.189.3` `37.187.26.111` - should be listed here though https://docs.mdoq.io/hc/en-gb/articles/4416058262929-MDOQ-IPs
- ZERO-1 `213.105.127.200`
- OWN IP - VERY IMPORTANT

> run `curl checkip.amazonaws.com` and ensure the servers own IP is listed to avoid the known issue where Magento reports `your web server is set up incorrectly and allows unauthorized access to sensitive files. please contact your hosting provider`
{.is-warning}

> Stackpath reported the reason for 429 errors were
cause I see that IP xxx.xxx.xxx.xxx (Host IP) is making a request to the  /app/etc/config.php and that it been blocked, and the tags that are appearing as the reason for the block are:
Spam Client: This client made a lot of consecutive POST requests with no referrer header.
DDOS client: This IP was part of multiple DDOS attacks on this domain
Multiple Repeated Violations: This client was failing to pass sanctions repeatedly thus confirmed being automation.
{.is-warning}




### Firewall Rules
Known Rules for common services - needs building out

| Service       | Rule        | Match    | Value                     |
|---------------|-------------|----------|---------------------------|
| EbizmartsPOS  | User Agent  | Equals   | `Ebizmarts_POS`           |
| Linnworks.net | User Agent  | Contains | `Linnworks`               |
| Sagepay       | User Agent  | Equals   | `SagePay-Notifier/1.0`    |
| Shipstation   | URL         | Contains |  `/index.php/api/auctane` |
| M2e Pro       | User Agent  | Equals   | `M2E Pro Cron Service/1.0`|
| Google LLC    | Organization| Equals   | `Google LLC`              |
| SEM Rush      | User Agent  | Contains | `SemrushBot`              |
| Pinterest     | User Agent  | Contains | `Pinterestbot`            |
| Better Uptime | User Agent  | Contains | `Better Uptime Bot`       |
| Mollie        | User Agent  | Contains | `Mollie HTTP client/1.0`  |
| GMC Crawler   | User Agent  | Contains | `google-xrawler`          |

  
  
## Redirect for non-www
Page Rules

  

## Server Side
To block traffic from all other sources other than Stackpath and Zero1 office do the following.
**N.B** this has _not_ been tested on a docker stack

1. add a `geo` map in the http context (next to server, where you would find `map`) for `$realip_remote_addr`. The list of IP addresses/ranges can be retrieved [here](https://support.stackpath.com/hc/en-us/articles/360001091666-IP-Blocks). Plus Zero1's office IP. at the time of writing this was:  
  ```
geo $realip_remote_addr $accessAllowed {
    default "no";

    2a0a:e200:1a00::/40    "yes";
    2a0a:e200:1c00::/40    "yes";
    2a0a:e200:1100:1100::/64    "yes";
    2a0a:e200:1100::/40    "yes";
    2a0a:e200:1200:1100::/64    "yes";
    2a0a:e200:1200::/40    "yes";
    2a0a:e200:1300::/40    "yes";
    2a0a:e200:1400::/40    "yes";
    2a0a:e200:1500::/40    "yes";
    2a0a:e200:1600::/40    "yes";
    2a0a:e200:1700::/40    "yes";
    2a0a:e200:1900:1100::/64    "yes";
    69.16.133.0/24    "yes";
    69.16.176.0/20    "yes";
    69.16.182.0/24    "yes";
    69.16.184.0/24    "yes";
    69.16.188.0/24    "yes";
    74.209.134.0/24    "yes";
    74.209.134.128/25    "yes";
    81.171.60.0/24    "yes";
    81.171.61.0/24    "yes";
    81.171.68.64/26    "yes";
    81.171.105.0/24    "yes";
    81.171.106.64/26    "yes";
    81.171.112.0/24    "yes";
    94.46.144.0/20    "yes";
    94.46.153.128/25    "yes";
    94.46.154.128/25    "yes";
    94.46.155.128/25    "yes";
    103.66.28.0/22    "yes";
    103.228.104.0/24    "yes";
    146.88.130.128/25    "yes";
    151.139.0.0/17    "yes";
    151.139.0.0/19    "yes";
    151.139.11.128/25    "yes";
    151.139.13.0/24    "yes";
    151.139.14.128/25    "yes";
    151.139.15.128/25    "yes";
    151.139.16.128/25    "yes";
    151.139.18.128/25    "yes";
    151.139.19.128/25    "yes";
    151.139.21.0/24    "yes";
    151.139.23.0/24    "yes";
    151.139.24.0/25    "yes";
    151.139.25.0/24    "yes";
    151.139.29.0/24    "yes";
    151.139.32.0/24    "yes";
    151.139.33.128/25    "yes";
    151.139.34.128/25    "yes";
    151.139.35.128/25    "yes";
    151.139.36.128/25    "yes";
    151.139.37.128/25    "yes";
    151.139.38.128/25    "yes";
    151.139.40.0/22    "yes";
    151.139.41.0/24    "yes";
    151.139.44.0/22    "yes";
    151.139.45.0/24    "yes";
    151.139.48.0/22    "yes";
    151.139.49.0/24    "yes";
    151.139.52.0/22    "yes";
    151.139.56.128/25    "yes";
    151.139.58.0/23    "yes";
    151.139.59.0/24    "yes";
    151.139.60.0/22    "yes";
    151.139.64.0/23    "yes";
    151.139.66.0/23    "yes";
    151.139.67.0/24    "yes";
    151.139.68.0/22    "yes";
    151.139.72.0/22    "yes";
    151.139.76.0/23    "yes";
    151.139.77.0/24    "yes";
    151.139.78.0/23    "yes";
    151.139.80.0/22    "yes";
    151.139.81.0/24    "yes";
    151.139.84.0/22    "yes";
    151.139.88.0/23    "yes";
    151.139.90.0/23    "yes";
    151.139.92.0/23    "yes";
    151.139.93.0/24    "yes";
    151.139.94.0/23    "yes";
    151.139.96.0/23    "yes";
    151.139.97.0/24    "yes";
    151.139.98.0/23    "yes";
    151.139.114.0/23    "yes";
    151.139.116.0/23    "yes";
    151.139.118.0/23    "yes";
    151.139.120.0/22    "yes";
    173.245.194.0/24    "yes";
    173.245.208.64/26    "yes";
    173.245.210.64/26    "yes";
    173.245.216.64/26    "yes";
    173.245.218.64/26    "yes";
    205.185.216.0/22    "yes";
    205.185.217.0/24    "yes";
    205.185.219.0/25    "yes";
    209.197.7.0/24    "yes";
    209.197.8.0/21    "yes";
    209.197.9.0/24    "yes";
    209.197.11.0/24    "yes";
    209.197.13.224/27    "yes";
    209.197.21.0/24    "yes";
    209.197.24.0/21    "yes";
    209.197.27.128/25    "yes";
    209.197.31.0/25    "yes";
    209.234.242.0/25    "yes";
    2001:4de0:0110::/64    "yes";
    2001:4de0:0210::/64    "yes";
    2001:4de0:0410::/64    "yes";
    2001:4de0:0510::/64    "yes";
    2001:4de0:0610::/64    "yes";
    2001:4de0:2010::/64    "yes";
    2001:4de0:2110::/64    "yes";
    2001:4de0:2210:1::/64    "yes";
    2001:4de0:2210::/64    "yes";
    2001:4de0:2310::/64    "yes";
    2001:4de0:3010::/64    "yes";
    2001:4de0:3110::/64    "yes";
    2001:4de0:4010::/64    "yes";
    2001:4de0:4110::/64    "yes";
    2001:4de0:4310::/64    "yes";
    2001:4de0:5010::/64    "yes";
    2001:4de0:7001:1::/64    "yes";
    2001:4de0:7002:1::/64    "yes";
    2001:4de0:7003:1::/64    "yes";
    2001:1938:7001:1::/64    "yes";
    2001:1938:7002:1::/64    "yes";
    2001:1938:7003:1::/64    "yes";
    2001:1938:7004:1::/64    "yes";
    2001:1938:7005:1::/64    "yes";
    2001:1938:7006:1::/64    "yes";
    2001:1938:7007:1::/64    "yes";
    2001:1938:7008:1::/64    "yes";
    2407:1580:1100::/40    "yes";
    2407:1580:1200:1100::/64    "yes";
    2407:1580:1200::/40    "yes";
    2407:1580:1300::/40    "yes";
    2407:1580:1400::/40    "yes";
    2407:1580:1500::/40    "yes";
    2407:1580:1600::/40    "yes";
    2407:1580:1700:1100::/64    "yes";
    2407:1580:1700::/40    "yes";
    2604:6840:1c00:1100::/64    "yes";
    2604:6840:1e00::/40    "yes";
    2604:6840:1100::/40    "yes";
    2604:6840:1200::/40    "yes";
    2604:6840:1300:1100::/64    "yes";
    2604:6840:1300::/40    "yes";
    2604:6840:1400:1100::/64    "yes";
    2604:6840:1400::/40    "yes";
    2604:6840:1500:1100::/64    "yes";
    2604:6840:1500::/40    "yes";
    2604:6840:1600::/40    "yes";
    2604:6840:1700::/40    "yes";
    2604:6840:1800:1100::/64    "yes";
    2604:6840:1800::/40    "yes";
    2604:6840:1900::/40    "yes";
    2606:ce80:6100:1::/64    "yes";
    2606:ce80:6200:1::/64    "yes";
    2606:ce80:6300:1::/64    "yes";
    2606:ce80:6400:1::/64    "yes";
    2606:ce80:6500:1::/64    "yes";
    2606:ce80:6600:1::/64    "yes";
    2606:ce80:6700:2::/64    "yes";
    2606:ce80:6900:1::/64    "yes";
    192.166.245.71/32    "yes";
    192.166.245.98/32    "yes";
    35.201.16.129/32    "yes";
    35.244.107.67/32    "yes";
    108.61.185.90/32    "yes";
    104.156.232.232/32    "yes";
    2001:19f0:5800:8bfc:5400:ff:fe1c:5b87/64    "yes";
    2001:19f0:5800:8d34:5400:ff:fe1c:5b8c/64    "yes";
    35.198.52.85/32    "yes";
    35.198.12.22/32    "yes";
    37.235.52.70/32    "yes";
    37.235.52.196/32    "yes";
    2a03:f80:56:37:235:52:70:1/112    "yes";
    2a03:f80:56:37:235:52:196:1/112    "yes";
    120.26.119.191/32    "yes";
    47.97.251.164/32    "yes";
    151.236.21.35/32    "yes";
    151.236.21.87/32    "yes";
    2a01:348:99:151:236:21:35:1/112    "yes";
    2a01:348:99:151:236:21:87:1/112    "yes";
    149.154.159.21/32    "yes";
    151.236.15.26/32    "yes";
    2a03:f80:49:149:154:159:21:1/112    "yes";
    2a03:f80:49:151:236:15:26:1/112    "yes";
    35.242.213.204/32    "yes";
    35.242.210.32/32    "yes";
    158.255.208.86/32    "yes";
    151.236.20.95/32    "yes";
    2a03:f80:852:158:255:208:86:1/112    "yes";
    2a03:f80:852:151:236:20:95:1/112    "yes";
    151.236.24.35/32    "yes";
    151.236.24.50/32    "yes";
    2a03:f80:354:151:236:24:35:1/112    "yes";
    2a03:f80:354:151:236:24:50:1/112    "yes";
    34.249.164.113/32    "yes";
    54.76.234.169/32    "yes";
    149.154.157.239/32    "yes";
    151.236.18.167/32    "yes";
    2001:b60:1000:149:154:157:239:1/112    "yes";
    2001:b60:1000:151:236:18:167:1/112    "yes";
    104.214.150.207/32    "yes";
    104.214.147.166/32    "yes";
    34.85.22.40/32    "yes";
    35.200.117.161/32    "yes";
    45.32.45.117/32    "yes";
    45.32.52.15/32    "yes";
    2001:19f0:7000:9aa1:5400:ff:fe1c:1090/64    "yes";
    2001:19f0:7000:9c35:5400:ff:fe1c:4562/64    "yes";
    103.209.192.93/32    "yes";
    45.252.191.10/32    "yes";
    213.183.56.71/32    "yes";
    213.183.56.187/32    "yes";
    2a03:f80:7:213:183:56:71:1/112    "yes";
    2a03:f80:7:213:183:56:187:1/112    "yes";
    35.186.155.99/32    "yes";
    34.87.56.240/32    "yes";
    102.133.165.127/32    "yes";
    102.133.168.247/32    "yes";
    151.236.23.78/32    "yes";
    151.236.23.142/32    "yes";
    2a00:1d70:ed15:151:236:23:78:1/112    "yes";
    2a00:1d70:ed15:151:236:23:142:1/112    "yes";
    46.246.93.179/32    "yes";
    46.246.126.136/32    "yes";
    2a00:1a28:1251:46:246:93:179:1/112    "yes";
    2a00:1a28:1251:46:246:126:136:1/112    "yes";
    34.90.24.209/32    "yes";
    35.204.22.69/32    "yes";
    151.236.14.231/32    "yes";
    151.236.14.238/32    "yes";
    2a00:1768:1003:151:236:14:231:1/112    "yes";
    2a00:1768:1003:151:236:14:238:1/112    "yes";
    95.138.170.88/32    "yes";
    95.138.175.4/32    "yes";
    2a00:1a48:7805:113:be76:4eff:fe08:25fa/64    "yes";
    2a00:1a48:7805:113:be76:4eff:fe09:1f07/64    "yes";
    45.32.183.237/32    "yes";
    45.32.179.191/32    "yes";
    2001:19f0:7401:834f:5400:ff:fe1c:c96/64    "yes";
    2001:19f0:7401:844e:5400:ff:fe1c:c99/64    "yes";
    185.157.232.52/32    "yes";
    185.157.233.153/32    "yes";
    2a07:4580:b0d:f::6324/64    "yes";
    2a07:4580:b0d:82::793a/64    "yes";
    23.253.20.207/32    "yes";
    23.253.22.201/32    "yes";
    2001:4801:7824:101:be76:4eff:fe10:55c6/64    "yes";
    2001:4801:7824:101:be76:4eff:fe10:24dc/64    "yes";
    207.148.1.50/32    "yes";
    149.28.254.195/32    "yes";
    45.32.69.31/32    "yes";
    45.32.94.5/32    "yes";
    2001:19f0:6000:9301:5400:00ff:fe1c:0085/64    "yes";
    2001:19f0:6000:95c5:5400:ff:fe1c:88/64    "yes";
    149.28.235.77/32    "yes";
    63.209.33.45/32    "yes";
    52.52.23.91/32    "yes";
    52.53.106.71/32    "yes";
    34.201.233.220/32    "yes";
    34.203.52.30/32    "yes";
    45.32.129.60/32    "yes";
    45.63.90.144/32    "yes";
    104.238.157.42/32    "yes";
    45.32.225.132/32    "yes";
    2001:19f0:8000:8652:5400:ff:fe1c:45c2/64    "yes";
    2001:19f0:8000:8706:5400:ff:fe1c:45c4/64    "yes";
    35.245.111.92/32    "yes";
    35.245.0.188/32    "yes";
    78.142.19.197/32    "yes";
    84.54.49.15/32    "yes";
    213.105.127.200   "yes"; #Zero1
}
```
2. Add this list again the file `/etc/nginx/conf.d/stackpath_real_ips.txt` but prefix with "set_realip_from". At the time of writing this was the output:  
  ```
  set_real_ip_from 2a0a:e200:1a00::/40;
set_real_ip_from 2a0a:e200:1c00::/40;
set_real_ip_from 2a0a:e200:1100:1100::/64;
set_real_ip_from 2a0a:e200:1100::/40;
set_real_ip_from 2a0a:e200:1200:1100::/64;
set_real_ip_from 2a0a:e200:1200::/40;
set_real_ip_from 2a0a:e200:1300::/40;
set_real_ip_from 2a0a:e200:1400::/40;
set_real_ip_from 2a0a:e200:1500::/40;
set_real_ip_from 2a0a:e200:1600::/40;
set_real_ip_from 2a0a:e200:1700::/40;
set_real_ip_from 2a0a:e200:1900:1100::/64;
set_real_ip_from 69.16.133.0/24;
set_real_ip_from 69.16.176.0/20;
set_real_ip_from 69.16.182.0/24;
set_real_ip_from 69.16.184.0/24;
set_real_ip_from 69.16.188.0/24;
set_real_ip_from 74.209.134.0/24;
set_real_ip_from 74.209.134.128/25;
set_real_ip_from 81.171.60.0/24;
set_real_ip_from 81.171.61.0/24;
set_real_ip_from 81.171.68.64/26;
set_real_ip_from 81.171.105.0/24;
set_real_ip_from 81.171.106.64/26;
set_real_ip_from 81.171.112.0/24;
set_real_ip_from 94.46.144.0/20;
set_real_ip_from 94.46.153.128/25;
set_real_ip_from 94.46.154.128/25;
set_real_ip_from 94.46.155.128/25;
set_real_ip_from 103.66.28.0/22;
set_real_ip_from 103.228.104.0/24;
set_real_ip_from 146.88.130.128/25;
set_real_ip_from 151.139.0.0/17;
set_real_ip_from 151.139.0.0/19;
set_real_ip_from 151.139.11.128/25;
set_real_ip_from 151.139.13.0/24;
set_real_ip_from 151.139.14.128/25;
set_real_ip_from 151.139.15.128/25;
set_real_ip_from 151.139.16.128/25;
set_real_ip_from 151.139.18.128/25;
set_real_ip_from 151.139.19.128/25;
set_real_ip_from 151.139.21.0/24;
set_real_ip_from 151.139.23.0/24;
set_real_ip_from 151.139.24.0/25;
set_real_ip_from 151.139.25.0/24;
set_real_ip_from 151.139.29.0/24;
set_real_ip_from 151.139.32.0/24;
set_real_ip_from 151.139.33.128/25;
set_real_ip_from 151.139.34.128/25;
set_real_ip_from 151.139.35.128/25;
set_real_ip_from 151.139.36.128/25;
set_real_ip_from 151.139.37.128/25;
set_real_ip_from 151.139.38.128/25;
set_real_ip_from 151.139.40.0/22;
set_real_ip_from 151.139.41.0/24;
set_real_ip_from 151.139.44.0/22;
set_real_ip_from 151.139.45.0/24;
set_real_ip_from 151.139.48.0/22;
set_real_ip_from 151.139.49.0/24;
set_real_ip_from 151.139.52.0/22;
set_real_ip_from 151.139.56.128/25;
set_real_ip_from 151.139.58.0/23;
set_real_ip_from 151.139.59.0/24;
set_real_ip_from 151.139.60.0/22;
set_real_ip_from 151.139.64.0/23;
set_real_ip_from 151.139.66.0/23;
set_real_ip_from 151.139.67.0/24;
set_real_ip_from 151.139.68.0/22;
set_real_ip_from 151.139.72.0/22;
set_real_ip_from 151.139.76.0/23;
set_real_ip_from 151.139.77.0/24;
set_real_ip_from 151.139.78.0/23;
set_real_ip_from 151.139.80.0/22;
set_real_ip_from 151.139.81.0/24;
set_real_ip_from 151.139.84.0/22;
set_real_ip_from 151.139.88.0/23;
set_real_ip_from 151.139.90.0/23;
set_real_ip_from 151.139.92.0/23;
set_real_ip_from 151.139.93.0/24;
set_real_ip_from 151.139.94.0/23;
set_real_ip_from 151.139.96.0/23;
set_real_ip_from 151.139.97.0/24;
set_real_ip_from 151.139.98.0/23;
set_real_ip_from 151.139.114.0/23;
set_real_ip_from 151.139.116.0/23;
set_real_ip_from 151.139.118.0/23;
set_real_ip_from 151.139.120.0/22;
set_real_ip_from 173.245.194.0/24;
set_real_ip_from 173.245.208.64/26;
set_real_ip_from 173.245.210.64/26;
set_real_ip_from 173.245.216.64/26;
set_real_ip_from 173.245.218.64/26;
set_real_ip_from 205.185.216.0/22;
set_real_ip_from 205.185.217.0/24;
set_real_ip_from 205.185.219.0/25;
set_real_ip_from 209.197.7.0/24;
set_real_ip_from 209.197.8.0/21;
set_real_ip_from 209.197.9.0/24;
set_real_ip_from 209.197.11.0/24;
set_real_ip_from 209.197.13.224/27;
set_real_ip_from 209.197.21.0/24;
set_real_ip_from 209.197.24.0/21;
set_real_ip_from 209.197.27.128/25;
set_real_ip_from 209.197.31.0/25;
set_real_ip_from 209.234.242.0/25;
set_real_ip_from 2001:4de0:0110::/64;
set_real_ip_from 2001:4de0:0210::/64;
set_real_ip_from 2001:4de0:0410::/64;
set_real_ip_from 2001:4de0:0510::/64;
set_real_ip_from 2001:4de0:0610::/64;
set_real_ip_from 2001:4de0:2010::/64;
set_real_ip_from 2001:4de0:2110::/64;
set_real_ip_from 2001:4de0:2210:1::/64;
set_real_ip_from 2001:4de0:2210::/64;
set_real_ip_from 2001:4de0:2310::/64;
set_real_ip_from 2001:4de0:3010::/64;
set_real_ip_from 2001:4de0:3110::/64;
set_real_ip_from 2001:4de0:4010::/64;
set_real_ip_from 2001:4de0:4110::/64;
set_real_ip_from 2001:4de0:4310::/64;
set_real_ip_from 2001:4de0:5010::/64;
set_real_ip_from 2001:4de0:7001:1::/64;
set_real_ip_from 2001:4de0:7002:1::/64;
set_real_ip_from 2001:4de0:7003:1::/64;
set_real_ip_from 2001:1938:7001:1::/64;
set_real_ip_from 2001:1938:7002:1::/64;
set_real_ip_from 2001:1938:7003:1::/64;
set_real_ip_from 2001:1938:7004:1::/64;
set_real_ip_from 2001:1938:7005:1::/64;
set_real_ip_from 2001:1938:7006:1::/64;
set_real_ip_from 2001:1938:7007:1::/64;
set_real_ip_from 2001:1938:7008:1::/64;
set_real_ip_from 2407:1580:1100::/40;
set_real_ip_from 2407:1580:1200:1100::/64;
set_real_ip_from 2407:1580:1200::/40;
set_real_ip_from 2407:1580:1300::/40;
set_real_ip_from 2407:1580:1400::/40;
set_real_ip_from 2407:1580:1500::/40;
set_real_ip_from 2407:1580:1600::/40;
set_real_ip_from 2407:1580:1700:1100::/64;
set_real_ip_from 2407:1580:1700::/40;
set_real_ip_from 2604:6840:1c00:1100::/64;
set_real_ip_from 2604:6840:1e00::/40;
set_real_ip_from 2604:6840:1100::/40;
set_real_ip_from 2604:6840:1200::/40;
set_real_ip_from 2604:6840:1300:1100::/64;
set_real_ip_from 2604:6840:1300::/40;
set_real_ip_from 2604:6840:1400:1100::/64;
set_real_ip_from 2604:6840:1400::/40;
set_real_ip_from 2604:6840:1500:1100::/64;
set_real_ip_from 2604:6840:1500::/40;
set_real_ip_from 2604:6840:1600::/40;
set_real_ip_from 2604:6840:1700::/40;
set_real_ip_from 2604:6840:1800:1100::/64;
set_real_ip_from 2604:6840:1800::/40;
set_real_ip_from 2604:6840:1900::/40;
set_real_ip_from 2606:ce80:6100:1::/64;
set_real_ip_from 2606:ce80:6200:1::/64;
set_real_ip_from 2606:ce80:6300:1::/64;
set_real_ip_from 2606:ce80:6400:1::/64;
set_real_ip_from 2606:ce80:6500:1::/64;
set_real_ip_from 2606:ce80:6600:1::/64;
set_real_ip_from 2606:ce80:6700:2::/64;
set_real_ip_from 2606:ce80:6900:1::/64;
set_real_ip_from 192.166.245.71/32;
set_real_ip_from 192.166.245.98/32;
set_real_ip_from 35.201.16.129/32;
set_real_ip_from 35.244.107.67/32;
set_real_ip_from 108.61.185.90/32;
set_real_ip_from 104.156.232.232/32;
set_real_ip_from 2001:19f0:5800:8bfc:5400:ff:fe1c:5b87/64;
set_real_ip_from 2001:19f0:5800:8d34:5400:ff:fe1c:5b8c/64;
set_real_ip_from 35.198.52.85/32;
set_real_ip_from 35.198.12.22/32;
set_real_ip_from 37.235.52.70/32;
set_real_ip_from 37.235.52.196/32;
set_real_ip_from 2a03:f80:56:37:235:52:70:1/112;
set_real_ip_from 2a03:f80:56:37:235:52:196:1/112;
set_real_ip_from 120.26.119.191/32;
set_real_ip_from 47.97.251.164/32;
set_real_ip_from 151.236.21.35/32;
set_real_ip_from 151.236.21.87/32;
set_real_ip_from 2a01:348:99:151:236:21:35:1/112;
set_real_ip_from 2a01:348:99:151:236:21:87:1/112;
set_real_ip_from 149.154.159.21/32;
set_real_ip_from 151.236.15.26/32;
set_real_ip_from 2a03:f80:49:149:154:159:21:1/112;
set_real_ip_from 2a03:f80:49:151:236:15:26:1/112;
set_real_ip_from 35.242.213.204/32;
set_real_ip_from 35.242.210.32/32;
set_real_ip_from 158.255.208.86/32;
set_real_ip_from 151.236.20.95/32;
set_real_ip_from 2a03:f80:852:158:255:208:86:1/112;
set_real_ip_from 2a03:f80:852:151:236:20:95:1/112;
set_real_ip_from 151.236.24.35/32;
set_real_ip_from 151.236.24.50/32;
set_real_ip_from 2a03:f80:354:151:236:24:35:1/112;
set_real_ip_from 2a03:f80:354:151:236:24:50:1/112;
set_real_ip_from 34.249.164.113/32;
set_real_ip_from 54.76.234.169/32;
set_real_ip_from 149.154.157.239/32;
set_real_ip_from 151.236.18.167/32;
set_real_ip_from 2001:b60:1000:149:154:157:239:1/112;
set_real_ip_from 2001:b60:1000:151:236:18:167:1/112;
set_real_ip_from 104.214.150.207/32;
set_real_ip_from 104.214.147.166/32;
set_real_ip_from 34.85.22.40/32;
set_real_ip_from 35.200.117.161/32;
set_real_ip_from 45.32.45.117/32;
set_real_ip_from 45.32.52.15/32;
set_real_ip_from 2001:19f0:7000:9aa1:5400:ff:fe1c:1090/64;
set_real_ip_from 2001:19f0:7000:9c35:5400:ff:fe1c:4562/64;
set_real_ip_from 103.209.192.93/32;
set_real_ip_from 45.252.191.10/32;
set_real_ip_from 213.183.56.71/32;
set_real_ip_from 213.183.56.187/32;
set_real_ip_from 2a03:f80:7:213:183:56:71:1/112;
set_real_ip_from 2a03:f80:7:213:183:56:187:1/112;
set_real_ip_from 35.186.155.99/32;
set_real_ip_from 34.87.56.240/32;
set_real_ip_from 102.133.165.127/32;
set_real_ip_from 102.133.168.247/32;
set_real_ip_from 151.236.23.78/32;
set_real_ip_from 151.236.23.142/32;
set_real_ip_from 2a00:1d70:ed15:151:236:23:78:1/112;
set_real_ip_from 2a00:1d70:ed15:151:236:23:142:1/112;
set_real_ip_from 46.246.93.179/32;
set_real_ip_from 46.246.126.136/32;
set_real_ip_from 2a00:1a28:1251:46:246:93:179:1/112;
set_real_ip_from 2a00:1a28:1251:46:246:126:136:1/112;
set_real_ip_from 34.90.24.209/32;
set_real_ip_from 35.204.22.69/32;
set_real_ip_from 151.236.14.231/32;
set_real_ip_from 151.236.14.238/32;
set_real_ip_from 2a00:1768:1003:151:236:14:231:1/112;
set_real_ip_from 2a00:1768:1003:151:236:14:238:1/112;
set_real_ip_from 95.138.170.88/32;
set_real_ip_from 95.138.175.4/32;
set_real_ip_from 2a00:1a48:7805:113:be76:4eff:fe08:25fa/64;
set_real_ip_from 2a00:1a48:7805:113:be76:4eff:fe09:1f07/64;
set_real_ip_from 45.32.183.237/32;
set_real_ip_from 45.32.179.191/32;
set_real_ip_from 2001:19f0:7401:834f:5400:ff:fe1c:c96/64;
set_real_ip_from 2001:19f0:7401:844e:5400:ff:fe1c:c99/64;
set_real_ip_from 185.157.232.52/32;
set_real_ip_from 185.157.233.153/32;
set_real_ip_from 2a07:4580:b0d:f::6324/64;
set_real_ip_from 2a07:4580:b0d:82::793a/64;
set_real_ip_from 23.253.20.207/32;
set_real_ip_from 23.253.22.201/32;
set_real_ip_from 2001:4801:7824:101:be76:4eff:fe10:55c6/64;
set_real_ip_from 2001:4801:7824:101:be76:4eff:fe10:24dc/64;
set_real_ip_from 207.148.1.50/32;
set_real_ip_from 149.28.254.195/32;
set_real_ip_from 45.32.69.31/32;
set_real_ip_from 45.32.94.5/32;
set_real_ip_from 2001:19f0:6000:9301:5400:00ff:fe1c:0085/64;
set_real_ip_from 2001:19f0:6000:95c5:5400:ff:fe1c:88/64;
set_real_ip_from 149.28.235.77/32;
set_real_ip_from 63.209.33.45/32;
set_real_ip_from 52.52.23.91/32;
set_real_ip_from 52.53.106.71/32;
set_real_ip_from 34.201.233.220/32;
set_real_ip_from 34.203.52.30/32;
set_real_ip_from 45.32.129.60/32;
set_real_ip_from 45.63.90.144/32;
set_real_ip_from 104.238.157.42/32;
set_real_ip_from 45.32.225.132/32;
set_real_ip_from 2001:19f0:8000:8652:5400:ff:fe1c:45c2/64;
set_real_ip_from 2001:19f0:8000:8706:5400:ff:fe1c:45c4/64;
set_real_ip_from 35.245.111.92/32;
set_real_ip_from 35.245.0.188/32;
set_real_ip_from 78.142.19.197/32;
set_real_ip_from 84.54.49.15/32;
```
3. Add the following into the main `server` block, **before the first location block**  
  ```
include conf.d/stackpath_real_ips.txt;

#To ignore the trusted IPs, and only use IPs not present on the list
real_ip_recursive on;

#To specify the header to use for the module
real_ip_header x-forwarded-for;

if ( $accessAllowed = "no" ) { return 403; }
```
4. Reload nginx: `/etc/init.d/nginx configtest && /etc/init.d/nginx reload`
5. Make sure frontend of the site is up (using public address)
6. Make sure the site is inaccessible from a non-allowed server. (salt server)  
  `curl -kH "Host: www.britishhardwood.co.uk" https://188.165.198.99/`
  The source IP can be retrieved from stackpath gui, under settings.


## Server Side - Cloudflare
Follow this guide: [Cloudflare Real IPs](https://docs.mdoq.io/hc/en-gb/articles/21539834071185-Cloudflare-Real-IPs)
To get the real IP in the Nginx logs
