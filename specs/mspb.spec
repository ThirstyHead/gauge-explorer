# MSPB (U.S. Merit Systems Protection Board)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://www.mspb.gov/"
* Lighthouse report "mspb-home-lighthouse"

## Accessibility page
* Visit "https://www.mspb.gov/publicaffairs/accessibility.htm"
* Lighthouse report "mspb-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
