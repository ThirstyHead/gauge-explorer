# CNCS (AmeriCorps, formerly Corporation for National and Community Service)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://americorps.gov/"
* Lighthouse report "cncs-home-lighthouse"

## Accessibility page
* Visit "https://americorps.gov/about/agency-overview/disability-accessibility"
* Lighthouse report "cncs-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
