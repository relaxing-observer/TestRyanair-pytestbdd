import allure
from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from .locators.locators import SearchCarsPageLocators


class SearchCarsPage(BrowserHelper, BasePage):
    @allure.step("Accept cookies")
    def accept_cookies(self):
        accept_cookies_button = self.find_visible_element(*SearchCarsPageLocators.ACCEPT_COOKIES_BUTTON)
        accept_cookies_button.click()

    @allure.step("Should be car card")
    def should_be_car_card(self):
        assert self.find_visible_element(*SearchCarsPageLocators.CAR_CARD), "No results with car cards"

    @allure.step("Should be correct location")
    def should_be_correct_location(self, location):
        actual_search_summary = self.find_visible_element(*SearchCarsPageLocators.SEARCH_SUMMARY)
        assert location in actual_search_summary.text, "There are no correct name location"

    @allure.step("Should be correct date of pick up")
    def should_be_correct_pick_up_date(self, pick_up_date):
        actual_search_summary = self.find_visible_element(*SearchCarsPageLocators.SEARCH_SUMMARY)
        pick_up_day = pick_up_date[:2].strip()
        assert pick_up_day in actual_search_summary.text, "There are no correct date to pick up"

    @allure.step("Should be correct date of drop off")
    def should_be_correct_drop_off_date(self, drop_off_date):
        actual_search_summary = self.find_visible_element(*SearchCarsPageLocators.SEARCH_SUMMARY)
        drop_off_day = drop_off_date[:2].strip()
        assert drop_off_day in actual_search_summary.text, "There are no correct date to drop off"

    @allure.step("Should be correct time of pick up")
    def should_be_correct_pick_up_time(self, pick_up_time):
        pick_up_hours = pick_up_time[:2].strip()
        actual_search_summary = self.find_visible_element(*SearchCarsPageLocators.SEARCH_SUMMARY)
        assert pick_up_hours in actual_search_summary.text, "There are no correct time to pick up"

    @allure.step("Should be correct time of drop off")
    def should_be_correct_drop_off_time(self, drop_off_time):
        pick_up_hours = drop_off_time[:2].strip()
        actual_search_summary = self.find_visible_element(*SearchCarsPageLocators.SEARCH_SUMMARY)
        assert pick_up_hours in actual_search_summary.text, "There are no correct time to drop off"

    @allure.step("Go to home page")
    def go_home_page(self):
        main_logo = self.find_visible_element(*SearchCarsPageLocators.MAIN_LOGO)
        main_logo.click()