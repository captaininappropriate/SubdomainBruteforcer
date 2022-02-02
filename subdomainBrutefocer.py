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
import threading
from sys import exit
from termcolor import colored

# function to generate a random value which will be used to test for wildcard DNS enteries
def wildcard_check(domainName, size=8, chars=string.ascii_lowercase + string.digits):
    return (''.join(random.choice(chars) for i in range(0, size)) + '.' + domainName)

# lopp through each line and attempt to resolve the IP address
# print only valid records
def bruteforce(domain, wordlist, testValue):

    try:
        wildcard = (dns.resolver.resolve(testValue))
        if wildcard:
            print(colored('\n[*] wildcard DNS record detected using %s' % (testValue),'red'))
            print(colored('[*] results will be unreliable, exiting bruteforce','red'))
            exit()
    except:
        print('\n[*]no wildcard detected, commencing bruteforce')
    try:
        for line in wordlist:
            subdomain = (line.rstrip('\n') + '.' + domain)
            print(subdomain)
            result = (dns.resolver.resolve(subdomain))
            for value in result:
                print(subdomain + ' has IP address of ' + str(value))
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.Timeout:
        pass
    except dns.exception.DNSException:
        pass

# create argparse structure
parser = argparse.ArgumentParser(description='A simple python script to bruteforce subdomains', prog='SubdomainBruteforcer')
parser.add_argument('-w', '--wordlist', type=argparse.FileType('r'), help='text file containing names subdomain names')
parser.add_argument('-d', '--domain', help='fully qualified domain name of target domain', type=str)
args = parser.parse_args()

# shift the passed arguments into global variables
fileData = args.wordlist
domainName = args.domain

# generate a random value to test for wildcard DNS enteries
testValue = wildcard_check(domainName)
print(colored('\n[*] using %s as wildcard check' % (testValue),'green'))

# start a subdomain bruteforce
bruteforce(domainName, fileData, testValue)
