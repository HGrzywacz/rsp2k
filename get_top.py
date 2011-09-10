#!/usr/bin/env python3
"""
Try:
    get_top.py kindle 21 new
    get_top.py 13 controversial month askreddit
    get_top.py 50 top all relationship_advice

to get idea what this script is for.
"""

import os
import sys

from red_get import red_get

WARNING_NUMBER = 50
TESTING = False

def main():

    categories = frozenset(['hot', 'top', 'new', 'controversial'])
    times = frozenset(['hour', 'day', 'week', 'month', 'year', 'all'])

    # Default values
    number = int(20)
    category = 'top'
    time = ''
    subreddit = 'askscience'

    args = sys.argv[1:]

    for a in args:
        try:
            number = int(a)
            continue
        except ValueError:
            pass
        if a in categories:
            category = a
            continue
        if a in times:
            time = a
            continue
        else:
            subreddit = a

    if (category != 'top' or category != 'controversial') and time != '':
        print('WARNING: time value works only with top or '
                + 'controversial categories.')

    if not time:
        time = 'all'

    if number >= WARNING_NUMBER:
        print('More than 50 posts? Really? (y/n)')
        a = sys.stdin.read(1)
        if a != 'y':
            sys.exit()

    print('Time: ' + time, end='')
    print('\tNumber: ' + str(number), end='')
    print('\tCategory: ' + category, end='')
    print('\tSubreddit: ' + subreddit)

    filename = subreddit + '_' + category + '_' + str(number) + '.txt'
    if TESTING:
        print(filename)

    def make_url(after):
        """ Makes url """
        # hot
        if category == 'hot':
            if after:
                url = ("http://www.reddit.com/r/" + subreddit
                        + '/.json?count=50&after=' + after)
                return url
            else:
                url = ("http://www.reddit.com/r/" + subreddit + "/.json")
        #top
        elif category == 'top':
            if after:
                url = ('http://www.reddit.com/r/' + subreddit
                        + '/top/.json?sort=top&count=50&after='
                        + after + '&t=' + time)
            else:
                url = ('http://www.reddit.com/r/' + subreddit + '/top/'
                        + '.json?sort=top&t=' + time)
        # new
        elif category == 'new':
            if after:
                url = ('http://www.reddit.com/r/' + subreddit
                        + '/new/.json?count=50&after=' + after)
            else:
                url = ('http://www.reddit.com/r/' + subreddit + '/new/.json')

        # controversial
        elif category == 'controversial':
            if after:
                url = ('http://www.reddit.com/r/' + subreddit
                    + '/controversial/.json?sort=controversial&count=50&after='
                    + after + '&t' + time)
            else:
                url = ('http://www.reddit.com/r/' + subreddit
                        + '/controversial/.json?sort=controversial&t=' + time)

        return url

    url = make_url('')

    if TESTING:
        print(url)

    try:
        response = red_get(url)
    except urllib.error.HTTPError:
        print('ERROR: check your subreddit spelling, maybe?'
                ' Exiting.')
        sys.exit()

    links = []

    i = 0  # original name for an index
    found = False

    for res in response['data']['children']:
        i = i + 1
        if i > number:
            found = True
            break
        links.append(res['data']['url'])

    while not found:
        after = response['data']['after']
        url = make_url(after)
        response = red_get(url)

        for res in response['data']['children']:
            i = i + 1
            if i > number:
                found = True
                break
            links.append(res['data']['url'])

    f = open(filename, 'w')  # also original name for a file handler

    print('Writing to file...')
    for line in links:
        f.write(line + '\n')

    f.close()

    print(str(len(links)) + ' links were saved to the ' + filename + ' file.')


if __name__ == '__main__':
    main()
    sys.exit()

