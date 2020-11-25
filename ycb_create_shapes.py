import os
import sys
import argparse
import numpy as np
# import open3d
import numpy.random as nr
import shutil
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)

sys.path.append(BASE_DIR)
# sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
# import pcio

import primitive_shapes_generator.primitive_shapes_generator as psg

DATA_DIR = os.path.join(BASE_DIR, 'data')
TEMP_DIR = '/tmp'

parser = argparse.ArgumentParser()
# parser.add_argument('--min_len', type=float, default='0.04', help='')
# parser.add_argument('--max_len', type=float, default='0.4', help='')
parser.add_argument('--num_points', type=int, default='1000', help='')
parser.add_argument('--num_samples', type=int, default='20', help='')
parser.add_argument('--shape_bias', type=int, default='8', help='')
parser.add_argument('--box_shapes', default='box_size_new.dat', help='')
parser.add_argument('--cyl_shapes', default='cylinder_size_new.dat', help='')
parser.add_argument('--sph_shapes', default='sphere_size_new.dat', help='')

FLAGS = parser.parse_args()

NUM_POINTS = FLAGS.num_points
NUM_SAMPLES = FLAGS.num_samples
SHAPE_BIAS = FLAGS.shape_bias / 100.0

DATA_DIR = os.path.join(DATA_DIR, 'ycb')
SAVE_DIR = os.path.join(TEMP_DIR, 'ycb_similar_SP'+str(FLAGS.num_samples)+'_BIAS'+str(FLAGS.shape_bias)+'_'+time.strftime("%Y-%m-%d",time.localtime(time.time())))
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


def create_ycb_shapes_random(num_points=1000, num_samples=200, shape_bias=0.2, error_percentage=0.0, partial_rate = 0.0):
	FILELIST_DIR = open(os.path.join(SAVE_DIR, 'filelist'), 'w+')
	
	#############################################################################################
	# Create box
	#############################################################################################
	FILELIST_DIR.write('box/\n')
	save_dir = os.path.join(SAVE_DIR, 'box')
	if not os.path.exists(save_dir): os.makedirs(save_dir)
	FILELIST_PCD = open(os.path.join(save_dir, 'filelist'), 'w+')
	BOX_SIZE = open(os.path.join(save_dir, 'box_size'), 'w+')

	for i in range(BOX_SHAPES.shape[0]):
		for j in range(num_samples):
			filename = str(i*num_samples+j)+'.pcd'
			file_save_dir = os.path.join(save_dir, filename)
			FILELIST_PCD.write(filename + '\n')
			
			L = ((1+shape_bias-(nr.random()*(shape_bias*2)))*BOX_SHAPES[i,0])
			W = ((1+shape_bias-(nr.random()*(shape_bias*2)))*BOX_SHAPES[i,1])
			H = ((1+shape_bias-(nr.random()*(shape_bias*2)))*BOX_SHAPES[i,2])
			create_box(save_dir=file_save_dir, L=L, W=W, H=H, num_points=num_points, error_percentage=0.0, partial_rate = 0.0)
			# print('L, W, H:', L, W, H)
			BOX_SIZE.write(str(round(L,4))+' '+str(round(W,4)) +' '+ str(round(H,4)) + '\n')
	
	#############################################################################################
	# Create cylinder
	#############################################################################################
	FILELIST_DIR.write('cylinder/\n')
	save_dir = os.path.join(SAVE_DIR, 'cylinder')
	if not os.path.exists(save_dir): os.makedirs(save_dir)
	FILELIST_PCD = open(os.path.join(save_dir, 'filelist'), 'w+')
	CYL_SIZE = open(os.path.join(save_dir, 'cylinder_size'), 'w+')

	for i in range(CYL_SHAPES.shape[0]):
		for j in range(num_samples):
			filename = str(i*num_samples+j)+'.pcd'
			file_save_dir = os.path.join(save_dir, filename)
			FILELIST_PCD.write(filename + '\n')
			
			D = (1+shape_bias-(nr.random()*(shape_bias*2)))*CYL_SHAPES[i,0]
			H = (1+shape_bias-(nr.random()*(shape_bias*2)))*CYL_SHAPES[i,1]
			create_cylinder(save_dir=file_save_dir, D=D, H=H, num_points=num_points, error_percentage=0.0, partial_rate = 0.0)
			# print('D, H:', D, H)
			CYL_SIZE.write(str(round(D,4))+' '+str(round(H,4)) + '\n')

	#############################################################################################
	# Create sphere
	#############################################################################################
	FILELIST_DIR.write('sphere/\n')
	save_dir = os.path.join(SAVE_DIR, 'sphere')
	if not os.path.exists(save_dir): os.makedirs(save_dir)
	FILELIST_PCD = open(os.path.join(save_dir, 'filelist'), 'w+')
	SPH_SIZE = open(os.path.join(save_dir, 'sphere_size'), 'w+')

	for i in range(SPH_SHAPES.shape[0]):
		for j in range(num_samples):
			filename = str(i*num_samples+j)+'.pcd'
			file_save_dir = os.path.join(save_dir, filename)
			FILELIST_PCD.write(filename + '\n')
			
			D = (1+shape_bias-(nr.random()*(shape_bias*2)))*SPH_SHAPES[i]
			create_sphere(save_dir=file_save_dir, D=D, num_points=num_points, error_percentage=0.0, partial_rate = 0.0)
			# print('D:', D)
			SPH_SIZE.write(str(round(D,4))+'\n')


if __name__ == "__main__":
	nr.seed()
	create_ycb_shapes_random(num_points=NUM_POINTS, num_samples=NUM_SAMPLES, shape_bias=SHAPE_BIAS)
	# create_shapes(FLAGS.num_points, FLAGS.min_len, FLAGS.max_len, FLAGS.num_samples)

	
