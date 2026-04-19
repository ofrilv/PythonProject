

def test_search_by_css(setup_playwright):
    page= setup_playwright
    page.goto("https://www.calculator.net/")
    grade_cal= page.locator('[href="/grade-calculator.html"]')
    grade_cal.click()
    grade= page.locator('input[class="in4char"]').first
    grade.fill("90")

    calculate= page.locator('input[value="Calculate"]').last

    calculate.click()
    assert "B+", "make sure average garde is B+"
    print ("results")


