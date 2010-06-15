#!/bin/python

import re
import sys


transformations = {
    re.compile(r'l\'?enfant', re.I): lambda complete, extracted: len(extracted.strip())>0 and extracted + " S.W." or "L'Enfant Plaza Metro",
    re.compile(r'mcpherson', re.I): lambda complete, extracted: len(extracted.strip())>0 and extracted + " N.W." or "McPherson Square",
    re.compile(r'tomorrow', re.I): lambda complete, extracted: "",
}

whitelist = "(dupont|u st|farragut|gallery pl|union station|L'Enfant|McPherson)"
numbered = "(1st|2nd|3rd|[0-9]+(th)?)"
street = "(((new\s|north\s|south\s|west\s)?\w+)( ave| st)?|%(numbered)s)" % {'numbered': numbered}
cross_street = "((%(numbered)s ?((and)|&) ?%(street)s)|(%(street)s ?((and)|&) ?%(numbered)s))" % {'street': street, 'numbered': numbered}
# >>>>>>> 68f1336cd91c9a119be9b52ae35a2793f5a23fb1
exact = "([0-9]+ \w+ (ave|st))"
address = '(((%(street)s between )?%(cross)s)|%(exact)s|%(whitelist)s)' % \
    {'street': street, 'cross': cross_street, 'exact': exact, 'whitelist': whitelist}
quadrant = re.compile(r'\s([NS])\.?([WE])\.?($|\W)')
exp = re.compile(address, re.I)

def extract(line):
    
    match = exp.search(line)
    
    quadrant_match = quadrant.search(line)

    m = None
    if match:
        m = match

    quadrant_string = ""
    if quadrant_match:
        quadrant_string = " %s.%s." % (quadrant_match.group(1), quadrant_match.group(2))

    extracted_text = ""
    if m is not None:
        extracted_text = m.group(1)
    for (regex, xform) in transformations.items():
        if regex.search(line) is not None:
            extracted_text = xform(line, extracted_text)
    
    if len(extracted_text)>0:
        return extracted_text + quadrant_string
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
        
