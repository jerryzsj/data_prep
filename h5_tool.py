""" Utility functions for data preperation.
	Providing simple function tools:
		get_ply_length()
		ply_to_numpy()

Author: Senjing Zheng
Date: September 2018
"""

import os
import sys
import numpy as np
import h5py

# Customized dir


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.dirname(BASE_DIR))
import provider

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, '../utils'))

#sys.path.append(os.path.join(BASE_DIR, '../third_party/mech_mesh/'))
from plyfile import PlyData, PlyElement
from eulerangles import euler2mat
import data_prep_util
import pc_util as pcu

from PIL import Image



def get_ply_length():
	""" Get the length of all ply data, return part length in np array, and total length in int """
	""" The filenames and directory were predifined in global values """
	a_part_length = np.zeros(len(filenames), dtype=np.uint32)
	a_total_length = 0
	#print('Geting the length of ply file ...')
	for i in range(0, len(filenames)):
		plydata = PlyData.read(DATA_DIR + filenames[i] + '.ply')
		a_part_length[i] = plydata.elements[0].count
		a_total_length += plydata.elements[0].count
	return(a_part_length, a_total_length)


def ply_to_numpy():
	""" Get all the points from ply file and save in numpy array form but in one row """
	""" The filenames and directory were predifined in global values """
	""" Return the numpy arrays a_data, a_label, and a_pid """
	a_part_length = np.zeros(len(filenames), dtype=np.uint32)
	a_total_length = 0
	a_part_length, a_total_length = get_ply_length()

	a_data = np.zeros((1, a_total_length, 3))
	a_label	= np.zeros((1, 1))
	a_pid = np.zeros((1, a_total_length))
	
	print('Converting ply file to numpy array ...')
	print('Have totally {} points to convert'.format(a_total_length))
	
	k = 0
	a_label[0] = 1
	for i in range(0, len(filenames)):
		plydata = PlyData.read(DATA_DIR + filenames[i] + '.ply')
		
		g = int(np.copy(a_part_length[i]))
		for j in range(0, g):
			a_pid[0, k] = i
			a_data[0, k] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
			k += 1
	print('Finish ply to numpy converting!')
	return(a_data, a_label, a_pid)




def ply_to_h5(h5_name, sampling, ply_dir, ply_filelist, ply_lablelist):
	""" utility for converting ply to h5 file """
	""" ply_file_list : file name of file list: "filelist2.txt". """
	DATA_DIR = os.path.join(BASE_DIR, ply_dir)

	f = h5py.File(h5_name, 'w')
 
	filenames = [line.rstrip() for line in open( DATA_DIR  + "/" +ply_filelist, 'r')]
	labelnames = [line.rstrip() for line in open( DATA_DIR  + "/" +ply_lablelist, 'r')]

	print(len(filenames))
	a_data = np.zeros((len(filenames), sampling, 3))
	a_label	= np.zeros((len(filenames), 1))

	print('Converting ply file to h5 file ...')
	for i in range(0, len(filenames)):
		plydata = PlyData.read(DATA_DIR + "/" + filenames[i] + '.ply')
		a_label[i] = labelnames[i]
		for j in range(0, sampling):
			a_data[i, j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
				
	data = f.create_dataset("data", data = a_data, dtype= 'float32')
	label = f.create_dataset("label", data = a_label, dtype= 'uint8')

	print('Finish ply to h5 Converting!')
	print('File saved in ' + h5_name)

	print(data)



def ply_to_h5_pid(h5_dir, h5_name, sampling, ply_dir, ply_filelist, ply_lablelist):
	""" utility for converting ply to h5 file with part id """

	DATA_DIR = os.path.join(BASE_DIR, ply_dir)
	H5_DIR = os.path.join(BASE_DIR, h5_dir)

	H5_FILE = os.path.join(H5_DIR, h5_name)

	f = h5py.File(H5_FILE, 'w')

	filenames = [line.rstrip() for line in open( DATA_DIR  + "/" +ply_filelist, 'r')]
	labelnames = [line.rstrip() for line in open( DATA_DIR  + "/" +ply_lablelist, 'r')]

	#init the numpy array a_data, a_label, a_pid 
	a_data = np.zeros((len(filenames), sampling, 3))
	a_label	= np.zeros((len(filenames), 1))
	a_pid = np.zeros((len(filenames), sampling))

	print('Converting ply file to h5 file ...')
	for i in range(0, len(filenames)):
		plydata = PlyData.read(DATA_DIR + "/" + filenames[i] + '.ply')
		a_label[i] = labelnames[i]
		for j in range(0, sampling):
			a_data[i, j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
			a_pid[i, j] = int(filenames[i]) - 1

	data = f.create_dataset("data", data = a_data, dtype= 'float32')
	label = f.create_dataset("label", data = a_label, dtype= 'uint8')
	pid = f.create_dataset("pid", data = a_pid, dtype = 'uint8')

	print('Finish ply to h5 Converting!')
	print('File saved in ' + h5_name)

	print(data)


import hashlib
def h5_sampling(h5_dir, input_h5_name, output_h5_name, sampling_h5_group, sampling_data_len):
	""" Gathering parts to assemly and shuffling """
	print('Gathering parts h5 file to assemly and shuffling ...')

	H5_DIR = os.path.join(BASE_DIR, h5_dir)
	IN_H5_FILE = os.path.join(H5_DIR, input_h5_name)
	OUT_H5_FILE =os.path.join(H5_DIR, output_h5_name)

	cur_data, cur_labels, cur_seg = provider.loadDataFile_with_seg(IN_H5_FILE)
	
	f = h5py.File(OUT_H5_FILE, 'w')

	m = hashlib.md5()
	m.update("md5_name")
	
	H5_GROUP = len (cur_labels)
	SAMPLE_LEN = sampling_data_len
	SAMPLE_GROUP = sampling_h5_group
	DATA_LENGTH = SAMPLE_LEN * SAMPLE_GROUP
	OUTPUT_LEN = H5_GROUP * SAMPLE_LEN
	


	a_data = np.zeros((SAMPLE_GROUP, OUTPUT_LEN, 3))
	a_label	= np.zeros((SAMPLE_GROUP, 1))
	a_pid = np.zeros((SAMPLE_GROUP, OUTPUT_LEN))

	b_data = np.zeros((SAMPLE_GROUP, OUTPUT_LEN, 3))
	b_label	= np.zeros((SAMPLE_GROUP, 1))
	b_pid = np.zeros((SAMPLE_GROUP, OUTPUT_LEN))
	
	a_shuffle = np.arange(DATA_LENGTH)
	b_shuffle = np.arange(OUTPUT_LEN)

	np.random.shuffle(a_shuffle)
	np.random.shuffle(b_shuffle)

	for i in range (0, SAMPLE_GROUP):
		
		for j in range (0, H5_GROUP):
			a_label[i] = cur_labels[j]
			for k in range (0, SAMPLE_LEN):
				temp_sample_y = a_shuffle[SAMPLE_LEN * i + k]
				a_data[i, (j * SAMPLE_LEN) + k] = cur_data[j, temp_sample_y]
				a_pid[i, (j * SAMPLE_LEN) + k] = cur_seg[j, temp_sample_y] + 1

	for i in range (0, SAMPLE_GROUP):
		np.random.shuffle(b_shuffle)
		a_idx = np.random.randint(OUTPUT_LEN, size = OUTPUT_LEN)
		b_data[i, :, :] = a_data[i, b_shuffle, :]
		b_pid[i, :] = a_pid[i, b_shuffle]

	data = f.create_dataset("data", data = b_data, dtype= 'float32')
	label = f.create_dataset("label", data = a_label, dtype= 'uint8')
	pid = f.create_dataset("pid", data = b_pid, dtype = 'uint8')
	print('Finish part h5 file sampling!')
	print('File saved in ' + output_h5_name)
	print(data)




def h5_to_annnotation(h5_dir, h5_name, sampling):
	""" converting h5 file to annotation seg & pts """
	print('Converting file ' + h5_name + ' for testing (PartAnnotation files .seg & .pts)')

	DATA_DIR = os.path.join(BASE_DIR, h5_dir)
	H5_FILE = os.path.join(DATA_DIR, h5_name)

	cur_data, cur_labels, cur_seg = provider.loadDataFile_with_seg(H5_FILE)

	DATA_LENGTH = sampling
	DATA_NUMBER = len (cur_labels)

	m = hashlib.md5()
	m.update("md5_name")

	for i in range (0, DATA_NUMBER):

		m.update(cur_labels[i])
		SEG_FILE = (m.hexdigest() + '.seg')
		PTS_FILE = (m.hexdigest() + '.pts')

		SEG_DIR = os.path.join(DATA_DIR, SEG_FILE)
		PTS_DIR = os.path.join(DATA_DIR, PTS_FILE)

		f_seg = open(SEG_DIR, 'a+')
		f_pts = open(PTS_DIR, 'a+')

		np.savetxt(SEG_DIR, cur_seg[i], fmt='%d', delimiter=" ", newline='\n')
		np.savetxt(PTS_DIR, cur_data[i], fmt='%f', delimiter=" ", newline='\n')

	SEG_FILE = (m.hexdigest() + '.seg')
	PTS_FILE = (m.hexdigest() + '.pts')

	print('Finish annotation file converting!')
	print('File saved in ' + DATA_DIR)
