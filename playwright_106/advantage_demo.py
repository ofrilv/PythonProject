from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/")
    cont_button= page.get_by_role("link",name="CONTACT_US")
    cont_button.click()


    print("end test")
    browser.close()