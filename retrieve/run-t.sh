#!/bin/bash
cat ../../../mywork/wiki.en-head-100.txt | python map.py | sort | python reduce.py
