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
author_list = []

for line in reader:
    # Process only the valid lines.
    if len(line) > 0:
        node_id, author_id = line
        this_key = node_id

        if old_key and old_key != this_key:
            results = author_list
            results[:0] = [old_key]
            writer.writerow(results)

            author_list = []

        old_key = this_key
        author_list.append(author_id)

if old_key != None:
    results = author_list
    results[:0] = [old_key]
    writer.writerow(results)
