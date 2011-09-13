"""Module for testing create_mobi package. Due to relative imports it is not
intended to be runned, only imported from ../test.py"""

if __name__=='__main__':
    print("This module isn't intended to be __main__")
    exit()

from create_mobi import arguments_for_create_mobi as arguments

import os, sys
from datetime import date

print('test_mobi_create imported')

md = arguments.MetaData
md.creator = 'Test_mobi_create module'
md.title = 'Testing book'
md.language = 'en-us'
md.date = date.today()

rfs = arguments.ReadyFiles()
dirname =  os.path.dirname(__file__)
rfs.directory = os.path.join(dirname, 'ready_files', '')
#print rfs.directory

rfs.add('section1.rhtm','Section 1')
rfs.add('section2.rhtm','Section 2')
rfs.add('section3.rhtm','Section 3')

#if os.path.exists(rfs.directory + 'toc.html'):
#    print "Removing old toc.html."
#    os.remove(rfs.directory + 'toc.html')

def test():
    from create_mobi import create_mobi
    create_mobi.create_mobi(rfs, md)

def clean():
    try:
        os.remove(rfs.directory + 'toc.html')
        print("toc.html removed")
    except OSError:
        pass
    try:
        os.remove(rfs.directory + 'toc.ncx')
        print("toc.ncx removed")
    except OSError:
        pass
    try:
        os.remove(rfs.directory + 'book.opf')
        print("book.opf removed")
    except OSError:
        pass
 
    

