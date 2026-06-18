import numpy as np

G = 6.67430e-11
M_T = 5.972e24
R_T = 6.371e6
C_D = 2.2
A = 1.0
m = 1000
H = 8500
rho_0 = 1.225

def Rm(t, X):
    dx, dy, vx, vy = X[0], X[1], X[2], X[3]

    r = np.sqrt(dx**2 + dy**2)
    v = np.sqrt(vx**2 + vy**2)

    rho = rho_0 * np.exp(-(r - R_T) / H)

    ax_g = -G * M_T * dx / r**3
    ay_g = -G * M_T * dy / r**3

    if v > 0:
        coeff = -0.5 * C_D * A * rho * v**2 / m
        ax_d = coeff * (vx / v)
        ay_d = coeff * (vy / v)
    else:
        ax_d, ay_d = 0, 0

    ax = ax_g + ax_d
    ay = ay_g + ay_d

    return np.array([vx, vy, ax, ay])

t0_sim = 0
tf_sim = 20000
h_sim = 0.1
x0_sim = np.array([
    R_T + 260e3,
    0,
    0,
    np.sqrt(G * M_T / (R_T + 260e3)) * 0.9951
])
