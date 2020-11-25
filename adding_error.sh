#!/bin/bash

DATATYPE=ycb
DATANAME=ycb_similar_norm

for i in {1..10}
do
	python adding_error.py --dataset_type=$DATATYPE --dataset_name=$DATANAME --error_level=$i
done