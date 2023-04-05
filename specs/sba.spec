# SBA (U.S. Small Business Administration)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://www.sba.gov/"
* Lighthouse report "sba-home-lighthouse"

## Accessibility page
* Visit "https://www.sba.gov/about-sba/open-government/about-sbagov-website/accessibility"
* Lighthouse report "sba-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
