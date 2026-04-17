from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.nike.com/il/")
    sport_button= page.locator('[class="menu-hover-trigger-link"]')
    sport_button= page.get_by_role("link", name="Sport")
    sport_button.click()
    url= page.url
    print(url)
    browser.close()
    print("End Test")