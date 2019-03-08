## utils for numpy

##Contributor: Senjing Zheng
#Email: jerryzsj@icloud.com
#Date: 29 Nov 2018

##Latest modified by: Senjing Zheng
#Email: jerryzsj@icloud.com
#Date: 29 Nov 2018


import numpy as np
import math




def get_normal(v1, v2):
	return np.cross(v1, v2)


def get_surface(v1, v2):
	return get_normal(v1, v2)


## functions for points
def get_point(x, y, z):
	return np.array([x, y, z], dtype=np.float32)

def get_expand_point(point):
	return np.array([point[0], point[1], point[2], 1], dtype=np.float32)

def get_shrink_point(point):
	return np.array([point[0], point[1], point[2]], dtype=np.float32)


## functions for vectors
def get_vector(v1, v2):
	return np.float32(v2-v1)

def get_homo_vector(vector):
	return np.array([vector[0]/vector[2], vector[1]/vector[2], 1], dtype=np.float32)

def get_expand_vector(vector):
	return np.array([vector[0], vector[1], vector[2], 1], dtype=np.float32)

def get_shrink_vector(vector):
	return np.array([vector[0], vector[1], vector[2]], dtype=np.float32)

def get_unit_vector(vector):
	return vector/np.linalg.norm(vector)


## functions for matrices
def get_homo_matrix(matrix):
	matrix = np.array([matrix[0,:], matrix[1,:], matrix[2,:], [0,0,0]])
	matrix = np.hstack((matrix, np.array([[0],[0],[0],[1]])))
	return matrix

def get_shrink_matrix(matrix):
	matrix = np.array([matrix[0,:3], matrix[1,:3], matrix[2,:3]])
	return matrix


## functions for angle
def degree_to_radian(degree):
	radian = degree/90*np.pi/2
	return radian

def radian_to_degree(radian):
	degree = radian * 180.0 /math.pi
	return np.float16(degree)

def d_sin(degree):
	if (degree%180==0):
		return 0
	else:
		return(np.sin(degree_to_radian(degree)))

def d_cos(degree):
	if ((degree+90)%180==0):
		return 0
	else:
		return(np.cos(degree_to_radian(degree)))


## Calculate rotation matrix
# input degree for rotating in axis-z, then in axis-x, and finally axis-y
def cal_rotation_matrix_zxy(o_z=0, o_x=0, o_y=0):
	
	s_z = d_sin(o_z)
	c_z = d_cos(o_z)
	r_z = np.array([[c_z, -s_z, 0], [s_z, c_z, 0], [0,0,1]])

	s_x = d_sin(o_x)
	c_x = d_cos(o_x)
	r_x = np.array([[1, 0, 0], [0, c_x, -s_x], [0, s_x, c_x]])

	s_y = d_sin(o_y)
	c_y = d_cos(o_y)
	r_y = np.array([[c_y, 0, s_y], [0, 1, 0], [-s_y, 0, c_y]])

	r_matrix = r_z.dot(r_x).dot(r_y)
	return r_matrix

def get_rotation_matrix_zxy(o_z=0, o_x=0, o_y=0):
	r_matrix = cal_rotation_matrix_zxy(o_z, o_x, o_y)
	return r_matrix

