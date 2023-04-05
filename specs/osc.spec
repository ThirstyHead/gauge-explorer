# OSC (U.S. Office of Special Counsel)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://osc.gov/"
* Lighthouse report "osc-home-lighthouse"

## Accessibility page
* Visit "https://osc.gov/Accessibility"
* Lighthouse report "osc-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
