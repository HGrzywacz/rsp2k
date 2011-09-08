#!/usr/bin/env python
"""
python3, fancy, eh?

Function get_post
1. Fetch post with via url red_get()
2. Write to file:
    a. head with title with write_title()
    b. text of post with write_post()
    c. comments with write_comments():
        -recursively!
    d. write tail
3. close file

TODO:
name of the file,
returning values for get_post (needed to build a mobi),
progressbar(?),
pep8 compatibility,
licence info,

Copyright Hubert Grzywacz (hgrzywacz@gmail.com)
"""

import urllib
import sys
import os
import json
from datetime import datetime
import urlparse


def red_get(url):

    scheme, host, path, params, query, fragment = urlparse.urlparse(url)

    if query:
        parsed_params = urlparse.parse_qs(query)
    else:
        parsed_params = query

    fragment = None

    assert path.endswith('.json') or path.endswith('/')
    if path.endswith('/'):
        path = path + '.json'

    new_urltuple = (scheme, host, path, params,
                    urllib.urlencode(parsed_params, doseq = True), fragment)
    composed_sourceurl = urlparse.urlunparse(new_urltuple)

    response = urllib.urlopen(composed_sourceurl)

    s = response.read()

    decoder = json.JSONDecoder()
    response = decoder.decode(s)

    return response # decoded json


def write_post(post, f):
    kind = post['kind']
    data = post['data']

    if kind != 't3':
        print('Oh gosh!')

    if data['is_self'] == False:
        pass
        return

    score = data['score']
    title = data['title']
    author = data['author']
    text = data['selftext']
    text_html = data['selftext_html']
    created = data['created']
    written = datetime.fromtimestamp(created)

    f.write('\n' + r'<div style="font-size:larger; font-weight: bold;">' + title + '</div>' + '\n')

    f.write(str(score)) # score

    if abs(int(score)) == 1:
        f.write(r' point')
    else:
        f.write(r' points')

    f.write(' | ' + author + ' | ') # author
    f.write(written.__str__() + '\n') # datetime
    f.write('<br>')
    f.write('<pre style="font-size:medium;">' + '\n')
    f.write(text) # text
    f.write('\n </pre> \n')
    f.write('<b>Comments:</b><br>')


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
    f.write(r'<pre style="font-size:medium; margin-left:' + str(intendation + 2) + 'px;">') # FIXME magic number
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


def write_head(f, title):
    f.write(r'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">')
    f.write(r'<html xmlns="http://www.w3.org/1999/xhtml">')
    f.write(r'<head>' + '\n' + r'<title>')
    f.write(title) # TODO: TITLE
    f.write('</title>')
#    f.write(r'<link rel="stylesheet" href="styles.css" type="text/css">')
    f.write(r'</head>' + '\n' + '<body>' + '\n')


def write_tail(f):
    f.write('\n' + r'</body>' + '\n')
    f.write(r'</html>' + '\n')


def get_post(url):
    response = red_get(url)

    try:
        os.remove('test.html')
    except OSError:
        pass # that PROBABLY means file doesn't exist

    f = open('test.html', 'w')
    temp = open('intend.html', 'r')
    lines = temp.readlines()
    temp.close()

    post = response[0]['data']['children'][0]
    comments = response[1]['data']['children']

    title = post['data']['title']

    write_head(f, title)

    write_post(post, f)

    for comment in comments:
        write_comment(comment, f)

    write_tail(f)
    f.close()

    return title

def main():
    try:
        url = str(sys.argv[1])
    except IndexError:
        url = 'http://www.reddit.com/r/TwoXChromosomes/comments/k812x/ladies_i_am_about_to_see_my_ex_for_the_first_time/'
    get_post(url)
    sys.exit()


if __name__== '__main__':
    main()
