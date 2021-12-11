"""
This module contains step definitions for flights search feature.
It uses Selenium WebDriver for browser interactions
"""
from pytest_bdd import scenarios, given, when, then, parsers

from pages.user_main_page import UserMainPage
from utils.links import Links
from utils.page_builder import PageConstructor

scenarios('../features/flight_search.feature')


@given(parsers.cfparse('I am on "{main}" page'), target_fixture='main_page')
def main_page(browser, user, password, main):
    main_page = PageConstructor.get_class(main)(browser, Links.get_page_link(main), timeout=0)
    main_page.open()
    main_page.accept_cookies()
    main_page.sign_in_user(user, password)

@when(parsers.cfparse('I input "{departure_airport}" to From Airport Form on "{flights}" tab'))
def input_departure_location(browser, departure_airport, flights):
    flight_page = PageConstructor.get_class(flights)(browser, browser.current_url)
    flight_page.input_depature_airport(departure_airport)

@when(parsers.cfparse('I input "{destination_airport}" to To Airport Form on "{flights}" tab'))
def input_destination_location(browser, destination_airport, flights):
    flight_page = PageConstructor.get_class(flights)(browser, browser.current_url)
    flight_page.input_destination_airport(destination_airport)


@when(parsers.cfparse('I choose "{depart_date}" at Depart Form on "{flights}" tab'))
def input_depart_date(browser, depart_date, flights):
    flight_page = PageConstructor.get_class(flights)(browser, browser.current_url)
    flight_page.input_depart_date(depart_date)


@when(parsers.cfparse('I choose "{return_date}" at Return Form on "{flights}" tab'))
def input_return_date(browser, return_date, flights):
    flight_page = PageConstructor.get_class(flights)(browser, browser.current_url)
    flight_page.input_return_date(return_date)
    flight_page.go_search()


@then(parsers.cfparse('I should see flight cards from "{departure_airport}" to "{destination_airport}" at "{depart_date}" and "{return_date}" at "{search_flights}" page'))
def should_be_flights(browser, departure_airport, destination_airport, depart_date, return_date, search_flights):
    search_flight_page = PageConstructor.get_class(search_flights)(browser, browser.current_url)
    search_flight_page.should_be_correct_page_url()
    search_flight_page.should_be_flight_card()
    search_flight_page.should_be_correct_depart_name(departure_airport)
    search_flight_page.should_be_correct_destination_name(destination_airport)
    search_flight_page.should_be_correct_depart_date(depart_date)
    search_flight_page.should_be_correct_return_date(return_date)
    search_flight_page.go_to_main_page()
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.log_out()
