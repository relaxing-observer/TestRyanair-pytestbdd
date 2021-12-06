from pytest_bdd import scenarios, given, when, then, parsers
from pages.guest_main_page import GuestMainPage

@given(parsers.parse('I am on "{main}" page', target_fixture='sign_in_to_user_main_page'))
def sign_in_to_user_main_page(browser, main):
    guest_main_page = GuestMainPage(browser, main)
    guest_main_page.choose_english_language()
    guest_main_page.accept_cookies()

