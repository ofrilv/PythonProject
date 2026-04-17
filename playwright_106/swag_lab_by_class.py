from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user =page.locator('[class="input_error form_input"]')
    password = page.locator('[class="input_error form_input"]')
    login_button = page.get_by_text("Login")
    user.click()
    user.fill("standard_user")
    password.click()
    password.type("secret_sauce")

    login_button.click()
    url = page.url
    print (url)