import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *
from normalize_data import *


parser = argparse.ArgumentParser()
parser.add_argument('--dump_dir', default='temp', help='dump folder path [dump]')
parser.add_argument('--filelist', default='filelist', help='Filelist for training data [filelist/filelist_clean/filelist_clean_error]')
parser.add_argument('--dataset_name', default='shapes_r0.02to0.05', help='Data forder [ycb_1_origin_1000scale/shapes_mm_radius20to50]')
parser.add_argument('--dataset_type', default='normalized', help='Dataset type [shapes/ycb/mechnet/normalized]')
parser.add_argument('--testset', default='false', help='Dataset type [shapes/ycb/mechnet/normalized]')
FLAGS = parser.parse_args()

FILELIST = FLAGS.filelist
DATASET_TYPE = FLAGS.dataset_type
DATASET_NAME = FLAGS.dataset_name
TEST_SET = FLAGS.testset
DUMP_DIR = FLAGS.dump_dir

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

DATA_DIR = os.path.join(PROJECT_DIR, 'data')
DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)
DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)
if TEST_SET=='true':
	DATA_DIR = os.path.join(DATA_DIR, 'test')


DUMP_DIR = os.path.join(PROJECT_DIR, DUMP_DIR)
DUMP_DIR = os.path.join(DUMP_DIR, DATASET_TYPE)
DUMP_DIR = os.path.join(DUMP_DIR, DATASET_NAME)
if FILELIST!='filelist':
	DUMP_DIR = os.path.join(DUMP_DIR, FILELIST)

if TEST_SET=='true':
	DUMP_DIR = os.path.join(DUMP_DIR, 'test')
if not os.path.exists(DUMP_DIR): os.makedirs(DUMP_DIR)


NP_DATA_DIR = os.path.join(DUMP_DIR, 'data')
LABEL_DIR = os.path.join(DUMP_DIR, 'label.txt')


if __name__=='__main__':

	if DATASET_TYPE=="shapes":
		TEST_DATA, TEST_LABELS = load_data(DATA_DIR, FILELIST)

	if DATASET_TYPE=="ycb":
		TEST_DATA, TEST_LABELS = load_data_ycb(DATA_DIR, FILELIST)

	if DATASET_TYPE=="normalized":
		TEST_DATA, TEST_LABELS = load_npy(DATA_DIR)


	normed_data = []

	for idx in range(TEST_DATA.shape[0]):
		norm_ = normalize_nppcd(TEST_DATA[idx])
		normed_data.append(norm_)
	np.save(NP_DATA_DIR, np.array(normed_data))
	np.savetxt(LABEL_DIR, TEST_LABELS, fmt='%d')

	# data = np.load('./temp/data.npy')
	print(TEST_LABELS.shape)
	print(TEST_DATA.shape)