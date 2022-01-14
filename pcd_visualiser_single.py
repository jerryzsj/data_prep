import numpy as np
import open3d as o3d
import time
import os
import sys
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'pcl_utils'))
from pcio import *

if __name__ == "__main__":
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	BASE_DIR = os.path.dirname(BASE_DIR)

	parser = argparse.ArgumentParser()
	parser.add_argument('--dataset_type', default='shapes', help='Dataset type [shapes/ycb/mechnet/normalized]')
	parser.add_argument('--dataset_name', default='shapes_luca_error_norm', help='Data forder [shapes_0.04to0.4/shapes_0.5to0.8/shapes_luca/ycb_50]')
	parser.add_argument('--save_dir', default='png', help='filelist [filelist/filelist_partial]')
	FLAGS = parser.parse_args()

	DATASET_TYPE = FLAGS.dataset_type
	DATASET_NAME = FLAGS.dataset_name

	DATA_DIR = os.path.join(PROJECT_DIR, 'data')
	DATA_DIR = os.path.join(DATA_DIR, DATASET_TYPE)

	DATA_DIR = os.path.join(DATA_DIR, DATASET_NAME)
	TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'train')
	TEST_DATA_DIR = os.path.join(DATA_DIR, 'test')

	SAVE_TRAIN_DIR = os.path.join(TRAIN_DATA_DIR, FLAGS.save_dir)
	SAVE_TEST_DIR = os.path.join(TEST_DATA_DIR, FLAGS.save_dir)
	if not os.path.exists(SAVE_TRAIN_DIR): os.makedirs(SAVE_TRAIN_DIR)
	if not os.path.exists(SAVE_TEST_DIR): os.makedirs(SAVE_TEST_DIR)

	TRAIN_DATA_DIR = os.path.join(TRAIN_DATA_DIR, 'pcd')
	TEST_DATA_DIR = os.path.join(TEST_DATA_DIR, 'pcd')

	pcd_all = []
	mesh_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.3, origin=[0, 0, 0])
	
	# os.makedirs('pcd-to-png/ycb_28_origin_SP20_norm')

	for i in range(1,2):
		print(i)
		f = TRAIN_DATA_DIR + '/' + str(i) + '.pcd'
		pcd = o3d.io.read_point_cloud(f)

		# vis = o3d.visualization.Visualizer()
		vis = o3d.visualization.draw_geometries_with_editing([pcd], width=600, height=600)
		# vis.create_window('pcl', width=1920, height=1080, left=50, top=50, visible=True)
		# vis.create_window()
		# vis.add_geometry(pcd)
		# vis.update_renderer()
		# out_depth = vis.capture_depth_float_buffer(True)
		# vis.add_geometry(mesh_frame)
		# vis.update_renderer()
		# out_depth = vis.capture_depth_float_buffer(True)
		# time.sleep(20)

		# vis.capture_screen_image(os.path.join(save_dir, str(i) +'.png'))
		# vis.destroy_window()
		
