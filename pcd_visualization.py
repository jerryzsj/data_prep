import numpy as np
import open3d as o3d

if __name__ == "__main__":

	# print("Load a ply point cloud, print it, and render it")
	# pcd_similar = o3d.io.read_point_cloud("/Users/senjing/3d-vision/data/ycb/ycb_28_similar_SP20_BIAS5_norm/train/pcd/0.pcd")
	# pcd_origin = o3d.io.read_point_cloud("/Users/senjing/3d-vision/data/ycb_dataset_original/ply_from_stl/box/003_cracker_box.ply")
	
	# simi_file = "/Users/senjing/3d-vision/data/ycb_origin_vs_similar_forvis/similar/0.pcd"

	dir_1 ='/Users/senjing/3d-vision/data/ycb/ycb_28_origin_SP20_norm/train/aligned_pcd/'
	dir_2 = '/Users/senjing/3d-vision/data/shapes/shapes_luca_clean_norm/train/aligned_pcd/'

	pcd_all = []

	for i in range(13,14):
		n = i
		f = dir_1 + str(n) + '.pcd'
		pcd = o3d.io.read_point_cloud(f)
		pcd_all.append(pcd)
		f = dir_2 + str(n) + '.pcd'
		pcd = o3d.io.read_point_cloud(f)
		pcd_all.append(pcd)

	o3d.visualization.draw_geometries(pcd_all)