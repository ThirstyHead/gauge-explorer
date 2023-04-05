# USDT (U.S. Department of the Treasury)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://home.treasury.gov/"
* Lighthouse report "usdt-home-lighthouse"

## Accessibility page
* Visit "https://home.treasury.gov/utility/accessibility/web-accessibility"
* Lighthouse report "usdt-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
