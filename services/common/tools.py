import urllib
import urlparse
import json
import re
import requests

# Thalemine root API
BASE_URL = 'https://api.araport.org/mine/0.5.0/service/'

def filter_name(name):
    return re.sub('[^\w\s\.\-_]', '_', name)

def do_request_post(endpoint, token, data, **kwargs):
    """Perform a request to SITE and return JSON."""

    url = urlparse.urljoin(BASE_URL, endpoint)
    headers = {"Authorization": "Bearer %s" % token, "Content-Type": "text/plain"}
    response = requests.post(url, headers=headers, data=data, params=kwargs)

    # Raise exception and abort if requests is not successful
    response.raise_for_status()

    try:
        # Try to convert result to JSON
        # abort if not possible
        return response.json()
    except ValueError:
        raise Exception('not a JSON object: {}'.format(response.text))

def do_request(endpoint, token, **kwargs):
    """Perform a request to SITE and return response."""

    url = urlparse.urljoin(BASE_URL, endpoint)
    headers = {"Authorization": "Bearer %s" % token}
    response = requests.get(url, headers=headers, params=kwargs)

    # Raise exception and abort if requests is not successful
    response.raise_for_status()

    try:
        # Try to convert result to JSON
        # abort if not possible
        return response.json()
    except ValueError:
        raise Exception('not a JSON object: {}'.format(response.text))
