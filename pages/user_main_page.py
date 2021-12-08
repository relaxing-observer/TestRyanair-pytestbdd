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
    def input_destination_airport(self, airport_name):
        """
        Method inputs name of destination airport in form
        """
        destination_form = self.find_clickable_element(*UserMainPageLocators.INPUT_DESTINATION_FORM)
        destination_form.click()
        destination_form.clear()
        destination_form.send_keys(airport_name)
        confirmation_button = self.find_visible_element(*UserMainPageLocators.CONFIRMATION_AIRPORT)
        confirmation_button.click()

    @allure.step("Input destination hotel")
    def input_destination_hotel_location(self, hotel_name):
        """
        Method inputs name of destination location
        """
        destination_form = self.find_visible_element(*UserMainPageLocators.DESTINATION_HOTEL_FORM)
        destination_form.click()
        destination_form.send_keys(hotel_name)
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


    @allure.step("Go searching flights")
    def go_flight_search(self):
        """
        Method clicks on Search button and start searching
        """
        search_button = self.find_visible_element(*UserMainPageLocators.SEARCH_FLIGHT_BUTTON)
        search_button.click()

    @allure.step("Go searching hotels")
    def go_hotel_search(self):
        """
        Method clicks on Search button and start searching
        """
        search_button = self.find_visible_element(*UserMainPageLocators.SEARCH_HOTEL_BUTTON)
        search_button.click()

    @allure.step("Go to hotels tab")
    def go_to_hotels(self):
        """
        Method clicks on Hotels tab
        """
        hotels_tab = self.find_visible_element(*UserMainPageLocators.HOTELS_TAB)
        hotels_tab.click()

    @allure.step("Log out")
    def log_out(self):
        """
        Method logs out form service
        """
        dropdown_profile = self.find_visible_element(*MainHeaderLocators.DROPDOWN_PROFILE)
        dropdown_profile.click()
        log_out_button = self.find_visible_element(*MainHeaderLocators.LOG_OUT_BUTTON)
        log_out_button.click()
