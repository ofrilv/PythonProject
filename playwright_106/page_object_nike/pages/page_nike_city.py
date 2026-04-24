

class PageNikeCity ():
    def __init__(self,page):
        print("### Page Welcome ###")
        self.page = page

    def set_nike_by_city(self):
        store = self.page.locator('[class="interactive-profile-element"]').first.click()
        search_location = self.page.locator('[class="nds-input-text-field has-prefix-icon css-1yzc0py e1fiih290"]')
        search_location.fill("London")
        self.page.keyboard.press("Enter")
        stores = self.page.locator('[class*="d-sm-flx"]').count()
        assert stores > 1, "Number of stores must be more than one"
