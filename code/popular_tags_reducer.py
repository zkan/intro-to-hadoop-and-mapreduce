#!/usr/bin/python

'''
-- Input
Tag and number of questions that have that tag

-- Output
Top 10 tags, ordered by the number of questions they appear in

This reducer takes the tags that are already ranked from the mapper(s), gathers
all of them and rank them again. Finally, it outputs only top 10 tags.
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
old_key = None
max_num_of_questions = -1
tagname_dict = {}

for line in reader:
    # Process only the valid lines.
    if len(line) > 0:
        tagname, num_of_questions = line
        num_of_questions = int(num_of_questions)

        this_key = tagname
        if old_key and old_key != this_key:
            max_num_of_questions = -1

        old_key = this_key
        if num_of_questions > max_num_of_questions:
            tagname_dict[this_key] = num_of_questions
            max_num_of_questions = num_of_questions

# Sort by value.
sorted_tagnames = sorted(tagname_dict.items(), key=lambda x: x[1])
sorted_tagnames.reverse()

for rank in range(top_n):
    record = [sorted_tagnames[rank][0], sorted_tagnames[rank][1]]
    writer.writerow(record)
