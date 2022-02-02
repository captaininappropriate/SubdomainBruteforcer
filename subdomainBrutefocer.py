#!/usr/bin/env python3
# Name          : subdomainBruteforcer.py 
# Description   : A simple python script for bruteforcing subdomains
#                 from a user supplied file containing one hostname per line
# Usage         : use --help for complete details. 
#                 TLDR; supply a file containing subdomains (-w) and a target domain (-d) name
# Version       : 1.0
# Author        : Greg Nimmo
# TODO          : Add a routine to save the subdomains identified as valid to a text file


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

# take the random value generated by generate_wildcard and attempt to resolve
# return value used to initiate bruteforce_subdomain function
def test_for_wildcard_dns(testValue):
    print(colored('[*] testing for wildcard DNS record with %s' % testValue,'green'))
    try:
        wildcard = (dns.resolver.resolve(testValue))
        for value in wildcard:
            if value:
                print(colored('\n[*] wildcard DNS entry detected','red'))
                print(colored('[*] results will be unreliable, exiting...','red'))
                exit(1)
    except Exception as e:
        return 1

# take each value in the list and try to resolve
def bruteforce_subdomain(wordlist, domainName):
    for line in wordlist:
        try:
            subdomain = (line.rstrip('\n') + '.' + domainName)
            result = (dns.resolver.resolve(subdomain))
            for value in result:
                # placeholder for try except statement to open and save the results to a file
                #psudo code
                # try open file in append mode
                # write current value 
                # close the file
                # except if file can't be opened just print to screen
                print('[*] %s ip address %s' % (subdomain, str(value)))
        except Exception as e:
            pass


# create argparse structure
parser = argparse.ArgumentParser(description='A simple python script to bruteforce subdomains', prog='SubdomainBruteforcer')
parser.add_argument('-w', '--wordlist', type=argparse.FileType('r'), help='text file containing names subdomain names')
parser.add_argument('-d', '--domain', help='fully qualified domain name of target domain', type=str)
args = parser.parse_args()

# some nicer looking global variables for supplied arguments
fileData = args.wordlist
domainName = args.domain

# call to generate a random value to test for wildcard DNS enteries
testValue = generate_wildcard(domainName)

# call the wildcard test function using the randomly generated value
noWildcard = test_for_wildcard_dns(testValue)

# start a subdomain bruteforce if no record is found
if noWildcard:
    print(colored('[*] no wildcard DNS recored detected, starting bruteforce','green'))
    bruteforce_subdomain(fileData, domainName)

