"""
This module contains step definitions for cucumbers.feature.
It uses Selenium WebDriver for browser interactions
"""
from pytest_bdd import scenarios, given, when, then, parsers

from pages.guest_main_page import GuestMainPage
from pages.user_main_page import UserMainPage
from utils.links import Links
from pages.search_hotels_page import SearchHotelsPage
from pages.user_main_hotels_page import UserMainHotelsPage
scenarios('../features/cars_search.feature')

@given('I am on main page', target_fixture='user_on_main_page')
def user_on_main_page(browser, user, password):
    guest_main_page = GuestMainPage(browser, Links.MAIN_PAGE_LINK, timeout=1)
    guest_main_page.open()
    guest_main_page.accept_cookies()
    guest_main_page.go_to_sign_in()
    guest_main_page.sign_in_user(user, password)

@when('I choose cars tab')
def select_hotels_tab(browser):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.go_to_cars()


@when(parsers.cfparse('I input {location} to City Form'))
def input_destination_location(browser, location):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_car_location(location)

@when(parsers.cfparse('I choose {pick_up_date} at Pick-Un Form'))
def input_pickup_date(browser, pick_up_date):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_pickup_date(pick_up_date)


@when(parsers.cfparse('I choose {drop_off_date} at Drop-Off Form'))
def input_return_date(browser, drop_off_date):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_dropoff_date(drop_off_date)
