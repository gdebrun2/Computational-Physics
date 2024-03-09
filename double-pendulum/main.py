from pend_funcs import *
from time_integrators import *
from utilities import *

#######################
#Main script.  
######################

#To generate a .gif animation of the solution, you need to install ffmpeg. (This may not work in the workspace.)
#For conda, use :- conda install -c conda-forge ffmpeg.
#For pip, use :- pip install ffmpeg OR pip3 install ffmpeg.

#(Remove both ''' below to uncomment this file)
'''
#Given properties. 
ks = np.array([1e2,1e2]) #Stifness values of both springs.
L0 = np.array([1,1]) #L0 value for both springs.
m = np.array([1,1]) #Mass of the two particles.

#Simulation time details
Tf = 600 #Final time.
h = 0.02 #Time step size.
N = int(Tf/h) #Number of steps based on above parameters.

#IC
u0 = np.array([1,0,1,1,0,0,0,0])

#AB2 
t1,y1 = ab2pend(u0,ks,L0,m,h,N)
E1 = pendulumEnergy(y1,ks,L0,m)

#Leapfrog 
t2,y2 = lfpend(u0,ks,L0,m,h,N)
E2 = pendulumEnergy(y2,ks,L0,m)

#RK4
t3,y3 = rk4pend(u0,ks,L0,m,h,N)
E3 = pendulumEnergy(y3,ks,L0,m)
 
#Plot the configuration at time t = Tf. Set save_image True or False as needed.
pend_plot_final_instant(t3,y3,save_image=True)

#Uncomment below line to generate animation (pend.gif). May not work in the workspace.
#Will produce a 10s gif by default.
#anim_l = 10
#pend_plot_gen_animation(t3,y3,N,animation_length = anim_l)

'''
