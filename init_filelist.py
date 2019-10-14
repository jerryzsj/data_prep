import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse
from shutil import copyfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)

sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *

def init_filelist(data_dir):
	# print(data_dir)
	os_list = os.listdir(data_dir)
	if 'filelist' in os_list :
		return
	else:
		# print(os_list)
		num_pcd = (len(os_list))
		F = open(os.path.join(data_dir, 'filelist'), 'w+')
		for i in range(num_pcd):
			F.write(str(i)+'.pcd\n')
		return


if __name__ == "__main__":
	PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
	BASE_DIR = os.path.dirname(PROJECT_DIR)
	DATA_DIR = os.path.join(BASE_DIR, 'data')

	parser = argparse.ArgumentParser()
	parser.add_argument('--dataset_type', default='ycb', help='Dataset type [shapes/ycb/mechnet/]')
	parser.add_argument('--dataset_name', default='ycb_stl_uni_norm', help='Data forder []')
	parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_partial]')
	# parser.add_argument('--num_point',type=int, default=1000, help='num_point [1000/2000]')
	# parser.add_argument('--num_sample',type=int, default=50, help='filelist [50]')
	FLAGS = parser.parse_args()

	DATA_DIR = os.path.join(DATA_DIR, FLAGS.dataset_type)
	DATA_DIR = os.path.join(DATA_DIR, FLAGS.dataset_name)

	TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'pcd')

	TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')
	TEST_DATA_DIR = os.path.join(TEST_DATA_DIR, 'pcd')
	# print(os.listdir(DATA_DIR))
	init_filelist(TRAIN_DATA_DIR)
	init_filelist(TEST_DATA_DIR)

	# os_list = os.listdir(TRAIN_DATA_DIR)
	# os_list.remove('filelist')

	# num_pcd = (len(os_list))
	
	# F = open(os.path.join(TRAIN_DATA_DIR, 'filelist'), 'w+')
	
	# for i in range(num_pcd):
	# 	F.write(str(i)+'.pcd\n')

	# F.close()
	# copyfile(os.path.join(TRAIN_DATA_DIR, 'filelist'), os.path.join(TEST_DATA_DIR, 'filelist'))



