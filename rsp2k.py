#!/usr/bin/env python3
"""
Main script merging the rest of the scripts.
One to rule them on, one could say.
"""

import sys
import os
import argparse
import string
import datetime
import shutil

from lib.create_mobi import create_mobi
from lib.create_mobi import arguments_for_create_mobi

import lib.get_post

def parse_path(path):
    filename_ext = os.path.split(path)[1]
    filename = os.path.splitext(filename_ext)[0]
    return filename


def from_file(onefile, directory, readyfiles):
    f = open(onefile, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        url = line.rstrip()
        filename, title = lib.get_post.get_post(url, directory)
        filename = os.path.split(filename)[1]
#        readyfile = arguments_for_create_mobi.ReadyFile(filename, title)
        readyfiles.add(filename, title)


def run_kindlegen(bookopf):

    # Yes there are two paths you can go by...
    kgen_here = os.path.join(os.getcwd(), 'kindlegen')
    kgen_here_exe = os.path.join(os.getcwd(), 'kindlegen.exe')

    if not (sys.platform.startswith('win') or sys.platform.startswith('Win')):
        os.system(kgen_here + ' ' + bookopf)
    else:
        os.system(kgen_here_exe + ' ' + bookopf)
    return


def main():

    if len(sys.argv) == 1:
        print('\nUsage: python ' + str(sys.argv[0]) + ' file1 file2 ...\n')
        sys.exit()

    fileslist = sys.argv[1:]

    readyfiles = arguments_for_create_mobi.ReadyFiles()

    for onefile in fileslist:
        filename = parse_path(onefile)
        directory = filename
        try:
            os.mkdir(directory)
        except OSError:
            print('\nFolder ' + directory + ' exists. Remove or move it.\n')
            continue
        print('Creating directory ' + directory + '.')
        from_file(onefile, directory, readyfiles)

    metadata = arguments_for_create_mobi.MetaData()
    metadata.creator = 'Reddit.com'
    metadata.title = directory
    metadata.language = 'en'
    metadata.date = str(datetime.date.today())

    readyfiles.directory = directory

    coverpath = os.path.join(directory, 'cover.jpg')
    shutil.copy('lib/testing/ready_files/cover.jpg', coverpath)
    print('Copying cover.')

    create_mobi.create_mobi(readyfiles, metadata)

    bookopf = os.path.join(directory, 'book.opf')

    run_kindlegen(bookopf)
    print('OK')

if __name__ == '__main__':
    main()
    sys.exit()
