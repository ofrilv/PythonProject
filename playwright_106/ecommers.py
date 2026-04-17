from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://ecommerce-playground.lambdatest.io/")
    search= page.locator("[name='search']").first
    search.click()
    search.fill("Iphone")
    search.click()

    url= page.url
    print(url)

    print("end test")
    browser.close()

