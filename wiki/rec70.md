# Pitch Email

Google TBT Score (Total Blocking Time)

Total Blocking Time (TBT) is a lab metric that measures the load responsiveness of a page. Higher TBT values usually indicate that the website reacts to a user input not as quickly as it should to make the user experience smooth.

TBT does this by measuring the total amount of time between First Contentful Paint and Time To Interactive and finding long tasks within the aforementioned timespan.

Google uses tools which inspects your LCP speed and then generates a score and it does this on a page-by-page basis for both desktop and mobile. Improving your TBT score is very important as it not only improves this part of the UX, but it makes up 25% of your overall performance score, which as we know can have a positive / negative affect on your rankings.

---

We will shortly follow up on this ticket to provide more information based on the assessments we have made along with the current data and and indication of the improvements we hope to make in the time provided.

# Follow up Email

Once you've gone into Google Search Console, get a report of what pages have the most errors and on what devices. Make a judgment call on which page / device you're gonna work on and let the client know. Ideally, the more focussed the better.

Eg. 

Hi Client,
Having just reviewed your web vitals I feel we should concentrate on your product list pages having received low scores. blah. 



# Instructions

FED to review Google Search Console initially to confirm pages with poorest score.


# TBT Issues (FED)

https://uploadcare.com/blog/what-is-total-blocking-time/

# Debugging

# Testing

You obviously get a score for FCP on the Lighthouse report (red, yellow, green). Quickest way is to look at that once you've made your changes to see what difference it's made.

The more substantial way is Google Search Console. In there, you'll find errors / warnings about FCP. You can ask Google to rescan the site once your changes are live to confirm in there that the errors / warnings are gone.
Not 100% sure how to do that but Max can help.
