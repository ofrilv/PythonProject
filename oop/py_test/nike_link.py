

def test_search_adv(setup_playwright):
    page= setup_playwright
    page.goto("https://www.nike.com/en")
    men_button= page.locator("[href='https://www.nike.com/men']")
    men_button.click()
    women_button= page.locator("[href='https://www.nike.com/women']")
    women_button.click()

    def test_search_help(setup_playwright):
        page = setup_playwright
        page.goto("https://www.nike.com/en")
        help_button= page.locator('[role="presentation"]')
        help_button.click()
        search_button= page.locator('[id="searchInput"]').click()
        search_button.fill("shirt")
