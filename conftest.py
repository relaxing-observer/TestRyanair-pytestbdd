import logging
import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store', 
                     default='en',
                     help="Choose language: ru, en, fr, it, es ... (etc.)"
                    )
    parser.addoption('--user',
                     action='store',
                     default='None',
                     help="Set a username"
                    )
    parser.addoption('--password',
                     action='store',
                     default='None',
                     help="Set a password"
                    )



@pytest.fixture(scope="session")
def browser(request):
    '''
    Method automatically initializes driver for browser by ChromeDriverManager.
    '''
    user_language = request.config.getoption("language")
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option(
        'prefs',{'intl.accept_languages': user_language})
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(ChromeDriverManager(log_level=logging.ERROR).install(), options=options)
    yield browser
    browser.quit()

@pytest.fixture()
def user(request):
    user = request.config.getoption("user")
    return user

@pytest.fixture()
def password(request):
    password = request.config.getoption("password")
    return password


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')

