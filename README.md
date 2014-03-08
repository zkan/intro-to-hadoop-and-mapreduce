Intro to Hadoop and MapReduce
=============================

To combine the data (on the local machine), run

`cat ../data/input/forum_node.tsv ../data/input/forum_users.tsv | python mapper_combine_datasets.py | sort | python reducer_combine_datasets.py > ../data/output/combine_results`
