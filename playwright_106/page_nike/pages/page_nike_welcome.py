

class PageNikeSearchwelcome():
    def __init__(self,page):
        print("### Page Welcome###")
        self.page = page

    def set_click_on_find_store(self):
        find_store = self.page.locator('[href="https://www.nike.com/retail"]')
        find_store.click()
