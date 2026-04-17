from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/login")
    user_name = page.locator('[id="userName"]')
    user_name.fill("userName")
    password = page.locator('[id="password"]')
    password.fill("password")
    password.click()
    login_button = page.get_by_text("Login")
    login_button.click()
    current_url = page.url
    assert current_url == "https://demo.applitools.com/app.html"
    page.close()
    browser.close()
    print("End Test***")
