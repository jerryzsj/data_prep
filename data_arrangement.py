import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse
import shutil
from shutil import copyfile
from pathlib import Path

from pcd_aligning import pcd_aligning
from init_filelist import init_filelist

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *

def main():

	PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
	BASE_DIR = os.path.dirname(PROJECT_DIR)
	DATA_DIR = os.path.join(BASE_DIR, 'data')

	parser = argparse.ArgumentParser()
	parser.add_argument('--dataset_type', default='shapes', help='Dataset type [shapes/ycb/mechnet/normalized]')
	parser.add_argument('--dataset_name', default='shapes_luca_clean', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
	FLAGS = parser.parse_args()

	DATA_DIR = os.path.join(DATA_DIR, FLAGS.dataset_type)
	DATA_DIR = os.path.join(DATA_DIR, FLAGS.dataset_name)

	dir_list = os.listdir(DATA_DIR)
	train_dir = os.path.join(DATA_DIR, 'train')
	test_dir = os.path.join(DATA_DIR, 'test')
	if 'train' not in dir_list:
		os.makedirs(str(train_dir))
		# return
	# else:
	
	for f_ in dir_list:
		file_dir = os.path.join(DATA_DIR, f_)
		if f_ == 'bbox_test.dat':
			shutil.move(file_dir ,os.path.join(test_dir, 'bbox.dat'))

		elif f_ == 'bbox_train.dat':
			shutil.move(file_dir ,os.path.join(train_dir, 'bbox.dat'))

		elif f_ != 'train' and f_ != 'test':
			shutil.move(file_dir ,os.path.join(train_dir, f_))

	train_dir_list = os.listdir(train_dir)
	
	if 'pcd' not in train_dir_list:
		train_save_dir = os.path.join(train_dir, 'pcd')
		test_save_dir = os.path.join(test_dir, 'pcd')

		train_data, _ = load_npy(train_dir)
		test_data, _ = load_npy(test_dir)

		for idx, val in enumerate(train_data):
			save_pcd_dir(val, idx, train_save_dir)
		for idx, val in enumerate(test_data):
			save_pcd_dir(val, idx, test_save_dir)

		init_filelist(train_save_dir)
		init_filelist(test_save_dir)


	# SAVE_TRAIN_DIR = os.path.join(DATA_DIR, DATASET_NAME+'_'+str(ERROR_LEVEL)+SAVE_DIR)
	# SAVE_TEST_DIR = os.path.join(SAVE_TRAIN_DIR, 'test')
	# if not os.path.exists(SAVE_TRAIN_DIR): os.makedirs(SAVE_TRAIN_DIR)
	# if not os.path.exists(SAVE_TEST_DIR): os.makedirs(SAVE_TEST_DIR)

	# DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)
	# TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')


if __name__ == "__main__":
	main()