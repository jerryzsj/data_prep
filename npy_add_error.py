import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse
import shutil


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from np_utils import *
from save_bbox import save_bbox


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *
from normalize_data import *


def add_error(nppcd, error_level):
	for idx in range(nppcd.shape[0]):
		nrshape = [nppcd.shape[1],3]
		# nppcd[idx] += (nr.rand(nppcd.shape[1],3)-0.5)*error_level/100
		nppcd[idx] += nr.uniform(-error_level/100, error_level/100, nrshape)
	return nppcd



if __name__=='__main__':
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	BASE_DIR = os.path.dirname(BASE_DIR)

	parser = argparse.ArgumentParser()
	parser.add_argument('--dataset_type', default='shapes', help='Dataset type [shapes/ycb/mechnet/normalized]')
	parser.add_argument('--dataset_name', default='ycb_28_similar_SP20_BIAS5_norm', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
	parser.add_argument('--save_dir', default='_error')
	FLAGS = parser.parse_args()

	DATASET_TYPE = FLAGS.dataset_type
	DATASET_NAME = FLAGS.dataset_name
	SAVE_DIR = FLAGS.save_dir

	DATA_DIR = os.path.join(PROJECT_DIR, 'data')
	DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)

	SAVE_DIR = os.path.join(DATA_DIR, DATASET_NAME+SAVE_DIR)
	SAVE_TRAIN_DIR = os.path.join(SAVE_DIR, 'train')
	SAVE_TEST_DIR = os.path.join(SAVE_DIR, 'test')
	if not os.path.exists(SAVE_TRAIN_DIR): os.makedirs(SAVE_TRAIN_DIR)
	if not os.path.exists(SAVE_TEST_DIR): os.makedirs(SAVE_TEST_DIR)

	DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)
	TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'train')
	TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')

	train_data, train_label = load_npy(TRAIN_DATA_DIR)
	test_data, test_label = load_npy(TEST_DATA_DIR)

	train_data = add_error(train_data, 2.5)
	test_data = add_error(test_data, 2.5)

	train_data = move_to_origin_batch(train_data)
	test_data = move_to_origin_batch(test_data)

	save_npy(train_data, train_label, SAVE_TRAIN_DIR)
	save_npy(test_data, test_label, SAVE_TEST_DIR)

	save_bbox(SAVE_DIR, train_data, test_data)

	for idx, val in enumerate(train_data):
		save_pcd_dir(val, idx, os.path.join(SAVE_TRAIN_DIR,'pcd'))
	for idx, val in enumerate(test_data):
		save_pcd_dir(val, idx, os.path.join(SAVE_TEST_DIR,'pcd'))
