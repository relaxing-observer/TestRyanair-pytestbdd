from pytest_bdd import scenarios, given, when, then, parsers

from pages.user_main_page import UserMainPage
from utils.url_storage import PageUrl
from utils.page_builder import PageConstructor

scenarios('../features/cars_search.feature')

@given(parsers.cfparse('I am on "{main}" page'), target_fixture='main_page')
def main_page(browser, user, password, main):
    user_main_page = PageConstructor.get_class(main)(browser, PageUrl.get_page_link(main))
    user_main_page.open()
    user_main_page.accept_cookies()
    user_main_page.sign_in_user(user, password)
