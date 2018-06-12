from scipy import spatial
import numpy as np
from sklearn.neighbors import BallTree

A = np.random.random((10, 2)) * 100
print(len(A))
print(A)
B = np.random.random((10, 2)) * 100
pt = [6,30]

distance,index = spatial.KDTree(A).query(pt)
print(A[spatial.KDTree(A).query(pt)[1]])
l= spatial.KDTree(A).query_ball_point(pt,17)
print("view")
for i in l:
    print(A[i])

D = spatial.KDTree(A).sparse_distance_matrix(spatial.KDTree(A),10)

print(distance,index)
print(D)
print(A)

print('_' * 20)
np.random.seed(10)
X = np.random.random((10, 3))
tree = BallTree(X, leaf_size=2)
dist, ind = tree.query([X[0]], k=9)
print(ind)
print(dist)

print('_' * 20)
X = np.random.random((10, 2))  # 10 points in 3 dimensions
print(X[0])
tree = BallTree(X, leaf_size=2)
ind = tree.query_radius([X[0]], r=0.4)
print(ind)
print(ind[0])

