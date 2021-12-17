from selenium.webdriver.common.by import By


class CarsTabMainPageLocators:
    CAR_LOCATION = (By.XPATH, "//*[@id='input-button__pick-up-location']")
    PICK_UP_FORM = (By.XPATH, "//hp-input-button[@uniqueid='pick-up-date']")
    PICK_UP_TIME_FORM = (By.XPATH, "//hp-input-button[@uniqueid='pick-up-time']")
    DROP_OFF_FORM = (By.XPATH, "//hp-input-button[@uniqueid='drop-off-date']")
    DROP_OFF_TIME_FORM = (By.XPATH, "//hp-input-button[@uniqueid='drop-off-time']")
    CONFIRMATION_CAR_LOCATION = (By.XPATH, "//hp-car-hire-location/div[1]")
    SEARCH_CARS_BUTTON = (By.XPATH, "//button[@data-ref='car-hire-widget__cta']")


class FlightsTabMainPageLocators:
    INPUT_DEPARTURE_FORM = (By.XPATH, "//*[@id='input-button__departure']")
    INPUT_DESTINATION_FORM = (By.XPATH, "//input[@id='input-button__destination']")
    SEARCH_FLIGHT_BUTTON = (By.XPATH, "//button[@data-ref='flight-search-widget__cta']")
    CONFIRMATION_AIRPORT = (By.XPATH, "(//span[@data-ref='airport-item__name'])[last()]")
    RETURN_FORM = (By.XPATH, "//fsw-input-button[@uniqueid='dates-to']")


class HotelsTabMainPageLocators:
    SEARCH_HOTEL_BUTTON = (By.XPATH, "//button[@data-ref='rooms-search-widget__cta']")
    DESTINATION_HOTEL_FORM = (By.XPATH, "//*[@id='input-button__locations-or-properties']")
    CHECK_IN_FORM = (By.XPATH, "//hp-input-button[@uniqueid='check-in']")
    CHECK_OUT_FORM = (By.XPATH, "//hp-input-button[@uniqueid='check-out']")
    CONFIRMATION_HOTEL = (By.XPATH, "//icon[@iconid='glyphs/destination-pin']")


class UserMainPageLocators:
    ACCEPT_COOKIES_BUTTON = (By.XPATH,
                             "//div[@id='cookie-popup-with-overlay']//button["
                             "@class='cookie-popup-with-overlay__button']")
    EMAIL_FORM = (By.XPATH, "//input[@placeholder='email@email.com']")
    PASSWORD_FORM = (By.XPATH, "//input[@placeholder='Password']")
    CONFIRMATION_LOG_IN_BUTTON = (By.XPATH, "//form[@data-ref='login_modal']//button[@type='submit']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@aria-label='Log in']")
    ACTUAL_LOG_OUT_BUTTON = (By.XPATH, "//a[@data-ref='header-dropdown-user__logout']")
    USER_MENU = (By.XPATH, "//button[@data-ref='header-menu-item__toggle-button']/hp-header-menu-user")
    FRAME_DATEPICKER = (By.XPATH, "//iframe[@id='_hjRemoteVarsFrame']")

    @staticmethod
    def get_search_tab(name):
        SEARCH_TAB = (By.XPATH, f"//hp-search-widget-tab[@iconid='glyphs/{name}']")
        return SEARCH_TAB


class SearchCarsPageLocators:
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    CAR_CARD = (By.XPATH, "//div[@data-coordinates]//div[@class='address_container']")
    SEARCH_SUMMARY = (By.XPATH, "//table[@class='ab-SearchSummary']")
    MAIN_LOGO = (By.XPATH, "//img[@class='rch-logo-image ']")


class SearchFlightsPageLocators:
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
    ACCOMMODATION_CARD = (By.XPATH, "//rooms-accommodation-card[@class]")
    ACCEPT_COOKIES_BUTTON = (By.XPATH,
                             "//div[@id='cookie-popup-with-overlay']//button["
                             "@class='cookie-popup-with-overlay__button']")
    DROPDOWN_PROFILE = (By.XPATH, "//icon[@class='user-controls__chevron-icon']")
    LOG_OUT = (By.XPATH, "//a[@data-ref='user-controls-logout-link']")
    ACTUAL_DESTINATION_SUMMARY = (By.XPATH, "//span[@class='search-summary__destination']")
    ACTUAL_DATES_SUMMARY = (By.XPATH, "//span[@class='search-summary__dates']")
