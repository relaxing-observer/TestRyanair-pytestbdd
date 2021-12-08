"""
This module contains step definitions for cucumbers.feature.
It uses Selenium WebDriver for browser interactions
"""
import time

from pytest_bdd import scenarios, given, when, then, parsers

from pages.guest_main_page import GuestMainPage
from pages.user_main_page import UserMainPage
from utils.links import Links
from pages.search_hotels_page import SearchHotelsPage
scenarios('../features/hotels_search.feature')


@given('I am on main page', target_fixture='user_on_main_page')
def user_on_main_page(browser):
    guest_main_page = GuestMainPage(browser, Links.MAIN_PAGE_LINK, timeout=0)
    guest_main_page.open()
    guest_main_page.accept_cookies()
    guest_main_page.go_to_sign_in()
    guest_main_page.sign_in_user()


@when('I choose hotels tab')
def select_hotels_tab(browser):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.go_to_hotels()


@when(parsers.cfparse('I input {location} to Destination Form'))
def input_destination_location(browser, location):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.go_to_hotels()
    user_main_page.input_destination_hotel_location(location)

@when(parsers.cfparse('I choose {check_in_date} at Check-In Form'))
def input_check_in_date(browser, check_in_date):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_check_in_date(check_in_date)


@when(parsers.cfparse('I choose {check_out_date} at Check-out Form'))
def input_check_out_date(browser, check_out_date):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_check_out_date(check_out_date)
    user_main_page.go_hotel_search()

@then(parsers.cfparse('I should see accommodation cards in {location} from {check_in_date} to {check_out_date}'))
def should_be_hotels(browser, location, check_in_date, check_out_date):
    search_flight_page = SearchHotelsPage(browser, browser.current_url)
    search_flight_page.accept_cookies()
    search_flight_page.should_be_correct_page_url()
    search_flight_page.should_be_accomodation_card()
    time.sleep(5)

#     search_flight_page.should_be_flight_card()
#     search_flight_page.should_be_correct_depart_name(departure_airport)
#     search_flight_page.should_be_correct_destination_name(destination_airport)
#     search_flight_page.should_be_correct_depart_date(depart_date)
#     search_flight_page.should_be_correct_return_date(return_date)
#     user_main_page = UserMainPage(browser, browser.current_url)
#     user_main_page.log_out()