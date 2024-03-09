import numpy as np

# Define the acceleration due to gravity
g = 9.81


# Complete the RHS f for double spring pendulum system y' = f.
# Return f as a numpy array of size 8.
def fpend(u, ks, L0, m):
    k1 = ks[0]
    k2 = ks[1]
    L1 = L0[0]
    L2 = L0[1]
    m1 = m[0]
    m2 = m[1]

    x1 = u[0]
    y1 = u[1]
    x2 = u[2]
    y2 = u[3]
    vx1 = u[4]
    vy1 = u[5]
    vx2 = u[6]
    vy2 = u[7]

    # Compute the RHS of the double spring pendulum system.
    # Return f as a numpy array of size 8.
    f = np.zeros(8)

    f1g = -m1 * g
    f2g = -m2 * g

    L1i = np.sqrt(x1**2 + y1**2)
    L2i = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    fspring1 = k1 * (L1i - L1)
    fspring2 = k2 * (L2i - L2)

    theta1 = np.arctan2(x1, y1)
    theta2 = np.arctan2(x2 - x1, y2 - y1)

    f[0] = vx1
    f[1] = vy1
    f[2] = vx2
    f[3] = vy2

    ax1 = (-fspring1 * np.sin(theta1) + fspring2 * np.sin(theta2)) / m1
    ay1 = (-fspring1 * np.cos(theta1) + fspring2 * np.cos(theta2) + f1g) / m1
    print(ay1)
    ax2 = (-fspring2 * np.sin(theta2)) / m2
    ay2 = (-fspring2 * np.cos(theta2) + f2g) / m2

    f[4] = ax1
    f[5] = ay1
    f[6] = ax2
    f[7] = ay2

    return f


# Function to compute the total energy of the system over time.
def pendulumEnergy(u, ks, L0, m):
    k1 = ks[0]
    k2 = ks[1]
    L1 = L0[0]
    L2 = L0[1]
    m1 = m[0]
    m2 = m[1]

    Es = np.zeros(u.shape[1])

    for i, ui in enumerate(u.T):
        x1 = ui[0]
        y1 = ui[1]
        x2 = ui[2]
        y2 = ui[3]
        vx1 = ui[4]
        vy1 = ui[5]
        vx2 = ui[6]
        vy2 = ui[7]

        KE = 0.5 * m1 * (vx1**2 + vy1**2) + 0.5 * m2 * (vx2**2 + vy2**2)

        PEspring = (
            0.5 * k1 * (np.sqrt(x1**2 + y1**2) - L1) ** 2
            + 0.5 * k2 * (np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) - L2) ** 2
        )

        PEgrav = m1 * g * y1 + m2 * g * y2

        E = KE + PEspring + PEgrav

        Es[i] = E

    return Es
