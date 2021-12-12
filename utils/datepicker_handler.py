from selenium.webdriver.common.by import By

class DatePickerHandler:

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
        month = DatePickerHandler.__set_month(date)
        MONTH_BUTTON = (By.XPATH, f"//div[@class='m-toggle__scrollable']//div[contains(text(), '{month}')]")
        return MONTH_BUTTON

    @staticmethod
    def get_day_button(date):
        day = DatePickerHandler.__set_day(date)
        DEPART_DAY_BUTTON = (By.XPATH,
                             f"//calendar[@class='datepicker__calendar datepicker__calendar--left']//"
                             f"div[@data-value='{day}' and @data-type='day']")
        return DEPART_DAY_BUTTON

    @staticmethod
    def get_time_button(time):
        TIME_BUTTON = (By.XPATH, f"//hp-time-selector-item[@data-ref='time-selector-item__button']"
                                 f"/div[contains(text(),'{time}')]")
        return TIME_BUTTON