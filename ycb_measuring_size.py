import os
import sys
import numpy as np
import numpy.random as nr
import h5py
from open3d import *
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from np_utils import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *
from normalize_data import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_type', default='ycb', help='Dataset type [shapes/ycb/mechnet/normalized]')
parser.add_argument('--dataset_name', default='stl_files_14cam', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
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
TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'train')
TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')


def pick_points(pcd):
    print("")
    print("1) Please pick at least three correspondences using [shift + left click]")
    print("   Press [shift + right click] to undo point picking")
    print("2) Afther picking points, press q for close the window")
    vis = VisualizerWithEditing()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.run() # user picks points
    vis.destroy_window()
    print("")
    idx = vis.get_picked_points()
    list = []
    for i in idx:
	    list.append(pcd.points[i])
    return list

def cal_box_shape(key_point):
	l_ = np.linalg.norm(key_point[0] - key_point[1])
	w_ = np.linalg.norm(key_point[0] - key_point[2])
	h_ = np.linalg.norm(key_point[0] - key_point[3])
	return np.array((l_, w_, h_))

def cal_box_shape_batch(key_point):
	kp = []
	for i in key_point:
		kp.append(cal_box_shape(i))
	return np.array(kp)

def cal_cyl_shape(key_point):
	r_ = np.linalg.norm(key_point[0] - key_point[1])
	h_ = np.linalg.norm(key_point[0] - key_point[2])
	return np.array((r_, h_))

def cal_cyl_shape_batch(key_point):
	kp = []
	for i in key_point:
		kp.append(cal_cyl_shape(i))
	return np.array(kp)

def cal_sph_shape(key_point):
	r_ = np.linalg.norm(key_point[0] - key_point[1])
	return np.array((r_))

def cal_sph_shape_batch(key_point):
	kp = []
	for i in key_point:
		kp.append(cal_sph_shape(i))
	return np.array(kp)


if __name__ == "__main__":
	
	# # find box's size
	# print('Finding boxes size points')
	# box_size_point = []
	# for i in range(12):
	# 	data = load_open3d_pcd(DATA_DIR + ('/' +str(i)+'.pcd'))
	# 	box_size_point.append(pick_points(data))
	# np.save(os.path.join(DATA_DIR, 'box_size_point.npy'), box_size_point)
	# 
	# print('Calculating boxes size')
	# data = np.load(os.path.join(DATA_DIR, 'box_size_point.npy'))
	# box_shape = cal_box_shape_batch(data)
	# np.savetxt(os.path.join(DATA_DIR, 'box_shapes.txt'), box_shape)
	# print(box_shape)
	
	
	# # find cylinder's size
	# print('Finding cyliners size points')
	# cylinder_size_point = []
	# for i in range(12,24):
	# 	print(str(i)+'.pcd')
	# 	data = load_open3d_pcd(DATA_DIR + ('/' +str(i)+'.pcd'))
	# 	cylinder_size_point.append(pick_points(data))
	# np.save(os.path.join(DATA_DIR, 'cylinder_size_point.npy'), cylinder_size_point)
	# 
	# print('Calculating cyliners size')
	# data = np.load(os.path.join(DATA_DIR, 'cylinder_size_point.npy'))
	# cylinder_shape = cal_cyl_shape_batch(data)
	# np.savetxt(os.path.join(DATA_DIR, 'cylinder_shapes.txt'), cylinder_shape)
	# print(cylinder_shape)
	
	
	
	# find sphere's size
	print('Finding spheres size points')
	sphere_size_point = []
	for i in range(24,36):
		print(str(i)+'.pcd')
		data = load_open3d_pcd(DATA_DIR + ('/' +str(i)+'.pcd'))
		sphere_size_point.append(pick_points(data))
	np.save(os.path.join(DATA_DIR, 'sphere_size_point.npy'), sphere_size_point)
	
	print('Calculating spheres size')
	data = np.load(os.path.join(DATA_DIR, 'sphere_size_point.npy'))
	sphere_shape = cal_sph_shape_batch(data)
	np.savetxt(os.path.join(DATA_DIR, 'sphere_shapes.txt'), sphere_shape)
	print(sphere_shape)
	
	
	
	
	# data = np.load(os.path.join(DATA_DIR, 'box_shapes.npy'))
	# print(data)

	# data = np.load(os.path.join(DATA_DIR, 'box_size_points.npy'))
	# # print(data)
	# box_shape = cal_box_shape_batch(data)
	# np.save(os.path.join(DATA_DIR, 'box_shapes.npy'), box_shape)
	# print(box_shape)

	# data = np.load(os.path.join(DATA_DIR, 'cyl_size_points.npy'))
	# # print(data)
	# cyl_shape = cal_cyl_shape_batch(data)
	# np.save(os.path.join(DATA_DIR, 'cyl_shapes.npy'), cyl_shape)
	# print(cyl_shape)

	# train_data, train_label = load_npy(TRAIN_DATA_DIR)
	# test_data, test_label = load_npy(TEST_DATA_DIR)
	
	# picked_point = []
	# for i in range(0, 12):
	# 	pcd = np_to_pcd(train_data[i])
	# 	picked_point.append(pick_points(pcd))
	# np.save(os.path.join(DATA_DIR, 'box_size_points.npy'), np.array(picked_point))

	# data = np.load(os.path.join(DATA_DIR, 'box_size_points.npy'))
	# # print(data)
	# box_shape = cal_box_shape_batch(data)
	# np.save(os.path.join(DATA_DIR, 'box_shapes.npy'), box_shape)
	# print(box_shape)


	# picked_point = []
	# for i in range(12, 24):
	# 	pcd = np_to_pcd(train_data[i])
	# 	picked_point.append(pick_points(pcd))
	# np.save(os.path.join(DATA_DIR, 'cyl_size_points.npy'), np.array(picked_point))

	# data = np.load(os.path.join(DATA_DIR, 'cyl_size_points.npy'))
	# # print(data)
	# cyl_shape = cal_cyl_shape_batch(data)
	# np.save(os.path.join(DATA_DIR, 'cyl_shapes.npy'), cyl_shape)
	# print(cyl_shape)

	# picked_point = []
	# for i in range(24, 36):
	# 	pcd = nppcd_to_open3d(train_data[i])
	# 	picked_point.append(pick_points(pcd))
	# np.save(os.path.join(DATA_DIR, 'sph_size_points.npy'), np.array(picked_point))

	# data = np.load(os.path.join(DATA_DIR, 'sph_size_points.npy'))
	# # print(data)
	# cyl_shape = cal_sph_shape_batch(data)
	# np.save(os.path.join(DATA_DIR, 'sph_shapes.npy'), cyl_shape)
	# print(cyl_shape)