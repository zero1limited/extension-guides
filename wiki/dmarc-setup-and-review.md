# DMARC Setup & Review
How to setup / configure dmarc reports and how to review them.

[TOC]

## Requirements
- The domains must be set up in cloudflare

## DMARC Setup
- log into cloudflare, nagviate to the domain.
- from the left nav, expand "Email" then select "DMARC Management" 
- select "Enable DMARC Management"
- click next to generate records. (You don't need to do anything, cloudflare will auto add them to DNS)
- it will take ~7days to get a real sample size


## DMARC Review
- log into cloudflare, nagviate to the domain.
- from the left nav, expand "Email" then select "DMARC Management" 
- from here you should be able to see the pass count and fail count on a daily basis
- If the fail count is less then 1% all okay?
  (this number is totally made up as a best effort first attempt)

- If there are a high number of fails BED required to review.