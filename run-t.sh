#!/bin/bash
cat ../../mywork/wiki.en-head-10000.txt | python map.py | sort | python reduce.py
