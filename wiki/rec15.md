# Sitemap XML
The easiest way for a search engine to crawl your website is via a sitemap submitted to Google Webmaster Tools, Bing Webmaster tools, Yahoo Site Explorer, etc. As you would expect, Magento will keep your sitemap up to date and generate this for you automatically. In order to enable this, go to System > Configuration > Google Sitemap (under the Catalog heading).

In here, we can configure the priority of each of our pages, along with how often they're updated and how often we want the sitemap to be updated. This section is a little hard to explain in a tutorial, as it completely depends on your type of store and what you're primarily optimising.

For the purpose of this article, we're going to assume your category pages are the most important pages, as these house all of your products and should be optimised for more general terms. We'd next prioritise product pages, as these are specific pages that you want people to hit if they're looking for a particular item. Finally, we'd have our CMS pages. These are pages that cover information such as terms and conditions, your privacy policy, and shipping information, so they're generally lower priority. Your homepage also comes under the CMS pages heading.

So, using the above as an example, we'd select the priority and frequency as follows:

Category Options: Frequency set to Daily; Priority set to 1.

Product Options: Frequency set to Daily; Priority set to 0.5.

CMS Page Options: Frequency set to Weekly; Priority set to 0.25.

With the above, if your product catalog and categories don't change very often, you could drop the frequency down to weekly, but this isn't necessary.

Note: For the Generation Settings to work, you will need to make sure your Magento cron works correctly.

Next, we need to generate the actual sitemap file. To do this, go to Catalog > Google Sitemap and click on  Add Sitemap Button in the Top Right. Then give your sitemap a name, and put a forward slash in the path file to get it to save in the root directory.

Once done, click Save & Generate and your sitemap should be viewable atyourdomain.com/sitemap.xml.

Assuming it all worked correctly, head over to Google, Bing and Yahoo and submit the sitemap URL you've just generated. We'll add it to the Robots.txt file later.

Additional Notes: If you're running multiple stores from the same Magento installation, you might want to separate your sitemaps. So using the example of an English and Spanish store, you might call one sitemap-en.xml and the other sitemap-es.xml. You might also want to put these into a subdirectory. The best approach following this might be to put rewrites into Nginx configuration files so that these can all be mapped properly when calling domain1.com/sitemap.xml and domain2.com/sitemap.xml respectively. Speak to Arron if you require clarification on this.
