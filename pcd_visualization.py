import numpy as np
import open3d as o3d
import time
import os

if __name__ == "__main__":

	# print("Load a ply point cloud, print it, and render it")
	# pcd_similar = o3d.io.read_point_cloud("/Users/senjing/3d-vision/data/ycb/ycb_28_similar_SP20_BIAS5_norm/train/pcd/0.pcd")
	# pcd_origin = o3d.io.read_point_cloud("/Users/senjing/3d-vision/data/ycb_dataset_original/ply_from_stl/box/003_cracker_box.ply")
	
	# simi_file = "/Users/senjing/3d-vision/data/ycb_origin_vs_similar_forvis/similar/0.pcd"
	# shapes_luca_error_norm
	# ycb_28_similar_SP20_BIAS5_norm_error5

	# dir_1 ='/Users/senjing/3d-vision/data/ycb/ycb_28_origin_SP20_norm/train/aligned_pcd/'
	dir_1 = '/home/senjing/3d-vision/data/shapes/ycb_28_origin_SP20_norm/test/aligned_pcd/'
	# dir_1 ='/Users/senjing/3d-vision/data/shapes/ycb_28_similar_SP20_BIAS5_norm_error/train/pcd/'
	# dir_2 = '/Users/senjing/3d-vision/data/shapes/shapes_luca_error_norm/train/aligned_pcd/'


	pcd_all = []
	mesh_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.3, origin=[0, 0, 0])
	
	# os.makedirs('pcd-to-png/ycb_28_origin_SP20_norm')

	for i in range(560):
		print(i)
		# pcd_all = []
	# for i in range(11,12):
		n = i
		f = dir_1 + str(n) + '.pcd'
		pcd = o3d.io.read_point_cloud(f)
		# pcd_all.append(pcd)
		# pcd_all.append(mesh_frame)
		# vis = o3d.visualization.draw_geometries(pcd_all)

		vis = o3d.visualization.Visualizer()
		vis.create_window('pcl', width=760, height=540, left=50, top=50, visible=True)
		vis.add_geometry(pcd)
		vis.add_geometry(mesh_frame)
		vis.update_renderer()
		out_depth = vis.capture_depth_float_buffer(True)
		time.sleep(0.01)
		vis.capture_screen_image('pcd-to-png/ycb_28_origin_SP20_norm/'+ str(i) +'.png')
		time.sleep(0.01)
		vis.destroy_window()
		time.sleep(0.01)

	# vis.capture_screen_image('pcl-img.png')
	# vis.destroy_window()

	# vis.update_geometry()
	# vis.poll_events()
	# vis.update_renderer()

	# Capture image
	# time.sleep(1)
	# vis.capture_screen_image('cameraparams.png')
	# image = vis.capture_screen_float_buffer()

	# vis.destroy_window()
		# f = dir_2 + str(n) + '.pcd'
		# pcd = o3d.io.read_point_cloud(f)
		# pcd_all.append(pcd)

		o3d.visualization.draw_geometries([pcd])
