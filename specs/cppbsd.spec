# CPPBSD (AbilityOne, AKA Committee for Purchase From People Who Are Blind or Severely Disabled)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://www.abilityone.gov/"
* Lighthouse report "cppbsd-home-lighthouse"

## Accessibility page
* Visit "https://www.abilityone.gov/accessibility.html"
* Lighthouse report "cppbsd-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
