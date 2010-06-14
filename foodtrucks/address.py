#!/bin/python

import re
import sys

whitelist = "(dupont|u st|farragut|gallery pl)"
numbered = "(1st|2nd|3rd|[0-9]+(th)?)"
street = "(\w+( ave| st)?|%(numbered)s)" % {'numbered': numbered}
cross_street = "(%(numbered)s ?((and)|&) ?%(street)s)" % {'street': street, 'numbered': numbered}
exact = "([0-9]+ \w+ (ave|st))"
address = '(((%(street)s between )?%(cross)s)|%(exact)s|%(whitelist)s)' % \
    {'street': street, 'cross': cross_street, 'exact': exact, 'whitelist': whitelist}

exp = re.compile(address, re.I)

def extract(line):
    match = exp.search(line)
    
    if match:
        return match.group(1)
    else:
        return None


if __name__ == '__main__':
    matched = list()
    unmatched = list()
    
    for line in sys.stdin:
        match = extract(line)
        if match:
            matched.append("%s <--- %s" % (match, line.strip()))
        else:
            unmatched.append(line.strip())

    print "%d lines matched:" % len(matched)
    for line in matched:
        print line
    print "\n%d lines not matched:" % len(unmatched)
    for line in unmatched:
        print line
        
