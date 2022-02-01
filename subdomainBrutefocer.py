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
from termcolor import colored

# function to generate a random value which will be used to test for wildcard DNS enteries
def wildcard_check(domainName, size=8, chars=string.ascii_lowercase + string.digits):
    return (''.join(random.choice(chars) for i in range(0, size)) + '.' + domainName)

# lopp through each line and attempt to resolve the IP address
# print only valid records
#def bruteforce(domain, wordlist, checker):
#    try:
#        for hostname in wordlist:
#            subdomain = (hostname.rstrip('\n') + '.' + domain)
#            result = (dns.resolver.resolve(subdomain))
#            for val in result:
#                print(subdomain + ' has IP address of ' + str(val))
#        return
#    except dns.resolver.NXDOMAIN:
#        pass
#    except dns.resolver.Timeout:
#        pass
#    except dns.exception.DNSException:
#        pass

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

# start the subdomain bruteforce
#bruteforce(domainName, fileData, testValue)
