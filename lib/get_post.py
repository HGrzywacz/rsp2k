#!/usr/bin/env python3.2
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
- LOADING MORE COMMENTS!
- name of the file,
- returning values for get_post (needed to build a mobi),
- progressbar(?),
- pep8 compatibility,
- licence info,

Copyright:
Hubert Grzywacz (hgrzywacz@gmail.com)
Derek Langley (derek@dereklangley.com)
"""

import sys
import os
import json
import urllib.request
import codecs
from datetime import datetime
import xml.sax.saxutils

from . import red_get
#import red_get


def write_post(post, f):
    kind = post['kind']
    data = post['data']

    if kind != 't3':
        print('Oh gosh!')

    score = data['score']
    title = data['title']
    author = data['author']
    text = xml.sax.saxutils.unescape(data['selftext'])
    text_html = data['selftext_html']
    created = data['created']
    written = datetime.fromtimestamp(created)

    f.write('\n' + r'<div style="font-size:larger; font-weight: bold;">' + title
            + '</div>' + '\n')

    f.write(str(score)) # score

    if abs(int(score)) == 1:
        f.write(r' point')
    else:
        f.write(r' points')

    f.write(' | ' + author + ' | ') # author
    f.write(written.__str__() + '\n') # datetime
    f.write('<br>')

    if data['is_self'] == False:
        f.write('<br><b>Comments:</b>')
        return

    f.write('<pre style="font-size:medium;">' + '\n') # text
    f.write(text)
    f.write('\n </pre> \n')
    f.write('<b>Comments:</b><br>')


def write_comment(comment, f=None, level=0):

    in_step = 15
    intendation = in_step * level

    kind = comment['kind']

    if kind != 't1':
        if kind == 'more':
            print('.', end='')
            # TODO: load more comments if element is 'more'
            # see: https://github.com/reddit/reddit/wiki/API - fetching
            # more
        return

    data = comment['data']
    body = xml.sax.saxutils.unescape(data['body'])
    body_html = xml.sax.saxutils.unescape(data['body_html'])
    author = str(data['author'])
    created = int(data['created'])
    written = datetime.fromtimestamp(created)

    points = int(int(data['ups']) - int(data['downs']))

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
    f.write(r'<pre style="font-size:medium; margin-left:' + str(intendation + 2)
            + 'px;">') # FIXME magic number
    f.write(body_html)
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


def write_head(f, title='What no title?!'):
    """Writes head to the file f, taking title of post as second argument"""

    f.write(r'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"' +
            r'"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">' + '\n')
    f.write(r'<html xmlns="http://www.w3.org/1999/xhtml">' + '\n')
    f.write(r'<head>' + '\n' + r'<title>')
    f.write(title) # TODO: TITLE
    f.write('</title>' + '\n')
#    f.write(r'<link rel="stylesheet" href="styles.css" type="text/css">')
    f.write(r'</head>' + '\n' + '<body>' + '\n')


def write_tail(f):
    """Just a tail."""
    f.write('\n' + r'</body>' + '\n')
    f.write(r'</html>')


def get_post(url, directory='.'):
    response = red_get.red_get(url)
    if response == "InvalidURL":
        return False

    post = response[0]['data']['children'][0]
    comments = response[1]['data']['children']

    title = post['data']['title']
    filename = post['data']['name'] + '.html'

    try:
        os.remove(filename)
    except OSError:
        pass # that PROBABLY means file doesn't exist

    filename = os.path.join(directory,filename)

    if __name__ == '__main__':
        print('\n' + 'Filename: ' + filename)

    f = codecs.open(filename, 'w', 'utf-8')

    write_head(f, title)

    write_post(post, f)

    for comment in comments:
        write_comment(comment, f)
    print()

    write_tail(f)
    f.close()

    # needed for mobi creation
    r = (filename, title)
    return r


def main():

    print('WARNING: Running this script as __main__ should be done only for '
            'testing purposes.')

    try:
        url = str(sys.argv[1])
    except IndexError:
        print('INFO: No URL passed to script, checking for links.txt')
        try:
            # If no URL is passed in via command line, check links.txt for list of links to use
            with codecs.open('links.txt', 'r', 'utf-8') as links:
                line_number = 0
                for link_line in links:
                    line_number += 1
                    get_post(link_line.rstrip())
        except IOError as e:
            print('INFO: links.txt was not found, using hardcoded URL.')
            url = 'http://www.reddit.com/r/reddit.com/comments/k8sny/a_survey_my_company_is_making_us_takei_think/'
            get_post(url)

    print('\n' + 'Finished.')

    sys.exit()


if __name__== '__main__':
    main()
