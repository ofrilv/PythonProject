from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto ("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    page.locator('[class="btn btn-primary btn-lg"]')
    page.get_by_text("Customer Login").click()

    drop_down_sort= page.locator('[id="userSelect"]').select_option(label= "Ron Weasly")
    page.get_by_role("button", name= "Login").click()

    browser.close()
    print("Test End")



