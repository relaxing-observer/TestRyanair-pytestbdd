import allure

from pages.base_page import BasePage
from pages.user_main_page import UserMainPage
from utils.browser_helper import BrowserHelper
from utils.datepicker_handler import DatePickerHandler
from .locators.locators import CarsTabMainPageLocators


class CarsTabMainPage(UserMainPage, BrowserHelper, BasePage):
    @allure.step("Input destination location for rent car")
    def input_location(self, location_name):
        """
        Method inputs name of location for rent car
        """
        self.send_keys(*CarsTabMainPageLocators.CAR_LOCATION, location_name)
        confirmation_button = self.find_visible_element(*CarsTabMainPageLocators.CONFIRMATION_CAR_LOCATION)
        confirmation_button.click()
    @allure.step
    def select_pickup_date(self, pickup_date):
        """
        Method inputs date of pick_up
        """
        pick_up_form = self.find_visible_element(*CarsTabMainPageLocators.PICK_UP_FORM)
        pick_up_form.click()
        pick_up_month = self.find_visible_element(*DatePickerHandler.get_month_button(pickup_date))
        pick_up_month.click()
        pick_up_day = self.find_visible_element(*DatePickerHandler.get_day_button(pickup_date))
        pick_up_day.click()

    @allure.step
    def select_dropoff_date(self, dropoff_date):
        """
        Method inputs date of drop off
        """
        drop_off_form = self.find_visible_element(*CarsTabMainPageLocators.DROP_OFF_FORM)
        drop_off_form.click()
        drop_off_month = self.find_visible_element(*DatePickerHandler.get_month_button(dropoff_date))
        drop_off_month.click()
        drop_off_day = self.find_visible_element(*DatePickerHandler.get_day_button(dropoff_date))
        drop_off_day.click()

    @allure.step
    def select_pickup_time(self, pickup_time):
        """
        Method inputs time of pick_up
        """
        pickup_time = self.find_visible_element(*DatePickerHandler.get_time_button(pickup_time))
        pickup_time.click()

    @allure.step
    def select_dropoff_time(self, dropoff_time):
        """
        Method inputs time of drop_off
        """
        dropoff_form = self.find_visible_element(*CarsTabMainPageLocators.DROP_OFF_TIME_FORM)
        dropoff_form.click()
        dropoff_time = self.find_visible_element(*DatePickerHandler.get_time_button(dropoff_time))
        dropoff_time.click()

    @allure.step("Go searching cars")
    def go_search(self):
        """
        Method clicks on Search button
        """
        search_button = self.find_visible_element(*CarsTabMainPageLocators.SEARCH_CARS_BUTTON)
        search_button.click()
