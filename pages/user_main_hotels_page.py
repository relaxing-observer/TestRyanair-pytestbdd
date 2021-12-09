from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
import allure
from .locators.locators import SearchHotelsPageLocators


class UserMainHotelsPage(BrowserHelper, BasePage):
    @allure.step("Log out from hotels page")
    def log_out_from_hotels_page(self):
        dropdown_profile = self.find_visible_element(*SearchHotelsPageLocators.DROPDOWN_PROFILE)
        dropdown_profile.click()
        log_out_button = self.find_visible_element(*SearchHotelsPageLocators.LOG_OUT)
        log_out_button.click()
