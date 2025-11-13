# Magento Command Line Interface (CLI) - bin/magento




## app:config:dump
Ideally we should be locking stuff down in Admin, this improves QA, stability.

Pro's
 * safer deployments
 * stable site
 * reduces risks caused by deploying code and config separately
 * reduces issues appearing in production based on config changes

Con's
 * Can piss clients off if they cannot change settings they want
 * critical config that needs to be different when on non-prod - Eg Crucials site forced index,follow directive



Needs
 * Clearly defined exclusion list of config paths that are NOT baked so we can app:config:dump safely?
 * 

I have written a module that intercepts app:config:dump with a defined list of paths that we can exclude. Can we either consider this or suggest a better option to standardise things across the business?

https://github.com/zero1limited/pozzani/tree/5d964d601e7259036cd3c7609cb3ffbc2e1ed033/app/code/Zero1/ConfigDumpExclusions
