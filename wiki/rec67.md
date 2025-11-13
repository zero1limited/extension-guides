# Pitch Email

Google FCP Score (First Contentful Paint)

The "First Contentful Paint" is the time it takes for your site to render a 'user-friendly' DOM. This could be either an image, text block or a non-white background. It's essentially the first visual interaction that a user has with your website.

Google uses tools which inspects your FCP speed and then generates a score. Google does this on a page-by-page basis for both desktop and mobile.

Improving your FCP is important, as it improves the speed of your site as psychologically perceived by your visitors. Just as importantly, your FCP score makes up 15% of your overall performance score, which as we know can have a positive / negative affect on your rankings.

---

We will shortly follow up on this ticket to provide more information based on the assessments we have made along with the current data and and indication of the improvements we hope to make in the time provided.

# Follow up Email

Once you've gone into Google Search Console, get a report of what pages have the most errors and on what devices. Make a judgment call on which page / device you're gonna work on and let the client know. Ideally, the more focussed the better.

Eg. 

Hi Client,
Having just reviewed your web vitals I feel we should concentrate on your product list pages having received low scores. blah. 



# Instructions

FED to review Google Search Console initially to confirm pages with poorest score.


# FCP Issues (FED)

One issue that's particularly important for FCP is font load time. Check out the Ensure text remains visible during webfont load post for ways to speed up your font loads.

Unless you have a specific reason for focusing on a particular metric, it's usually better to focus on improving your overall Performance score.

Use the Opportunities section of your Lighthouse report to determine which improvements will have the most value for your page. The more significant the opportunity, the greater the effect it will have on your Performance score. For example, the Lighthouse screenshot below shows that eliminating render-blocking resources will yield the biggest improvement:

# Debugging

# Testing

You obviously get a score for FCP on the Lighthouse report (red, yellow, green). Quickest way is to look at that once you've made your changes to see what difference it's made.

The more substantial way is Google Search Console. In there, you'll find errors / warnings about FCP. You can ask Google to rescan the site once your changes are live to confirm in there that the errors / warnings are gone.
Not 100% sure how to do that but Max can help.
