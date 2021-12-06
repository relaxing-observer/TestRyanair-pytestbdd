"""
This module contains step definitions for service.feature.
It uses the requests package:
http://docs.python-requests.org/
"""

import requests

from functools import partial

from pytest_bdd import scenarios, given, then, parsers


# Shared Variables

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'

EXTRA_TYPES = {'Text': str, }

parse_phrase = partial(parsers.cfparse, extra_types=EXTRA_TYPES)


# Scenarios


scenarios('../features/service.feature')


# Given Steps

@given(parse_phrase('the DuckDuckGo API is queried with "{phrase:Text}"'), target_fixture='ddg_response')
def ddg_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response


# Then Steps

@then(parse_phrase('the response contains results for "{phrase:Text}"'))
def ddg_response_contents(ddg_response, phrase):
    # A more comprehensive test would check 'RelatedTopics' for matching phrases
    assert phrase.lower() == ddg_response.json()['Heading'].lower()


@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code