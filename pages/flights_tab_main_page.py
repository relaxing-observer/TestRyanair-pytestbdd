import allure

from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from utils.datepicker_handler import DatePickerHandler
from pages.user_main_page import UserMainPage
from .locators.locators import UserMainPageLocators
from .locators.locators import FlightsTabMainPageLocators


class FlightTabMainPage(UserMainPage, BrowserHelper, BasePage):
    @allure.step("Input departure airport")
    def input_depature_airport(self, name_airport):
        """
        Method inputs name of departure airport in form
        """
        self.send_keys(*FlightsTabMainPageLocators.INPUT_DEPARTURE_FORM, name_airport)
        confirmation_button = self.find_visible_element(*FlightsTabMainPageLocators.CONFIRMATION_AIRPORT)
        confirmation_button.click()

    @allure.step("Input destination airport")
    def input_destination_airport(self, airport_name):
        """
        Method inputs name of destination airport in form
        """
        self.send_keys(*FlightsTabMainPageLocators.INPUT_DESTINATION_FORM, airport_name)
        confirmation_button = self.find_visible_element(*FlightsTabMainPageLocators.CONFIRMATION_AIRPORT)
        confirmation_button.click()

    @allure.step("Input depart date")
    def select_depart_date(self, depart_date):
        """
        Method inputs date of departure
        """
        depart_month = self.find_visible_element(*DatePickerHandler.get_month_button(depart_date))
        depart_month.click()
        depart_day = self.find_visible_element(*DatePickerHandler.get_day_button(depart_date))
        depart_day.click()

    @allure.step("Input return date")
    def select_return_date(self, return_date):
        """
        Method inputs date of returning
        """
        return_form = self.find_visible_element(*FlightsTabMainPageLocators.RETURN_FORM)
        return_form.click()
        return_month = self.find_visible_element(*DatePickerHandler.get_month_button(return_date))
        return_month.click()
        return_day = self.find_visible_element(*DatePickerHandler.get_day_button(return_date))
        return_day.click()

    @allure.step("Go searching flights")
    def go_search(self):
        """
        Method clicks on Search button
        """
        search_button = self.find_visible_element(*FlightsTabMainPageLocators.SEARCH_FLIGHT_BUTTON)
        search_button.click()
