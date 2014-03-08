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
hours = []
hours_counter = {}

for line in reader:
    if len(line) > 0:
        author_id, hour = line
        this_key = author_id

        if old_key and old_key != this_key:
            for hour in hours:
                if hour in hours_counter:
                    hours_counter[hour] += 1
                else:
                    hours_counter[hour] = 1

            popular_hours = sorted(
                hours_counter,
                key=hours_counter.get,
                reverse=True
            )

            results = [author_id, popular_hours[0]]
            writer.writerow(results)

            hours = []
            hours_counter = {}

        old_key = this_key
        hours.append(hour)

if old_key != None:
    for hour in hours:
        if hour in hours_counter:
            hours_counter[hour] += 1
        else:
            hours_counter[hour] = 1

    popular_hours = sorted(
        hours_counter,
        key=hours_counter.get,
        reverse=True
    )

    results = [author_id, popular_hours[0]]
    writer.writerow(results)
