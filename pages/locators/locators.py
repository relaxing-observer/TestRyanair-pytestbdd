
from selenium.webdriver.common.by import By


class BasePageLocators:
    # LOGIN_LINK = (By.XPATH, "//a[contains(@href, '/login')]")
    pass

class GuestMainPageLocators:
    ENG_LANGUAGE_BUTTON = (By.XPATH, "//div[contains(text(), 'UK (English)')]")
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[@id='nas-button-7']")

class MainHeaderLocators:
    SIGN_IN_BUTTON = (By.XPATH, "//*[@id='profileHeaderBar']/a[@class]")

class SigningInPageLocators:
    EMAIL_FORM = (By.XPATH, "//input[@id='nas-element-login-box-0-username']")
    PASSWORD_FORM = (By.XPATH, "//input[@id='nas-element-login-box-0-password']")
    SIGN_IN_CONFIRM_BUTTON = (By.XPATH, "//button[@id='nas-element-login-box-0-login-button']")
