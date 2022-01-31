#!/usr/bin/env python3
# Description   : A simple python script for bruteforcing subdomains
# Usage         : Pass in a file containing subdomains and a target domain name
# Version       : 1.0
# Author        : Greg Nimmo

# import required modules
import sys
import random
import os.path
import dns.resolver
import argparse
import string
import threading

# wildcard DNS check function
def wildcard_check(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(0, size))

# create argparse structure
parser = argparse.ArgumentParser(description='A simple python script to bruteforce subdomains', prog='SubdomainBruteforcer')
parser.add_argument('-w', '--wordlist', type=argparse.FileType('r'), help='text file containing names subdomain names')
parser.add_argument('-d', '--domain', help='fully qualified domain name of target domain', type=str)
args = parser.parse_args()

# generate a check for wildcard DNS enteries
checker = wildcard_check()
print('Using %s.%s as wildcard check' % (checker, args.domain))

# loop through the file contents provided by user
fileData = args.wordlist

### test data
###for line in fileData:
###    print(line.rstrip("\n"))
###

