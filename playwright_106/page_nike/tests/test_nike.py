from playwright_106.page_nike.pages.page_nike_click_on_link import PageNikeLink
from playwright_106.page_nike.pages.page_nike_welcome import PageNikeSearchwelcome
from playwright_106.page_nike.pages.page_search_by_city import PageNikeCity


def test_nike_search(setup_playwright_nike):
    page = setup_playwright_nike
    page.goto("https://www.nike.com/")
    page_nike_search= PageNikeSearchwelcome(page)
    print("### Test end ###")


def test_nike_search_by_city(setup_playwright_nike):
    page = setup_playwright_nike
    page.goto("https://www.nike.com/")
    page_nike_by_city= PageNikeCity(page)
    page_nike_by_city.set_nike_by_city()
    print("### Test end ###")

def test_nike_click_on_link(setup_playwright_nike):
    page = setup_playwright_nike
    page.goto("https://www.nike.com/")
    page_nike_click_on_link= PageNikeLink(page)

    print("### Test end ###")
