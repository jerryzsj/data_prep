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

if __name__ == "__main__":

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





