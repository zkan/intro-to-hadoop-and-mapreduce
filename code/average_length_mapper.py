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

        node_type = line[5]
        if node_type in ['question', 'answer']:
            if node_type == 'question':
                node_id = line[0]
                post_length = len(line[4])

                record = [post_length]
                sys.stdout.write(node_id + '\tA')
            elif node_type == 'answer':
                abs_parent_id = line[7]
                answer_length = len(line[4])

                sys.stdout.write(abs_parent_id + '\tB')
                record = [answer_length]

            writer.writerow(record)
