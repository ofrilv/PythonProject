class PageNikeLink ():
    def __init__(self,page):
        print("### Page Welcome ###")
        self.page = page

    def set_nike_by_link(self):

        men_button = self.page.get_by_role("link", name="Men").first.click()

        assert "men" in self.page.url.lower()

        women_button = self.page.get_by_role("link", name="Women").last.click()


        assert "women" in self.page.url.lower()


