""" Tool to extract/downsampling point clouds from YCB model set

Author: Senjing Zheng
Date: Octorber 2021
Email: Senjing.Zheng@gmail.com
"""

import os
import sys
import numpy as np
import h5py
import json
from plyfile import PlyData, PlyElement

# Customized dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, '../pcl_utils'))

import pcio

PROJECT_DIR = os.path.dirname(BASE_DIR) # 3d-vision project
DATA_BASE_DIR = os.path.join(PROJECT_DIR, 'data') # 3d-vision/data folder

def load_h5(h5_filename):
	f = h5py.File(h5_filename)
	# data = f['data'][:]
	# label = f['label'][:]
	return (data, label)


def read_ply_np(file_dir):
	pcl = PlyData.read(file_dir)
	x = np.array(pcl['vertex']['x'])
	y = np.array(pcl['vertex']['y'])
	z = np.array(pcl['vertex']['z'])
	return np.stack((x, y, z), axis=-1)




if __name__ == '__main__':
	NUM_POINT = 1000
	NUM_SAMPLE = 20

	DATA_BASE_DIR = os.path.join(DATA_BASE_DIR, 'ycb_dataset_original')
	SAVE_BASE_DIR = os.path.join(DATA_BASE_DIR, 'sampled_pcd_from_berkeley_processed')

	json_dir = os.path.join(DATA_BASE_DIR, 'ycb28_primitives_list.json')
	DATA_DIR = os.path.join(DATA_BASE_DIR, 'berkeley_processed')

	objects = json.load(open(json_dir,))
	box_list = objects['box']
	cylinder_list = objects['cylinder']
	sphere_list = objects['sphere']
	
	all_nppcd = []
	all_label = []


	for file_name in box_list:
		file_base_dir = os.path.join(DATA_DIR, file_name)
		file_dir = os.path.join(file_base_dir, 'clouds')
		file_dir = os.path.join(file_dir, 'merged_cloud.ply')

		save_base_dir = os.path.join(SAVE_BASE_DIR, file_name)
		if not os.path.exists(save_base_dir):
			os.makedirs(save_base_dir)
		# print(save_base_dir)

		nppcd = read_ply_np(file_dir)
		lenpcd = nppcd.shape[0]
		print(file_name, lenpcd)
		idx_all = np.arange(lenpcd)
		np.random.shuffle(idx_all)
		np.save(os.path.join(save_base_dir, 'suffled_idx.npy'), idx_all)
		for nsample in range(NUM_SAMPLE):
			save_name = str(nsample)
			save_dir = os.path.join(save_base_dir, save_name+'.pcd')
			sample_pcd = nppcd[idx_all[nsample*NUM_POINT:(nsample*NUM_POINT+NUM_POINT)]]
			pcio.save_nppcd(sample_pcd, save_dir)

			all_nppcd.append(sample_pcd)
			all_label.append(0)



	for file_name in cylinder_list:
		file_base_dir = os.path.join(DATA_DIR, file_name)
		file_dir = os.path.join(file_base_dir, 'clouds')
		file_dir = os.path.join(file_dir, 'merged_cloud.ply')

		save_base_dir = os.path.join(SAVE_BASE_DIR, file_name)
		if not os.path.exists(save_base_dir):
			os.makedirs(save_base_dir)
		# print(save_base_dir)

		nppcd = read_ply_np(file_dir)
		lenpcd = nppcd.shape[0]
		print(file_name, lenpcd)
		idx_all = np.arange(lenpcd)
		np.random.shuffle(idx_all)
		np.save(os.path.join(save_base_dir, 'suffled_idx.npy'), idx_all)
		for nsample in range(NUM_SAMPLE):
			save_name = str(nsample)
			save_dir = os.path.join(save_base_dir, save_name+'.pcd')
			sample_pcd = nppcd[idx_all[nsample*NUM_POINT:(nsample*NUM_POINT+NUM_POINT)]]
			pcio.save_nppcd(sample_pcd, save_dir)

			all_nppcd.append(sample_pcd)
			all_label.append(1)



	for file_name in sphere_list:
		file_base_dir = os.path.join(DATA_DIR, file_name)
		file_dir = os.path.join(file_base_dir, 'clouds')
		file_dir = os.path.join(file_dir, 'merged_cloud.ply')

		save_base_dir = os.path.join(SAVE_BASE_DIR, file_name)
		if not os.path.exists(save_base_dir):
			os.makedirs(save_base_dir)
		# print(save_base_dir)

		nppcd = read_ply_np(file_dir)
		lenpcd = nppcd.shape[0]
		print(file_name, lenpcd)
		idx_all = np.arange(lenpcd)
		np.random.shuffle(idx_all)
		np.save(os.path.join(save_base_dir, 'suffled_idx.npy'), idx_all)
		for nsample in range(NUM_SAMPLE):
			save_name = str(nsample)
			save_dir = os.path.join(save_base_dir, save_name+'.pcd')
			sample_pcd = nppcd[idx_all[nsample*NUM_POINT:(nsample*NUM_POINT+NUM_POINT)]]
			pcio.save_nppcd(sample_pcd, save_dir)

			all_nppcd.append(sample_pcd)
			all_label.append(2)

	print(np.shape(all_nppcd))
	np.save(os.path.join(SAVE_BASE_DIR, 'nppcd.npy'), np.array(all_nppcd))
	np.savetxt(os.path.join(SAVE_BASE_DIR, 'label.txt'), np.array(all_label), fmt='%d')

	# file_name = 'calibration.h5'
	# file_dir = os.path.join(DATA_DIR, file_name)

	# hfile = h5py.File(file_dir, 'r')
	# print((hfile['data']))
	









