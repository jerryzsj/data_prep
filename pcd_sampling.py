import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse
import shutil

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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_type', default='mechnet', help='Dataset type [shapes/ycb/mechnet/]')
parser.add_argument('--dataset_name', default='FC', help='Data forder []')
parser.add_argument('--filelist_test', default='filelist_test', help='filelist [filelist/filelist_partial]')
parser.add_argument('--filelist_train', default='filelist_train', help='filelist [filelist/filelist_partial]')
parser.add_argument('--num_point',type=int, default=1000, help='num_point [1000/2000]')
parser.add_argument('--num_sample',type=int, default=50, help='filelist [50]')
FLAGS = parser.parse_args()

NUM_POINT = FLAGS.num_point
NUM_SAMPLE = FLAGS.num_sample

FILELIST_TEST = FLAGS.filelist_test
FILELIST_TRAIN = FLAGS.filelist_train
DATASET_TYPE = FLAGS.dataset_type
DATASET_NAME = FLAGS.dataset_name

DATA_DIR = os.path.join(PROJECT_DIR, 'data')
DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)

DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)

TEMP_DIR = '/tmp/'
SAVE_DIR = os.path.join(TEMP_DIR, DATASET_TYPE)
SAVE_DIR = os.path.join(SAVE_DIR, DATASET_NAME+'_'+str(NUM_POINT))
SAVE_TEST_DIR = os.path.join(SAVE_DIR, 'test')

shutil.rmtree(SAVE_DIR, ignore_errors=True)
shutil.rmtree(SAVE_TEST_DIR, ignore_errors=True)
os.makedirs(SAVE_DIR)
os.makedirs(SAVE_TEST_DIR)


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

	# print(SAVE_TEST_DIR)
	data_test, label_test = load_oneforder_pcd(DATA_DIR, FILELIST_TEST)
	data_train, label_train = load_oneforder_pcd(DATA_DIR, FILELIST_TRAIN)
	
	OBJECT_LIST = get_filename(DATA_DIR, 'filelist')
	np.savetxt(os.path.join(SAVE_DIR, 'filelist'), OBJECT_LIST, fmt='%s')
	np.savetxt(os.path.join(SAVE_TEST_DIR, 'filelist'), OBJECT_LIST, fmt='%s')

	print('Loaded', label_test.shape[0], 'pcd files')
	nr.seed()

	obj_file_test = open((os.path.join(SAVE_TEST_DIR, 'object_list.dat')),'w+')
	obj_file_train = open((os.path.join(SAVE_DIR, 'object_list.dat')),'w+')

	# Sampling testing datasets
	for i in range(label_test.shape[0]):
		sample_data, sample_label = sample_np_pcd(data_test[i], label_test[i])
		sample_data = move_to_origin_batch(sample_data)
		for j in range(sample_data.shape[0]):
			sample_data[j] = np.dot(sample_data[j],get_rotation_matrix_zxy(nr.random()*360, nr.random()*360, nr.random()*360).T)
		save_sample_np_pcd(sample_data, sample_label, os.path.join(SAVE_TEST_DIR, OBJECT_LIST[i]))
		obj_file_test.write(sample_data.shape[0]*(OBJECT_LIST[i][:-1]+'\n'))

	# Sampling training datasets
	for i in range(label_train.shape[0]):
		sample_data, sample_label = sample_np_pcd(data_train[i], label_train[i])
		sample_data = move_to_origin_batch(sample_data)
		for j in range(sample_data.shape[0]):
			sample_data[j] = np.dot(sample_data[j],get_rotation_matrix_zxy(nr.random()*360, nr.random()*360, nr.random()*360).T)
		save_sample_np_pcd(sample_data, sample_label, os.path.join(SAVE_DIR, OBJECT_LIST[i]))
		obj_file_train.write(sample_data.shape[0]*(OBJECT_LIST[i][:-1]+'\n'))
