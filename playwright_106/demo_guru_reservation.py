from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demo.guru99.com/test/newtours/")
    page.fill("[name='userName']", "tutorial")
    page.fill("[name='password']", "tutorial")
    page.click("[name='submit']")
    flights = page.get_by_role("link", name="Flights")
    flights.click()

    if (page.locator("[class='cb-close']").count() > 0):
        page.locator("[class='cb-close']").click()

    page.locator('text=Flights').click()

    page.click('input[value="oneway"]')
    page.select_option('select[name="passCount"]', "2")
    page.select_option('select[name="fromPort"]', "Toronto")
    page.select_option('select[name="toPort"]', "London")
    page.click('input[name="submit"]')



    find_flights = page.locator('input[name="findFlights"]')
    find_flights.wait_for(state="visible")
    find_flights.click()

    print("clicked successfully ✅")

    page.wait_for_timeout(5000)
    browser.close()