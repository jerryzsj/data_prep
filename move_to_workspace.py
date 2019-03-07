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
parser.add_argument('--dataset_name', default='ycb_50', help='Data forder [shapes_meter/shapes_luca/ycb_50]')
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

DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)
TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')


if __name__ == "__main__":

	if DATASET_TYPE == 'shapes':
		train_data, train_label = load_npy(DATA_DIR)
		test_data, test_label = load_npy(TEST_DATA_DIR)

	if DATASET_TYPE == 'ycb':
		train_data, train_label = load_npy(DATA_DIR)
		test_data, test_label = load_npy(TEST_DATA_DIR)

	print(train_data)
	mv_data = move_to_ws_batch(train_data)

	print(mv_data)
	print(train_data.shape)
	print(mv_data.shape)



