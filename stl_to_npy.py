import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse
import math
from stl import mesh
import shutil


# source lib from abs-dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from np_utils import *
# from save_bbox import *

# source lib from dir under project dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *
from normalize_data import *

# relink base_dir & project_dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

# parsers
parser = argparse.ArgumentParser()
parser.add_argument('--dataset_dir', default='ycb_dataset_original', help='Dataset type [shapes/ycb/mechnet/normalized]')
parser.add_argument('--dataset_name', default='stl_files', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_clear]')
FLAGS = parser.parse_args()

FILELIST = FLAGS.filelist
DATASET_DIR = FLAGS.dataset_dir
DATASET_NAME = FLAGS.dataset_name

DATA_DIR = os.path.join(PROJECT_DIR, 'data')
DATA_DIR = os.path.join(DATA_DIR, DATASET_DIR)
DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)

SAVE_DIR = os.path.join('/tmp/', 'temp')
SAVE_DIR = os.path.join(SAVE_DIR, DATASET_DIR)
SAVE_DIR = os.path.join(SAVE_DIR, DATASET_NAME)
SAVE_TEST_DIR = os.path.join(SAVE_DIR, 'test')
shutil.rmtree(SAVE_DIR, ignore_errors=True)
shutil.rmtree(SAVE_TEST_DIR, ignore_errors=True)
os.makedirs(SAVE_DIR)
os.makedirs(SAVE_TEST_DIR)


# return normal and vertice from stl file
def stl_to_pcd(dir_list_, name_list_, save_dir_, save_test_dir_, num_points):
	if not os.path.exists(save_dir_): os.makedirs(save_dir_)
	if not os.path.exists(save_test_dir_): os.makedirs(save_test_dir_)
	filelist_train = open(save_dir_+'/filelist','a')
	filelist_test = open(save_test_dir_+'/filelist','a')

	for j in range(len(name_list_)):
		filelist_train.write(name_list_[j][:-4]+"/\n")
		filelist_test.write(name_list_[j][:-4]+"/\n")

		temp_dir = os.path.join(save_dir_, name_list_[j][:-4])
		temp_test_dir = os.path.join(save_test_dir_, name_list_[j][:-4])
		if not os.path.exists(temp_dir): os.makedirs(temp_dir)
		if not os.path.exists(temp_test_dir): os.makedirs(temp_test_dir)

		filelist_object_train = open(temp_dir+'/filelist','a')
		filelist_object_test = open(temp_test_dir+'/filelist','a')

		stl_mesh = mesh.Mesh.from_file(dir_list_[j])
		vertice = stl_mesh.vectors
		vertice = np.reshape(vertice, (vertice.shape[0]*vertice.shape[1], 3))
		idx = np.arange(vertice.shape[0])
		if vertice.shape[0]<2*num_points:
			print('too less points', name_list_[j])
		for i in range(50):
			nr.shuffle(idx)
			save_pcd_dir(vertice[idx[0:num_points]], str(i), temp_dir)
			save_pcd_dir(vertice[idx[num_points:2*num_points]], str(i), temp_test_dir)
			filelist_object_train.write(str(i)+".pcd\n")
			filelist_object_test.write(str(i)+".pcd\n")

	filelist_object_train.close()
	filelist_object_test.close()
	filelist_train.close()
	filelist_test.close()




if __name__=="__main__":
	nr.seed()

	stl_dir = get_filelist(DATA_DIR, 'filelist')

	box_list = get_filelist(stl_dir[0], 'filelist')
	box_name = get_objectlist(stl_dir[0], 'filelist')
	cyl_list = get_filelist(stl_dir[1], 'filelist')
	cyl_name = get_objectlist(stl_dir[1], 'filelist')
	sph_list = get_filelist(stl_dir[2], 'filelist')
	sph_name = get_objectlist(stl_dir[2], 'filelist')

	
	BOX_DIR = os.path.join(SAVE_DIR, 'box')
	BOX_TEST_DIR = os.path.join(SAVE_TEST_DIR, 'box')
	CYL_DIR = os.path.join(SAVE_DIR, 'cylinder')
	CYL_TEST_DIR = os.path.join(SAVE_TEST_DIR, 'cylinder')
	SPH_DIR = os.path.join(SAVE_DIR, 'sphere')
	SPH_TEST_DIR = os.path.join(SAVE_TEST_DIR, 'sphere')

	num_points = 2000

	stl_to_pcd(box_list, box_name, BOX_DIR, BOX_TEST_DIR, num_points)
	stl_to_pcd(cyl_list, cyl_name, CYL_DIR, CYL_TEST_DIR, num_points)
	stl_to_pcd(sph_list, sph_name, SPH_DIR, SPH_TEST_DIR, num_points)

	filelist_train = open(SAVE_DIR+'/filelist','w')
	filelist_test = open(SAVE_TEST_DIR+'/filelist','w')
	filelist_train.write("box/\ncylinder/\nsphere/\n")
	filelist_test.write("box/\ncylinder/\nsphere/\n")
	filelist_train.close()
	filelist_test.close()

