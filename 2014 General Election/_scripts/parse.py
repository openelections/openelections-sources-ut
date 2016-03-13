#!/usr/bin/env python

import re

raw = open('./2014 General Election Box Elder SOVC.txt', 'rb').read()

matches = re.split("\f", raw)
actualMatches = 0
goodData = []

for match in matches:
    if not match:
        continue
    turnout = re.search("(turn out|straight party)", match, re.I)
    if turnout:
        continue
    matchSections = re.split("SOVC For Jurisdiction Wide, All Counters, All Races", match)
    if len(matchSections) != 2:
        raise Exception('Something happened')
    goodData.append(matchSections[1].strip())

stateFederalData = []

for page in goodData:
    countyMatches = re.search("^(county|constitutional)", page, re.I)

    if countyMatches:
        continue
    actualMatches += 1
    stateFederalData.append(page)

print 'Pages to parse: ' + str(actualMatches)
print 'Total pages: ' + str(len(matches))
