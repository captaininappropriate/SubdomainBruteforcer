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

# wildcard DNS check function
def wildcard_check(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(0, size))

def bruteforce(domain, wordlist):
    try:
        for hostname in wordlist:
            subdomain = (hostname.rstrip('\n') + '.' + domain)
            result = (dns.resolver.resolve(subdomain))
            for val in result:
                print(subdomain + ' has IP address of ' + str(val))
        return
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

# generate a check for wildcard DNS enteries
checker = wildcard_check()
print(colored('\n[*] using %s.%s as wildcard check' % (checker, args.domain),'green'))

# start the subdomain bruteforce
fileData = args.wordlist
domainName = args.domain
bruteforce(domainName,fileData)
