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
from plyfile import PlyData, PlyElement


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
parser.add_argument('--dataset_name', default='ply_from_stl', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_clear]')
parser.add_argument('--num_points', type=int, default=2000)
parser.add_argument('--num_batch', type=int, default=50)
FLAGS = parser.parse_args()

FILELIST = FLAGS.filelist
DATASET_DIR = FLAGS.dataset_dir
DATASET_NAME = FLAGS.dataset_name
NUM_POINTS = FLAGS.num_points
NUM_BATCH = FLAGS.num_batch

DATA_DIR = os.path.join(PROJECT_DIR, 'data')
DATA_DIR = os.path.join(DATA_DIR, DATASET_DIR)
DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)

SAVE_DIR = os.path.join('/tmp/', 'temp')
SAVE_DIR = os.path.join(SAVE_DIR, DATASET_DIR)
SAVE_DIR = os.path.join(SAVE_DIR, 'pcd_files')
SAVE_TEST_DIR = os.path.join(SAVE_DIR, 'test')
shutil.rmtree(SAVE_DIR, ignore_errors=True)
shutil.rmtree(SAVE_TEST_DIR, ignore_errors=True)
os.makedirs(SAVE_DIR)
os.makedirs(SAVE_TEST_DIR)

def read_ply_np(file_dir):
	pcl = PlyData.read(file_dir)
	x = np.array(pcl['vertex']['x'])
	y = np.array(pcl['vertex']['y'])
	z = np.array(pcl['vertex']['z'])
	return np.stack((x, y, z), axis=-1)


def save_ply_to_pcd(file_list, name_list, train_dir, test_dir):
	if not os.path.exists(train_dir): os.makedirs(train_dir)
	if not os.path.exists(test_dir): os.makedirs(test_dir)
	for i in range(len(file_list)):
		ply = read_ply_np(file_list[i])
		pcd = sample_numpoint(ply, NUM_POINTS, 2*NUM_BATCH)
		
		temp_train_dir = os.path.join(train_dir, name_list[i])
		temp_test_dir =  os.path.join(test_dir, name_list[i])
		if not os.path.exists(temp_train_dir): os.makedirs(temp_train_dir)
		if not os.path.exists(temp_test_dir): os.makedirs(temp_test_dir)

		objectlist_train = open(train_dir+'/filelist','a')
		objectlist_test  = open(test_dir+'/filelist','a')
		objectlist_train.write(name_list[i]+"/\n")
		objectlist_test.write(name_list[i]+"/\n")
		for j in range(NUM_BATCH):
			save_pcd_dir(pcd[j], j, temp_train_dir)
			save_pcd_dir(pcd[j+NUM_BATCH], j, temp_test_dir)

			filelist_train = open(temp_train_dir+'/filelist','a')
			filelist_test = open(temp_test_dir+'/filelist','a')

			filelist_train.write(str(j)+".pcd\n")
			filelist_test.write(str(j)+".pcd\n")


if __name__ == "__main__":
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

	save_ply_to_pcd(box_list, box_name, BOX_DIR, BOX_TEST_DIR)
	save_ply_to_pcd(cyl_list, cyl_name, CYL_DIR, CYL_TEST_DIR)
	save_ply_to_pcd(sph_list, sph_name, SPH_DIR, SPH_TEST_DIR)