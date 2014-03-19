#!/usr/bin/python

'''
-- Input
Udacity forum data that contain all forum questions and answers in one table
(forum_node.tsv)

-- Output
Key: author ID
Value: hour during which the student has posted

This mapper reads the data and then output in the desired format.
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

        author_id = line[3]
        # The added_at field is stored in the format
        # like this 2012-02-25 08:09:06.787181+00.
        added_at = line[8].split(' ')
        hour = added_at[1][0:2]

        # Use author ID as key and the hour as value.
        record = [author_id, hour]
        writer.writerow(record)
