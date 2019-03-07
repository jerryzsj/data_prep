#!/bin/bash


SHAPE=shapes_mm_radius20to50
SHAPE2=shapes_mm_radius10to100
YCB=ycb_1_origin_1000scale
TEST=true
NOTEST=false
PARTIAL=filelist_partial
NOPARTIAL=filelist

python normalizing_pcd.py --dataset_name=$SHAPE --testset=$TEST --filelist=$PARTIAL --dataset_type="shapes"
python normalizing_pcd.py --dataset_name=$SHAPE --testset=$NOTEST --filelist=$PARTIAL --dataset_type="shapes"

python normalizing_pcd.py --dataset_name=$SHAPE --testset=$TEST --filelist=$NOPARTIAL --dataset_type="shapes"
python normalizing_pcd.py --dataset_name=$SHAPE --testset=$NOTEST --filelist=$NOPARTIAL --dataset_type="shapes"

python normalizing_pcd.py --dataset_name=$SHAPE2 --testset=$TEST --filelist=$PARTIAL --dataset_type="shapes"
python normalizing_pcd.py --dataset_name=$SHAPE2 --testset=$NOTEST --filelist=$PARTIAL --dataset_type="shapes"

python normalizing_pcd.py --dataset_name=$SHAPE2 --testset=$TEST --filelist=$NOPARTIAL --dataset_type="shapes"
python normalizing_pcd.py --dataset_name=$SHAPE2 --testset=$NOTEST --filelist=$NOPARTIAL --dataset_type="shapes"

python normalizing_pcd.py --dataset_name=$YCB --testset=$TEST --filelist=$NOPARTIAL --dataset_type="ycb"
python normalizing_pcd.py --dataset_name=$YCB --testset=$NOTEST --filelist=$NOPARTIAL --dataset_type="ycb"