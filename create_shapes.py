import os
import sys
import numpy as np
import h5py
import open3d
import numpy.random as nr


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)

sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
import pcio

sys.path.append(os.path.join(BASE_DIR, 'primitive_shapes_generator'))
import primitive_shapes_generator as psg

DATA_DIR = os.path.join(BASE_DIR, 'data')
TEMP_DIR = os.path.join('/tmp/', 'temp')


def create_spheres(n_points, radius_min, radius_max, n_sphere):
	train_dir = os.path.join(TEMP_DIR, 'clean/sphere')
	test_dir = os.path.join(TEMP_DIR, 'test/clean/sphere')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)
	filelist_train = open(train_dir+'/filelist','w')
	filelist_test = open(test_dir+'/filelist','w')
	
	for i in range(n_sphere):
		radius_ = nr.random()*(radius_max - radius_min) + radius_min
		# print(radius_)
		scene = psg.Sphere(n_points, radius_)
		scene.save(train_dir + "/" + str(i) + ".pcd")
		filelist_train.write(str(i)+".pcd\n")

	for i in range(n_sphere):
		radius_ = nr.random()*(radius_max - radius_min) + radius_min
		# print(radius_)
		scene = psg.Sphere(n_points, radius_)
		scene.save(test_dir + "/" + str(i) + ".pcd")
		filelist_test.write(str(i)+".pcd\n")
	filelist_train.close()
	filelist_test.close()


def create_partial_spheres(n_points, radius_min, radius_max, n_sphere, partial_rate=0.5):
	train_dir = os.path.join(TEMP_DIR, 'partial/sphere')
	test_dir = os.path.join(TEMP_DIR, 'test/partial/sphere')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)
	filelist_train = open(train_dir+'/filelist','w')
	filelist_test = open(test_dir+'/filelist','w')
	
	for i in range(n_sphere):
		radius_ = nr.random()*(radius_max - radius_min) + radius_min
		partial_ = nr.random()*partial_rate
		
		scene = psg.Sphere(n_points, radius_)
		scene.remove_part(partial_)
		scene.save(train_dir + "/" + str(i) + ".pcd")
		filelist_train.write(str(i)+".pcd\n")

	for i in range(n_sphere):
		radius_ = nr.random()*(radius_max - radius_min) + radius_min
		partial_ = nr.random()*partial_rate
		# print(radius_)
		scene = psg.Sphere(n_points, radius_)
		scene.remove_part(partial_)
		scene.save(test_dir + "/" + str(i) + ".pcd")
		filelist_test.write(str(i)+".pcd\n")
	filelist_train.close()
	filelist_test.close()


def create_error_spheres(n_points, radius_min, radius_max, n_sphere, error_percentage=0.1):
	train_dir = os.path.join(TEMP_DIR, 'error/sphere')
	test_dir = os.path.join(TEMP_DIR, 'test/error/sphere')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)
	filelist_train = open(train_dir+'/filelist','w')
	filelist_test = open(test_dir+'/filelist','w')
	
	for i in range(n_sphere):
		radius_ = nr.random()*(radius_max - radius_min) + radius_min
		# print(radius_)
		scene = psg.Sphere(n_points, radius_)
		scene.add_error(error_percentage)
		scene.save(train_dir + "/" + str(i) + ".pcd")
		filelist_train.write(str(i)+".pcd\n")

	for i in range(n_sphere):
		radius_ = nr.random()*(radius_max - radius_min) + radius_min
		# print(radius_)
		scene = psg.Sphere(n_points, radius_)
		scene.add_error(error_percentage)
		scene.save(test_dir + "/" + str(i) + ".pcd")
		filelist_test.write(str(i)+".pcd\n")
	filelist_train.close()
	filelist_test.close()


def create_error_partial_spheres(n_points, radius_min, radius_max, n_sphere, partial_rate = 0.5, error_percentage=0.1):
	train_dir = os.path.join(TEMP_DIR, 'error_partial/sphere')
	test_dir = os.path.join(TEMP_DIR, 'test/error_partial/sphere')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)
	filelist_train = open(train_dir+'/filelist','w')
	filelist_test = open(test_dir+'/filelist','w')
	
	for i in range(n_sphere):
		radius_ = nr.random()*(radius_max - radius_min) + radius_min
		partial_ = nr.random()*partial_rate
		
		scene = psg.Sphere(n_points, radius_)
		scene.remove_part(partial_)
		scene.add_error(error_percentage)
		scene.save(train_dir + "/" + str(i) + ".pcd")
		filelist_train.write(str(i)+".pcd\n")

	for i in range(n_sphere):
		radius_ = nr.random()*(radius_max - radius_min) + radius_min
		partial_ = nr.random()*partial_rate
		
		scene = psg.Sphere(n_points, radius_)
		scene.remove_part(partial_)
		scene.add_error(error_percentage)
		scene.save(test_dir + "/" + str(i) + ".pcd")
		filelist_test.write(str(i)+".pcd\n")
	filelist_train.close()
	filelist_test.close()


def create_boxes(n_points, length_min, length_max, n_box):
	train_dir = os.path.join(TEMP_DIR, 'clean/box')
	test_dir = os.path.join(TEMP_DIR, 'test/clean/box')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','w')
	filelist_test = open(test_dir+'/filelist','w')
	
	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		width_ = nr.random()*(length_max - length_min) + length_min
		depth_ = nr.random()*(length_max - length_min) + length_min
		
		scene = psg.Box(n_points, height_, width_, depth_)
		scene.rotate()
		scene.save(train_dir + "/" + str(i) + ".pcd")
		
		filelist_train.write(str(i)+".pcd\n")

	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		width_ = nr.random()*(length_max - length_min) + length_min
		depth_ = nr.random()*(length_max - length_min) + length_min
		
		scene = psg.Box(n_points, height_, width_, depth_)
		scene.rotate()
		scene.save(test_dir + "/" + str(i) + ".pcd")
		
		filelist_test.write(str(i)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_partial_boxes(n_points, length_min, length_max, n_box, partial_rate=0.5):
	train_dir = os.path.join(TEMP_DIR, 'partial/box')
	test_dir = os.path.join(TEMP_DIR, 'test/partial/box')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','w')
	filelist_test = open(test_dir+'/filelist','w')
	
	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		width_ = nr.random()*(length_max - length_min) + length_min
		depth_ = nr.random()*(length_max - length_min) + length_min
		partial_ = nr.random()*partial_rate

		scene = psg.Box(n_points, height_, width_, depth_)
		scene.remove_part(partial_)
		scene.rotate()
		scene.save(train_dir + "/" + str(i) + ".pcd")
		
		filelist_train.write(str(i)+".pcd\n")

	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		width_ = nr.random()*(length_max - length_min) + length_min
		depth_ = nr.random()*(length_max - length_min) + length_min
		partial_ = nr.random()*partial_rate

		scene = psg.Box(n_points, height_, width_, depth_)
		scene.remove_part(partial_)
		scene.rotate()
		scene.save(test_dir + "/" + str(i) + ".pcd")
		
		filelist_test.write(str(i)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_error_boxes(n_points, length_min, length_max, n_box, error_percentage=0.1):
	train_dir = os.path.join(TEMP_DIR, 'error/box')
	test_dir = os.path.join(TEMP_DIR, 'test/error/box')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','w')
	filelist_test = open(test_dir+'/filelist','w')
	
	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		width_ = nr.random()*(length_max - length_min) + length_min
		depth_ = nr.random()*(length_max - length_min) + length_min
		
		scene = psg.Box(n_points, height_, width_, depth_)
		scene.rotate()
		scene.add_error(error_percentage)
		scene.save(train_dir + "/" + str(i) + ".pcd")
		
		filelist_train.write(str(i)+".pcd\n")

	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		width_ = nr.random()*(length_max - length_min) + length_min
		depth_ = nr.random()*(length_max - length_min) + length_min
		
		scene = psg.Box(n_points, height_, width_, depth_)
		scene.rotate()
		scene.add_error(error_percentage)
		scene.save(test_dir + "/" + str(i) + ".pcd")
		
		filelist_test.write(str(i)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_error_partial_boxes(n_points, length_min, length_max, n_box, partial_rate=0.5, error_percentage=0.1):
	train_dir = os.path.join(TEMP_DIR, 'error_partial/box')
	test_dir = os.path.join(TEMP_DIR, 'test/error_partial/box')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','w')
	filelist_test = open(test_dir+'/filelist','w')
	
	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		width_ = nr.random()*(length_max - length_min) + length_min
		depth_ = nr.random()*(length_max - length_min) + length_min
		
		partial_ = nr.random()*partial_rate

		scene = psg.Box(n_points, height_, width_, depth_)
		scene.remove_part(partial_)
		scene.rotate()
		scene.add_error(error_percentage)
		scene.save(train_dir + "/" + str(i) + ".pcd")
		
		filelist_train.write(str(i)+".pcd\n")

	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		width_ = nr.random()*(length_max - length_min) + length_min
		depth_ = nr.random()*(length_max - length_min) + length_min
		
		partial_ = nr.random()*partial_rate

		scene = psg.Box(n_points, height_, width_, depth_)
		scene.remove_part(partial_)
		scene.rotate()
		scene.add_error(error_percentage)
		scene.save(test_dir + "/" + str(i) + ".pcd")
		
		filelist_test.write(str(i)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_cylinders(n_points, length_min, length_max, n_box):  # radius = length / 2
	train_dir = os.path.join(TEMP_DIR, 'clean/cylinder')
	test_dir = os.path.join(TEMP_DIR, 'test/clean/cylinder')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','w')
	filelist_test = open(test_dir+'/filelist','w')
	
	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		radius_ = nr.random()*(length_max - length_min) + length_min
		
		scene = psg.Cylinder(n_points, height_, radius_)
		scene.rotate()
		scene.save(train_dir + "/" + str(i) + ".pcd")
		
		filelist_train.write(str(i)+".pcd\n")

	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		radius_ = nr.random()*(length_max - length_min) + length_min
		
		scene = psg.Cylinder(n_points, height_, radius_)
		scene.rotate()
		scene.save(test_dir + "/" + str(i) + ".pcd")
		
		filelist_test.write(str(i)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_partial_cylinders(n_points, length_min, length_max, n_box, partial_rate=0.5):  # radius = length / 2
	train_dir = os.path.join(TEMP_DIR, 'partial/cylinder')
	test_dir = os.path.join(TEMP_DIR, 'test/partial/cylinder')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','w')
	filelist_test = open(test_dir+'/filelist','w')
	
	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		radius_ = nr.random()*(length_max - length_min) + length_min
		partial_ = nr.random()*partial_rate
		scene = psg.Cylinder(n_points, height_, radius_)
		scene.remove_part(partial_)
		scene.rotate()
		scene.save(train_dir + "/" + str(i) + ".pcd")
		
		filelist_train.write(str(i)+".pcd\n")

	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		radius_ = nr.random()*(length_max - length_min) + length_min
		partial_ = nr.random()*partial_rate
		scene = psg.Cylinder(n_points, height_, radius_)
		scene.remove_part(partial_)
		scene.rotate()
		scene.save(test_dir + "/" + str(i) + ".pcd")
		
		filelist_test.write(str(i)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_error_cylinders(n_points, length_min, length_max, n_box, error_percentage=0.1):  # radius = length / 2
	train_dir = os.path.join(TEMP_DIR, 'error/cylinder')
	test_dir = os.path.join(TEMP_DIR, 'test/error/cylinder')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','w')
	filelist_test = open(test_dir+'/filelist','w')
	
	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		radius_ = nr.random()*(length_max - length_min) + length_min
		
		scene = psg.Cylinder(n_points, height_, radius_)
		scene.rotate()
		scene.add_error(error_percentage)
		scene.save(train_dir + "/" + str(i) + ".pcd")
		
		filelist_train.write(str(i)+".pcd\n")

	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		radius_ = nr.random()*(length_max - length_min) + length_min
		
		scene = psg.Cylinder(n_points, height_, radius_)
		scene.rotate()
		scene.add_error(error_percentage)
		scene.save(test_dir + "/" + str(i) + ".pcd")
		
		filelist_test.write(str(i)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()

def create_error_partial_cylinders(n_points, length_min, length_max, n_box, partial_rate=0.5, error_percentage=0.1):  # radius = length / 2
	train_dir = os.path.join(TEMP_DIR, 'error_partial/cylinder')
	test_dir = os.path.join(TEMP_DIR, 'test/error_partial/cylinder')
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)

	filelist_train = open(train_dir+'/filelist','w')
	filelist_test = open(test_dir+'/filelist','w')
	
	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		radius_ = nr.random()*(length_max - length_min) + length_min
		partial_ = nr.random()*partial_rate
		scene = psg.Cylinder(n_points, height_, radius_)
		scene.remove_part(partial_)
		scene.rotate()
		scene.add_error(error_percentage)
		scene.save(train_dir + "/" + str(i) + ".pcd")
		
		filelist_train.write(str(i)+".pcd\n")

	for i in range(n_box):
		height_ = nr.random()*(length_max - length_min) + length_min
		radius_ = nr.random()*(length_max - length_min) + length_min
		
		partial_ = nr.random()*partial_rate
		scene = psg.Cylinder(n_points, height_, radius_)
		scene.remove_part(partial_)
		scene.rotate()
		scene.add_error(error_percentage)
		scene.save(test_dir + "/" + str(i) + ".pcd")
		
		filelist_test.write(str(i)+".pcd\n")
	
	filelist_train.close()
	filelist_test.close()


def create_shapes():

	nr.seed()
	create_spheres(1000, 0.02, 0.2, 1000)
	create_boxes(1000, 0.04, 0.4, 1000)
	create_cylinders(1000, 0.04, 0.4, 1000)

	create_error_spheres(1000, 0.02, 0.2, 1000)
	create_error_boxes(1000, 0.04, 0.4, 1000)
	create_error_cylinders(1000, 0.04, 0.4, 1000)

	create_partial_spheres(1000, 0.02, 0.2, 1000)
	create_partial_boxes(1000, 0.04, 0.4, 1000)
	create_partial_cylinders(1000, 0.04, 0.4, 1000)

	create_error_partial_spheres(1000, 0.02, 0.2, 1000)
	create_error_partial_boxes(1000, 0.04, 0.4, 1000)
	create_error_partial_cylinders(1000, 0.04, 0.4, 1000)


if __name__ == "__main__":
	
	create_shapes()

	# height = 300
	# width = 120
	# depth = 120
	# scene = psg.Box(1000, height, width, depth)
	# for i in range (10):

	# 	scene.rotate()
	# 	scene.save(TEMP_DIR + "/test_box_" + str(i) + ".pcd")
