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
from normalize_data import *
from save_bbox import *


parser = argparse.ArgumentParser()
parser.add_argument('--dataset_type', default='mech12', help='Dataset type [shapes/ycb/mechnet/normalized]')
parser.add_argument('--dataset_name', default='3cam_origin_1000_norm', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_partial]')
parser.add_argument('--save_dir', default='_error', help='filelist [filelist/filelist_partial]')
parser.add_argument('--error_level', type=int, default=10, help='')
FLAGS = parser.parse_args()

FILELIST = FLAGS.filelist
DATASET_TYPE = FLAGS.dataset_type
DATASET_NAME = FLAGS.dataset_name
SAVE_DIR = FLAGS.save_dir
ERROR_LEVEL = FLAGS.error_level

DATA_DIR = os.path.join(PROJECT_DIR, 'data')
DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)

SAVE_DIR = os.path.join(DATA_DIR, DATASET_NAME+'_'+str(ERROR_LEVEL)+SAVE_DIR)
SAVE_TRAIN_DIR = os.path.join(SAVE_DIR, 'train')
SAVE_TEST_DIR = os.path.join(SAVE_DIR, 'test')
if not os.path.exists(SAVE_TRAIN_DIR): os.makedirs(SAVE_TRAIN_DIR)
if not os.path.exists(SAVE_TEST_DIR): os.makedirs(SAVE_TEST_DIR)

DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)
TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'train')
TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')


if __name__=='__main__':
	nr.seed()

	train_data, train_label = load_npy(TRAIN_DATA_DIR)
	test_data, test_label = load_npy(TEST_DATA_DIR)

	for idx in range(train_data.shape[0]):
		train_data[idx] += (nr.rand(train_data.shape[1],3)-0.5)*ERROR_LEVEL/100

	for idx in range(test_data.shape[0]):
		test_data[idx] += (nr.rand(train_data.shape[1],3)-0.5)*ERROR_LEVEL/100

	save_npy(train_data, train_label, SAVE_TRAIN_DIR)
	save_npy(test_data, test_label, SAVE_TEST_DIR)

	save_bbox(SAVE_DIR, train_data, test_data)
	
	# if DATASET_TYPE == 'ycb' or 'mechnet':
	# 	copyfile(os.path.join(DATA_DIR,'object_list.dat'), os.path.join(SAVE_TRAIN_DIR,'object_list.dat'))
	# 	copyfile(os.path.join(TEST_DATA_DIR,'object_list.dat'), os.path.join(SAVE_TEST_DIR,'object_list.dat'))
