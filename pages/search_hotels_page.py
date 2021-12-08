import allure
from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from .locators.locators import SearchHotelsPageLocators


class SearchHotelsPage(BrowserHelper, BasePage):
    @allure.step("Accept cookies")
    def accept_cookies(self):
        try:
            accept_button = self.find_clickable_element(*SearchHotelsPageLocators.ACCEPT_COOKIES_BUTTON, timeout=1)
            accept_button.click()
        except:
            pass

    @allure.step("Should be correct URL of page")
    def should_be_correct_page_url(self):
        assert self.wait_phrase_in_url(SearchHotelsPageLocators.URL_IDENTIFIER),\
            "Probably you don't chose flight"

    @allure.step("Should be accomodation card")
    def should_be_accomodation_card(self):
        assert self.find_visible_element(*SearchHotelsPageLocators.ACCOMODATION_CARD),\
            "There are no accomodation cards with hotels on the page"



