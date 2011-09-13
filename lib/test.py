#!/usr/bin/env python

""" Flexible testing for 2Kindle """

__author__ = "Hubert Grzywacz"
__author_email__ = "hgrzywacz@gmail.com"
__development_status__ = "Production"
__license__ = "GPL"

import os
import sys
import testing.test_mobi_create

def clean():
    print("Cleaning...")
    testing.test_mobi_create.clean()

def test():
    testing.test_mobi_create.test()

def test_mobi():
    testing.test_mobi_create.test()

operations = {"clean": clean, "test": test, "test_mobi": test_mobi}

for arg in sys.argv[1:]:
    operations[arg]()

if len(sys.argv) == 1:
    test()

exit()

