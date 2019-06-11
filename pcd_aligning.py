import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
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


def pca_transform(data_dir_, filelist_, save_dir_):
	data_list = get_filelist(data_dir_, filelist_)
	name_list = get_filename(data_dir_, filelist_)

	# temp_pcd = open3d.PointCloud()
	
	for idx, filedir in enumerate(data_list):
		save_dir = os.path.join(save_dir_, name_list[idx])

		pcd = load_pcd(filedir)
		pca = PCA(n_components=3)
		pca.fit(pcd)
		pcd_after=pca.fit_transform(pcd)
		
		save_nppcd(pcd_after, save_dir)
		# temp_pcd.points = open3d.Vector3dVector(pcd_after)
		# open3d.write_point_cloud(save_dir, temp_pcd)


if __name__ == "__main__":
	PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
	BASE_DIR = os.path.dirname(PROJECT_DIR)

	parser = argparse.ArgumentParser()
	parser.add_argument('--dataset_type', default='ycb', help='Dataset type [shapes/ycb/mechnet/]')
	parser.add_argument('--dataset_name', default='ycb_stl_uni_norm', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
	parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_partial]')
	parser.add_argument('--save_dir', default='aligned_pcd', help='filelist [filelist/filelist_partial]')
	FLAGS = parser.parse_args()

	FILELIST = FLAGS.filelist

	DATA_DIR = os.path.join(BASE_DIR, 'data')
	DATA_DIR = os.path.join(DATA_DIR, FLAGS.dataset_type)
	DATA_DIR = os.path.join(DATA_DIR, FLAGS.dataset_name)

	TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'train')
	TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')

	TRAIN_SAVE_DIR = os.path.join(TRAIN_DATA_DIR, FLAGS.aligned_pcd)
	TEST_SAVE_DIR = os.path.join(TEST_SAVE_DIR, FLAGS.aligned_pcd)
	if not os.path.exists(TRAIN_SAVE_DIR): os.makedirs(TRAIN_SAVE_DIR)
	if not os.path.exists(TEST_SAVE_DIR): os.makedirs(TEST_SAVE_DIR)
	
	pcd_aligning(TRAIN_DATA_DIR, FILELIST)
	pcd_aligning(TEST_DATA_DIR, FILELIST)
	
		
		



