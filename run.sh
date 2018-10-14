#!/bin/bash
hadoop jar ${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar \
	-input /user/jason/ \
	-output /user/mr-output \
	-mapper map.py  \
	-reducer reduce.py \
	-file map.py \
	-file reduce.py
