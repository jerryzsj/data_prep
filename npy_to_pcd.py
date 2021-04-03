import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse
from shutil import copyfile

from init_filelist import init_filelist

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *
from normalize_data import *
from save_bbox import *


if __name__=='__main__':
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	BASE_DIR = os.path.dirname(BASE_DIR)

	parser = argparse.ArgumentParser()
	parser.add_argument('--dataset_type', default='mech12', help='Dataset type [shapes/ycb/mechnet/normalized]')
	parser.add_argument('--dataset_name', default='3cam_origin_1000_norm', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
	parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_partial]')
	parser.add_argument('--save_dir', default='pcd', help='filelist [filelist/filelist_partial]')
	FLAGS = parser.parse_args()

	FILELIST = FLAGS.filelist
	DATASET_TYPE = FLAGS.dataset_type
	DATASET_NAME = FLAGS.dataset_name

	DATA_DIR = os.path.join(PROJECT_DIR, 'data')
	DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)

	DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)
	TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'train')
	TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')

	SAVE_TRAIN_DIR = os.path.join(TRAIN_DATA_DIR, FLAGS.save_dir)
	SAVE_TEST_DIR = os.path.join(TEST_DATA_DIR, FLAGS.save_dir)
	if not os.path.exists(SAVE_TRAIN_DIR): os.makedirs(SAVE_TRAIN_DIR)
	if not os.path.exists(SAVE_TEST_DIR): os.makedirs(SAVE_TEST_DIR)

	print(TRAIN_DATA_DIR)
	print(TEST_DATA_DIR)
	train_data, train_label = load_npy(TRAIN_DATA_DIR)	
	test_data, test_label = load_npy(TEST_DATA_DIR)

	for idx, val in enumerate(train_data):
		save_pcd_dir(val, idx, SAVE_TRAIN_DIR)
	for idx, val in enumerate(test_data):
		save_pcd_dir(val, idx, SAVE_TEST_DIR)

	# save_bbox(SAVE_DIR, train_data, test_data)

	init_filelist(SAVE_TRAIN_DIR)
	init_filelist(SAVE_TEST_DIR)