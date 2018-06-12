"""
This class searchs a Nearest Neighbors given a set queries of points based on KD-Tree; this methodoly is explained in:
https://www.datasciencecentral.com/profiles/blogs/implementing-kd-tree-for-fast-range-search-nearest-neighbor
(read in order to have more information)

The diferent methods are:
a) Ball Tree wit KdTree :bt (take a radius to search within a neighbor) using kdtree
    Complexity O( N * log(N)) ---> O(N^2)
b) Brutal Force:bf (take a sparce distance matrix of each query point and determine what points are within a certain cutoff called radio)
   Complexity: O(N^2) --> O(N * log (n))
c) Ball Tree:Complexity O( N * log(N))


@autor: Leonardo Ledesma Domínguez
Creation date:: 28/05/2018
"""
from scipy import spatial
import numpy as np
import time
from math import sqrt
from sklearn.neighbors import BallTree as btree
from Decorators import timePass

class Neighbor():
    def __init__(self, method=None, x=None, y=None, neighbor=None, r=None):
        self.__method = method
        self.__x = x
        self.__y = y
        self.__neighbor = neighbor
        self.__location = {}
        self.__r = r

    def method(self):
        return self.__method

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def neighbor(self):
        return self.__neighbor

    def r(self):
        return self.__r

    def location(self):
        return self.__location

    @timePass
    def nearest_neighbors(self, method=None):

        method = self.__method
        point = 0
        start_time = time.time()
        self.__neighbor = dict()
        Tree = list (zip (self.__x, self.__y))

        if method == 'bt':
            print("The Search Method is KD-Tree with Ball Tree by Binary Search")
            print('_' * 40)

            for p in Tree:
                l = spatial.KDTree(Tree).query_ball_point(p, self.__r / 2)
                self.__location[point] = l
                self.__neighbor[p] = []
                for k in l:
                    if Tree[k][0] != p[0] or Tree[k][1] != p[1]:
                        self.__neighbor[p].append([Tree[k]])
                point += 1

        elif method == 'bf':
            print("The Search Method is Brutal Force")
            print('_' * 40)
            for p in Tree:
                self.__location[point] = []
                self.__neighbor[p] = []
                edp = 0
                for q in Tree:
                    if q != p:
                        x1 = p[0]
                        x2 = q[0]
                        y1 = p[1]
                        y2 = q[1]
                        euclidean = sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))
                        if euclidean <= self.__r/2:
                            self.__neighbor[p].append([q])
                            self.__location[point].append(edp)
                    edp += 1
                point += 1

        elif method == 'ball':
            # you can put in this part of code the different distance metric that exists:
            # hamming, seuclidean, sokalneath, kulsinski,  minkowski (default) and so on
            # See more: https://github.com/scikit-learn/scikit-learn/pull/4525
            print("The Search Method Ball Tree with Minkowski Distance")
            print('_' * 40)
            BinaryTree = btree(Tree, leaf_size=2)
            for p in Tree:
                ind = BinaryTree.query_radius([p], r=self.__r/2)
                ind = ind[0]
                self.__location[point] = ind.tolist()
                self.__neighbor[p] = []
                for q in ind:
                    # self.__neighbor[p].append([Tree[q]])
                    if (Tree[q][0] != p[0]) or (Tree[q][1] != p[1]):
                        self.__neighbor[p].append([Tree[q]])
                point += 1

        print("Search Time in NN method:")
        print("--- %s seconds ---" % (time.time() - start_time))
        return self.__neighbor


if __name__ == '__main__':
    # Unit Tests
    d1 = Neighbor('ball', [1, 1, 3, 5], [1, 2, 4, 5], r=5.0)
    print(d1.x(), d1.y(), d1.r())
    print('_' * 20)
    print(d1.method())
    d1.nearest_neighbors()
    print(d1.neighbor())

