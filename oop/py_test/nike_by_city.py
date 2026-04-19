
def test_search_by_css(setup_playwright):
    page= setup_playwright
    page.goto("https://www.nike.com/en")
    store=page.locator('[class="interactive-profile-element"]').first.click()
    search_location= page.locator('[class="nds-input-text-field has-prefix-icon css-1yzc0py e1fiih290"]')
    search_location.fill("London")
    page.keyboard.press("Enter")
    stores= page.locator('[class*="d-sm-flx"]').count()
    assert stores> 1, "Number of stores must be more than one"


    print("test end")




