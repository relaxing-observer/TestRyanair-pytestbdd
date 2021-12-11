import allure

from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from .locators.locators import DatePickerLocators
from .locators.locators import UserMainPageLocators


class UserMainPage(BrowserHelper, BasePage):

    @allure.step("Accept cookies")
    def accept_cookies(self):
        """
        Method accepts cookies.
        """
        try:
            accept_button = self.find_clickable_element(*UserMainPageLocators.ACCEPT_COOKIES_BUTTON, timeout=0)
            accept_button.click()
        except:
            pass
    @allure.step("Go to search tab")
    def go_to_tab(self, tab_name):
        """
        Method clicks on cars tab
        """
        search_tab = self.find_visible_element(*UserMainPageLocators.get_search_tab(tab_name))
        search_tab.click()

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
        dropdown_profile = self.find_visible_element(*UserMainPageLocators.USER_MENU)
        dropdown_profile.click()
        log_out_button = self.find_visible_element(*UserMainPageLocators.ACTUAL_LOG_OUT_BUTTON)
        log_out_button.click()

    @allure.step("Signing in")
    def sign_in_user(self, username, password):
        """
        Method goes to signing in from main header of page.
        """
        signing_in_button = self.find_visible_element(*UserMainPageLocators.SIGN_IN_BUTTON)
        signing_in_button.click()
        self.send_keys(*UserMainPageLocators.EMAIL_FORM, username)
        self.send_keys(*UserMainPageLocators.PASSWORD_FORM, password)
        confirm_button = self.find_visible_element(*UserMainPageLocators.CONFIRMATION_LOG_IN_BUTTON)
        confirm_button.click()