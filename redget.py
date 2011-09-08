#!/usr/bin/python2.7
import httplib
import urllib, urllib2
import sys, os
import json
from datetime import datetime
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


def write_comment(comment, f=None, level=0):

    in_step = 15
    intendation = in_step * level

    kind = comment['kind']

    if kind != 't1':
        if kind == 'more':
            print('There are more comments')
            # TODO: load more comments if element is 'more'
            # see: https://github.com/reddit/reddit/wiki/API - fetching
            # more
        return

    data = comment['data']
    body = data['body']
    body_html = data['body_html']
    author = str(data['author'])
    created = int(data['created'])
    written = datetime.fromtimestamp(created)

    try:
        points = int(data['ups'])
    except KeyError:
        points = int( 0 - int(data['downs']))

    # New paragraph
    f.write(r'<p style="margin-left:' + str(intendation) + 'px;">')

    # Header:
    f.write(r'<b>') # author
    f.write(author)
    f.write(r'</b>')
    f.write(r' | ')
    f.write(str(points)) # points
    if abs(int(points)) == 1:
        f.write(r' point')
    else:
        f.write(r' points')
    f.write(r' | ') # date
    f.write(written.__str__())

    # Body:
    f.write(r'<pre style="margin-left:' + str(intendation + 2) + 'px;">') # FIX magic number
    f.write(body)
    f.write('</pre>' + '\n')
    f.write(r'</p>' + '\n')

    # Self explanatory:
    replies = data['replies']
    if replies == '':
        return

    # Otherwise, run this function recursively with inreasing
    # intendation lever
    for i in data['replies']['data']['children']:
        write_comment(i, f, level + 1)

    return

def main():

    try:
        url = str(sys.argv[1])
    except IndexError:
        url = 'http://www.reddit.com/r/TwoXChromosomes/comments/k812x/ladies_i_am_about_to_see_my_ex_for_the_first_time/'

    response = red_get(url)

    try:
        os.remove('test.html')
    except OSError:
        pass # that PROBABLY means file doesn't exist

    f = open('test.html', 'w')
    temp = open('intend.html', 'r')
    lines = temp.readlines()
    temp.close()

    for i in lines[0:5]: # TODO - cause this is shit
        f.write(i)

    for comment in response[1]['data']['children']:
        write_comment(comment, f)

    for i in lines[8:]: # TODO
        f.write(i)

    exit()

def test():
    url = 'http://www.reddit.com/r/TwoXChromosomes/comments/k812x/ladies_i_am_about_to_see_my_ex_for_the_first_time/'
    response = red_get(url)
    return response


if __name__== '__main__':
    main()
