import time

from pytest_bdd import scenarios, given, when, then, parsers
from pages.guest_main_page import GuestMainPage
from utils.links import Links

@given(('I am on main page'), target_fixture='sign_in_to_user_main_page')
def sign_in_to_user_main_page(browser):
    guest_main_page = GuestMainPage(browser, Links.MAIN_PAGE_LINK)
    guest_main_page.open()
    guest_main_page.accept_cookies()
    guest_main_page.go_to_sign_in()
    guest_main_page.sign_in_user()



