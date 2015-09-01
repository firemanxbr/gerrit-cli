#!/usr/bin/python

import argparse
from netrc import netrc

"""
Variable for use ~/.netrc data
"""
auth = netrc().hosts


parser = argparse.ArgumentParser(description=
        'Gerrit Client utility the simple tool for administrators')
parser.add_argument('--netrc', help="using netrc file", action="store_true")
args = parser.parse_args()

if args.netrc:
    print 'test'

