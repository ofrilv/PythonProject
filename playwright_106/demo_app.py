from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.applitools.com/#")
    user_name = page.locator('[id="username"]')
    user_name.fill("username")
    password = page.locator('[id="password"]')
    password.fill("password")
    password.click()
    login_button = page.get_by_text("sign in")
    login_button.click()
    current_url = page.url
    print(current_url)
    assert current_url == "https://demo.applitools.com/app.html"
    page.close()
    browser.close()
    print("End Test***")
