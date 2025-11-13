# Project Setup / Project Onboarding

Checklist of actions to carry out when onboarding a new client, or setting up a new site.

1. Add ZERO1 Repman
  ```bash
  composer config repositories.zero1-repman composer https://zero1.repo.repman.io
  ```
  You then need to get a token from [here](https://app.repman.io/organization/zero1/token) and add to project
2. Install ZERO1 metapackage
  ```bash
  composer require zero1/core
  ```
3. Install Dev Tools
  ```bash
  composer require --dev -- mage2tv/magento-cache-clean zero1/magento-dev
  ```

