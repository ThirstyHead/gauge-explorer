# DOD (U.S. Department of Defense)

This test suite will visit the website's home page and test 
the accessibility of the page. It will also visit the website's 
accessibility page. 

[comment]: # (These setup steps will be run before each scenario below)
* Open browser

## Home page
* Visit "https://www.defense.gov/"
* Lighthouse report "dod-home-lighthouse"

## Accessibility page
* Visit "https://dodcio.defense.gov/DoDSection508/Std_Stmt.aspx"
* Lighthouse report "dod-accessibility-lighthouse"

_____
[comment]: # (These teardown steps will be run after each scenario above)
* Close browser
