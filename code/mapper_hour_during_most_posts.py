#!/usr/bin/python

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
    if len(line) == 19:
        if line[0] == 'id':
            continue

        author_id = line[3]
        added_at = line[8].split(' ')

        record = [author_id, added_at[1][0:2]]

        writer.writerow(record)
