from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    bank_manager_button= page.locator('text=Bank Manager Login')
    bank_manager_button.get_by_text("Bank Manager Login")
    bank_manager_button.click()
    url= page.url
    print(url)
    browser.close()
    print("Bank Manager Login is found")