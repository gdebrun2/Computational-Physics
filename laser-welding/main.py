import numpy as np
from utilities import *
from fea_functions import *

#if using the given meshes uncomment the two lines below and set the filename.
#filename = "coarse.msh"
#p, LM, nodeFlag = msh_reader_2D(filename)

#If you are writing your own small mesh, then explicitly define p, LM and nodeFlag below.
#p = ...
#LM = ...
#nodeFlag = ...

#Check if the mesh you got is what you expected by using the given plotting function.
#plt.figure(2)
#plot_mesh(LM.shape[1], p, LM)

#Define the material properties and loading conditions.
k = 1 #Conductivity
Q = 200 #Body heating term
To = 10 #Dirichlet temperature on the straight edges.
Ti = 20 #Dirichlet condition on the arc.

#Compute the fea solution using the above mesh, material properties and loading conditions.
#T = solve_fea_heat2d(p, LM, nodeFlag, k, Q, To, Ti)

#Plot the contour of the solution field T
#plot_solution_contour(LM.shape[1], p, LM, T)
