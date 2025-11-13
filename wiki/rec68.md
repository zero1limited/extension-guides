# Pitch Email

Google CLS Score (Content Layout Shift)

Large layout shifts can create a frustrating experience for your users as they make your page appear visually jarring, as page elements suddenyly appear, move around, and affect how your visitors interact with the page.

This 'Layout shift' affects the way users interact with your website, particularly on mobile devices. 

Google uses tools which inspects your CLS (content layout shifts) and then generates a score. Google does this on a page-by-page basis for both desktop and mobile; a poor CLS score indicates that your page is visually unstable (known in the industry as janky).

---

We will shortly follow up on this ticket to provide more information based on the assessments we have made along with the current data and and indication of the improvements we hope to make in the time provided.

# Follow up Email

Once you've gone into Google Search Console, get a report of what pages have the most errors and on what devices. Make a judgment call on which page / device you're gonna work on and let the client know. Ideally, the more focussed the better.

Eg. 

Hi Client,
Having just reviewed your web vitals I feel we should concentrate on your product list pages having received low scores. blah. 



# Instructions

FED to review Google Search Console initially to confirm pages with poorest score.


# CLS Issues (FED)

Content Layout Shifts are basically when elements on the site move around while the page is loading. An example would be if the header contains a block which initially loads at say 150px in height. Then, when CSS loads and styles it up, it changes to 100px in height. This would be a CLS because there's a chance that a user goes to click that block, but then misses once it's loaded it's CSS and reduces in height.

There's a shit load on Google on how to fix it but it's gonna be very client specific on what's actually happening. Another example is nav items...
When they load, they have standard letter-spacing (no CSS yet). Then when the CSS kicks in, the letter spacing increases to 2px and forces all the elements to change in width. Again potentially causing the user to click the wrong thing.

# Debugging

It's a tough one to get bang on, but I usually open Chrome dev tools, go to performance and enable throttling and choose a dog shit internet connection. You can then usually stop the page from loading before you see these layout shifts so you can inspect element and apply fixes.

There's also a 'paint' which is shown in Lighthouse. If you run a Lighthouse audit, you'll see the Performance section. At the bottom of that, there's a "View Original Trace" button which then shows you the full paint of the page and allows you to see what CLS's are happening. Only problem is, you can't inspect the page so you might need to use the method above for that.

# Testing

You obviously get a score for CLS on the Lighthouse report (red, yellow, green). Quickest way is to look at that once you've made your changes to see what difference it's made.

The more substantial way is Google Search Console. In there, you'll find errors / warnings about CLS's. You can ask Google to rescan the site once your changes are live to confirm in there that the errors / warnings are gone.
Not 100% sure how to do that but Max can help.
