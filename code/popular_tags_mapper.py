#!/usr/bin/python

'''
-- Input
Udacity forum data that contain all forum questions and answers in one table
(forum_node.tsv)

-- Output
Key: tag name for question node
Value: number of questions that have tag name

This mapper reads the data, counts the number of tags for each question, then
outputs only the top 10 tags that are most used in the forum (only question
type).
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

top_n = 10
tagname_dict = {}

for line in reader:
    # Process only the valid lines.
    if len(line) == 19:
        # Skip the header line.
        if line[0] == 'id':
            continue

        tagnames = line[2]
        node_type = line[5]
        if node_type == 'question':
            for tagname in tagnames.split(' '):
                if len(tagname) > 0:
                    if tagname in tagname_dict:
                        tagname_dict[tagname] += 1
                    else:
                        tagname_dict[tagname] = 1

# Sort by value.
sorted_tagnames = sorted(tagname_dict.items(), key=lambda x: x[1])
sorted_tagnames.reverse()

for rank in range(top_n):
    record = [sorted_tagnames[rank][0], sorted_tagnames[rank][1]]
    writer.writerow(record)
