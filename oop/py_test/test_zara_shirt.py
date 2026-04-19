


def test_search_menu(setup_playwright):
    page = setup_playwright
    page.goto("https://www.zara.com/il/en/search/home")
    search_bnt= page.locator('[type="search"]')
    search_bnt.click()
    search_bnt.fill("Shirt")
    page.keyboard.press("Enter")

    search_button = page.locator('[class="product-grid-product-info__main-info"]')
    print("Shirt appears in search")