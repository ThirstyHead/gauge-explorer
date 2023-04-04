# HHS (U.S. Department of Health and Human Services)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://www.hhs.gov/"
* Lighthouse report "hhs-home-lighthouse"

## Accessibility page
* Visit "https://www.hhs.gov/web/section-508/"
* Lighthouse report "hhs-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
