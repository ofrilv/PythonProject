


def test_search_main_menu(setup_playwright):
    page= setup_playwright
    page.goto(" https://www.calculator.net/interest-calculator.html")
    initial = page.locator("[id='cstartingprinciple']")
    initial.click()
    initial.clear()
    initial.fill("30,000")

def test_main_menu(setup_playwright):
        page = setup_playwright
        page.goto(" https://www.calculator.net/interest-calculator.html")
        annual_cont = page.locator("[id='cannualaddition']")
        annual_cont.click()
        annual_cont.clear()
        annual_cont.fill("6,000")

def test_main_menu(setup_playwright):
        page = setup_playwright
        page.goto(" https://www.calculator.net/interest-calculator.html")
        calculate= page.locator('[value="Calculate"]')
        calculate.click()




        print("fff")





