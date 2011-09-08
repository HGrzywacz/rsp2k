import httplib
import urllib, urllib2
import sys, os
import json
import time, datetime
import re

from urlparse import urlparse, urlunparse, parse_qs

import config


def red_get(url):

    scheme, host, path, params, query, fragment = urlparse(url)

    if query:
        parsed_params = parse_qs(query)
    else:
        parsed_params = query

    #parsed_params['limit'] = [config.limit]

    fragment = None

    assert path.endswith('.json') or path.endswith('/')
    if path.endswith('/'):
        path = path + '.json'

    new_urltuple = (scheme, host, path, params,
                    urllib.urlencode(parsed_params, doseq = True), fragment)
    composed_sourceurl = urlunparse(new_urltuple)

    response = urllib.urlopen(composed_sourceurl)

    s = response.read()

    decoder = json.JSONDecoder()
    response = decoder.decode(s)

    return response # decoded json


def write_comment(comment, f=None, intendation=0):

    in_step = 5

    if comment['kind'] != 't1':
        print('Not a comment.')
        sys.exit()

    data = comment['data']
    f.write(r'<p style="margin-left:' + str(intendation * in_step) + 'px;">')
    f.write(str(data['ups']) + ' ' + str(data['author']))
    f.write(r'</p>' + '\n')

    replies = data['replies']
    if replies == '':
        return

    for i in data['replies']['data']['children']:
        write_comment(i, f, intendation + 1)



def main():
    url = 'http://www.reddit.com/r/TwoXChromosomes/comments/k812x/ladies_i_am_about_to_see_my_ex_for_the_first_time/'
    response = red_get(url)


def test():
    url = 'http://www.reddit.com/r/TwoXChromosomes/comments/k812x/ladies_i_am_about_to_see_my_ex_for_the_first_time/'
    response = red_get(url)
    return response


if __name__== '__main__':
    response = test()

    try:
        os.remove('test.html')
    except OSError:
        pass

    f = open('test.html', 'w')
    temp = open('intend.html', 'r')
    lines = temp.readlines()
    temp.close()

    for i in lines[0:4]:
        f.write(i)

    for comment in response[1]['data']['children']:
        write_comment(comment, f)

    for i in lines[7:]:
        f.write(i)

    exit()
