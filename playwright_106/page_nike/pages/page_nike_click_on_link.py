class PageNikeLink ():
    def __init__(self,page):
        print("### Page Welcome ###")
        self.page = page

    def set_nike_by_link(self):
        self.page.goto("https://www.nike.com/en")
        men_button = self.page.locator("[href='https://www.nike.com/men']")
        men_button.click()
        women_button = self.page.locator("[href='https://www.nike.com/women']")
        women_button.click()
