# Entry-into-the-atmosphere-simulation
# Numerical Analysis II - Atmospheric Entry Simulation

This repository contains a numerical analysis project focused on simulating a capsule's atmospheric entry. The project implements and evaluates various numerical schemes for solving Ordinary Differential Equations (ODEs) and non-linear systems of equations, applying them to the physical model of a spacecraft descending towards Earth.

## Project Structure

The project is organized into modular files to prevent circular dependencies and separation of concerns:
- **`odesolve.py`**: Contains the physical parameters of the Earth (gravity, atmospheric density model) and defines the system's differential equation $\frac{dX}{dt} = R_m(t, X)$ capturing aerodynamic drag and gravitational forces.
- **`solution_num.py`**: A laboratory module containing reference implementations, stability analyses, and error convergence tests (e.g., using a test circular trajectory or stable linear systems) to verify theoretical orders of convergence.
- **Main Script (`core`)**: The orchestrator file that includes the solver implementations (`fixedPoint`, `newton`, `ODEsolve`) and executes the final atmospheric entry simulation.

---

## Implemented Numerical Methods

### 1. Non-linear Systems Solvers
Used to resolve implicit steps within advanced numerical ODE schemes:
* **Fixed-Point Iteration (`fixedPoint`)**: Solves $x = f(x)$ iteratively within a tolerance $\text{tol} = 10^{-8}$.
* **Newton-Raphson Method (`newton`)**: Implemented for multi-dimensional systems ($\mathbb{R}^n$) solving $x_{k+1} = x_k - J_f(x_k)^{-1}f(x_k)$.

### 2. ODE Solvers (`ODEsolve`)
The unified solver handles vector fields and supports multiple classical integration schemes:
* **Explicit Euler**: First-order explicit scheme.
* **Implicit Euler**: First-order implicit scheme (utilizing the fixed-point solver).
* **Crank-Nicholson**: Second-order implicit method combining explicit and implicit Euler.
* **Runge-Kutta 2 (RK2)**: Second-order explicit predictor-corrector method.
* **Runge-Kutta 4 (RK4)**: Fourth-order explicit scheme providing high accuracy for orbital mechanics.

---

## Physical Modelization

The simulation tracks the spacecraft's state vector $X = [x, y, v_x, v_y]^T$ factoring in:
1. **Newtonian Gravity**: Centered gravitational acceleration:
   $$a_g = -\frac{G M_T}{r^3}\vec{r}$$
2. **Aerodynamic Drag**: Dependent on atmospheric density $\rho(r)$ decaying exponentially with altitude:
   $$\rho(r) = \rho_0 e^{-\frac{r - R_T}{H}}$$
   $$a_d = -\frac{1}{2}\frac{C_D A \rho(r) v^2}{m} \vec{u}_v$$

---

## Execution & Visualization

The main simulation plots the trajectory of a spacecraft beginning entry from Low Earth Orbit ($R_T + 260\text{ km}$) with a slight perturbation from a perfectly circular velocity vector. 

### Prerequisites
Ensure you have the required scientific stack and the background asset (`globe.png`) placed at the root directory:
```bash
pip install numpy matplotlib
