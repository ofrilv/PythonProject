


class PageSearchNike ():
    def __init__(self,page):
        print("### Page Welcome ###")
        self.page = page

    def set_search(self):
        search= self.page.locator('[class="search-input-container"]')
        search.click()
        search.get_by_text("shoes")
        results = self.page.locator("text=Shoes")
        results_as_float= float(results)
        assert results.count() > 0, "make sure shoes appears in search"
        print("### Set Search ###")

