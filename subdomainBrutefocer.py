#!/usr/bin/env python3
# Description   : A simple python script for bruteforcing subdomains
# Usage         : Pass in a file containing subdomains and a target domain name
# Version       : 1.0
# Author        : Greg Nimmo

# import required modules
import random
import dns.resolver
import argparse
import string
from sys import exit
from termcolor import colored

# function to generate a random value which will be used to test for wildcard DNS enteries
def generate_wildcard(domainName, size=8, chars=string.ascii_lowercase + string.digits):
    return (''.join(random.choice(chars) for i in range(0, size)) + '.' + domainName)

def test_for_wildcard_dns(testValue):
    print(colored('[*] testing for wildcard DNS record with %s' % testValue,'green'))
    try:
        wildcard = (dns.resolver.resolve(testValue))
        for value in wildcard:
            if value:
                print(colored('\n[*] wildcard DNS entry exists','red'))
                print(colored('[*] results will be unreliable, exiting...','red'))
                exit(1)
    except Exception as e:
        return 0

def bruteforce_subdomain(wordlist, domainName):
    for line in wordlist:
        try:
            subdomain = (line.rstrip('\n') + '.' + domainName)
            result = (dns.resolver.resolve(subdomain))
            print(result)
        except Exception as e:
            print(e)


# create argparse structure
parser = argparse.ArgumentParser(description='A simple python script to bruteforce subdomains', prog='SubdomainBruteforcer')
parser.add_argument('-w', '--wordlist', type=argparse.FileType('r'), help='text file containing names subdomain names')
parser.add_argument('-d', '--domain', help='fully qualified domain name of target domain', type=str)
args = parser.parse_args()

# shift the passed arguments into global variables
fileData = args.wordlist
domainName = args.domain

# generate a random value to test for wildcard DNS enteries
testValue = generate_wildcard(domainName)

# check if wildcard DNS is in use
noDNS = test_for_wildcard_dns(testValue)

# start a subdomain bruteforce
if not noDNS:
    print(colored('[*] no wildcard DNS recored detected, starting bruteforce','green'))
    bruteforce_subdomain(fileData, domainName)

