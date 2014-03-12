Intro to Hadoop and MapReduce
=============================

To combine the data (on the local machine), run

`cat ../data/input/forum_node.tsv ../data/input/forum_users.tsv | python mapper_combine_datasets.py | sort | python reducer_combine_datasets.py`

To find for each student what is the hour during which the student has posted the most posts (on the local machine), run

`cat ../data/input/forum_node.tsv | python student_times_mapper.py | sort | python student_times_reducer.py`

To find the length of the post and the average answer (just answer, not comment) length for each post (on the local machine), run

`cat ../data/input/forum_node.tsv | python average_length_mapper.py | sort | python average_length_reducer.py`
