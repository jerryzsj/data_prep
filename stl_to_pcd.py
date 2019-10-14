import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse
from sklearn.decomposition import PCA
from shutil import copyfile
from stl import mesh

from init_filelist import init_filelist

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)

sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *

def stl_to_pcd(pcd_dir, save_pcd_dir_, s_points=1000):
	input_mesh = mesh.Mesh.from_file('some_file.stl')
	vertice = input_mesh.vectors
	vertice = np.reshape(vertice, (vertice.shape[0]*vertice.shape[1], 3))
	save_nppcd(vertice, save_pcd_dir_)


if __name__ == "__main__":
	PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
	BASE_DIR = os.path.dirname(PROJECT_DIR)

	parser = argparse.ArgumentParser()
	parser.add_argument('--dataset_type', default='mechnet', help='Dataset type [shapes/ycb/mechnet/]')
	parser.add_argument('--dataset_name', default='14_cam_raw', help='Data forder []')
	parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_partial]')
	parser.add_argument('--save_dir', default='pcd', help='filelist [filelist/filelist_partial]')
	FLAGS = parser.parse_args()

	FILELIST = FLAGS.filelist

	DATA_DIR = os.path.join(BASE_DIR, 'data')
	DATA_DIR = os.path.join(DATA_DIR, FLAGS.dataset_type)
	DATA_DIR = os.path.join(DATA_DIR, FLAGS.dataset_name)

	TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'train')
	TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')

	
	stl_to_pcd("abc","bcd")
	
		
		



