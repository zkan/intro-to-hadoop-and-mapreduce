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

        node_id = line[0]
        author_id = line[3]
        node_type = line[5]
        abs_parent_id = line[7]
        if node_type == 'question':
            record = [node_id, author_id]
        elif node_type == 'answer':
            record = [abs_parent_id, author_id]

        writer.writerow(record)
