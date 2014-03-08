Intro to Hadoop and MapReduce
=============================

To combine the data (on the local machine), run

`cat ../data/input/forum_node.tsv ../data/input/forum_users.tsv | python mapper_combine_datasets.py | sort | python reducer_combine_datasets.py`

To find for each student what is the hour during which the student has posted the most posts (on the local machine), run

`cat ../data/input/forum_node.tsv | python student_times_mapper.py | sort | python student_times_reducer.py`
