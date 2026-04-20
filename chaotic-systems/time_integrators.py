from pend_funcs import *
import numpy as np
from utilities import *


# Adams Bashforth 2.
def ab2pend(u0, ks, L0, m, h, N):
    ts = np.arange(N + 1) * h
    u = np.zeros((N + 1, 8))
    u[0] = u0

    for i in range(N):
        if i == 0:
            k1 = h * fpend(u[i], ks, L0, m)
            k2 = h * fpend(u[i] + k1 / 2, ks, L0, m)

            u[i + 1] = u[i] + k2

        else:
            u[i + 1] = (
                u[i]
                + (3 / 2) * h * fpend(u[i], ks, L0, m)
                - (1 / 2) * h * fpend(u[i - 1], ks, L0, m)
            )

    return ts, u.T


# Leapfrog
def lfpend(u0, ks, L0, m, h, N):
    ts = np.arange(N + 1) * h
    u = np.zeros((N + 1, 8))
    u[0] = u0

    for i in range(N):
        if i == 0:
            k1 = h * fpend(u[i], ks, L0, m)
            k2 = h * fpend(u[i] + k1 / 2, ks, L0, m)

            u[i + 1] = u[i] + k2

        else:
            u[i + 1] = u[i - 1] + 2 * h * fpend(u[i], ks, L0, m)

    return ts, u.T


# RK-4
def rk4pend(u0, ks, L0, m, h, N):
    ts = np.arange(N + 1) * h
    u = np.zeros((N + 1, 8))
    u[0] = u0

    for i in range(1, N + 1):
        k1 = h * fpend(u[i - 1], ks, L0, m)
        k2 = h * fpend(u[i - 1] + k1 / 2, ks, L0, m)
        k3 = h * fpend(u[i - 1] + k2 / 2, ks, L0, m)
        k4 = h * fpend(u[i - 1] + k3, ks, L0, m)

        u[i] = u[i - 1] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    return ts, u.T


u0 = np.array([0, -1, 0, -2, 0, 0, 0, 0])
ks = np.array([100, 100])
L0 = np.array([1.0, 1.0])
m = np.array([1.0, 1.0])
h = 0.02
N = 200
t, u = lfpend(u0, ks, L0, m, h, N)
pend_plot_gen_animation(t, u, N, animation_length=10)
