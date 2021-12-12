"""
This module contains step definitions for cucumbers.feature.
It uses Selenium WebDriver for browser interactions
"""
from pytest_bdd import scenarios, given, when, then, parsers

from utils.links import Links
from utils.page_builder import PageConstructor

scenarios('../features/hotels_search.feature')


@given(parsers.cfparse('I am on "{main}" page'), target_fixture='main_page')
def main_page(browser, main, user, password):
    main_page = PageConstructor.get_class(main)(browser, Links.get_page_link(main))
    main_page.open()
    main_page.accept_cookies()
    main_page.sign_in_user(user, password)


@when(parsers.cfparse('I choose "{hotels}" tab on "{main}" page'))
def select_hotels_tab(browser, hotels, main):
    main_page = PageConstructor.get_class(main)(browser, browser.current_url)
    main_page.go_to_tab(hotels)


@when(parsers.cfparse('I input "{location}" to Destination Form on "{hotels}" tab'))
def input_destination_location(browser, location, hotels):
    hotel_page = PageConstructor.get_class(hotels)(browser, browser.current_url)
    hotel_page.input_location(location)

@when(parsers.cfparse('I choose "{check_in_date}" at Check-In Form on "{hotels}" tab'))
def input_check_in_date(browser, check_in_date, hotels):
    hotel_page = PageConstructor.get_class(hotels)(browser, browser.current_url)
    hotel_page.select_check_in_date(check_in_date)

@when(parsers.cfparse('I choose "{check_out_date}" at Check-out Form on "{hotels}" tab'))
def input_check_out_date(browser, check_out_date, hotels):
    hotel_page = PageConstructor.get_class(hotels)(browser, browser.current_url)
    hotel_page.select_check_out_date(check_out_date)
    hotel_page.go_search()

@then(parsers.cfparse('I should see accommodation cards in "{location}" from "{check_in_date}" to "{check_out_date}" on "{search_hotels}" page'))
def should_be_hotels(browser, location, check_in_date, check_out_date, search_hotels):
    search_hotels_page = PageConstructor.get_class(search_hotels)(browser, browser.current_url)
    search_hotels_page.accept_cookies()
    search_hotels_page.should_be_correct_page_url()
    search_hotels_page.should_be_accommodation_card()
    search_hotels_page.should_be_correct_location_name(location)
    search_hotels_page.should_be_correct_dates(check_in_date, check_out_date)
    search_hotels_page.log_out()
