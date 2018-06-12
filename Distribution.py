"""
This class makes a normal gaussian distribution given a standard deviation (sigma) and a mean (mu)
by default sigma = 1.6 and mean = 1, this values change according to domain boundaries and its width and heigth

@autor: Leonardo Ledesma Domínguez
Creation date: 27/05/2018
"""
import numpy as np


class Distribution():

    def __init__(self, shape= None, a=None, b=None, nodes=None, domain=None, dp=None):
        self.__shape = shape
        self.__a = a
        self.__b = b
        self.__nodes = nodes
        self.__NB = 0
        self.__NI = 0
        self.__dp = dp
        self.__width = domain.width()
        self.__height = domain.height()

    def a(self):
        return self.__a

    def b(self):
        return self.__b

    def nodes(self):
        return self.__nodes

    def NI(self):
        return self.__NI

    def NB(self):
        return self.__NB

    def Ny(self):
        return self.__Ny

    def Nx(self):
        return self.__Ny

    def dp(self):
        return self.__dp

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def aNI(self):
        return self.__a[0:self.__NI], self.__b[0:self.__NI]

    def aNB(self):
        return self.__a[self.__NI:self.__nodes], self.__b[self.__NI:self.__nodes]

    def calcDist(self, shape='rdp', nodes=100, width=None, height=None, bx=None, by=None, dp=None):

        a = np.zeros(1)
        b = np.zeros(1)

        if shape == 'ngd':
            # random points
            n = nodes
            X = abs(np.random.normal(1, 1.6, n))
            Y = abs(np.random.normal(1, 1.6, n))
            # applied limits of domain

            for i in range(0, len (X)):
                if 0 <= X[i] <= width:
                    if 0 <= Y[i] <= height:
                        a = np.append(a, X[i])
                        b = np.append(b, Y[i])
                        self.__NI += 1

        elif shape == 'rdp':
            # calc points for regular mesh
            setline_x = bx[0][0]
            setline_y = by[1][0]
            dec = 1/dp

            for k in range(1, len(setline_x)-1):
                for j in range(1, len(setline_y)-1):
                    a = np.append(a, setline_x[k])
                    b = np.append(b, setline_y[j])
                    self.__NI += 1

        # remove corners redundant
        by[1][0] = by[1][0][1:-1]
        bx[1][0] = bx[1][0][1:-1]
        by[3][0] = by[3][0][1:-1]
        bx[3][0] = bx[3][0][1:-1]

        for i in range(0, len(bx)):
            a = np.append(a, bx[i][0])
            b = np.append(b, by[i][0])

        self.__Nx = len(bx[0][0])
        self.__Ny = len(by[1][0])

        #print(len(bx[0][0]))
        #print(bx[0][0], by[0][0])

        boundaries = len(bx[1][0])*2 + len(bx[2][0])*2
        self.__NB = boundaries

        a = a[1:]
        b = b[1:]

        self.__a = a
        self.__b = b
        #print(a[self.__NI], b[self.__NI])

        self.__nodes = self.__NI + self.__NB
        return self.__a, self.__b

if __name__ == '__main__':

    # Unit Tests
    dst = Distribution(nodes=200)
    print(dst.nodes())
    print('_' * 20)
    #dst.calcDist(shape='ngd',width=2,height=4)
    #print(len(dst.a()), len(dst.b()), dst.nodes())