from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user_name = page.locator('[id="user-name"]')
    user_name.fill("standard_user")
    password = page.locator('[id="password"]')
    password.fill("secret_sauce")
    password.click()
    login_button = page.get_by_text("login")
    login_button.click()
    current_url = page.url
    #assert current_url == "https://www.saucedemo.com/inventory.html" , "current_url is not as expected"
    page.close()
    browser.close()
    print("End Test***")




