# NRC (U.S. Nuclear Regulatory Commission)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://www.nrc.gov/"
* Lighthouse report "nrc-home-lighthouse"

## Accessibility page
* Visit "https://www.nrc.gov/site-help/access.html"
* Lighthouse report "nrc-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
