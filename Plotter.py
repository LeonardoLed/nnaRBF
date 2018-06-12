#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 17:19:54 2018

@author: Alejandro Urritia
@modified by: Leonardo Ledesma Domínguez
"""
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from Decorators import timePass
 
class plotter():
    
    def __init__(self,solv, kernel):
        self.__solver = solv
        self.__kernel = kernel
    
    @timePass
    def levelplot(self, title = None, xlabel = None, ylabel = None, barlabel = None, fileName = None):
        knots = self.__solver.getKnots()
        factorX = knots.width () * knots.dp ()
        factorY = knots.height () * knots.dp ()
        x = np.linspace(0,knots.width(),factorX)
        y = np.linspace(0,knots.height(),factorY)
        X, Y = np.meshgrid(x, y)
        Z = self.__solver.interpolate(self.__kernel)
        
        fig, ax = plt.subplots()
        CS = plt.contourf(X, Y, Z, 10, alpha=.75, cmap=plt.cm.jet)
        cbar = plt.colorbar(CS)
        C = plt.contour(X, Y, Z, 10, colors='black')
        plt.clabel(C, inline=1, fontsize=7.5)
        
        
        #cbar.add_lines(CS)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if barlabel:
            cbar.ax.set_ylabel(barlabel)
        if fileName:
            plt.savefig(fileName)
        plt.show()
        
    @timePass
    def surface3D(self, title = None, xlabel = None, ylabel = None, barlabel = None):
        knots = self.__solver.getKnots()
        factorX = knots.width () * knots.dp ()
        factorY = knots.height () * knots.dp ()
        x = np.linspace (0, knots.width (), factorX)
        y = np.linspace (0, knots.height (), factorY)
        X, Y = np.meshgrid(x, y)
        Z = self.__solver.interpolate(self.__kernel)

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        
        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
        
        # Customize the z axis.
        #ax.set_zlim(-1.01, 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        
        # Add a color bar which maps values to colors.
        #fig.colorbar(surf, shrink=0.5, aspect=5)
        cbar = plt.colorbar(surf)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if barlabel:
            cbar.ax.set_ylabel(barlabel)
        
        plt.show()
     
    @timePass    
    def regularMesh2D(self,title = None, xlabel = None, ylabel = None):

        NIx,NIy = self.__solver.getKnots().aNI()
        NBx,NBy = self.__solver.getKnots().aNB()
        plt.scatter(NIx,NIy,c='b', marker = '.')
        plt.scatter(NBx,NBy,c='r', marker = '.')
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        plt.show()
        
    def u(x,y,A,alfa):
        return -A*np.cos(alfa*np.pi*y)*np.sin(alfa*np.pi*x)

    def v(x,y,A,alfa):
        return A*np.sin(alfa*np.pi*y)*np.cos(alfa*np.pi*x)
    