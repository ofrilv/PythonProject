


class PageZaraShoppingBag ():
    def __init__(self,page):
        print("### Page Welcome ###")
        self.page = page

    def set_zara_shopping_bag(self):
        self.page.goto("https://www.zara.com/il/en/search/home")

        shopping_button = self.page.locator("[class='layout-actionable link']").all()[0]
        # shopping_button = page.locator("[class*='layout-actionabl']").all()[0]

        shopping_button_text = shopping_button.inner_text()
        index = shopping_button_text.index("bag")
        count = shopping_button_text[index + 3:]
        count_1 = shopping_button_text[-1:]
        assert shopping_button==0, "shopping bag contains 0 items"
        print("Shopping bag contains 0")
