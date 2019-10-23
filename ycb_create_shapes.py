import os
import sys
import argparse
import numpy as np
import h5py
import open3d
import numpy.random as nr
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)

sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
import pcio

import primitive_shapes_generator.primitive_shapes_generator as psg

DATA_DIR = os.path.join(BASE_DIR, 'data')
TEMP_DIR = '/tmp'

parser = argparse.ArgumentParser()
parser.add_argument('--min_len', type=float, default='0.04', help='')
parser.add_argument('--max_len', type=float, default='0.4', help='')
parser.add_argument('--num_points', type=int, default='1000', help='')
parser.add_argument('--num_samples', type=int, default='100', help='')
parser.add_argument('--box_shapes', default='box_shapes.txt', help='')
parser.add_argument('--cyl_shapes', default='cylinder_shapes.txt', help='')
parser.add_argument('--sph_shapes', default='sphere_shapes.txt', help='')

FLAGS = parser.parse_args()

NUM_SAMPLE = FLAGS.num_samples

DATA_DIR = os.path.join(DATA_DIR, 'ycb')
SAVE_DIR = os.path.join(TEMP_DIR, 'ycb_similar')
if not os.path.exists(SAVE_DIR): os.makedirs(SAVE_DIR)

# box shapes: L,W,H
BOX_SHAPES = np.loadtxt(os.path.join(DATA_DIR,FLAGS.box_shapes))
# cyl shapes: D,H
CYL_SHAPES = np.loadtxt(os.path.join(DATA_DIR,FLAGS.cyl_shapes))
# sph shapes: D
SPH_SHAPES = np.loadtxt(os.path.join(DATA_DIR,FLAGS.sph_shapes))


def create_box(save_dir, L, W, H, num_points=1000, error_percentage=0.0, partial_rate = 0.0):
	scene = psg.Box(num_points, L, W, H)
	if partial_rate != 0.0:
		scene.remove_part(partial_rate)
	if error_percentage != 0.0:
		scene.set_error(error_percentage)
	scene.rotate()
	scene.save(save_dir)

def create_cylinder(save_dir, D, H, num_points=1000, error_percentage=0.0, partial_rate = 0.0):
	scene = psg.Cylinder(num_points, H, D/2.0)
	if partial_rate != 0.0:
		scene.remove_part(partial_rate)
	if error_percentage != 0.0:
		scene.set_error(error_percentage)
	scene.rotate()
	scene.save(save_dir)

def create_sphere(save_dir, D, num_points=1000, error_percentage=0.0, partial_rate = 0.0):
	R = D/2.0
	scene = psg.Sphere(num_points, R)
	if partial_rate != 0.0:
		scene.remove_part(partial_rate)
	if error_percentage != 0.0:
		scene.set_error(error_percentage)
	scene.save(save_dir)


def create_ycb_shapes(num_points=1000, num_samples=200, shape_bias=0.2, error_percentage=0.0, partial_rate = 0.0):
	FILELIST_DIR = open(os.path.join(SAVE_DIR, 'filelist'), 'w+')
	
	FILELIST_DIR.write('box/\n')
	save_dir = os.path.join(SAVE_DIR, 'box')
	if not os.path.exists(save_dir): os.makedirs(save_dir)
	FILELIST_PCD = open(os.path.join(save_dir, 'filelist'), 'w+')
	
	for i in range(BOX_SHAPES.shape[0]):
		for j in range(num_samples):
			filename = str(i*num_samples+j)+'.pcd'
			file_save_dir = os.path.join(save_dir, filename)
			FILELIST_PCD.write(filename + '\n')
			
			L = (1+shape_bias-(nr.random()*(shape_bias*2)))*BOX_SHAPES[i,0]
			W = (1+shape_bias-(nr.random()*(shape_bias*2)))*BOX_SHAPES[i,1]
			H = (1+shape_bias-(nr.random()*(shape_bias*2)))*BOX_SHAPES[i,2]
			create_box(save_dir=file_save_dir, L=L, W=W, H=W, num_points=num_points, error_percentage=0.0, partial_rate = 0.0)

	FILELIST_DIR.write('cylinder/\n')
	save_dir = os.path.join(SAVE_DIR, 'cylinder')
	if not os.path.exists(save_dir): os.makedirs(save_dir)
	FILELIST_PCD = open(os.path.join(save_dir, 'filelist'), 'w+')
	
	for i in range(CYL_SHAPES.shape[0]):
		for j in range(num_samples):
			filename = str(i*num_samples+j)+'.pcd'
			file_save_dir = os.path.join(save_dir, filename)
			FILELIST_PCD.write(filename + '\n')
			
			D = (1+shape_bias-(nr.random()*(shape_bias*2)))*CYL_SHAPES[i,0]
			H = (1+shape_bias-(nr.random()*(shape_bias*2)))*CYL_SHAPES[i,1]
			create_cylinder(save_dir=file_save_dir, D=D, H=H, num_points=num_points, error_percentage=0.0, partial_rate = 0.0)
			
	FILELIST_DIR.write('sphere/\n')
	save_dir = os.path.join(SAVE_DIR, 'sphere')
	if not os.path.exists(save_dir): os.makedirs(save_dir)
	FILELIST_PCD = open(os.path.join(save_dir, 'filelist'), 'w+')
	for i in range(SPH_SHAPES.shape[0]):
		for j in range(num_samples):
			filename = str(i*num_samples+j)+'.pcd'
			file_save_dir = os.path.join(save_dir, filename)
			FILELIST_PCD.write(filename + '\n')
			
			D = (1+shape_bias-(nr.random()*(shape_bias*2)))*SPH_SHAPES[i]
			create_sphere(save_dir=file_save_dir, D=D, num_points=num_points, error_percentage=0.0, partial_rate = 0.0)


if __name__ == "__main__":
	nr.seed()
	create_ycb_shapes(num_samples=NUM_SAMPLE)
	# create_shapes(FLAGS.num_points, FLAGS.min_len, FLAGS.max_len, FLAGS.num_samples)

	
