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

old_key = None
old_post_length = 0
total_answer_length = 0
answer_count = 0

for line in reader:
    # Process only the valid lines.
    if len(line) > 0:
        node_id = line[0]
        this_key = node_id

        if line[1][0] == 'A':
            # remove 'A' from the field
            post_length = line[1][2:-1]
        elif line[1][0] == 'B':
            # remove 'B' from the field
            answer_length = line[1][2:-1]
            total_answer_length += float(answer_length)
            answer_count += 1

        if old_key and old_key != this_key:
            if answer_count != 0:
                average_answer_length = total_answer_length / answer_count
            else:
                average_answer_length = 0.0

            results = [old_key, old_post_length, average_answer_length]
            writer.writerow(results)

            total_answer_length = 0
            answer_count = 0

        old_key = this_key
        old_post_length = post_length

if old_key != None:
    average_answer_length = total_answer_length / answer_count
    results = [old_key, old_post_length, average_answer_length]
    writer.writerow(results)
