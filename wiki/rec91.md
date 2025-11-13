# Crawler Review
To ensure your site only handles the traffic it should be we regularly review a list of approved crawlers. We then block others to avoid them from having a determintal effect on your site.


## Prerequisites
- The customer must be using StackPath for their WAF

## Instrcutions
1. Log into stackpath an navigate to the clients "stack"
2. For any frontend or CDN sites (the sites used by customers - if unsure please consult someone e.g www.example.com static.example.com media.example.com) disable all crawlers except for:
  - Applebot
  - Chrome Compression Proxy
  - Facebook External Hit bot
  - Google ads bot
  - Google bot
  - Google FeedFetcher bot
  - Google Image bot
  - Google Image Proxy
  - Google Mediapartners bot
  - Google Mobile Ads Bot
  - Google News bot
  - Google Page Speed Insights
  - Google Structured Data Testing Tool
  - Google verification bot
  - Google Video bot
  - Google Web Light
  - Googlebot
  - LinkedIn bot
  - Microsoft Bing bot
  - Microsfot Bing Preview bot
  - Paypal IPN
  - Pingdom
  - Pingdom bot IP
  - Pingdom bot IP - more ips
  - SagePay
  - Slack bot
  - Stripe
  - Twitter bot
  - Zendesk bot
  Crawler settings can be found at Sites | WAF > Allow Known Bots

3. For any backend sites e.g admin.example.com block all crawlers except for:
  - Chrome Compression Proxy
  - Paypal IPN
  - Pingdom
  - SagePay
  - Stripe

4. Done

### Additional Notes
Please blag Arron for what to do here.
This was originally related to [this](https://zero1.teamwork.com/#/tasks/27230405) task.
