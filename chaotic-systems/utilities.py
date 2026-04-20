import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from pend_funcs import *

def pend_plot_gen_animation(t,y,N,animation_length=10):
    
    filename = "pend.gif"
    filepath = os.path.join(os.getcwd(),filename)
    if os.path.exists(filepath):
        os.remove(filepath)

    fps_ = int(N/animation_length)
    FFMpegWriter = animation.writers['ffmpeg']
    writer = FFMpegWriter(fps=fps_)

    fig = plt.figure()
    
    with writer.saving(fig, filename, dpi=150):

        for i,j in enumerate(t):
            time = i
            fig = plt.clf()
            plt.xlim([-3,3])
            plt.ylim([-3.5,3.5])
            plt.scatter(0,0,c='blue',marker='.')
            plt.scatter(y[0,time],y[1,time],c='blue',marker='o')
            plt.plot([0,y[0,time]],[0,y[1,time]],color='black')
            plt.scatter(y[2,time],y[3,time],c='blue',marker='o')
            plt.scatter(y[2,0:i],y[3,0:i],c='orange',marker='.')
            plt.plot([y[2,time],y[0,time]],[y[3,time],y[1,time]],color='black')
            writer.grab_frame()

        
def pend_plot_final_instant(t,y,save_image=False):
    time = t.shape[0] - 1
    plt.clf()
    plt.xlim([-3,3])
    plt.ylim([-3.5,3.5])
    plt.scatter(0,0,c='blue',marker='.')
    plt.scatter(y[0,time],y[1,time],c='blue',marker='o')
    plt.plot([0,y[0,time]],[0,y[1,time]],color='black')
    plt.scatter(y[2,time],y[3,time],c='blue',marker='o')
    plt.plot([y[2,time],y[0,time]],[y[3,time],y[1,time]],color='black')
    plt.title("t = " + str(t[time]))
    if save_image:
        plt.savefig("final_instant.png")
    plt.show()