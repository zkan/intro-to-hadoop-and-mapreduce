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
    # Process only the valid lines.
    if len(line) == 19:
        # Skip the header line.
        if line[0] == 'id':
            continue

        author_id = line[3]
        # The added_at field is stored in the format
        # like this 2012-02-25 08:09:06.787181+00.
        added_at = line[8].split(' ')

        # Use author ID as key and the hour as value.
        record = [author_id, added_at[1][0:2]]
        writer.writerow(record)
