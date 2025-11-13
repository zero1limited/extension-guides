# Instructions
Max to help, link to Bing official instructions?
Prerequisites:
Client Must have Bing Ads account
We Must have management access to the account 
Client must have Google Tag Manager 

From their Bing Ads account navigate to “Tools” (located in the top Nav Bar Spanner Icon)
Select “UET Tag” from the “Conversion Tracking” Drop Down Menu
Select “Create UET Tag” from the page that loads
Enter UET Tag Name and a short Description
Enable “Microsoft Clarity” using the radio button 
Select “Only used by xxxxx” Radio Button Under sharing 
Then Save 
From the pop up box download or copy the code for the UET Tag:
Set Up in Tag Manager
To send information from Google Tag Manager to Microsoft Advertising, you need to create a "container" in Google Tag Manager and then add the Microsoft Advertising UET tag to it.
Here's how you can get started with the basic UET tag that fires on all pages:
When you set up an account in Google Tag Manager, enter your website's URL in the Container name box.
From the Overview page of this container's workspace, select the container ID (formatted like "GTM-XXXXXX") in the toolbar. You will see the Google Tag Manager container code and instructions.
Copy the container code and paste it into the head or body section of every page of your website.
Back on the Overview page of your container's workspace, select New tag.
In the Tag Configuration pane, choose a tag type to begin setup.
Search for Microsoft Advertising Universal Event Tracking.
Ensure that the track type is set to UET config/page view (required). You need to add only one tag of this track type and you must trigger it on all pages.
Enter your Microsoft Advertising. You can find the tag ID in Microsoft Advertising by selecting Conversion Tracking > UET tags.
If you have more than one UET tag tracking code on a webpage, enter the global event tracking object name within the UET tag script that you want Google Tag Manager to track into the UETQ Variable ID box. Otherwise, use the default uetq value. Learn more about reasons for creating more than one UET tag and how to rename the uetq event tracker.
If you don't use a different uetq variable, the UET Tag Helper will return the "Multiple UET tags on this webpage use the same event name" issue. If you have multiple tags placed on the site and one of those is implemented through Google Tag Manager, it's possible that the UET Tag Helper will fail to detect the "Multiple UET tag on this webpage use the same event name" issue.
If you have already implemented the UET tag tracking code on your website, then we recommend removing the tracking code before you add the UET tag for page view from Google Tag Manager.
In the Triggering pane, select the pencil icon and select All pages. A tag must have at least one trigger for it to fire. Triggers are evaluated during runtime and are fired when the trigger conditions are met. Select Save.
Enter a Tag Name, and then select Save.
In the toolbar of your container's workspace, select Submit > Publish to enable the tag and add a version.
In Microsoft Advertising, select Conversion Tracking > UET tags to verify that you are receiving conversions. It typically takes up to 24 hours for a tag to be verified.
Using the UET Tag Helper, browse your website and confirm that all pages fire the UET page load event.
Custom events require dynamic values, so you need to tell Google Tag Manager how to read them.
Set up Google Tag Manager variables to read dynamic values from your page: While Google Tag Manager supports many types of variables (read from html elements, functions, JavaScript variables, data layer variables, etc.), we'll set up Google Tag Manager variables to read data layer variables in this example.
Visit our Google Tag Manager sample page (English only), right-click in the webpage, and then select View source or View page source depending on your browser. You will see the following variables:
<script>
	dataLayer.push({
		'event': 'Purchase',
		'ecomm_prodid': ['abc123', 'xyz456'],
		'ecomm_pagetype': 'purchase',
		'ecomm_totalvalue’: 55.55,
		'currency’: ‘USD’,
		'items': [{ 'id': 'abc123', 'price': 11.11, 'quantity': 1 }, { 'id': 'xyz456', 'price': 22.22, 'quantity': 2 }],
		'transaction_id': 'tid123456',
	});				
</script>
You'll need to make sure that the variables in your website's code match the parameters needed for the custom event required for your scenarios (e.g., custom event conversions, variable revenue, or dynamic remarketing). For this example, let's say that you have the above parameters in your website, and you want Google Tag Manager to read them.
In your Google Tag Manager container's workspace, select Variables.
Under User-Defined Variables, select New.
In the Variable Configuration pane, select the pencil icon.
Under Page Variables, select Data Layer Variable.
In the Variable Name box, enter the name you gave this variable in your data layer. In our example, this would be one of the following: ecomm_prodid, ecomm_pagetype, ecomm_totalvalue, currency, items, or transaction_id.
Assign a name to your variable and select Save. For example, the variable for ecomm_prodid is named 'Product IDs'.
Repeat the above process, creating a new variable for each parameter that is required for the scenario you use in Microsoft Advertising.
Set up a trigger:
In your Google Tag Manager container's workspace, select Triggers, and then New.
In the Trigger Configuration pane, select the pencil icon and select Custom Event.
Enter an Event Name, and select Save. In our example, the event name is 'Purchase'.
Enter a Trigger Name, and select Save.
Your triggers in Google Tag Manager must match the possible interactions that are coded on your webpage.
Look at our Google Tag Manager sample page for an example. On this page, we have coded for a click on a button. Right-click in the webpage, and then select View source or View page source depending on your browser, and look for the code with id=btnCustomEvent.
Create a new tag: This will be a custom event tag that ties together the event variables and trigger you just created.
In your Google Tag Manager container's workspace, select Tags, and then New.
In the Tag Configuration pane, select the pencil icon.
Under More, select Microsoft Advertising Universal Event Tracking.
If you have more than one UET tag tracking code on a webpage, enter the global event tracking object name within the UET tag script that you want Google Tag Manager to track into the UETQ Variable ID box. Otherwise, use the default uetq value.
Select the appropriate track type depending on the scenario you are trying to add the UET tag for. The track types available are: Vertical: E-commerce, Vertical: Hotels, Vertical: Travel, Variable revenue for destination URL, Custom conversion, Page view (Single page application), or Define your own.
Select the appropriate event action based on your scenario. For example, on the purchase confirmation page, set Event action to ‘Purchase’.
Enter the variables you created in step 1 in the respective Event Parameters boxes. You can select the variables using the plus icon. In our example, we set 'Retail product ID' to {{Product IDs}}, 'Retail price' to {{Total value}}, and 'Retail total value' to {{Total price}}.
Add the items array for per product price, transaction ID, and any additional parameters by selecting Add parameter. In our example, we add the previously created parameters and set their values. We set 'items' to {{UET items array}} and 'transaction_id' to {{Transaction id}}.
In the Triggering pane, select the pencil icon and select the trigger that you created in step 2. Select Save.
Enter a Tag Name, and then select Save.
Publish your changes: In the toolbar of your Google Tag Manager container's workspace, select Submit > Publish.
Check your website's code: Verify that you have added the below variables to the data layer on the webpage where customers complete the event, e.g., the product purchase confirmation. In our example from above:
<script>
	dataLayer.push({
		'event': 'Purchase',
		'ecomm_prodid': ['abc123', 'xyz456'],
		'ecomm_pagetype': 'purchase',
		'ecomm_totalvalue’: 55.55,
		'currency’: ‘USD’,
		'items': [{ 'id': 'abc123', 'price': 11.11, 'quantity': 1 }, { 'id': 'xyz456', 'price': 22.22, 'quantity': 2 }],
		'transaction_id': 'tid123456',
	});			
</script>
Validate your tags: Use the UET Tag Helper to confirm that the event and the corresponding parameters in the event are being fired from your website.
Example Variable UET:
 




<!DOCTYPE html>




<html>


<head>


<title>UET Variable</title>


<meta charset="utf-8" />


<link href="StyleSheet/styles.css" rel="stylesheet">


</head>


<body>


<!--BEGIN: Microsoft Advertising UET Javascript tag.-->


<script>(function (w, d, t, r, u) { var f, n, i; w[u] = w[u] || [], f = function () { var o = { ti: "5637647" }; o.q = w[u], w[u] = new UET(o), w[u].push("pageLoad") }, n = d.createElement(t), n.src = r, n.async = 1, n.onload = n.onreadystatechange = function () { var s = this.readyState; s && s !== "loaded" && s !== "complete" || (f(), n.onload = n.onreadystatechange = null) }, i = d.getElementsByTagName(t)[0], i.parentNode.insertBefore(n, i) })(window, document, "script", "//bat.bing.com/bat.js", "uetq");</script>


<!--END: Microsoft Advertising UET Javascript tag-->


<!--BEGIN: JS to set variable revenue-->


<script>


var varRevenue = 7;


</script>


<!--END: JS to set variable revenue-->


<!--BEGIN: Custom code to report variable revenue for Destination URL type goal. In this sample we are reading dynamic value for the variable revenue from a JS variable. You can just as easily send static values or read from a JS function or from HTML elements etc. -->


<script> window.uetq = window.uetq || []; window.uetq.push({ 'gv': varRevenue });</script>


<!--END: Custom code to report variable revenue-->


<!--BEGING: Commented out example of how to read variable revenue from a JS Function -->


<!--


<script>


function GetRevenueValue()


{


return 6;


}


</script>


<script> window.uetq = window.uetq || []; window.uetq.push({ 'gv': GetRevenueValue()});</script>


-->


<!--END: JS Function to compute event value-->


<!--BEGING: Commented out example of how to read variable revenue from an HTML Element -->


<!--


<script> window.uetq = window.uetq || []; window.uetq.push({ 'gv': txtRevenue.value});</script>


-->


<!--END: JS Function to compute event value-->






<input type="hidden" id="txtRevenue" value="8" />






<nav class="navbar-default navbar-fixed-top" role="banner" container-id="header">


<nav class="navbar-header" role="banner" container-id="header">


<a class="navbar-brand" href="Index.html" title="Microsoft Advertising"></a>


<div class="navbar-brand-divider"></div>


<div class="navbar-brand-text"></div>


</nav>


</nav>


<article>


<h2>Advanced: Reporting variable revenue</h2>


<p><b>This webpage is meant to be used in conjunction with the </b><a target="_blank" href="https://go.microsoft.com/fwlink/?linkid=2019824"><b>How to report variable revenue with UET</b></a><b> Microsoft Advertising Help article.</b></p>


<p>We have installed a JavaScript Microsoft Advertising UET tag tracking code in the body of this webpage. This code has been customized to report variable revenue for a destination URL goal. To see how we did it, right-click in the webpage and then click <b>View source</b> or <b>View page source</b> depending on your browser. Our UET tag tracking code is right after the &lt;body&gt; tag, but you can put yours anywhere in your webpage’s head or body sections (either before the closing head tag or before the closing body tag).</p>


<p>As the webpage loads, it triggers the UET tag, resulting in a number of HTTP requests. The most important request is to "bat.bing" (the one that looks like "http://bat.bing.com/action/0?ti=..."). This request tells Microsoft Advertising about the user visits to your webpage. You can use third-party tools such as Fiddler to monitor all the requests that your browser is making when your webpage loads.</p>


<p>For variable revenue, an additional HTTP request is triggered to report this value to Microsoft Advertising. It is similar to the bat.bing but it has different parameters to report revenue (as opposed to just page visit).</p>


<p><b>Note: </b>A JavaScript UET tag is required to ensure you have access to the full functionalities of conversion tracking and remarketing. If you are using a non-JavaScript tag, please switch over to a JavaScript tag. <a target="_blank" href="https://go.microsoft.com/fwlink/?linkid=2019714">Learn how to create a JavaScript UET tag</a></p>


<!DOCTYPE html>
<html>
<head>
    <title>UET Variable</title>
    <meta charset="utf-8" />
    <link href="StyleSheet/styles.css" rel="stylesheet">
</head>
<body>
  <p><b>Note: </b>Variable UET Tracking Example Visit this pPage and View Soource. <a target="_blank" href="https://bingadsuet.azurewebsites.net/UETDirectOnSite_ReportVariableRevenue.html">Variable Revenue Traking Example</a></p>
  <h2>Advanced: Reporting variable revenue Example</h2>
  <p><!DOCTYPE html>
<html>
<head>
    <title>UET Variable</title>
    <meta charset="utf-8" />
    <link href="StyleSheet/styles.css" rel="stylesheet">
</head>
<body>
    <!--BEGIN: Microsoft Advertising UET Javascript tag.-->
    <script>(function (w, d, t, r, u) { var f, n, i; w[u] = w[u] || [], f = function () { var o = { ti: "5637647" }; o.q = w[u], w[u] = new UET(o), w[u].push("pageLoad") }, n = d.createElement(t), n.src = r, n.async = 1, n.onload = n.onreadystatechange = function () { var s = this.readyState; s && s !== "loaded" && s !== "complete" || (f(), n.onload = n.onreadystatechange = null) }, i = d.getElementsByTagName(t)[0], i.parentNode.insertBefore(n, i) })(window, document, "script", "//bat.bing.com/bat.js", "uetq");</script>
    <!--END: Microsoft Advertising UET Javascript tag-->
    <!--BEGIN: JS to set variable revenue-->
    <script>
        var varRevenue = 7;
    </script>
    <!--END: JS to set variable revenue-->
    <!--BEGIN: Custom code to report variable revenue for Destination URL type goal. In this sample we are reading dynamic value for the variable revenue from a JS variable. You can just as easily send static values or read from a JS function or from HTML elements etc.   -->
    <script> window.uetq = window.uetq || []; window.uetq.push({ 'gv': varRevenue });</script>
    <!--END: Custom code to report variable revenue-->
    <!--BEGING: Commented out example of how to read variable revenue from a JS Function -->
    <!--
    <script>
      function GetRevenueValue()
        {
            return 6;
        }
    </script>
    <script> window.uetq = window.uetq || []; window.uetq.push({ 'gv': GetRevenueValue()});</script>
     -->
    <!--END: JS Function to compute event value-->
    <!--BEGING: Commented out example of how to read variable revenue from an HTML Element -->
    <!--
    <script> window.uetq = window.uetq || []; window.uetq.push({ 'gv': txtRevenue.value});</script>
     -->
    <!--END: JS Function to compute event value-->

    <input type="hidden" id="txtRevenue" value="8" />

    <nav class="navbar-default navbar-fixed-top" role="banner" container-id="header">
        <nav class="navbar-header" role="banner" container-id="header">
            <a class="navbar-brand" href="Index.html" title="Microsoft Advertising"></a>
            <div class="navbar-brand-divider"></div>
            <div class="navbar-brand-text"></div>
        </nav>
    </nav>
    <article>
        <h2>Advanced: Reporting variable revenue</h2>
        <p><b>This webpage is meant to be used in conjunction with the </b><a target="_blank" href="https://go.microsoft.com/fwlink/?linkid=2019824"><b>How to report variable revenue with UET</b></a><b> Microsoft Advertising Help article.</b></p>
        <p>We have installed a JavaScript Microsoft Advertising UET tag tracking code in the body of this webpage. This code has been customized to report variable revenue for a destination URL goal. To see how we did it, right-click in the webpage and then click <b>View source</b> or <b>View page source</b> depending on your browser.  Our UET tag tracking code is right after the &lt;body&gt; tag, but you can put yours anywhere in your webpage’s head or body sections (either before the closing head tag or before the closing body tag).</p>
        <p>As the webpage loads, it triggers the UET tag, resulting in a number of HTTP requests. The most important request is to "bat.bing" (the one that looks like "http://bat.bing.com/action/0?ti=..."). This request tells Microsoft Advertising about the user visits to your webpage. You can use third-party tools such as Fiddler to monitor all the requests that your browser is making when your webpage loads.</p>
        <p>For variable revenue, an additional HTTP request is triggered to report this value to Microsoft Advertising. It is similar to the bat.bing but it has different parameters to report revenue (as opposed to just page visit).</p>
        <p><b>Note: </b>A JavaScript UET tag is required to ensure you have access to the full functionalities of conversion tracking and remarketing. If you are using a non-JavaScript tag, please switch over to a JavaScript tag. <a target="_blank" href="https://go.microsoft.com/fwlink/?linkid=2019714">Learn how to create a JavaScript UET tag</a></p>
        <p><b>Learn more: </b><a target="_blank" href="https://go.microsoft.com/fwlink/?linkid=2019717">What is UET and how can it help me?</a></p>
    </article>
    <footer>
        <nav role="navigation" class="navbar-footer navbar-fixed-bottom">
            <div class="container-fluid">
                <ul class="navbar-right">
                    <li class="footer-logo"></li>
                </ul>
            </div>
        </nav>
    </footer>
</body>
</html>

  
  

</article>


<footer>
