# MDOQ Releases / Release Process
How to prepare and do releases on MDOQ.

## Preparing a release

- When creating a deployment, the format for the tag is either `3.YYYY.WW.PP` or `YYYY.WW.PP`, where:
  - `YYYY` is the 4 digit year
  - `WW` is the 2 digit ISO week number, you can get this from: https://www.epochconverter.com/weeknumbers
  - `PP` is the 2 digit path number, this should start from `00` or `01` and just be incremented by 1 each time.

## Doing a release

1. is zero downtime or not
2. are there PRAs
3. slack notification
4. ticket update
