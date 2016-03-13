# parse

This script takes a text file generated by `pdftotext`.

- It removes (at least) some state and unnecessary data.
   - Any pages with "TURN OUT"
   - Any pages with "STRAIGHT PARTY"
   - Any results with "County" or "Constitutional"
- Removes headers

Currently prints number of matches, total number of pages

It also only parses one particular file -- `2014 General Election Box Elder SOVC.txt`.

## TODO

- Accept filename as argument
- Parse data (obviously)