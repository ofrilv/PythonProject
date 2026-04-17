


def test_login_by_css(setup_playwright):
    print("login swag labs")
    page = setup_playwright
    page.goto("https://www.saucedemo.com")
    user_name = page.locator('input[class*="input_error"]').first
    user_name.click()
    user_name .fill("standard_user")
    password = page.locator('input[class*="input_error"]').last
    password.click()
    password.fill("secret_sauce")

    login=page.locator('input[class="submit-button btn_action"]')
    login.click()

    print("test point")