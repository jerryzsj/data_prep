import numpy as np
import argparse
import time
import os
import sys
from statistics import mean, median
import matplotlib.pyplot as plt


def plot_genome_disb(data, num_class=3, num_data=200, num_batch=20, batch_size=10, num_pixel=10, save_dir=None):
	stack_data = []

	for d in data:
		
		epoch_data = np.zeros(num_class)
		
		for i in range(num_class):

			epoch_data[i] += np.sum(d[(i*num_data): ((i+1)*num_data)]) 
		stack_data.append(epoch_data)
	
	stack_data = np.array(stack_data).T
	out_data = []
	for d in stack_data:
		for i in range(num_pixel):
			out_data.append(d)
	
	fig, ax = plt.subplots()
	
	im = plt.imshow(np.array(out_data), cmap="YlOrRd")
	
	ax.set_yticks(np.arange(0+num_pixel/2,num_class*num_pixel+num_pixel/2, num_pixel))
	ax.set_yticklabels(SHAPE_NAMES)
	ax.set_xlabel('Training Epoch')
	# print(len(out_x_label))
	# plt.imshow(data, cmap='YlGn')
	# fig.tight_layout()
	plt.subplots_adjust(top=0.9, bottom=0.1,left=0.3, right=0.85, hspace=0.4, wspace=0.2)
	cax = plt.axes([0.9, 0.1, 0.02, 0.8])
	plt.colorbar(cax=cax)
	# plt.colorbar()
	# if show_img:
	plt.show()
	# if(save_dir!=None):
	# 	fig.savefig(save_dir, format='eps')

def plot_class_genome_disb(data, num_data=200, num_pixel=5, num_class=3, save_dir=None, show_img=True):
	box = data[:,:220]
	cylinder = data[:,220:410]
	sphere = data[:,410:]
	sum_b = np.sum(box, axis=1)
	sum_c = np.sum(cylinder, axis=1)
	sum_s = np.sum(sphere, axis=1)
	stack_data = []
	blank = np.zeros(num_data)

	for p in range(num_pixel):
		stack_data.append(sum_b)
	stack_data.append(blank)
	for p in range(num_pixel):
		stack_data.append(sum_c)
	stack_data.append(blank)
	for p in range(num_pixel):
		stack_data.append(sum_s)
	
	stack_data = np.array(stack_data)
	im = plt.imshow(stack_data, cmap="YlGn")

	ytick = np.arange(num_pixel*0.5, num_class*num_pixel, num_pixel+1)
	plt.gca().set_yticks(ytick)
	label = ['box', 'cylinder', 'sphere']
	plt.gca().set_yticklabels(label)

	plt.subplots_adjust(top=0.9, bottom=0.1,left=0.1, right=0.8, hspace=0.2, wspace=0.2)
	cax = plt.axes([0.9, 0.1, 0.02, 0.8])
	plt.colorbar(cax=cax)
	
	if(save_dir!=None):
		plt.savefig(save_dir, dpi=600, format='eps')
	if show_img:
		plt.show()

def plot_multi_class_genome_disb()


def plot_all_genome_disb(data, num_pixel=1, scale=1, save_dir=None):
	
	stack_data = []
	print('genome disb data shape:',data.shape)
	for d in data:
		# print(d.shape)
		# for j in range(num_pixel):
		# 	temp_stack_data = []
		for i in range(num_pixel):
			stack_data.append(d*scale)
			# stack_data.append(temp_stack_data)
		# print(np.shape(stack_data))
	
	stack_data = np.array(stack_data)
	# stack_data = np.array(stack_data).T
	print(stack_data.shape)
	plt.imshow(stack_data, cmap="YlGn")
	# plt.imshow(data, cmap='YlGn')
	plt.subplots_adjust(top=0.9, bottom=0.1,left=0.1, right=0.8, hspace=0.2, wspace=0.2)
	# plt.tight_layout()
	cax = plt.axes([0.9, 0.1, 0.02, 0.8])
	plt.colorbar(cax=cax)
	plt.show()

	sum_d = np.sum(stack_data, axis=0)
	plt.plot(sum_d)
	plt.show()
	log_d = np.log(sum_d)
	plt.plot(log_d)

	plt.show()



if __name__=='__main__':

	num_class = 3
	num_data = 591

	train_data_name = 'shapes_luca_clean_norm'
	test_data_name = 'shapes_luca_clean_norm'
	exp_name = 'shapes_ea_history_selection_B70_HL200_FC90_EXP0'
	num_vote = 'dump_num_votes_1'

	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	
	SHAPE_NAMES = [line.rstrip() for line in \
			open((os.path.dirname(BASE_DIR) + '/data/shapes/objectlist'))]

	DUMP_DIR = os.path.join(BASE_DIR, 'result')
	LOG_DIR = os.path.join(BASE_DIR, 'log')

	DUMP_DIR = os.path.join(DUMP_DIR, exp_name)
	DUMP_DIR = os.path.join(DUMP_DIR, train_data_name)
	DUMP_DIR = os.path.join(DUMP_DIR, num_vote)
	DUMP_DIR = os.path.join(DUMP_DIR, test_data_name)

	disb_dir = os.path.join(DUMP_DIR, 'genome_disb.txt')
	
	disb_base_dir = '/home/senjing/3d-vision/ea_pointnet/log/shapes_ea_history_selection_B70_HL200_FC90_EXP0/shapes_luca_clean_norm/'
	for i in range(10):
		disb_dir = disb_base_dir + str(i) + '/all_genome_disb.txt'
		save_dir = disb_base_dir + '/class_genome_disb_' + str(i) +'.eps'
	# disb_dir = '/home/senjing/3d-vision/ea_pointnet/log/shapes_ea_history_selection_B70_HL200_FC90_EXP0/shapes_luca_clean_norm/0/all_genome_disb.txt'
	

		genome_disb = np.loadtxt(disb_dir)
		plot_class_genome_disb(genome_disb, save_dir=save_dir)
