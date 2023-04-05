# USPS (U.S. Postal Service)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://www.usps.com/"
* Lighthouse report "usps-home-lighthouse"

## Accessibility page
* Visit "https://about.usps.com/who/legal/section-508/welcome.htm"
* Lighthouse report "usps-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
