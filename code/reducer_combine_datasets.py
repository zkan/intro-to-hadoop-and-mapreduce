#!/usr/bin/python

# Here you will be able to combine the values that come from 2 sources
# Value start starts with A will be the user data
# Values that start with B will be forum node data

import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(
    sys.stdout,
    delimiter='\t',
    quotechar='"',
    quoting=csv.QUOTE_ALL
)

for line in reader:
    if len(line) > 0:
        author_id = line[0]
        if line[1][0] == 'A':
            reputation = line[1][2:-1]
            gold = line[2]
            silver = line[3]
            bronze = line[4]
        elif line[1][0] == 'B':
            line[1] = line[1][2:-1]
            line.append(reputation)
            line.append(gold)
            line.append(silver)
            line.append(bronze)

            writer.writerow(line)

