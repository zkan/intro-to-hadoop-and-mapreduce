#!/usr/bin/python

# Your task is to write a mapper code that combines 2 datasets
# This is fairly involved task.
# You want to combine the datasets by joining them by the userid
# so, the mapper key should be "user_ptr_id" from "forum_users.tsv"
# and "author_id" from "forum_nodes.tsv" file. The value would be the full line
# from the respective files: either reputation and badges for the user,
# or full information about forum node.
# To be able to combine the records in the reducer you also need to know
# from which of the tables the informations comes from.
# So, the mapper should output A or B (or something similar) in front
# of the value. Output would be:
# 12345\tA"11"\t"0"\t"0"\t"0"
# 12345\tB"6336"\t"Unit 1: Same Value Q"\t"cs101 value same"  (etc...)

# The reducer will get the values sorted, so the line starting with "A"
# will be information about the user, values starting with "B" will be forum nodes.
# Then you can store the user information, append this information to each forum node
# that this user had made, and print it out.

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

        node_id = line[0]
        author_id = line[3]
        body = line[4].strip().replace('\n', ' ')
        added_at = line[8].split(' ')

        record = [node_id, body, added_at[1][0:2]]

        sys.stdout.write(author_id + '\tB')
        writer.writerow(record)
    elif len(line) == 5:
        if line[0] == 'user_ptr_id':
            continue

        user_ptr_id, reputation, gold, silver, bronze = line

        record = [reputation, gold, silver, bronze]

        sys.stdout.write(user_ptr_id + '\tA')
        writer.writerow(record)
