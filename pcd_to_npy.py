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
parser.add_argument('--dataset_name', default='ycb_fix_numpoint_1000', help='Data forder [shapes_meter/shapes_luca/ycb_fix_numpoint_1000]')
parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_partial]')
FLAGS = parser.parse_args()

FILELIST = FLAGS.filelist
DATASET_TYPE = FLAGS.dataset_type
DATASET_NAME = FLAGS.dataset_name

DATA_DIR = os.path.join(PROJECT_DIR, 'data')
DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)
DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)
TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')


if __name__ == "__main__":

	if DATASET_TYPE == 'shapes':
		train_data, train_label = load_shapes_pcd(DATA_DIR, FILELIST)
		test_data, test_label = load_shapes_pcd(TEST_DATA_DIR, FILELIST)
		save_npy(train_data, train_label, DATA_DIR)
		save_npy(test_data, test_label, TEST_DATA_DIR)

	if DATASET_TYPE == 'ycb':
		train_data, train_label = load_ycb_pcd(DATA_DIR, FILELIST)
		test_data, test_label = load_ycb_pcd(TEST_DATA_DIR, FILELIST)
		save_npy(train_data, train_label, DATA_DIR)
		save_npy(test_data, test_label, TEST_DATA_DIR)

	train_data, train_label = load_npy(DATA_DIR)
	test_data, test_label = load_npy(TEST_DATA_DIR)
