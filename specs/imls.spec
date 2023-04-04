# IMLS (Institute of Museum and Library Services)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://www.imls.gov/"
* Lighthouse report "imls-home-lighthouse"

## Accessibility page
* Visit "https://www.imls.gov/about-us/policy-notices/website-accessibility"
* Lighthouse report "imls-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
