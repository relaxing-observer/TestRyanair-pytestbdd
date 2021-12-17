import allure
from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from utils.url_storage import IdentityPhraseUrl
from .locators.locators import SearchFlightsPageLocators


class SearchFlightsPage(BasePage):
    @allure.step("Go to main page")
    def go_to_main_page(self):
        home_logo = BrowserHelper.find_visible_element(self.browser, *SearchFlightsPageLocators.MAIN_LOGO)
        home_logo.click()

    @allure.step("Should be correct URL of page")
    def should_be_correct_page_url(self):
        assert BrowserHelper.wait_phrase_in_url(self.browser, IdentityPhraseUrl.SearchFlightsPage), "Probably you don't chose flight"

    @allure.step("Should be flight item")
    def should_be_flight_card(self):
        flight_card = BrowserHelper.find_visible_element(self.browser, *SearchFlightsPageLocators.FLIGHT_CARD)
        assert flight_card, "There are no flights cards for any destinations"

    @allure.step("Should be correct depart name airport")
    def should_be_correct_depart_name(self, scenario_airport):
        depart_name = BrowserHelper.find_visible_element(self.browser, *SearchFlightsPageLocators.get_departure_header(scenario_airport))
        assert scenario_airport in depart_name.text,\
            "Scenario name should be equal to name of airport at page"

    @allure.step("Should be correct destination name airport")
    def should_be_correct_destination_name(self, scenario_airport):
        destination_name = BrowserHelper.find_visible_element(self.browser, *SearchFlightsPageLocators.get_departure_header(scenario_airport))
        assert scenario_airport in destination_name.text,\
            "Scenario name should be equal to name of airport at page"

    @allure.step("Should be correct depart dates")
    def should_be_correct_depart_date(self, depart_date):
        depart_day_and_month = depart_date[:5]
        actual_flights_details = BrowserHelper.find_visible_element(self.browser, *SearchFlightsPageLocators.FLIGHT_DETAILS).text
        assert depart_day_and_month in actual_flights_details, "Depart date should be in flight details"

    @allure.step("Should be correct return dates")
    def should_be_correct_return_date(self, return_date):
        return_day_and_month = return_date[:5]
        actual_flights_details = BrowserHelper.find_visible_element(self.browser, *SearchFlightsPageLocators.FLIGHT_DETAILS).text
        assert return_day_and_month in actual_flights_details, "Return date should be in flight details"
