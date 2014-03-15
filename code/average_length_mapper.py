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

                # Put 'A' to mark it as question.
                sys.stdout.write(node_id + '\tA')
                record = [post_length]
            elif node_type == 'answer':
                abs_parent_id = line[7]
                answer_length = len(line[4])

                # Put 'B' to mark it as answer.
                sys.stdout.write(abs_parent_id + '\tB')
                record = [answer_length]

            writer.writerow(record)
