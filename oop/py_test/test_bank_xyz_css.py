
def test_search_by_css(setup_playwright):
    page= setup_playwright
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    page.locator('[class*="btn"]')
    page.get_by_text("Customer Login").click()

    drop_down_sort = page.locator('[id="userSelect"]').select_option(label="Ron Weasly")
    page.get_by_role("button", name="Login").click()

    print("Test End")
