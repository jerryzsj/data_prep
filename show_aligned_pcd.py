import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)

sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_name', default='shapes_ycb_20per_0%_error_norm', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_partial]')
parser.add_argument('--aligned_dir', default='aligned_pcd', help='filelist [filelist/filelist_partial]')
FLAGS = parser.parse_args()

FILELIST = FLAGS.filelist
DATASET_NAME = FLAGS.dataset_name

DATA_DIR = os.path.join(PROJECT_DIR, DATASET_NAME)
DATA_DIR = os.path.join(DATA_DIR, FLAGS.aligned_dir)

TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'train') 
TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')


def show_aligned_pcd(data_dir_, filelist_, num_pcd_):
	dir_list = get_filelist(data_dir_, filelist_)
	name_list = get_filename(data_dir_, filelist_)

	temp_pcd = open3d.PointCloud()
	
	merge_pcd = []

	for idx in range(num_pcd_):

		pcd = load_pcd(dir_list[400+idx*10])
		pca = PCA(n_components=3)
		pca.fit(pcd)
		pcd_after=pca.fit_transform(pcd)
		merge_pcd.append(pcd_after)
	merge_pcd=np.array(merge_pcd)
	merge_pcd=np.reshape(merge_pcd, [num_pcd_*1000, 3])
	show_nppcd(merge_pcd)

if __name__ == "__main__":
	
	show_aligned_pcd(TRAIN_DATA_DIR, FILELIST, 5)
	
		
		



