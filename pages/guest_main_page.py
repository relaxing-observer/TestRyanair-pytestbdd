import allure
from pages.base_page import BasePage
from utils.browser_helper import BrowserHelper
from .locators.locators import GuestMainPageLocators
from .locators.locators import UserMainPageLocators
from utils.credentials import Credentials


class GuestMainPage(BrowserHelper, BasePage):
    @allure.step("Accept cookies")
    def accept_cookies(self):
        """
        Method accepts cookies.
        """
        try:
            accept_button = self.find_clickable_element(*GuestMainPageLocators.ACCEPT_COOKIES_BUTTON, timeout=0)
            accept_button.click()
        except:
            pass

    @allure.step("Go to sighing in")
    def go_to_sign_in(self):
        """
        Method goes to signing in from main header of page.
        """
        signing_in_button = self.find_visible_element(*UserMainPageLocators.SIGN_IN_BUTTON)
        signing_in_button.click()

    @allure.step("Signing in")
    def sign_in_user(self):
        """
        Method goes to signing in from main header of page.
        """
        self.send_keys(*GuestMainPageLocators.EMAIL_FORM, Credentials.USERNAME)
        self.send_keys(*GuestMainPageLocators.PASSWORD_FORM, Credentials.PASSWORD)
        confirm_button = self.find_visible_element(*GuestMainPageLocators.CONFIRMATION_LOG_IN_BUTTON)
        confirm_button.click()
