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
parser.add_argument('--dataset_dir', default='mechnet_stl', help='Dataset type [shapes/ycb/mechnet/normalized]')
parser.add_argument('--filelist', default='filelist_blade', help='filelist [filelist/filelist_clear]')
FLAGS = parser.parse_args()

FILELIST = FLAGS.filelist
DATASET_DIR = FLAGS.dataset_dir

DATA_DIR = os.path.join(PROJECT_DIR, 'data')
DATA_DIR = os.path.join(DATA_DIR, DATASET_DIR)

SAVE_DIR = os.path.join('/tmp/', 'stl_combination')
SAVE_DIR = os.path.join(SAVE_DIR, DATASET_DIR)
if not os.path.exists(SAVE_DIR): os.makedirs(SAVE_DIR)



if __name__=="__main__":
	
	stl_name = get_objectlist(DATA_DIR, FILELIST)
	print(stl_name)
	SAVE_DIR = os.path.join(SAVE_DIR, stl_name[0][:-2]+".stl")

	stl_file = []
	stl_dir = get_filelist(DATA_DIR, FILELIST)
	combined = mesh.Mesh.from_file(stl_dir[0]).data
	for i in range(1,len(stl_dir)):
		combined=np.concatenate([combined.data, mesh.Mesh.from_file(stl_dir[i]).data])
	combined_mesh = mesh.Mesh(combined)
	combined_mesh.save(SAVE_DIR, mode=stl.Mode.ASCII)  # save as ASCII

	

