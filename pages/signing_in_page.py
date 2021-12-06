import allure
from base_page import BasePage
from utils.browser_helper import BrowserHelper
from locators.locators import SigningInPageLocators

class GuestMainPage(BrowserHelper, BasePage):
    @allure.step("Choose english language")
    def choose_english_language(self):
        """
        Method chooses english language.
        """
        english_button = self.find_visible_element(*SigningInPageLocators.EMAIL_FORM)
        english_button.click()