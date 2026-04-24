from playwright_106.page_object_zara.pages.page_welcome_zara import PageWelcomeZara
from playwright_106.page_object_zara.pages.page_zara_kids_button import PageZara_kids_button
from playwright_106.page_object_zara.pages.page_zara_shopping_bag import PageZaraShoppingBag


def test_zara_search(setup_playwright_zara_search):
    page = setup_playwright_zara_search
    page.goto("https://www.zara.com/il/en/search/home")
    page_welcome_zara= PageWelcomeZara(page)
    print("test end")


def test_zara_shopping_bag(setup_playwright_zara_search):
    page = setup_playwright_zara_search
    page.goto("https://www.zara.com/il/en/search/home")
    page_zara_shopping_bag= PageZaraShoppingBag(page)
    print("test end")

def test_zara_kids_button(setup_playwright_zara_search):
    page = setup_playwright_zara_search
    page.goto("https://www.zara.com/il/en/search/home")
    page_zara_kids_button= PageZara_kids_button(page)