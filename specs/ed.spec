# ED (U.S. Department of Education)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://www.ed.gov/"
* Lighthouse report "ed-home-lighthouse"

## Accessibility page
* Visit "https://www2.ed.gov/notices/accessibility/"
* Lighthouse report "ed-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
