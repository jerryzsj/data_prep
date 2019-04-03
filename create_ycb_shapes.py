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

sys.path.append(os.path.join(BASE_DIR, 'primitive_shapes_generator'))
import primitive_shapes_generator as psg

DATA_DIR = os.path.join(BASE_DIR, 'data')
TEMP_DIR = os.path.join('/tmp/', 'temp')

parser = argparse.ArgumentParser()
parser.add_argument('--min_len', type=float, default='0.04', help='')
parser.add_argument('--max_len', type=float, default='0.4', help='')
parser.add_argument('--num_points', type=int, default='1000', help='')
parser.add_argument('--num_samples', type=int, default='200', help='')
parser.add_argument('--ycb', default='True', help='')
parser.add_argument('--box_shapes', default='box_shapes.npy', help='')
parser.add_argument('--cyl_shapes', default='cyl_shapes.npy', help='')
parser.add_argument('--sph_shapes', default='sph_shapes.npy', help='')

FLAGS = parser.parse_args()

if FLAGS.ycb == 'False':
	TEMP_DIR = os.path.join(TEMP_DIR, str(FLAGS.min_len)+'to'+str(FLAGS.max_len))
	if not os.path.exists(TEMP_DIR): os.makedirs(TEMP_DIR)

if FLAGS.ycb == 'True':
	TEMP_DIR = os.path.join(TEMP_DIR, 'shapes_ycb')
	if os.path.exists(TEMP_DIR): shutil.rmtree(TEMP_DIR, ignore_errors=True)
	if not os.path.exists(TEMP_DIR): os.makedirs(TEMP_DIR)
	BOX_SHAPES = np.load(FLAGS.box_shapes)
	CYL_SHAPES = np.load(FLAGS.cyl_shapes)
	SPH_SHAPES = np.load(FLAGS.sph_shapes)



def create_spheres(idx, diameter_train, diameter_test, n_points=1000):
	radius_train = diameter_train/2.0
	radius_test = diameter_test/2.0
	train_dir = os.path.join(TEMP_DIR, 'clean/sphere')
	test_dir = os.path.join(TEMP_DIR, 'test/clean/sphere')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)
	filelist_train = open(train_dir+'/filelist','a')
	filelist_test = open(test_dir+'/filelist','a')
	
	scene = psg.Sphere(n_points, radius_train)
	scene.save(train_dir + "/" + str(idx) + ".pcd")
	filelist_train.write(str(idx)+".pcd\n")
	
	scene = psg.Sphere(n_points, radius_test)
	scene.save(test_dir + "/" + str(idx) + ".pcd")
	filelist_test.write(str(idx)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_partial_spheres(idx, diameter_train, diameter_test, n_points=1000, partial_rate=0.5):
	radius_train = diameter_train/2.0
	radius_test = diameter_test/2.0
	train_dir = os.path.join(TEMP_DIR, 'partial/sphere')
	test_dir = os.path.join(TEMP_DIR, 'test/partial/sphere')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)
	filelist_train = open(train_dir+'/filelist','a')
	filelist_test = open(test_dir+'/filelist','a')

	partial_ = nr.random()*partial_rate
	scene = psg.Sphere(n_points, radius_train)
	scene.remove_part(partial_)
	scene.save(train_dir + "/" + str(idx) + ".pcd")
	filelist_train.write(str(idx)+".pcd\n")
	
	partial_ = nr.random()*partial_rate
	scene = psg.Sphere(n_points, radius_test)
	scene.remove_part(partial_)
	scene.save(test_dir + "/" + str(idx) + ".pcd")
	filelist_test.write(str(idx)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()



def create_error_spheres(idx, diameter_train, diameter_test, n_points=1000, error_percentage=0.1):
	radius_train = diameter_train/2.0
	radius_test = diameter_test/2.0
	train_dir = os.path.join(TEMP_DIR, 'error/sphere')
	test_dir = os.path.join(TEMP_DIR, 'test/error/sphere')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)
	filelist_train = open(train_dir+'/filelist','a')
	filelist_test = open(test_dir+'/filelist','a')
	
	scene = psg.Sphere(n_points, radius_train)
	scene.set_error(error_percentage)
	scene.save(train_dir + "/" + str(idx) + ".pcd")
	filelist_train.write(str(idx)+".pcd\n")
	
	scene = psg.Sphere(n_points, radius_test)
	scene.set_error(error_percentage)
	scene.save(test_dir + "/" + str(idx) + ".pcd")
	filelist_test.write(str(idx)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()



def create_error_partial_spheres(idx, diameter_train, diameter_test, n_points=1000, partial_rate = 0.5, error_percentage=0.1):
	radius_train = diameter_train/2.0
	radius_test = diameter_test/2.0
	train_dir = os.path.join(TEMP_DIR, 'error_partial/sphere')
	test_dir = os.path.join(TEMP_DIR, 'test/error_partial/sphere')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)
	filelist_train = open(train_dir+'/filelist','a')
	filelist_test = open(test_dir+'/filelist','a')
	
	partial_ = nr.random()*partial_rate
	scene = psg.Sphere(n_points, radius_train)
	scene.remove_part(partial_)
	scene.set_error(error_percentage)
	scene.save(train_dir + "/" + str(idx) + ".pcd")
	filelist_train.write(str(idx)+".pcd\n")
	
	partial_ = nr.random()*partial_rate
	scene = psg.Sphere(n_points, radius_test)
	scene.remove_part(partial_)
	scene.set_error(error_percentage)
	scene.save(test_dir + "/" + str(idx) + ".pcd")
	filelist_test.write(str(idx)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()



def create_boxes(idx,l_train, w_train, h_train, l_test, w_test, h_test, n_points=1000):
	train_dir = os.path.join(TEMP_DIR, 'clean/box')
	test_dir = os.path.join(TEMP_DIR, 'test/clean/box')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','a')
	filelist_test = open(test_dir+'/filelist','a')
	
	scene = psg.Box(n_points, l_train, w_train, h_train)
	scene.rotate()
	scene.save(train_dir + "/" + str(idx) + ".pcd")
	filelist_train.write(str(idx)+".pcd\n")

	scene = psg.Box(n_points, l_test, w_test, h_test)
	scene.rotate()
	scene.save(test_dir + "/" + str(idx) + ".pcd")
	filelist_test.write(str(idx)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_partial_boxes(idx,l_train, w_train, h_train, l_test, w_test, h_test, n_points=1000, partial_rate=0.5):
	train_dir = os.path.join(TEMP_DIR, 'partial/box')
	test_dir = os.path.join(TEMP_DIR, 'test/partial/box')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','a')
	filelist_test = open(test_dir+'/filelist','a')
	
	scene = psg.Box(n_points, l_train, w_train, h_train)
	scene.rotate()
	partial_ = nr.random()*partial_rate
	scene.remove_part(partial_)
	scene.save(train_dir + "/" + str(idx) + ".pcd")
	filelist_train.write(str(idx)+".pcd\n")

	scene = psg.Box(n_points, l_test, w_test, h_test)
	scene.rotate()
	partial_ = nr.random()*partial_rate
	scene.remove_part(partial_)
	scene.save(test_dir + "/" + str(idx) + ".pcd")
	filelist_test.write(str(idx)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_error_boxes(idx,l_train, w_train, h_train, l_test, w_test, h_test, n_points=1000, error_percentage=0.1):
	train_dir = os.path.join(TEMP_DIR, 'error/box')
	test_dir = os.path.join(TEMP_DIR, 'test/error/box')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','a')
	filelist_test = open(test_dir+'/filelist','a')
	
	scene = psg.Box(n_points, l_train, w_train, h_train)
	scene.rotate()
	scene.set_error(error_percentage)
	# partial_ = nr.random()*partial_rate
	# scene.remove_part(partial_)
	scene.save(train_dir + "/" + str(idx) + ".pcd")
	filelist_train.write(str(idx)+".pcd\n")

	scene = psg.Box(n_points, l_test, w_test, h_test)
	scene.rotate()
	scene.set_error(error_percentage)
	# partial_ = nr.random()*partial_rate
	# scene.remove_part(partial_)
	scene.save(test_dir + "/" + str(idx) + ".pcd")
	filelist_test.write(str(idx)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_error_partial_boxes(idx,l_train, w_train, h_train, l_test, w_test, h_test, n_points=1000, partial_rate=0.5, error_percentage=0.1):
	train_dir = os.path.join(TEMP_DIR, 'error_partial/box')
	test_dir = os.path.join(TEMP_DIR, 'test/error_partial/box')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','a')
	filelist_test = open(test_dir+'/filelist','a')
	
	scene = psg.Box(n_points, l_train, w_train, h_train)
	scene.rotate()
	partial_ = nr.random()*partial_rate
	scene.remove_part(partial_)
	scene.set_error(error_percentage)
	scene.save(train_dir + "/" + str(idx) + ".pcd")
	filelist_train.write(str(idx)+".pcd\n")

	scene = psg.Box(n_points, l_test, w_test, h_test)
	scene.rotate()
	partial_ = nr.random()*partial_rate
	scene.remove_part(partial_)
	scene.set_error(error_percentage)
	scene.save(test_dir + "/" + str(idx) + ".pcd")
	filelist_test.write(str(idx)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_cylinders(idx, diameter_train, height_train, diameter_test, height_test, n_points=1000):
	radius_train = diameter_train/2.0
	radius_test = diameter_test/2.0

	train_dir = os.path.join(TEMP_DIR, 'clean/cylinder')
	test_dir = os.path.join(TEMP_DIR, 'test/clean/cylinder')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','a')
	filelist_test = open(test_dir+'/filelist','a')
	
	scene = psg.Cylinder(n_points, height_train, radius_train)
	scene.rotate()
	scene.save(train_dir + "/" + str(idx) + ".pcd")
	filelist_train.write(str(idx)+".pcd\n")

	scene = psg.Cylinder(n_points, height_test, radius_test)
	scene.rotate()
	scene.save(test_dir + "/" + str(idx) + ".pcd")
	filelist_test.write(str(idx)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_partial_cylinders(idx, diameter_train, height_train, diameter_test, height_test, n_points=1000, partial_rate=0.5):
	train_dir = os.path.join(TEMP_DIR, 'partial/cylinder')
	test_dir = os.path.join(TEMP_DIR, 'test/partial/cylinder')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','a')
	filelist_test = open(test_dir+'/filelist','a')
	
	radius_train = diameter_train/2.0
	radius_test = diameter_test/2.0

	scene = psg.Cylinder(n_points, height_train, radius_train)
	scene.rotate()
	partial_ = nr.random()*partial_rate
	scene.remove_part(partial_)
	scene.save(train_dir + "/" + str(idx) + ".pcd")
	filelist_train.write(str(idx)+".pcd\n")

	scene = psg.Cylinder(n_points, height_test, radius_test)
	scene.rotate()
	partial_ = nr.random()*partial_rate
	scene.remove_part(partial_)
	scene.save(test_dir + "/" + str(idx) + ".pcd")
	filelist_test.write(str(idx)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()

	

def create_error_cylinders(idx, diameter_train, height_train, diameter_test, height_test, n_points=1000, error_percentage=0.1):  # radius = length / 2
	train_dir = os.path.join(TEMP_DIR, 'error/cylinder')
	test_dir = os.path.join(TEMP_DIR, 'test/error/cylinder')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','a')
	filelist_test = open(test_dir+'/filelist','a')
	
	radius_train = diameter_train/2.0
	radius_test = diameter_test/2.0

	scene = psg.Cylinder(n_points, height_train, radius_train)
	scene.rotate()
	# partial_ = nr.random()*partial_rate
	# scene.remove_part(partial_)
	scene.set_error(error_percentage)
	scene.save(train_dir + "/" + str(idx) + ".pcd")
	filelist_train.write(str(idx)+".pcd\n")

	scene = psg.Cylinder(n_points, height_test, radius_test)
	scene.rotate()
	# partial_ = nr.random()*partial_rate
	# scene.remove_part(partial_)
	scene.set_error(error_percentage)
	scene.save(test_dir + "/" + str(idx) + ".pcd")
	filelist_test.write(str(idx)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_error_partial_cylinders(idx, diameter_train, height_train, diameter_test, height_test, n_points=1000, partial_rate=0.5, error_percentage=0.1):  # radius = length / 2
	train_dir = os.path.join(TEMP_DIR, 'error_partial/cylinder')
	test_dir = os.path.join(TEMP_DIR, 'test/error_partial/cylinder')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','a')
	filelist_test = open(test_dir+'/filelist','a')
	
	radius_train = diameter_train/2.0
	radius_test = diameter_test/2.0

	scene = psg.Cylinder(n_points, height_train, radius_train)
	scene.rotate()
	partial_ = nr.random()*partial_rate
	scene.remove_part(partial_)
	scene.set_error(error_percentage)
	scene.save(train_dir + "/" + str(idx) + ".pcd")
	filelist_train.write(str(idx)+".pcd\n")

	scene = psg.Cylinder(n_points, height_test, radius_test)
	scene.rotate()
	partial_ = nr.random()*partial_rate
	scene.remove_part(partial_)
	scene.set_error(error_percentage)
	scene.save(test_dir + "/" + str(idx) + ".pcd")
	filelist_test.write(str(idx)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_ycb_shapes(num_points=2000, num_samples=20, bias=0.2, error_percentage=0.09):

	for i in range(BOX_SHAPES.shape[0]):
		for j in range(num_samples):
			l_train = (1+bias-(nr.random()*(bias*2)))*BOX_SHAPES[i,0]
			w_train = (1+bias-(nr.random()*(bias*2)))*BOX_SHAPES[i,1]
			h_train = (1+bias-(nr.random()*(bias*2)))*BOX_SHAPES[i,2]
			l_test = (1+bias-(nr.random()*(bias*2)))*BOX_SHAPES[i,0]
			w_test = (1+bias-(nr.random()*(bias*2)))*BOX_SHAPES[i,1]
			h_test = (1+bias-(nr.random()*(bias*2)))*BOX_SHAPES[i,2]
			# create_boxes(j+i*num_samples, l_train, w_train, h_train, l_test, w_test, h_test, num_points)
			create_error_boxes(j+i*num_samples, l_train, w_train, h_train, l_test, w_test, h_test, num_points, error_percentage)
			# create_partial_boxes(j+i*num_samples, l_train, w_train, h_train, l_test, w_test, h_test, num_points)
			# create_error_partial_boxes(j+i*num_samples, l_train, w_train, h_train, l_test, w_test, h_test, num_points)

	for i in range(CYL_SHAPES.shape[0]):
		for j in range(num_samples):
			d_train = (1+bias-(nr.random()*(bias*2)))*CYL_SHAPES[i,0]
			h_train = (1+bias-(nr.random()*(bias*2)))*CYL_SHAPES[i,1]
			d_test = (1+bias-(nr.random()*(bias*2)))*CYL_SHAPES[i,0]
			h_test = (1+bias-(nr.random()*(bias*2)))*CYL_SHAPES[i,1]
			# create_cylinders(j+i*num_samples, d_train, h_train, d_test, h_test, num_points)
			create_error_cylinders(j+i*num_samples, d_train, h_train, d_test, h_test, num_points, error_percentage)
			# create_partial_cylinders(j+i*num_samples, d_train, h_train, d_test, h_test, num_points)
			# create_error_partial_cylinders(j+i*num_samples, d_train, h_train, d_test, h_test, num_points)

	for i in range(SPH_SHAPES.shape[0]):
		for j in range(num_samples):
			d_train = (1+bias-(nr.random()*(bias*2)))*SPH_SHAPES[i]
			d_test = (1+bias-(nr.random()*(bias*2)))*SPH_SHAPES[i]
			# create_spheres(j+i*num_samples, d_train, d_test, num_points)
			create_error_spheres(j+i*num_samples, d_train, d_test, num_points, error_percentage)
			# create_partial_spheres(j+i*num_samples, d_train, d_test, num_points)
			# create_error_partial_spheres(j+i*num_samples, d_train, d_test, num_points)


	# create_spheres(num_points, min_size, max_size, num_samples)
	
	# create_cylinders(num_points, min_size, max_size, num_samples)

	# create_error_spheres(num_points, min_size, max_size, num_samples)
	
	# create_error_cylinders(num_points, min_size, max_size, num_samples)

	# create_partial_spheres(num_points, min_size, max_size, num_samples)
	
	# create_partial_cylinders(num_points, min_size, max_size, num_samples)

	# create_error_partial_spheres(num_points, min_size, max_size, num_samples)
	
	# create_error_partial_cylinders(num_points, min_size, max_size, num_samples)





if __name__ == "__main__":
	nr.seed()
	create_ycb_shapes()
	# create_shapes(FLAGS.num_points, FLAGS.min_len, FLAGS.max_len, FLAGS.num_samples)

	
