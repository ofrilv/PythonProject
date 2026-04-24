class PageWelcomeZara ():
    def __init__(self,page):
        print("### Page Welcome ###")
        self.page = page

    def set_zara_search(self):
        self.page.goto("conftest.py")
        search_bnt = self.page.locator('[type="search"]')
        search_bnt.click()
        search_bnt.fill("Shirt")
        self.page.keyboard.press("Enter")
        results = self.page.locator('class*=["product-link _item"]')
        results_as_float = float(results)
        assert results.count() > 0, "make sure shirt appears in search"