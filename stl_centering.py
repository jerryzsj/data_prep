import os
import sys
import numpy as np
import numpy.random as nr
import h5py
import open3d
import argparse
import math
import stl
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
parser.add_argument('--dataset_type', default='ycb', help='Dataset type [shapes/ycb/mechnet/normalized]')
parser.add_argument('--dataset_name', default='stl_files_measure_size')
parser.add_argument('--filelist', default='filelist', help='filelist [filelist/filelist_clear]')
FLAGS = parser.parse_args()

FILELIST = FLAGS.filelist
DATASET_TYPE = FLAGS.dataset_type
DATASET_NAME = FLAGS.dataset_name

DATA_DIR = os.path.join(PROJECT_DIR, 'data')
DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)
DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)

SAVE_DIR = os.path.join('/tmp/', 'stl_normalization')
SAVE_DIR = os.path.join(SAVE_DIR, DATASET_TYPE)
if not os.path.exists(SAVE_DIR): os.makedirs(SAVE_DIR)



if __name__=="__main__":
	
	stl_name = get_objectlist(DATA_DIR, FILELIST)
	stl_file = []
	stl_dir = get_filelist(DATA_DIR, FILELIST)
	for i in range(len(stl_name)):
		print('normalizing ',stl_name[i])
		save_dir = os.path.join(SAVE_DIR, stl_name[i]+".stl")
		orgin_data = mesh.Mesh.from_file(stl_dir[i]).data
	
		orgin_data['vectors'] += -(np.mean(orgin_data['vectors'], axis=0))
		
		orgin_data['vectors'] = orgin_data['vectors']*1000.0
		
		normed_mesh= mesh.Mesh(orgin_data)
		normed_mesh.save(save_dir, mode=stl.Mode.ASCII)  # save as ASCII
		
	

