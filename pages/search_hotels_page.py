import allure
from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from .locators.locators import SearchHotelsPageLocators


class SearchHotelsPage(BrowserHelper, BasePage):
    @allure.step("Accept cookies")
    def accept_cookies(self):
        try:
            accept_button = self.find_clickable_element(*SearchHotelsPageLocators.ACCEPT_COOKIES_BUTTON, timeout=0)
            accept_button.click()
        except:
            pass

    @allure.step("Should be correct URL of page")
    def should_be_correct_page_url(self):
        is_url_correct = self.wait_phrase_in_url(SearchHotelsPageLocators.URL_IDENTIFIER)
        assert is_url_correct, "Probably you don't chose flight"

    @allure.step("Should be accomodation card")
    def should_be_accomodation_card(self):
        accomodation_card = self.find_visible_element(*SearchHotelsPageLocators.ACCOMODATION_CARD)
        assert accomodation_card, "There are no accomodation cards with hotels on the page"

    @allure.step("Should be correct destination name")
    def should_be_correct_location_name(self, location):
        actual_location = self.find_visible_element(*SearchHotelsPageLocators.ACTUAL_DESTINATION_SUMMARY)
        assert location in actual_location.text, "Location in step is not equal with actual"

    @allure.step("Should be correct dates of check-in and check-out")
    def should_be_correct_dates(self, check_in_date, check_out_date):
        actual_dates = self.find_visible_element(*SearchHotelsPageLocators.ACTUAL_DATES_SUMMARY)
        assert check_in_date and check_out_date in actual_dates.text, "Given dates is not in actual dates on the page"



