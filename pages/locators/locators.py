from selenium.webdriver.common.by import By

class BasePageLocators:
    pass


class GuestMainPageLocators:
    ACCEPT_COOKIES_BUTTON = (By.XPATH,
                             "//div[@id='cookie-popup-with-overlay']//button[@class='cookie-popup-with-overlay__button']")
    EMAIL_FORM = (By.XPATH, "//input[@placeholder='email@email.com']")
    PASSWORD_FORM = (By.XPATH, "//input[@placeholder='Password']")
    CONFIRMATION_LOG_IN_BUTTON = (By.XPATH, "//form[@data-ref='login_modal']//button[@type='submit']")


class MainHeaderLocators:
    SIGN_IN_BUTTON = (By.XPATH, "//button[@aria-label='Log in']")


class UserMainPageLocators:
    INPUT_DEPARTURE_FORM = (By.XPATH, "//*[@id='input-button__departure']")
    INPUT_DESTINATION_FORM = (By.XPATH, "//input[@id='input-button__destination']")
    CONFIRMATION_AIRPORT = (By.XPATH, "(//span[@data-ref='airport-item__name'])[last()]")
    FRAME_DATEPICKER = (By.XPATH, "//iframe[@id='_hjRemoteVarsFrame']")
    SEARCH_BUTTON = (By.XPATH, "//button[@data-ref='flight-search-widget__cta']")





class DatePickerLocators():
    @staticmethod
    def __set_month(date):
        month = date.split()[1]
        return month

    @staticmethod
    def __set_day(date):
        day = date.split()[0]
        return day

    @staticmethod
    def get_month_button(date):
        month = DatePickerLocators.__set_month(date)
        MONTH_BUTTON = (By.XPATH, f"//div[contains(text(), '{month}')]")
        return MONTH_BUTTON

    @staticmethod
    def get_day_button(date):
        day = DatePickerLocators.__set_day(date)
        DEPART_DAY_BUTTON = (By.XPATH,
        f"//calendar[@class='datepicker__calendar datepicker__calendar--left']//"
        f"div[@data-value='{day}' and @data-type='day']")
        return DEPART_DAY_BUTTON




