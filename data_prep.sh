#!/bin/bash


# # create_shapes(0.5, 0.8)
# python create_shapes.py --min_len=0.04 --max_len=0.4
# python create_shapes.py --min_len=0.5 --max_len=0.8

# create_shapes(0.20, 0.25)
# python create_shapes.py --min_len=0.04 --max_len=0.20
# python create_shapes.py --min_len=0.04 --max_len=0.25
# python create_shapes.py --min_len=0.02 --max_len=0.20
# python create_shapes.py --min_len=0.02 --max_len=0.15
# python create_shapes.py --min_len=0.02 --max_len=0.10
# python create_shapes.py --min_len=0.02 --max_len=0.11
# python create_shapes.py --min_len=0.02 --max_len=0.12
# python create_shapes.py --min_len=0.02 --max_len=0.13
# python create_shapes.py --min_len=0.02 --max_len=0.14
# python create_shapes.py --min_len=0.02 --max_len=0.12

# # save pcd files into data.npy + md5.dat + label.dat
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.04to0.4_200'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.5to0.8_200'

# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.04to0.2_200'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.04to0.25_200'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.2_200'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.15_200'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.1_200'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.11_200'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.12_200'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.13_200'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.14_200'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.12_200_thin

# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_0%_error_2k' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_0%_error_2k'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_1%_error_2k' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_1%_error_2k'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_2%_error_2k' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_2%_error_2k'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_3%_error_2k' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_3%_error_2k'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_4%_error_2k' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_4%_error_2k'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_5%_error_2k' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_5%_error_2k'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_6%_error_2k' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_6%_error_2k'
# python pcd_to_npy.py --dataset_type='ycb' --dataset_name='ycb_stl_2k' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='ycb' --dataset_name='ycb_stl_2k'

# python pcd_to_npy.py --dataset_type='ycb' --dataset_name='ycb_stl_2k' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='ycb' --dataset_name='ycb_stl_2k'

python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_luca' --filelist='filelist_double_error'
python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_luca_double_error'

# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_10%_error_2k' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_10%_error_2k'

# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_gaussian_5' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_gaussian_5'

# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_7%_error' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_7%_error'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_8%_error' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_8%_error'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_9%_error' --filelist='filelist'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb_20per_9%_error'


# python pcd_to_npy.py --dataset_type='ycb' --dataset_name='ycb_50'

# # create partial ycb dataset by partial filelist
# python pcd_to_npy.py --dataset_type='ycb' --dataset_name='ycb_50' --filelist='filelist_0'
# python pcd_to_npy.py --dataset_type='ycb' --dataset_name='ycb_50' --filelist='filelist_1'
# python pcd_to_npy.py --dataset_type='ycb' --dataset_name='ycb_50' --filelist='filelist_2'
# python pcd_to_npy.py --dataset_type='ycb' --dataset_name='ycb_50' --filelist='filelist_3'
# python pcd_to_npy.py --dataset_type='ycb' --dataset_name='ycb_50' --filelist='filelist_clear'



# # normalize pcd, make largest value=1, smallest value=0
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_0.04to0.4_200'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_0.5to0.8_200'


# python normalizing_pcd.py --dataset_type='ycb' --dataset_name='ycb_50'
# python normalizing_pcd.py --dataset_type='ycb' --dataset_name='ycb_50_rot'
# python normalizing_pcd.py --dataset_type='ycb' --dataset_name='ycb_50_partial_0'
# python normalizing_pcd.py --dataset_type='ycb' --dataset_name='ycb_50_partial_1'
# python normalizing_pcd.py --dataset_type='ycb' --dataset_name='ycb_50_partial_2'
# python normalizing_pcd.py --dataset_type='ycb' --dataset_name='ycb_50_partial_3'
# python normalizing_pcd.py --dataset_type='ycb' --dataset_name='ycb_clear'


# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_0.04to0.2_200'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_0.04to0.25_200'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.2_200'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.15_200'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.1_200'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.11_200'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.12_200'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.13_200'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.14_200'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_0.02to0.12_200_thin'
# python normalizing_pcd.py --dataset_type='shapes' --dataset_name='shapes_ycb'

