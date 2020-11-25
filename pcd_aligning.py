import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d as o3d
import argparse
from sklearn.decomposition import PCA
from shutil import copyfile

from init_filelist import init_filelist

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)

sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *

def pcd_aligning(data_dir_, filelist_):
	train_dir_ = os.path.join(data_dir_, 'train')
	test_dir_ = os.path.join(data_dir_, 'test')
	
	train_save_dir_ = os.path.join(train_dir_, 'aligned_pcd')
	test_save_dir_ = os.path.join(test_dir_, 'aligned_pcd')

	if not os.path.exists(train_save_dir_): os.makedirs(train_save_dir_)
	if not os.path.exists(test_save_dir_): os.makedirs(test_save_dir_)

	train_pcd_dir_ = os.path.join(train_dir_, 'pcd')
	test_pcd_dir_ = os.path.join(test_dir_, 'pcd')

	train_dir_list = os.listdir(train_pcd_dir_)
	if 'filelist' not in train_dir_list:
		init_filelist(train_pcd_dir_)
		
	test_dir_list = os.listdir(test_pcd_dir_)
	if 'filelist' not in test_dir_list:
		init_filelist(test_pcd_dir_)
	
	pca_transform(train_pcd_dir_, filelist_, train_save_dir_)
	pca_transform(test_pcd_dir_, filelist_, test_save_dir_)

	copyfile(os.path.join(train_pcd_dir_, filelist_), os.path.join(train_save_dir_, filelist_))
	copyfile(os.path.join(test_pcd_dir_, filelist_), os.path.join(test_save_dir_, filelist_))


def pca_transform(data_):
	pca = PCA(n_components=3)
	pca.fit(data_)
	pcd_transformed=pca.fit_transform(data_)
	
	# save_nppcd(pcd_after, save_dir)
		# temp_pcd.points = open3d.Vector3dVector(pcd_after)
		# open3d.write_point_cloud(save_dir, temp_pcd)
	return(pcd_transformed)


if __name__ == "__main__":
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument('--dataset_type', default='ycb', help='Dataset type [shapes/ycb/mechnet/normalized]')
# 	parser.add_argument('--dataset_name', default='ycb_28_similar_SP20_BIAS3_norm', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
# 	FLAGS = parser.parse_args()

# 	DATASET_TYPE = FLAGS.dataset_type
# 	DATASET_NAME = FLAGS.dataset_name

	for i in range(1,11):
		DATASET_TYPE = 'ycb'
		DATASET_NAME = 'ycb_28_similar_SP20_BIAS'+ str(i) +'_norm'


		PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
		BASE_DIR = os.path.dirname(PROJECT_DIR)
		DATA_DIR = os.path.join(BASE_DIR, 'data')
		DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)	
		DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)

		TRAIN_DIR = os.path.join(DATA_DIR, 'train')
		TEST_DIR = os.path.join(DATA_DIR, 'test')

		TRAIN_SAVE_DIR = os.path.join(TRAIN_DIR, 'aligned_pcd')
		TEST_SAVE_DIR = os.path.join(TEST_DIR, 'aligned_pcd')
		if not os.path.exists(TRAIN_SAVE_DIR): os.makedirs(TRAIN_SAVE_DIR)
		if not os.path.exists(TEST_SAVE_DIR): os.makedirs(TEST_SAVE_DIR)

		TRAIN_DATA = np.load(os.path.join(TRAIN_DIR, 'data.npy'))
		TEST_DATA = np.load(os.path.join(TEST_DIR, 'data.npy'))

		train_pcd_list = []
		num_train = TRAIN_DATA.shape[0]
		for i in range(num_train):
			transformed = pca_transform(TRAIN_DATA[i])
			save_nppcd(transformed, os.path.join(TRAIN_SAVE_DIR, str(i)+'.pcd'))
			train_pcd_list.append(transformed)
		np.save(os.path.join(TRAIN_DIR, 'data_aligned.npy'), np.array(train_pcd_list))

		if np.shape(train_pcd_list) != TRAIN_DATA.shape:
			print('Something wrong with pcd aligning')

		test_pcd_list = []
		num_test = TEST_DATA.shape[0]
		for i in range(num_test):
			transformed = pca_transform(TEST_DATA[i])
			save_nppcd(transformed, os.path.join(TEST_SAVE_DIR, str(i)+'.pcd'))
			test_pcd_list.append(transformed)
		np.save(os.path.join(TEST_DIR, 'data_aligned.npy'), np.array(test_pcd_list))

		if np.shape(test_pcd_list) != TEST_DATA.shape:
			print('Something wrong with pcd aligning')

		print('Finish pcd aligning with dataset: '+DATASET_NAME)



