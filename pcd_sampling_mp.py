import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse
import shutil
from stl import mesh


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from np_utils import *
from save_bbox import save_bbox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *
from normalize_data import *



def sample_np_pcd(np_pcd, label):
	idx = np.arange(0 , np_pcd.shape[0])
	nr.shuffle(idx)
	pcd_sample = []
	for i in range(NUM_SAMPLE):
		nr.shuffle(idx)
		pcd_sample.append(np_pcd[idx[:NUM_POINT]])
	data = np.array(pcd_sample)
	label = np.full(NUM_SAMPLE, label, dtype=int)
	data = move_to_origin_batch(data)
	data=np.dot(data,get_rotation_matrix_zxy(nr.random()*360, nr.random()*360, nr.random()*360).T)
	return data, label


def save_sample_np_pcd(np_pcd, label, save_dir):
	if not os.path.exists(save_dir): os.makedirs(save_dir)
	filelist = open((os.path.join(save_dir, 'filelist')),'a')
	for i in range(np_pcd.shape[0]):
		save_pcd_dir(np_pcd[i], i, save_dir)
		filelist.write(str(i)+".pcd\n")

	label_dir = os.path.join(save_dir, 'label.dat')
	np.savetxt(label_dir, label, fmt='%d')
	return





if __name__ == "__main__":
	PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
	BASE_DIR = os.path.dirname(BASE_DIR)

	parser = argparse.ArgumentParser()
	parser.add_argument('--dataset_type', default='mech12', help='Dataset type [shapes/ycb/mechnet/]')
	parser.add_argument('--dataset_name', default='14cam_origin', help='Data forder []')
	parser.add_argument('--num_point',type=int, default=1000, help='num_point [1000/2000]')
	parser.add_argument('--num_sample',type=int, default=1, help='filelist [50]')
	FLAGS = parser.parse_args()

	NUM_POINT = FLAGS.num_point
	NUM_SAMPLE = FLAGS.num_sample

	DATASET_TYPE = FLAGS.dataset_type
	DATASET_NAME = FLAGS.dataset_name

	# Data directory
	DATA_DIR = os.path.join(BASE_DIR, 'data')
	DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)

	# Get object list
	OBJECT_LIST = get_filename(DATA_DIR, 'objectlist')

	DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)
	TRAIN_DIR = os.path.join(DATA_DIR, 'train') 
	TEST_DIR = os.path.join(DATA_DIR, 'test')

	# Saving directory
	SAVE_DIR = os.path.join(BASE_DIR, 'data')
	SAVE_DIR = os.path.join(SAVE_DIR, DATASET_TYPE)
	SAVE_DIR = os.path.join(SAVE_DIR, DATASET_NAME+'_'+str(NUM_POINT))
	SAVE_TRAIN_DIR = os.path.join(SAVE_DIR, 'train')
	SAVE_TEST_DIR = os.path.join(SAVE_DIR, 'test')

	# Create save dir
	if not os.path.exists(SAVE_TRAIN_DIR):os.makedirs(SAVE_TRAIN_DIR)
	if not os.path.exists(SAVE_TEST_DIR):os.makedirs(SAVE_TEST_DIR)

	

	# # for training data:
	# for o_list in OBJECT_LIST:
	# 	# dir for point clouds
	# 	data_dir = os.path.join(TRAIN_DIR, o_list)

	# 	# save dir for new point clouds
	# 	save_dir =  os.path.join(SAVE_TRAIN_DIR, o_list)
	# 	if not os.path.exists(save_dir):os.makedirs(save_dir)

	# 	# copy filelist in datadir
	# 	if NUM_SAMPLE==1:
	# 		shutil.copyfile((os.path.join(data_dir, 'filelist')), (os.path.join(save_dir, 'filelist')))
	# 	else:
	# 		save_filelist = open((os.path.join(save_dir, 'filelist')),'w+')

	# 	# read filelist and get filedir
	# 	filedir = get_filelist(data_dir, 'filelist')

	# 	for f_id, f_list in enumerate(filedir):
	# 		np_pcd = load_pcd(f_list)
	# 		idx = np.arange(0 , np_pcd.shape[0])
	# 		nr.shuffle(idx)
	# 		for i in range(NUM_SAMPLE):
	# 			save_name = str(f_id*NUM_SAMPLE+i)+'.pcd'
	# 			nr.shuffle(idx)
	# 			np_pcd = (np_pcd[idx[:NUM_POINT]])
	# 			np_pcd = move_to_origin(np_pcd)
	# 			save_nppcd(np_pcd, os.path.join(save_dir, save_name))
	# 			if not NUM_SAMPLE ==1:
	# 				save_filelist.write(save_name)


	# for testing data:
	for o_list in OBJECT_LIST:
		# dir for point clouds
		data_dir = os.path.join(TEST_DIR, o_list)

		# save dir for new point clouds
		save_dir =  os.path.join(SAVE_TEST_DIR, o_list)
		if not os.path.exists(save_dir):os.makedirs(save_dir)

		# copy filelist in datadir
		if NUM_SAMPLE==1:
			shutil.copyfile((os.path.join(data_dir, 'filelist')), (os.path.join(save_dir, 'filelist')))
		else:
			save_filelist = open((os.path.join(save_dir, 'filelist')),'w+')

		# read filelist and get filedir
		filedir = get_filelist(data_dir, 'filelist')

		for f_id, f_list in enumerate(filedir):
			np_pcd = load_pcd(f_list)
			idx = np.arange(0 , np_pcd.shape[0])
			nr.shuffle(idx)
			for i in range(NUM_SAMPLE):
				save_name = str(f_id*NUM_SAMPLE+i)+'.pcd'
				nr.shuffle(idx)
				np_pcd = (np_pcd[idx[:NUM_POINT]])
				np_pcd = move_to_origin(np_pcd)
				save_nppcd(np_pcd, os.path.join(save_dir, save_name))
				if not NUM_SAMPLE ==1:
					save_filelist.write(save_name)
