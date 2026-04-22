

def test_search_by_css(setup_playwright):
    page= setup_playwright
    page.goto("https://www.nike.com/en")
    search_button= page.locator('[id="gn-search-input"]')
    search_button.click()
    search_button.get_by_text("shoes")
    results = page.locator("text=Shoes")
    assert results.count() > 0, "make sure shoes appears in search"

    print ("Shoes appears in search")