import allure


class BasePage(object):
    """
    Class for base page of website with URL. URL is defined in class Links module Links.
    """
    def __init__(self, browser, url):
        """
        browser: driver instance. url: correct URL for tests
        timeout: Time (seconds) for implicitly waiting of any
        find_element methods. Default value - 2 seconds.
        """
        self.browser = browser
        self.url = url

    @allure.step("Opening the page")
    def open(self):
        """
        Method opens the transferred link in initialization method.
        """
        self.browser.get(self.url)
