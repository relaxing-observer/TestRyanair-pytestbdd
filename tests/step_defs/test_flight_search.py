"""
This module contains step definitions for cucumbers.feature.
It uses Selenium WebDriver for browser interactions
"""
import time

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.user_main_page import UserMainPage

from utils.links import Links

CONVERTERS = {
    'departure airport': str,
    'destination airport': str,
    'depart date': str,
    'return date': str,
}

scenarios('../features/flight_search.feature')



@when(parsers.cfparse('I input "{departure_airport}" to From Airport Form'), converters=CONVERTERS)
def input_departure_location(browser, departure_airport):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_depature_airport(departure_airport)

@when(parsers.cfparse('I input "{destination_airport}" to To Airport Form'), converters=CONVERTERS)
def input_destination_location(browser, destination_airport):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_destination_airport(destination_airport)

@when(parsers.cfparse('I choose "{depart_date}" at Depart Form'), converters=CONVERTERS)
def input_depart_date(browser, depart_date):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_depart_date(depart_date)

@when(parsers.cfparse('I choose "{return_date}" at Return Form'), converters=CONVERTERS)
def input_return_date(browser, return_date):
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.input_return_date(return_date)
    user_main_page.go_search()
    time.sleep(10)


@then(parsers.cfparse('I should see "flight_contents" from "{departure_airport}"'
                      ' to "{destination_airport}" at "{depart_date}"'), converters=CONVERTERS)
def should_be_flights_contents(browser, departure_airport, destination_airport, depart_date):
    pass


