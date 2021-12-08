import allure
from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from .locators.locators import SearchFlightsPageLocators


class SearchFlightsPage(BrowserHelper, BasePage):
    @allure.step("Should be correct URL of page")
    def should_be_correct_page_url(self):
        assert self.wait_phrase_in_url(SearchFlightsPageLocators.URL_IDENTIFIER), "Probably you don't chose flight"

    @allure.step("Should be flight item")
    def should_be_flight_card(self):
        flight_cards = self.browser.find_elements(*SearchFlightsPageLocators.FLIGHT_CARD)
        assert len(flight_cards) > 1, "There are no flights for return way or no any flights"

    @allure.step("Should be correct depart name airport")
    def should_be_correct_depart_name(self, scenario_airport):
        depart_name = self.find_visible_element(*SearchFlightsPageLocators.get_departure_header(scenario_airport))
        assert scenario_airport in depart_name.text,\
            "Scenario name should be equal to name of airport at page"

    @allure.step("Should be correct destination name airport")
    def should_be_correct_destination_name(self, scenario_airport):
        destination_name = self.find_visible_element(*SearchFlightsPageLocators.get_departure_header(scenario_airport))
        assert scenario_airport in destination_name.text,\
            "Scenario name should be equal to name of airport at page"

    @allure.step("Should be correct depart dates")
    def should_be_correct_depart_date(self, depart_date):
        depart_day_and_month = depart_date[:5]
        actual_flights_details = self.find_visible_element(*SearchFlightsPageLocators.FLIGHT_DETAILS).text
        assert depart_day_and_month in actual_flights_details, "Depart date should be in flight details"

    @allure.step("Should be correct return dates")
    def should_be_correct_return_date(self, return_date):
        return_day_and_month = return_date[:5]
        actual_flights_details = self.find_visible_element(*SearchFlightsPageLocators.FLIGHT_DETAILS).text
        assert return_day_and_month in actual_flights_details, "Return date should be in flight details"
