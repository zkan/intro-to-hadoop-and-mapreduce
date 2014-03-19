#!/usr/bin/python

'''
-- Input
Udacity forum data that contain all forum questions and answers in one table
(forum_node.tsv)

-- Output
Key: node ID
Value: author ID

This mapper reads the data, checks if it is question, answer, or commnet. If it
is question, then just outputs node ID and author ID. If it is answer/comment,
the outputs the parent ID of the answer/comment and authod ID.
'''

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
        else:
            record = [abs_parent_id, author_id]

        writer.writerow(record)
