# SRE - Site Reliabiliy Engineer

This document is the foundation point for service Site Reliability and how we use the various tools


https://uptime.betterstack.com/


We also have a POC Hearbeat monitor system working on Barr Display - talk to Arron
We are testing the idea of improving what /health_check.php could do for us to improve things
Callum has developed a POC on Divine Trash - `curl https://www.zero1.co.uk/metrics-beta.sh | bash -s -- 2 https://hooks.slack.com/services/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 divinetrash`



# Customer Success
In order to gain a high level of customer trust, we must communicate when there is a Site Reliability Issue ideally raising a ticket immediately and having some automation which keeps them well informed.

• Agree scheduled maintenance windows - 50+ hour contracts can have them daily (range from 7am to 10am), anything lower is once weekly, these maintenance windows must be agreed and the windows kept.




NOTES

  Callum Breeze
  16 Aug at 13:16
I've found sometimes a site can be down for <1 min for example. Something we don't really drop everything and jump on.
I suppose really what I'm trying to say is there a way of separating the alerts to something that we know is a proper outage requiring me or Adam. If so I can set my phone to alert for that channel etc.
At the moment if I set my phone to always alert to messages in site-monitoring channel, 90% of them dont require action from a dev.
Also there is the fact that TC's monitoring caught the fact that their site was showing nothing more than a header for an hour, and ours didn't. we had to white lie and say all engineers were commuting, so it didn't make our monitoring look bad.
I don't have a solution for anything above or expect one to magically appear but just raising it for discussion.

  
  Arron Moss
  16 Aug at 14:01
nice one @Callum Ext 14/514
 in that case we need to split things out into the difference causes. Im going to create an SRE WIKI so we can lay the foundations for these scenarios.
things we need
split out sites that we do not need to act on - client doesnt have support, new prospect etc etc
designate maintenance windows so we keep to set times when alerts will NOT go off
design more intelligent tests that can test other things, explore health_check.php etc
