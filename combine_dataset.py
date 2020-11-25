import numpy as np
import os
import sys

# Source pcl_utils
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)

sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *

# Source base_dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)

# Define data_dir
DATA_DIR = os.path.join(BASE_DIR, 'data')

# print(BASE_DIR)

# Combine D1 into D2
# define picked idx
D1_train_idx = [0, 10, 20]
D2_test_idx = range(1, 10, 1) + range(11, 20, 1) + range(21, 28, 1)
# print(D2_test_idx)

# define D1 dir
D1_TYPE='ycb'
D1_NAME='ycb_origin_28_SP20_norm'

D1_DIR = os.path.join(DATA_DIR, D1_TYPE)
D1_DIR = os.path.join(D1_DIR, D1_NAME)

# define D2 dir
D2_TYPE='shapes'
D2_NAME='shapes_luca_clean_norm'

D2_DIR = os.path.join(DATA_DIR, D2_TYPE)
D2_DIR = os.path.join(D2_DIR, D2_NAME)

# print(D1_DIR)
# print(D2_DIR)

# define save_dir
SAVE_DIR = os.path.join(DATA_DIR, 'shapes')
SAVE_DIR = os.path.join(SAVE_DIR, 'shapes_transfer_learning_0_10_20_norm')

SAVE_TRAIN_DIR = os.path.join(SAVE_DIR, 'train')
SAVE_TEST_DIR = os.path.join(SAVE_DIR, 'test')
if not os.path.exists(SAVE_TRAIN_DIR): os.makedirs(SAVE_TRAIN_DIR)
if not os.path.exists(SAVE_TEST_DIR): os.makedirs(SAVE_TEST_DIR)

################
# For Training #
################
# picked data
p_data = []
p_label = []

# read d1 & d2 data & label
f_dir = 'train'
D1_data, D1_label = load_npy(os.path.join(D1_DIR, f_dir))	
D2_data, D2_label = load_npy(os.path.join(D2_DIR, f_dir))
# print(D2_data.shape)

# pick data & label from D1
for idx in D1_train_idx:
	# print(idx)
	for i in range(20):
		p_data.append(D1_data[idx*20+i])
		p_label.append(D1_label[idx*20+i])
# print(p_label)
# print(p_data[20])
p_data = np.array(p_data)
p_label = np.array(p_label)
# print(p_data.shape)

# append data into D2
new_train_data = np.append(D2_data, p_data, axis=0)
new_train_label = np.append(D2_label, p_label)
# print(D2_data.shape)
# print(D2_label.shape)
save_npy(new_train_data, new_train_label, SAVE_TRAIN_DIR)

###############
# For Testing #
###############
# picked data
p_data = []
p_label = []
# read d1 test data & label
f_dir = 'test'
D1_data, D1_label = load_npy(os.path.join(D1_DIR, f_dir))

# pick data & label from D1
for idx in D2_test_idx:
	# print(idx)
	for i in range(20):
		p_data.append(D1_data[idx*20+i])
		p_label.append(D1_label[idx*20+i])
# print(p_label)
# print(p_data[20])
p_data = np.array(p_data)
p_label = np.array(p_label)
# print(p_data.shape)

# append data into D2
new_test_data = p_data
new_test_label = p_label

save_npy(new_test_data, new_test_label, SAVE_TEST_DIR)


