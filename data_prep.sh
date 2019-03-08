#!/bin/bash


# create_shapes(0.5, 0.8)
# python create_shapes.py --min_len=0.04 --max_len=0.4
# python create_shapes.py --min_len=0.5 --max_len=0.8

# # save pcd files into data.npy + md5.dat + label.dat
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.04to0.4_200'
# python pcd_to_npy.py --dataset_type='shapes' --dataset_name='shapes_0.5to0.8_200'
# # python pcd_to_npy.py --dataset_type='ycb' --dataset_name='ycb_50'

# # move npy data to workspace x[0.1,0.9], y[0.1,0.9], z[0.1,0.9]
python move_to_workspace.py --dataset_type='shapes' --dataset_name='shapes_0.04to0.4_200'
python move_to_workspace.py --dataset_type='shapes' --dataset_name='shapes_0.5to0.8_200'
# # python move_to_workspace.py --dataset_type='ycb' --dataset_name='ycb_50'