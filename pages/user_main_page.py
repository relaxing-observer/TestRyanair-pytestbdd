import allure

from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from .locators.locators import UserMainPageLocators
import time

class UserMainPage(BasePage):

    @allure.step("Accept cookies")
    def accept_cookies(self):
        """
        Method accepts cookies.
        """

        # accept_button = self.find_clickable_element(*UserMainPageLocators.ACCEPT_COOKIES_BUTTON, timeout=0)
        try:
            accept_button = BrowserHelper.find_clickable_element(self.browser, *UserMainPageLocators.ACCEPT_COOKIES_BUTTON, timeout=0)
            accept_button.click()
        except:
            pass

    @allure.step("Go to required tab")
    def go_to_tab(self, tab_name):
        """
        Method clicks on cars tab
        """
        search_tab = BrowserHelper.find_visible_element(self.browser, *UserMainPageLocators.get_search_tab(tab_name))
        search_tab.click()

    @allure.step("Log out")
    def log_out(self):
        """
        Method logs out form service
        """
        dropdown_profile = BrowserHelper.find_visible_element(self.browser, *UserMainPageLocators.USER_MENU)
        dropdown_profile.click()
        log_out_button = BrowserHelper.find_visible_element(self.browser, *UserMainPageLocators.ACTUAL_LOG_OUT_BUTTON)
        log_out_button.click()

    @allure.step("Signing in")
    def sign_in_user(self, username, password):
        """
        Method goes to signing in from main header of page.
        """

        signing_in_button = BrowserHelper.find_visible_element(self.browser, *UserMainPageLocators.SIGN_IN_BUTTON)
        signing_in_button.click()
        BrowserHelper.send_keys(self.browser, *UserMainPageLocators.EMAIL_FORM, username)
        BrowserHelper.send_keys(self.browser, *UserMainPageLocators.PASSWORD_FORM, password)
        confirm_button = BrowserHelper.find_visible_element(self.browser, *UserMainPageLocators.CONFIRMATION_LOG_IN_BUTTON)
        confirm_button.click()