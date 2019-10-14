#!/bin/bash

THREECAM=3cam_origin_1000_norm_
ERROR=_error

for i in {1..10}
do
	python npy_to_pcd.py --dataset_type='mech12' --dataset_name=$THREECAM$i$ERROR
done


# python npy_to_pcd.py --dataset_type='mechnet' --dataset_name=shapes_luca_clean_norm_norm

# python npy_to_pcd.py --dataset_type=shapes --dataset_name=shapes_ycb_20per_0%_error_norm_norm
# python npy_to_pcd.py --dataset_type=shapes --dataset_name=shapes_ycb_20per_1%_error_norm_norm
# python npy_to_pcd.py --dataset_type=shapes --dataset_name=shapes_ycb_20per_2%_error_norm_norm
# python npy_to_pcd.py --dataset_type=shapes --dataset_name=shapes_ycb_20per_3%_error_norm_norm
# python npy_to_pcd.py --dataset_type=shapes --dataset_name=shapes_ycb_20per_4%_error_norm_norm
# python npy_to_pcd.py --dataset_type=shapes --dataset_name=shapes_ycb_20per_5%_error_norm_norm
# python npy_to_pcd.py --dataset_type=shapes --dataset_name=shapes_ycb_20per_6%_error_norm_norm
# python npy_to_pcd.py --dataset_type=shapes --dataset_name=shapes_ycb_20per_7%_error_norm_norm
# python npy_to_pcd.py --dataset_type=shapes --dataset_name=shapes_ycb_20per_8%_error_norm_norm
# python npy_to_pcd.py --dataset_type=shapes --dataset_name=shapes_ycb_20per_9%_error_norm_norm
# python npy_to_pcd.py --dataset_type=shapes --dataset_name=shapes_ycb_20per_10%_error_norm_norm