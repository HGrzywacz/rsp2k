""" Just a function """

import sys
import urllib.parse
import urllib.request
import json


def red_get(url):
    """ Function that takes reddits url and returns parsed
    json response from API."""

    scheme, host, path, params, query, fragment = urllib.parse.urlparse(url)

    if query:
        parsed_params = urllib.parse.parse_qs(query)
    else:
        parsed_params = query

    fragment = None

    try:
        assert path.endswith('.json') or path.endswith('/')
        if path.endswith('/'):
            path = path + '.json'
    except AssertionError:
        print('\n' + 'Invalid URL.')
        return "InvalidURL"

    new_urltuple = (scheme, host, path, params,
                    urllib.parse.urlencode(parsed_params, doseq=True),
                    fragment)

    composed_sourceurl = urllib.parse.urlunparse(new_urltuple)

    response = urllib.request.urlopen(composed_sourceurl)

    s = response.read().decode('utf-8')

    decoder = json.JSONDecoder()
    response = decoder.decode(s)

    return response  # decoded json

if __name__ == '__main__':
    print('Nothing to see here.')
    sys.exit()
