**Multiple Integrals**

Multiple integrals involve integrating a function of more than one variable. For example, the double integral:

$$
\int_a^b \int_c^d f(x, y) \, dx \, dy
$$

This is used to compute areas, volumes, mass, center of mass, and other quantities over two-dimensional or higher-dimensional regions.

---

### Gaussian Quadrature in 2D

A numerical technique for evaluating integrals. For a 2D function $f(x, y)$:

1. Choose $N$ sample points along each axis using Gauss-Legendre quadrature.
2. Approximate the integral using:

$$
\sum_{i=1}^N \sum_{j=1}^N w_i w_j f(x_i, y_j)
$$

This is called **product quadrature**.

---

### Alternative Sampling Methods

* **Sobol sequences**: Low-discrepancy quasi-random points, good for high-dimensional integration.
* **Monte Carlo integration**: Random sampling, useful when the domain is irregular or high-dimensional.

---

### Irregular Integration Domains

When integration limits depend on each other (e.g., triangular or curved domains), use nested integrals or advanced techniques:

* Set function to zero outside domain.
* Use Monte Carlo or adaptive methods for better accuracy.

---

### Exercise 5.14: Gravity from a Sheet

A uniform square sheet of metal is floating motionless in space.
It has:

* **Side length**: $L = 10 \text{ m}$
* **Mass**: $M = 10^4 \text{ kg}$
* A **1 kg point mass** is located a vertical distance $z$ above the center of the square.

---

## (a) Derive the Expression for Force

Let the square lie in the $xy$-plane with center at the origin.

The mass per unit area of the sheet is:

$\sigma = \frac{M}{L^2} = \frac{10^4}{100} = 100 \text{ kg/m}^2$

An infinitesimal element of the sheet $dA = dx\,dy$ at position $(x, y)$ contributes an infinitesimal gravitational force:

$d\vec{F} = -\frac{G \cdot \sigma \cdot m \cdot \vec{r}}{r^3} \, dx\,dy$

where:

* $\vec{r} = x \hat{i} + y \hat{j} + z \hat{k}$
* $r = \sqrt{x^2 + y^2 + z^2}$

We want the component of the force in the z-direction:

$dF_z = -\frac{G \sigma m z}{(x^2 + y^2 + z^2)^{3/2}} dx\,dy$

Integrating over the square:

$F_z = -G \sigma m z \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} \frac{dx\,dy}{(x^2 + y^2 + z^2)^{3/2}}$

---

## (b) Numerical Calculation Using Gaussian Quadrature

```python
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss

G = 6.674e-11       # Gravitational constant (m^3 kg^-1 s^-2)
L = 10              # Side length of square (m)
M = 1e4             # Mass of sheet (kg)
sigma = M / (L * L) # Mass per unit area (kg/m^2)
m = 1               # Point mass (kg)
N = 100             # Gaussian quadrature points per axis

x, wx = leggauss(N)
y, wy = leggauss(N)

# Transform from [-1,1] to [-L/2, L/2]
x = x * (L / 2)
y = y * (L / 2)
wx = wx * (L / 2)
wy = wy * (L / 2)

# Meshgrid for 2D integral
X, Y = np.meshgrid(x, y)
WX, WY = np.meshgrid(wx, wy)
W = WX * WY

def compute_force_z(z):
    R_squared = X**2 + Y**2 + z**2
    integrand = z / R_squared**(3/2)
    Fz = -G * sigma * m * np.sum(integrand * W)
    return Fz

# z range and compute force
z_values = np.linspace(0.1, 10, 200)
Fz_values = [compute_force_z(z) for z in z_values]

# Plot
plt.figure(figsize=(8, 5))
plt.plot(z_values, Fz_values)
plt.xlabel("z (m)")
plt.ylabel("Gravitational Force Fz (N)")
plt.title("Gravitational Force vs. Height Above Sheet")
plt.grid(True)
plt.show()
```
