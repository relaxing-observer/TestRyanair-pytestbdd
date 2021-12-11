from selenium.webdriver.common.by import By

class UserMainPageLocators:
    ACCEPT_COOKIES_BUTTON = (By.XPATH,
        "//div[@id='cookie-popup-with-overlay']//button[@class='cookie-popup-with-overlay__button']")
    EMAIL_FORM = (By.XPATH, "//input[@placeholder='email@email.com']")
    PASSWORD_FORM = (By.XPATH, "//input[@placeholder='Password']")
    CONFIRMATION_LOG_IN_BUTTON = (By.XPATH, "//form[@data-ref='login_modal']//button[@type='submit']")

    INPUT_DEPARTURE_FORM = (By.XPATH, "//*[@id='input-button__departure']")
    INPUT_DESTINATION_FORM = (By.XPATH, "//input[@id='input-button__destination']")
    DESTINATION_HOTEL_FORM = (By.XPATH, "//*[@id='input-button__locations-or-properties']")
    CAR_LOCATION = (By.XPATH, "//*[@id='input-button__pick-up-location']")

    FRAME_DATEPICKER = (By.XPATH, "//iframe[@id='_hjRemoteVarsFrame']")

    SEARCH_FLIGHT_BUTTON = (By.XPATH, "//button[@data-ref='flight-search-widget__cta']")
    SEARCH_HOTEL_BUTTON = (By.XPATH, "//button[@data-ref='rooms-search-widget__cta']")
    SEARCH_CARS_BUTTON = (By.XPATH, "//button[@data-ref='car-hire-widget__cta']")

    HOTELS_TAB = (By.XPATH, "//hp-search-widget-tab[@iconid='glyphs/hotels']")
    CARS_TAB = (By.XPATH, "//hp-search-widget-tab[@iconid='glyphs/cars']")

    @staticmethod
    def get_search_tab(name):
        SEARCH_TAB = (By.XPATH, f"//hp-search-widget-tab[@iconid='glyphs/{name}']")
        return SEARCH_TAB

    CHECK_IN_FORM = (By.XPATH, "//hp-input-button[@uniqueid='check-in']")
    CHECK_OUT_FORM = (By.XPATH, "//hp-input-button[@uniqueid='check-out']")
    PICK_UP_FORM = (By.XPATH, "//hp-input-button[@uniqueid='pick-up-date']")
    PICK_UP_TIME_FORM = (By.XPATH, "//hp-input-button[@uniqueid='pick-up-time']")
    DROP_OFF_FORM = (By.XPATH, "//hp-input-button[@uniqueid='drop-off-date']")
    DROP_OFF_TIME_FORM = (By.XPATH, "//hp-input-button[@uniqueid='drop-off-time']")

    CONFIRMATION_AIRPORT = (By.XPATH, "(//span[@data-ref='airport-item__name'])[last()]")
    CONFIRMATION_HOTEL = (By.XPATH, "//icon[@iconid='glyphs/destination-pin']")
    CONFIRMATION_CAR_LOCATION = (By.XPATH, "//hp-car-hire-location/div[1]")

    SIGN_IN_BUTTON = (By.XPATH, "//button[@aria-label='Log in']")

    ACTUAL_LOG_OUT_BUTTON = (By.XPATH, "//a[@data-ref='header-dropdown-user__logout']")
    USER_MENU = (By.XPATH, "//button[@data-ref='header-menu-item__toggle-button']/hp-header-menu-user")

class SearchCarsPageLocators:
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    CAR_CARD = (By.XPATH, "//div[@data-coordinates]//div[@class='address_container']")
    SEARCH_SUMMARY = (By.XPATH, "//table[@class='ab-SearchSummary']")
    MAIN_LOGO = (By.XPATH, "//img[@class='rch-logo-image ']")

class SearchFlightsPageLocators:
    URL_IDENTIFIER = ("trip/flights/select")
    FLIGHT_CARD = (By.XPATH, "//flight-card")
    FLIGHT_DETAILS = (By.XPATH, "//flights-trip-details/div")
    DROPDOWN_PROFILE = (By.XPATH, "//logged-in")
    LOG_OUT_BUTTON = (By.XPATH, "//ry-log-out-button//button")
    MAIN_LOGO = (By.XPATH, "//icon[@class='ry-header__logo']")

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

class SearchHotelsPageLocators:
    URL_IDENTIFIER = "rooms.ryanair.com"
    ACCOMODATION_CARD = (By.XPATH, "//rooms-accommodation-card[@class]")
    ACCEPT_COOKIES_BUTTON = (By.XPATH,
                             "//div[@id='cookie-popup-with-overlay']//button[@class='cookie-popup-with-overlay__button']")
    DROPDOWN_PROFILE = (By.XPATH, "//icon[@class='user-controls__chevron-icon']")
    LOG_OUT = (By.XPATH, "//a[@data-ref='user-controls-logout-link']")
    ACTUAL_DESTINATION_SUMMARY = (By.XPATH, "//span[@class='search-summary__destination']")
    ACTUAL_DATES_SUMMARY = (By.XPATH, "//span[@class='search-summary__dates']")

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

    # @staticmethod
    # def __set_pick_time(time):
    #     return time

    @staticmethod
    def get_time_button(time):
        TIME_BUTTON = (By.XPATH, f"//hp-time-selector-item[@data-ref='time-selector-item__button']"
                                      f"/div[contains(text(),'{time}')]")
        return TIME_BUTTON




