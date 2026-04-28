class PageZara_kids_button ():
    def __init__(self,page):
        print("### Page Welcome ###")
        self.page = page


    def test_zara_kids_button(self):

        kids_button = self.page.get_by_role("button, name=kids")
        assert "kids" in self.page.url.lower()
