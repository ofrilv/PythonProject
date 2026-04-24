

from playwright_106.page_object_nike.pages.page_nike_by_city import PageNikeCity
from playwright_106.page_object_nike.pages.page_nike_link import PageNikeLink
from playwright_106.page_object_nike.pages.page_search_nike import PageSearchNike


def test_nike_search(setup_playwright_nike_search):
    page = setup_playwright_nike_search
    page.goto("https://www.nike.com/en")
    page_nike_search= PageSearchNike(page)
    print("test end")

def test_nike_by_city(setup_playwright_nike_search):
    page = setup_playwright_nike_search
    page.goto("https://www.nike.com/")
    page_nike_city= PageNikeCity(page)
    print("test end")

def test_nike_by_link(setup_playwright_nike_search):
    page = setup_playwright_nike_search
    page.goto("https://www.nike.com/")
    page_nike_link= PageNikeLink(page)
    print("test end")

