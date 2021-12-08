import allure

from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from .locators.locators import DatePickerLocators
from .locators.locators import MainHeaderLocators
from .locators.locators import UserMainPageLocators


class UserMainPage(BrowserHelper, BasePage):
    @allure.step("Input departure airport")
    def input_depature_airport(self, name_airport):
        """
        Method inputs name of departure airport in form
        """
        departure_form = self.find_clickable_element(*UserMainPageLocators.INPUT_DEPARTURE_FORM)
        departure_form.click()
        departure_form.clear()
        departure_form.send_keys(name_airport)
        confirmation_button = self.find_visible_element(*UserMainPageLocators.CONFIRMATION_AIRPORT)
        confirmation_button.click()

    @allure.step("Input destination airport")
    def input_destination_airport(self, name_airport):
        """
        Method inputs name of destination airport in form
        """
        destination_form = self.find_clickable_element(*UserMainPageLocators.INPUT_DESTINATION_FORM)
        destination_form.click()
        destination_form.clear()
        destination_form.send_keys(name_airport)
        confirmation_button = self.find_visible_element(*UserMainPageLocators.CONFIRMATION_AIRPORT)
        confirmation_button.click()

    @allure.step("Input depart date")
    def input_depart_date(self, depart_date):
        """
        Method inputs date of departure
        """
        depart_month = self.find_visible_element(*DatePickerLocators.get_month_button(depart_date))
        depart_month.click()
        depart_day = self.find_visible_element(*DatePickerLocators.get_day_button(depart_date))
        depart_day.click()

    @allure.step("Input return date")
    def input_return_date(self, return_date):
        """
        Method inputs date of returning
        """
        return_form = self.find_visible_element(*DatePickerLocators.RETURN_FORM)
        return_form.click()
        return_month = self.find_visible_element(*DatePickerLocators.get_month_button(return_date))
        return_month.click()
        return_day = self.find_visible_element(*DatePickerLocators.get_day_button(return_date))
        return_day.click()


    @allure.step("Go searching")
    def go_search(self):
        """
        Method clicks on Search button and start searching
        """
        search_button = self.find_visible_element(*UserMainPageLocators.SEARCH_BUTTON)
        search_button.click()

    @allure.step("Log out")
    def log_out(self):
        """
        Method logs out form service
        """
        dropdown_profile = self.find_visible_element(*MainHeaderLocators.DROPDOWN_PROFILE)
        dropdown_profile.click()
        log_out_button = self.find_visible_element(*MainHeaderLocators.LOG_OUT_BUTTON)
        log_out_button.click()
