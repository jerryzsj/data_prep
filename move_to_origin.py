import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *
from normalize_data import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

parser = argparse.ArgumentParser()

parser.add_argument('--dataset_type', default='ycb', help='Dataset type [shapes/ycb/mechnet/normalized]')
parser.add_argument('--dataset_name', default='ycb_50', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_partial]')
parser.add_argument('--save_dir', default='_ws', help='filelist [filelist/filelist_partial]')

FLAGS = parser.parse_args()

FILELIST = FLAGS.filelist
DATASET_TYPE = FLAGS.dataset_type
DATASET_NAME = FLAGS.dataset_name
SAVE_DIR = FLAGS.save_dir

DATA_DIR = os.path.join(PROJECT_DIR, 'data')
DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)

SAVE_TRAIN_DIR = os.path.join(DATA_DIR, DATASET_NAME+SAVE_DIR)
SAVE_TEST_DIR = os.path.join(SAVE_TRAIN_DIR, 'test')
if not os.path.exists(SAVE_TRAIN_DIR): os.makedirs(SAVE_TRAIN_DIR)
if not os.path.exists(SAVE_TEST_DIR): os.makedirs(SAVE_TEST_DIR)

DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)
TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')



if __name__ == "__main__":


	train_data, train_label = load_npy(DATA_DIR)
	test_data, test_label = load_npy(TEST_DATA_DIR)

	mv_train_data = move_to_origin_batch(train_data)
	mv_test_data = move_to_origin_batch(test_data)
	save_npy(mv_train_data, train_label, SAVE_TRAIN_DIR)
	save_npy(mv_test_data, test_label, SAVE_TEST_DIR)

	train_data, train_label = load_npy(SAVE_TRAIN_DIR)
	test_data, test_label = load_npy(SAVE_TEST_DIR)

	print(bbox_nppcd(train_data))
	print(bbox_nppcd(test_data))




