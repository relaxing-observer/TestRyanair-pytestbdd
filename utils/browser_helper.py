import allure
import time
from datetime import datetime
from allure_commons.types import AttachmentType
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from loguru import logger
from utils.project_logger import LogConfig


class BrowserHelper(BasePage):
    LogConfig.set_logger_config()

    @allure.step("Verification of the presence of the element '{1}' and '{2}'")
    def is_element_present(self, how, what):
        """
        The method that catches the exceptions. How: how to search (css, id, xpath, etc.)
        Selector string. True - if element is on the page, False - if not.
        """
        logger.info(f"Verification of the presence of the element '{how}' and '{what}'")
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            allure.attach(self.browser.get_screenshot_as_png(), name=f'Failure {datetime.now()}',
                          attachment_type=AttachmentType.PNG)
            logger.error(f"Can't find element {how}, '{what}' ")
            return False
        return True

    @allure.step("Verification that element '{1}' '{2}' is disappeared from page during '{timeout}' seconds")
    def is_disappeared(self, how, what, timeout=3):
        """
        Method that allows you to determine that element is not on the page and does not appear within
        timeout. Default timeout - 3 seconds. How to search (css, id, xpath, etc.). What: selector string.
        True - if element will disappear. False - if element is present.
        """
        logger.info(f"Verification that element {how} {what} is disappeared from page during {timeout} seconds")
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            logger.error(f"Element {how} {what} isn't disappeared")
            return False
        return True

    @allure.step("Verification that element '{1}' '{2}' is not appear  on the page during '{timeout}' seconds")
    def is_not_element_present(self, how, what, timeout=3):
        """
        Method determines the absence of an element on the page over a period of time. Default timeout - 3 seconds.
        how  - how to search (css, id, xpath, etc.). what: selector string.
        timeout: Time to determine absence of element.
        True - if element doesn't exist. False - if element is present.
        """
        logger.info(f"Verification that element {how} {what} is not appear  on the page during {timeout} seconds")
        try:
            WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            logger.error(f"Element {how} {what} is appeared or was on the page")
            return True
        return False

    @allure.step("Find visible element by '{1}', '{2}' for max - '{timeout}' seconds")
    def find_visible_element(self, how, what, timeout=4):
        """
        The method wait for the element, when it becomes visible. How: how to search (css, id, xpath, etc.)
        What: Selector string.
        """
        logger.info(f"Find visible element by {how}, {what} become visible for {timeout} seconds")
        required_element = WebDriverWait(self.browser, timeout).until(
            expected_conditions.visibility_of_element_located((how, what)))
        self.highlight(required_element)
        return required_element

    @allure.step("Waiting that URL will contain '{1}' for '{timeout}' seconds")
    def wait_phrase_in_url(self, phrase, timeout=3):
        """
        The method wait for the element, when it becomes visible. How: how to search (css, id, xpath, etc.)
        What: Selector string.
        """
        logger.info(f"Waiting that URL will contain {phrase} for {timeout} seconds")
        return WebDriverWait(self.browser, timeout).until(expected_conditions.url_contains(phrase))

    @allure.step("Waiting for element by '{1}', '{2}' become clickable for '{timeout}' seconds")
    def find_clickable_element(self, how, what, timeout=3):
        """
        The method wait for the element, when it becomes clickable. How: how to search (css, id, xpath, etc.)
        What: Selector string.
        """
        logger.info(f"Waiting for element {how}, '{what}' become clickable for {timeout} seconds")
        required_element = WebDriverWait(self.browser, timeout).until(
            expected_conditions.element_to_be_clickable((how, what)))
        self.highlight(required_element)
        return required_element


    def highlight(self, element):
        """
        Highlights (blinks) a Selenium Webdriver element
        """

        def apply_style(style):
            self.browser.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                        element, style)

        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        time.sleep(.1)
        apply_style(original_style)

    @allure.step("Send values to the form of element '{1}' '{2}' after clearing")
    def send_keys(self, how, what, value, timeout=2, clear_first=True, click_first=True):
        required_element = WebDriverWait(self.browser, timeout).until(
            expected_conditions.element_to_be_clickable((how, what)))
        self.highlight(required_element)
        if click_first:
            logger.info(f"Clicking at element {how} {what}")
            required_element.click()
        if clear_first:
            logger.info(f"Clearing form of {how} {what}")
            required_element.clear()
        logger.info(f"Send values to {how} {what}")
        required_element.send_keys(value)
