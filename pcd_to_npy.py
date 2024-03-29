import os
import sys
import numpy as np
import numpy.random as nrp
import open3d
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from np_utils import *
from save_bbox import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *
from normalize_data import *


if __name__ == "__main__":

	PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
	BASE_DIR = os.path.dirname(PROJECT_DIR)

	parser = argparse.ArgumentParser()
	parser.add_argument('--dataset_type', default='ycb', help='Dataset type [shapes/ycb/mechnet/normalized]')
	parser.add_argument('--dataset_name', default='ycb_similar_SP20_BIAS1', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
	parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_partial]')
	# parser.add_argument('--filelist_2', default='filelist', help='filelist [filelist/filelist_partial]')
	parser.add_argument('--num_point', type=int, default=1000)
	# parser.add_argument('--num_sample', type=int, default=50)
	FLAGS = parser.parse_args()

	NUM_POINT = (FLAGS.num_point)
	# NUM_SAMPLE = FLAGS.num_sample

	FILELIST = FLAGS.filelist
	DATASET_TYPE = FLAGS.dataset_type
	DATASET_NAME = FLAGS.dataset_name

	DATA_DIR = os.path.join(BASE_DIR, 'data')
	DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)

	if FILELIST!='filelist':
		SAVE_DIR = os.path.join(DATA_DIR, DATASET_NAME + FILELIST[8:])
		SAVE_TEST_DIR = os.path.join(SAVE_DIR, 'test')
		if not os.path.exists(SAVE_DIR): os.makedirs(SAVE_DIR)
		if not os.path.exists(SAVE_TEST_DIR): os.makedirs(SAVE_TEST_DIR)

	if FILELIST=='filelist':
		SAVE_DIR = os.path.join(DATA_DIR, DATASET_NAME)
		SAVE_TRAIN_DIR = os.path.join(SAVE_DIR, 'train')
		SAVE_TEST_DIR = os.path.join(SAVE_DIR, 'test')
		if not os.path.exists(SAVE_DIR): os.makedirs(SAVE_DIR)
		if not os.path.exists(SAVE_TEST_DIR): os.makedirs(SAVE_TEST_DIR)

	DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)
	TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'train')
	TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')


	if DATASET_TYPE == 'mech12':
		TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'train')
		train_data, train_label = load_oneforder_pcd(TRAIN_DATA_DIR)
		test_data, test_label = load_oneforder_pcd(TEST_DATA_DIR)
		print(train_data.shape)
		print(test_data.shape)

		TRAIN_SAVE_DIR = os.path.join(SAVE_DIR, 'train')
		TEST_SAVE_DIR = os.path.join(SAVE_DIR, 'test')

		save_npy(train_data, train_label, TRAIN_SAVE_DIR)
		save_npy(test_data, test_label, TEST_SAVE_DIR)



	if DATASET_TYPE == 'shapes':
		train_data, train_label = load_shapes_pcd(DATA_DIR, FILELIST)
		test_data, test_label = load_shapes_pcd(TEST_DATA_DIR, FILELIST)
		train_data = move_to_origin_batch(train_data)
		test_data = move_to_origin_batch(test_data)
		save_npy(train_data, train_label, SAVE_DIR)
		save_npy(test_data, test_label, SAVE_TEST_DIR)
		save_bbox(SAVE_DIR, train_data, test_data)


	if DATASET_TYPE == 'ycb':
		data, label = load_oneforder_pcd(TEST_DATA_DIR, FILELIST)
		data = move_to_origin_batch(data)
		save_npy(data, label, SAVE_TEST_DIR)

		data, label = load_oneforder_pcd(TRAIN_DATA_DIR, FILELIST)
		data = move_to_origin_batch(data)
		save_npy(data, label, SAVE_TRAIN_DIR)

		# data, label = load_threeforder_pcd(TRAIN_DATA_DIR, FILELIST, FILELIST, FILELIST)
		# data = move_to_origin_batch(data)
		# save_npy(data, label, SAVE_TRAIN_DIR)

		# data, label = load_threeforder_pcd(TEST_DATA_DIR, FILELIST, FILELIST, FILELIST)
		# data = move_to_origin_batch(data)
		# save_npy(data, label, SAVE_TEST_DIR)


	# if DATASET_TYPE == 'ycb':
	# 	train_data, train_label, train_object_list = load_ycb_pcd(DATA_DIR, FILELIST)
	# 	test_data, test_label, test_object_list = load_ycb_pcd(TEST_DATA_DIR, FILELIST)
	# 	print(test_data.shape)
	# 	train_data = move_to_origin_batch(train_data)
	# 	test_data = move_to_origin_batch(test_data)
	# 	print(test_data.shape)
		
	# 	nr.seed()
	# 	for i in range(train_data.shape[0]):
	# 		train_data[i] = np.dot(train_data[i],get_rotation_matrix_zxy(nr.random()*360, nr.random()*360, nr.random()*360).T)
	# 	for i in range(test_data.shape[0]):
	# 		test_data[i] = np.dot(test_data[i],get_rotation_matrix_zxy(nr.random()*360, nr.random()*360, nr.random()*360).T)
		
	# 	save_npy(train_data, train_label, SAVE_DIR)
	# 	save_npy(test_data, test_label, SAVE_TEST_DIR)

	# 	np.savetxt(SAVE_DIR+'/object_list.dat', train_object_list, fmt='%s')
	# 	np.savetxt(SAVE_TEST_DIR+'/object_list.dat', test_object_list, fmt='%s')

	# 	save_bbox(SAVE_DIR, train_data, test_data)

	if DATASET_TYPE == 'mechnet':
		train_data, train_label = load_twoforder_pcd(DATA_DIR, filelist_1=FILELIST)
		test_data, test_label = load_twoforder_pcd(TEST_DATA_DIR, filelist_1=FILELIST)
		save_npy(train_data, train_label, SAVE_DIR)
		save_npy(test_data, test_label, SAVE_TEST_DIR)
		save_bbox(SAVE_DIR, train_data, test_data)

	if DATASET_TYPE == 'kinect':
		data, label, object_list = load_twoforder_pcd(DATA_DIR, filelist_2=FILELIST)

		save_npy(data, label, SAVE_DIR)
		# save_npy(test_data, test_label, SAVE_TEST_DIR)
		# save_bbox(SAVE_DIR, train_data, test_data)
		objectlist_savedir = os.path.join(SAVE_DIR, 'object_list.dat')
		# print(object_list)
		save_list(object_list, objectlist_savedir)