import os
import sys
import numpy as np
import numpy.random as nr
import h5py
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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_type', default='shapes', help='Dataset type [shapes/ycb/mechnet/normalized]')
parser.add_argument('--dataset_name', default='shapes_ycb', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_partial]')
FLAGS = parser.parse_args()

FILELIST = FLAGS.filelist
DATASET_TYPE = FLAGS.dataset_type
DATASET_NAME = FLAGS.dataset_name

DATA_DIR = os.path.join(PROJECT_DIR, 'data')
DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)

if FILELIST!='filelist':
	SAVE_DIR = os.path.join(DATA_DIR, DATASET_NAME +'_partial_'+FILELIST[-1])
	SAVE_TEST_DIR = os.path.join(SAVE_DIR, 'test')
	if not os.path.exists(SAVE_DIR): os.makedirs(SAVE_DIR)
	if not os.path.exists(SAVE_TEST_DIR): os.makedirs(SAVE_TEST_DIR)

DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)
TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')




if __name__ == "__main__":

	if DATASET_TYPE == 'shapes':
		train_data, train_label = load_shapes_pcd(DATA_DIR, FILELIST)
		test_data, test_label = load_shapes_pcd(TEST_DATA_DIR, FILELIST)
		train_data = move_to_origin_batch(train_data)
		test_data = move_to_origin_batch(test_data)
		save_npy(train_data, train_label, DATA_DIR)
		save_npy(test_data, test_label, TEST_DATA_DIR)
		save_bbox(DATA_DIR, train_data, test_data)


	if DATASET_TYPE == 'ycb' and FILELIST=='filelist':
		train_data, train_label, train_object_list = load_ycb_pcd(DATA_DIR, FILELIST)
		test_data, test_label, test_object_list = load_ycb_pcd(TEST_DATA_DIR, FILELIST)

		train_data = move_to_origin_batch(train_data)
		test_data = move_to_origin_batch(test_data)
		
		nr.seed()
		for i in range(train_data.shape[0]):
			train_data[i] = np.dot(train_data[i],get_rotation_matrix_zxy(nr.random()*360, nr.random()*360, nr.random()*360).T)
		for i in range(test_data.shape[0]):
			test_data[i] = np.dot(test_data[i],get_rotation_matrix_zxy(nr.random()*360, nr.random()*360, nr.random()*360).T)
		
		save_npy(train_data, train_label, DATA_DIR)
		save_npy(test_data, test_label, TEST_DATA_DIR)

		np.savetxt(DATA_DIR+'/object_list.dat', train_object_list, fmt='%s')
		np.savetxt(TEST_DATA_DIR+'/object_list.dat', test_object_list, fmt='%s')

		save_bbox(DATA_DIR, train_data, test_data)


	if DATASET_TYPE == 'ycb' and FILELIST!='filelist':
		train_data, train_label, train_object_list = load_ycb_pcd(DATA_DIR, FILELIST)
		test_data, test_label, test_object_list = load_ycb_pcd(TEST_DATA_DIR, FILELIST)
		
		train_data = move_to_origin_batch(train_data)
		test_data = move_to_origin_batch(test_data)
		
		nr.seed()
		for i in range(train_data.shape[0]):
			train_data[i] = np.dot(train_data[i],get_rotation_matrix_zxy(nr.random()*360, nr.random()*360, nr.random()*360).T)
		for i in range(test_data.shape[0]):
			test_data[i] = np.dot(test_data[i],get_rotation_matrix_zxy(nr.random()*360, nr.random()*360, nr.random()*360).T)
		
		save_npy(train_data, train_label, SAVE_DIR)
		save_npy(test_data, test_label, SAVE_TEST_DIR)

		# print(np.shape(train_object_list))
		np.savetxt(SAVE_DIR+'/object_list.dat', train_object_list, fmt='%s')
		np.savetxt(SAVE_TEST_DIR+'/object_list.dat', test_object_list, fmt='%s')

		save_bbox(SAVE_DIR, train_data, test_data)
	# train_data, train_label = load_npy(DATA_DIR)
	# test_data, test_label = load_npy(TEST_DATA_DIR)
