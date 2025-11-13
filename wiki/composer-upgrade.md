# Composer upgrade


1. roll up instance
2. `composer2 install`
3. add `composer.lock` to source control
4. change composer version in MDOQ ui for instance
4. test?
5. on approval:
  - zero downtime release
  - change composer version in MDOQ ui for prod
  - sync php and cron
  
