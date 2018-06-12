"""
This class makes a rectangle mesh given its width and its heigth.
Return a group coordinates that determine the boundary of domain

@autor: Leonardo Ledesma Domínguez
Creation date: 27/05/2018
"""
import numpy as np


class Domain():

    def __init__(self, width=None, height=None, nodes_x=None, nodes_y =None):
        self.__width = width
        self.__height = height
        self.__nodes_x = nodes_x
        self.__nodes_y = nodes_y

    def nodes_x(self):
        return self.__nodes_x

    def nodes_y(self):
        return self.__nodes_y

    def height(self):
        return self.__height

    def width(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def setHeight(self, height):
        self.__height = height

    def __del__(self):
        del self.__width
        del self.__nodes_x
        del self.__nodes_y
        del self.__height

    def createSquare(self, dp = None):

        #dp = 5
        incr_x = self.__width * dp
        incr_y = self.__height * dp
        side_basex = np.linspace(0, self.__width, incr_x)
        side_basey = np.linspace(0, self.__height, incr_y)
        vacuum_x = np.zeros(self.__height * dp)
        vacuum_y = np.zeros(self.__width * dp)

        self.__nodes_x = np.array([
            [side_basex],
            [vacuum_x + self.__width],
            [side_basex],
            [vacuum_x]])

        self.__nodes_y = np.array([
            [vacuum_y + self.__height],
            [side_basey],
            [vacuum_y],
            [side_basey]])

        return self.__nodes_x, self.__nodes_y


if __name__ == '__main__':

    # Unit Tests
    d1 = Domain(2, 2)
    print(d1.nodes_y(), d1.nodes_x(), d1.width(), d1.height())
    print('_' * 20)
    d1.createSquare(dp=10)
    print(d1.nodes_y(), d1.nodes_x(), d1.width(), d1.height())
    print('_' * 20)
    print(d1.nodes_y()[0][0])