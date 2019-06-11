#!/bin/bash_norm


# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_luca_error
# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_luca_error_norm
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_luca_double_error
# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_luca_double_error_norm
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_0%_error_2k
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_1%_error_2k
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_2%_error_2k
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_3%_error_2k
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_4%_error_2k
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_5%_error_2k
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_6%_error_2k
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_7%_error_2k
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_8%_error_2k
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_9%_error_2k
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_10%_error_2k

# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_0%_error_2k_norm
# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_1%_error_2k_norm
# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_2%_error_2k_norm
# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_3%_error_2k_norm
# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_4%_error_2k_norm
# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_5%_error_2k_norm
# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_6%_error_2k_norm
# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_7%_error_2k_norm
# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_8%_error_2k_norm
# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_9%_error_2k_norm
# python npy_to_pcd.py --dataset_type='shapes' --dataset_name=shapes_ycb_20per_10%_error_2k_norm

# python normalizing_pcd.py --dataset_type='mechnet' --dataset_name=3cam
# python adding_error.py --dataset_type='mechnet' --dataset_name=3cam_1000_norm
# python npy_to_pcd.py --dataset_type='mechnet' --dataset_name=3cam_1000_norm_10_error

THREECAM1000=3cam_1000
THREECAM2000=3cam_2000
THREECAM=3cam_
FC1000=FC_1000
FC2000=FC_2000
NORM=_norm
ERROR=_error
DASH=_

for i in {3..5}
do
	# python normalizing_pcd.py --dataset_type='mechnet' --dataset_name=$THREECAM$i'000'
	# # python adding_error.py --dataset_type='mechnet' --dataset_name=$THREECAM$i'000'$NORM --error_level=$i
	# python npy_to_pcd.py --dataset_type='mechnet' --dataset_name=$THREECAM$i'000'$NORM
	python npy_to_pcd.py --dataset_type='mechnet' --dataset_name=$THREECAM$i'000'
done
