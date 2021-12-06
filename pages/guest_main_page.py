import allure
from base_page import BasePage
from utils.browser_helper import BrowserHelper
from locators.locators import GuestMainPageLocators
from locators.locators import MainHeaderLocators

class GuestMainPage(BrowserHelper, BasePage):
    @allure.step("Choose english language")
    def choose_english_language(self):
        """
        Method chooses english language.
        """
        english_button = self.find_visible_element(*GuestMainPageLocators.ENG_LANGUAGE_BUTTON)
        english_button.click()

    @allure.step("Accept cookies")
    def accept_cookies(self):
        """
        Method accepts cookies.
        """
        accept_button = self.find_visible_element(*GuestMainPageLocators.ACCEPT_COOKIES_BUTTON)
        accept_button.click()


    # @allure.step("Verification of link to login page")
    # def should_be_login_link(self):
    #     """
    #     The method checks for the presence of a link to go to the login page
    #     """
    #     assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
    #         "Login link is not presented"

    @allure.step("Signing in")
    def go_to_sign_in(self):
        """
        Method goes to signing in from main header of page.
        """
        signing_in_button = self.find_visible_element(*MainHeaderLocators.SIGN_IN_BUTTON)
        signing_in_button.click()
