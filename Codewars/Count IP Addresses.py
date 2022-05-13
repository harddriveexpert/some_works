# Count IP Addresses (https://www.codewars.com/kata/526989a41034285187000de4)

# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

# Examples

# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246

import re


def ips_between(start, end):
        start = [int(i) for i in re.findall(r'[0-9]+', start)]
        end = [int(i) for i in re.findall(r'[0-9]+', end)]
        ip1 = (start[0]*(256**3))+(start[1]*(256**2))+(start[2]*256)+start[3]
        ip2 = (end[0]*(256**3))+(end[1]*(256**2))+(end[2]*256)+end[3]
        return ip2 - ip1