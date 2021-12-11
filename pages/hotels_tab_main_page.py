import allure

from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from .locators.locators import DatePickerLocators
from pages.user_main_page import UserMainPage
from .locators.locators import UserMainPageLocators

class HotelsTabMainPage(UserMainPage, BrowserHelper, BasePage):
    @allure.step("Input destination hotel")
    def input_destination_hotel_location(self, hotel_name):
        """
        Method inputs name of destination location
        """
        self.send_keys(*UserMainPageLocators.DESTINATION_HOTEL_FORM, hotel_name)
        confirmation_button = self.find_visible_element(*UserMainPageLocators.CONFIRMATION_HOTEL)
        confirmation_button.click()

    @allure.step
    def input_check_in_date(self, check_in_date):
        """
        Method inputs date of check-in
        """
        check_in_form = self.find_visible_element(*UserMainPageLocators.CHECK_IN_FORM)
        check_in_form.click()
        check_in_month = self.find_visible_element(*DatePickerLocators.get_month_button(check_in_date))
        check_in_month.click()
        check_in_day = self.find_visible_element(*DatePickerLocators.get_day_button(check_in_date))
        check_in_day.click()

    @allure.step
    def input_check_out_date(self, check_out_date):
        """
        Method inputs date of check-out
        """
        check_out_form = self.find_visible_element(*UserMainPageLocators.CHECK_OUT_FORM)
        check_out_form.click()
        check_out_month = self.find_visible_element(*DatePickerLocators.get_month_button(check_out_date))
        check_out_month.click()
        check_out_day = self.find_visible_element(*DatePickerLocators.get_day_button(check_out_date))
        check_out_day.click()


    @allure.step("Go searching hotels")
    def go_search(self):
        """
        Method clicks on Search button
        """
        search_button = self.find_visible_element(*UserMainPageLocators.SEARCH_HOTEL_BUTTON)
        search_button.click()