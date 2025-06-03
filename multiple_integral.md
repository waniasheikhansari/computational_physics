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

* A square sheet (10m x 10m, 10,000 kg) exerts gravitational force on a 1 kg mass located a distance $z$ above the center.
* The z-component of force is:

$$
F_z(z) = G \sigma z \int_{-L/2}^{L/2} \int_{-L/2}^{L/2} \frac{dx \ dy}{(x^2 + y^2 + z^2)^{3/2}}
$$

Where:

* $G$ is gravitational constant.
* $\sigma =$ mass/area.

You solve it with 2D Gaussian quadrature and plot $F_z(z)$ vs $z$.

---

### Artifact at z \approx 0

At very small $z$, the integral may show a sudden drop. This is numerical error due to:

* Denominator approaching zero.
* Too coarse sampling near the singularity.

**Fix:**

* Use adaptive mesh refinement.
* Avoid evaluating the function too close to $z = 0$.

---

### Applications

Used in:

* Gravity/mass simulations
* Quantum mechanics
* Thermodynamics
* Electromagnetism
* Fluid dynamics

---
