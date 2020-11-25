import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse
from shutil import copyfile
import math

from pcd_aligning import pcd_aligning

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'shapes-recognition'))

from shapes_profiling import *
import primitive_shapes_generator.primitive_shapes_generator as pg

# def feature_extracting(data_dir_, filelist_):
# 	train_dir_ = os.path.join(data_dir_, 'train')
# 	test_dir_ = os.path.join(data_dir_, 'test')
	
# 	train_save_dir_ = os.path.join(train_dir_, 'feature.dat')
# 	test_save_dir_ = os.path.join(test_dir_, 'feature.dat')

# 	train_pcd_dir_ = os.path.join(train_dir_, 'aligned_pcd')
# 	test_pcd_dir_ = os.path.join(test_dir_, 'aligned_pcd')

# 	if not os.path.exists(test_pcd_dir_) or not os.path.exists(train_pcd_dir_): pcd_aligning(data_dir_, filelist_)

# 	train_data_list = get_filelist(train_pcd_dir_, filelist_)
# 	train_out_feature = extract_feature_batch(train_data_list)
# 	save_feature_batch(train_out_feature, train_save_dir_)

# 	test_data_list = get_filelist(test_pcd_dir_, filelist_)
# 	test_out_feature = extract_feature_batch(test_data_list)
# 	save_feature_batch(test_out_feature, test_save_dir_)


def extract_feature(data_):
	c_ = np.mean(data_, axis=0)
	single_feature_ = []
	pc=[d for d in data_]
	c = resetShapePosition(pc)

	if c_.all() != np.array(c).all():
		print('Something wrong with finding Central Point')
	
	for i in [0,1,2]: # all the orthogonal projections
		signal=getProjectionSignal(pc,i)
		vals = [s[1] for s in signal]
		mu=np.float32(sum(vals))/len(vals)
		single_feature_.append(mu)
		single_feature_.append(np.float32(sum([pow(v-mu,2) for v in vals]))/len(vals))
	
	return single_feature_


# def extract_feature_batch(data_list_):
# 	batch_feature_ = []
# 	for i in range(len(data_list_)):
# 		batch_feature_.append(extract_feature(data_list_[i]))
# 	return batch_feature_


# def save_feature_batch(feature_, save_dir_):
# 	f = open(save_dir_, 'w+')
# 	for feat in feature_:
# 		for i in range(6):
# 			f.write('%f '%feat[i])
# 		f.write('\n')
# 	f.close()


if __name__ == "__main__":
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument('--dataset_type', default='ycb', help='Dataset type [shapes/ycb/mechnet/normalized]')
# 	parser.add_argument('--dataset_name', default='ycb_28_similar_SP20_BIAS5_norm', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
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

		TRAIN_DATA = np.load(os.path.join(TRAIN_DIR, 'data_aligned.npy'))
		TEST_DATA = np.load(os.path.join(TEST_DIR, 'data_aligned.npy'))

		feature_all = []
		for d in TRAIN_DATA:
			feature_all.append(extract_feature(d))
		np.savetxt(os.path.join(TRAIN_DIR, 'feature.dat'), np.array(feature_all), fmt='%.6f')

		feature_all = []
		for d in TEST_DATA:
			feature_all.append(extract_feature(d))
		np.savetxt(os.path.join(TEST_DIR, 'feature.dat'), np.array(feature_all), fmt='%.6f')

		print('Finish feature extraction with dataset: '+DATASET_NAME)





