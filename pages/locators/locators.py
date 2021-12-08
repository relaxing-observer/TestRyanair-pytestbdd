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
    DROPDOWN_PROFILE = (By.XPATH, "//logged-in")
    LOG_OUT_BUTTON = (By.XPATH, "//ry-log-out-button//button")


class UserMainPageLocators:
    INPUT_DEPARTURE_FORM = (By.XPATH, "//*[@id='input-button__departure']")
    INPUT_DESTINATION_FORM = (By.XPATH, "//input[@id='input-button__destination']")
    CONFIRMATION_AIRPORT = (By.XPATH, "(//span[@data-ref='airport-item__name'])[last()]")
    FRAME_DATEPICKER = (By.XPATH, "//iframe[@id='_hjRemoteVarsFrame']")
    SEARCH_BUTTON = (By.XPATH, "//button[@data-ref='flight-search-widget__cta']")

class SearchFlightsPageLocators:
    URL_IDENTIFIER = ("trip/flights/select")
    FLIGHT_CARD = (By.XPATH, "//flight-card")
    FLIGHT_DETAILS = (By.XPATH, "//flights-trip-details/div")

    @staticmethod
    def __set_depart_aiport(departure_airport):
        return departure_airport

    @staticmethod
    def __set_return_airport(destination_airport):
        return destination_airport

    @staticmethod
    def get_departure_header(departure_airport):
        depart = SearchFlightsPageLocators.__set_depart_aiport(departure_airport)
        DEPARTURE_LOCATION_HEADER = (By.XPATH,
            f"//h4[@class='ng-tns-c55-3 ng-star-inserted' and contains(text(),'{depart}')]")
        return DEPARTURE_LOCATION_HEADER

    @staticmethod
    def get_destination_header(destination_airport):
        destination = SearchFlightsPageLocators.__set_depart_aiport(destination_airport)
        DESTINATION_LOCATION_HEADER = (By.XPATH,
            f"//h4[@class='ng-tns-c55-3 ng-star-inserted' and contains(text(),'{destination}')]")
        return DESTINATION_LOCATION_HEADER


class DatePickerLocators():
    RETURN_FORM = (By.XPATH, "//fsw-input-button[@uniqueid='dates-to']")

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
        MONTH_BUTTON = (By.XPATH, f"//div[@class='m-toggle__scrollable']//div[contains(text(), '{month}')]")
        return MONTH_BUTTON

    @staticmethod
    def get_day_button(date):
        day = DatePickerLocators.__set_day(date)
        DEPART_DAY_BUTTON = (By.XPATH,
        f"//calendar[@class='datepicker__calendar datepicker__calendar--left']//"
        f"div[@data-value='{day}' and @data-type='day']")
        return DEPART_DAY_BUTTON




