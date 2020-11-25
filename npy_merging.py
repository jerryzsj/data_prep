import os
import sys
import numpy as np
import numpy.random as nr
# import h5py
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
	parser.add_argument('--filelist', default='npy_merging_filelist', help='filelist [filelist/filelist_partial]')
	parser.add_argument('--data_dir', default='data')
	parser.add_argument('--save_dir', default='transfer_learning_ycb_stl', help='filelist [filelist/filelist_partial]')
	parser.add_argument('--train_idx',type=int, default=[0,3,9,11,14,18])
	parser.add_argument('--test_idx', type=int, default=[3,9,11,14,18,25])
	parser.add_argument('--idx_batch', type=int, default=50)
	FLAGS = parser.parse_args()

	# FILELIST = FLAGS.filelist

	IDX_BATCH= FLAGS.idx_batch
	TRAIN_IDX = np.array(FLAGS.train_idx, dtype=int) * IDX_BATCH
	TRAIN_IDX = np.reshape(TRAIN_IDX, (-1,2))
	TEST_IDX = np.array(FLAGS.test_idx, dtype=int) * IDX_BATCH
	TEST_IDX = np.reshape(TEST_IDX, (-1,2))

	DATA_DIR = os.path.join(PROJECT_DIR, FLAGS.data_dir)
	FILELIST = get_filelist(DATA_DIR, FLAGS.filelist)

	SAVE_DIR = os.path.join(DATA_DIR, FLAGS.save_dir)
	SAVE_TRAIN_DIR = os.path.join(SAVE_DIR, 'train')
	SAVE_TEST_DIR = os.path.join(SAVE_DIR, 'test')
	if not os.path.exists(SAVE_TRAIN_DIR): os.makedirs(SAVE_TRAIN_DIR)
	if not os.path.exists(SAVE_TEST_DIR): os.makedirs(SAVE_TEST_DIR)

	data = []
	label = []

	# for first dataset
	f_dir = FILELIST[0]
	train_dir = dir_merge(f_dir, 'train')
	test_dir = dir_merge(f_dir, 'test')
	print(train_dir)
	print(test_dir)

	train_data, train_label = load_npy(train_dir)
	test_data, test_label = load_npy(train_dir)

	data.append()
	
	# print(train_idx)
	# print(test_idx)
	for i in TRAIN_IDX:
		data.extend(source_data[i[0]:i[1]])
		label.extend(source_label[i[0]:i[1]])

	data = np.array(data)
	label = np.array(label)
	# print(data)
	# print(label)




