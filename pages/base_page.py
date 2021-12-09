import allure


class BasePage:
    """
    Class for base page of website with URL. URL is defined in class Links module Links.
    """
    def __init__(self, browser, url, timeout=2):
        """
        browser: driver instance. url: correct URL for tests
        timeout: Time (seconds) for implicitly waiting of any
        find_element methods. Default value - 2 seconds.
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    @allure.step("Opening the page with")
    def open(self):
        """
        Method opens the transferred link in initialization method.
        """
        self.browser.get(self.url)
