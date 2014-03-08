Intro to Hadoop and MapReduce
=============================

To combine the data (on the local machine), run

`cat ../data/input/forum_node.tsv ../data/input/forum_users.tsv | python mapper_combine_datasets.py | sort | python reducer_combine_datasets.py`

To find for each student what is the hour during which the student has posted the most posts (on the local machine), run

`cat ../data/input/forum_node.tsv | python mapper_hour_during_most_posts.py | sort | python reducer_hour_during_most_posts.py`
