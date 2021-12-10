"""
This module contains step definitions for flights search feature.
It uses Selenium WebDriver for browser interactions
"""
from pytest_bdd import scenarios, given, when, then, parsers

from pages.guest_main_page import GuestMainPage
from pages.search_flights_page import SearchFlightsPage
from pages.user_main_page import UserMainPage
from utils.links import Links


scenarios('../features/flight_search.feature')


@given('I am on main page', target_fixture='user_on_main_page')
def user_on_main_page(browser, user, password):
    guest_main_page = GuestMainPage(browser, Links.MAIN_PAGE_LINK, timeout=0)
    guest_main_page.open()
    guest_main_page.accept_cookies()
    guest_main_page.go_to_sign_in()
    guest_main_page.sign_in_user(user, password)


@when(parsers.cfparse('I input {departure_airport} to From Airport Form'))
def input_departure_location(browser, departure_airport):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_depature_airport(departure_airport)


@when(parsers.cfparse('I input {destination_airport} to To Airport Form'))
def input_destination_location(browser, destination_airport):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_destination_airport(destination_airport)


@when(parsers.cfparse('I choose {depart_date} at Depart Form'))
def input_depart_date(browser, depart_date):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_depart_date(depart_date)


@when(parsers.cfparse('I choose {return_date} at Return Form'))
def input_return_date(browser, return_date):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_return_date(return_date)
    user_main_page.go_flight_search()


@then(parsers.cfparse('I should see flight cards from {departure_airport} to {destination_airport} at {depart_date} '
                      'and {return_date}'))
def should_be_flights(browser, departure_airport, destination_airport, depart_date, return_date):
    search_flight_page = SearchFlightsPage(browser, browser.current_url)
    search_flight_page.should_be_correct_page_url()
    search_flight_page.should_be_flight_card()
    search_flight_page.should_be_correct_depart_name(departure_airport)
    search_flight_page.should_be_correct_destination_name(destination_airport)
    search_flight_page.should_be_correct_depart_date(depart_date)
    search_flight_page.should_be_correct_return_date(return_date)
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.log_out_from_fligths()
