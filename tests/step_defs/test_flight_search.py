"""
This module contains step definitions for cucumbers.feature.
It uses Selenium WebDriver for browser interactions
"""

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from utils.links import Links
scenarios('../features/flight_search.feature')

