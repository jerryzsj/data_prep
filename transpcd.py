import pypcd

folder = '../data/mechnet/FC_2000_norm'
filepath1 = folder + '/test/pcd/'
filepath2 = folder + '/pcd/'
max_idx = 600

for i in range(max_idx):
	pc = pypcd.PointCloud.from_path(filepath1+str(i)+'.pcd')
	pc.save((filepath1+str(i)+'.pcd') )

for i in range(max_idx):
	pc = pypcd.PointCloud.from_path(filepath2+str(i)+'.pcd')
	pc.save((filepath2+str(i)+'.pcd') )
