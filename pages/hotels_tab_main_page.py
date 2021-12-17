import allure

from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from utils.datepicker_handler import DatePickerHandler
from pages.user_main_page import UserMainPage
from .locators.locators import HotelsTabMainPageLocators


class HotelsTabMainPage(UserMainPage, BasePage):
    @allure.step("Input destination hotel")
    def input_location(self, hotel_name):
        """
        Method inputs name of destination location
        """
        BrowserHelper.send_keys(self.browser, *HotelsTabMainPageLocators.DESTINATION_HOTEL_FORM, hotel_name)
        confirmation_button = BrowserHelper.find_visible_element(self.browser, *HotelsTabMainPageLocators.CONFIRMATION_HOTEL)
        confirmation_button.click()

    @allure.step
    def select_check_in_date(self, check_in_date):
        """
        Method inputs date of check-in
        """
        check_in_form = BrowserHelper.find_visible_element(self.browser, *HotelsTabMainPageLocators.CHECK_IN_FORM)
        check_in_form.click()
        check_in_month = BrowserHelper.find_visible_element(self.browser, *DatePickerHandler.get_month_button(check_in_date))
        check_in_month.click()
        check_in_day = BrowserHelper.find_visible_element(self.browser, *DatePickerHandler.get_day_button(check_in_date))
        check_in_day.click()

    @allure.step
    def select_check_out_date(self, check_out_date):
        """
        Method inputs date of check-out
        """
        check_out_form = BrowserHelper.find_visible_element(self.browser, *HotelsTabMainPageLocators.CHECK_OUT_FORM)
        check_out_form.click()
        check_out_month = BrowserHelper.find_visible_element(self.browser, *DatePickerHandler.get_month_button(check_out_date))
        check_out_month.click()
        check_out_day = BrowserHelper.find_visible_element(self.browser, *DatePickerHandler.get_day_button(check_out_date))
        check_out_day.click()

    @allure.step("Go searching hotels")
    def go_search(self):
        """
        Method clicks on Search button
        """
        search_button = BrowserHelper.find_visible_element(self.browser, *HotelsTabMainPageLocators.SEARCH_HOTEL_BUTTON)
        search_button.click()
