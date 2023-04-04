# NASA (National Aeronautics and Space Administration)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://www.nasa.gov/"
* Lighthouse report "nasa-home-lighthouse"

## Accessibility page
* Visit "https://www.nasa.gov/content/accessibility-policy/"
* Lighthouse report "nasa-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
