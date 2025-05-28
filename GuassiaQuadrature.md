# Gaussian Quadrature - Complete Notes


Gaussian Quadrature is a numerical method used to approximate definite integrals, especially useful when exact integration is hard or impossible.

We approximate:

$$
\int_{-1}^{1} f(x) \, dx \approx \sum_{i=1}^{n} w_i f(x_i)
$$

Where:

* $x_i$: special points called **nodes** (roots of Legendre polynomials)
* $w_i$: corresponding **weights**

---

## Why Use Gaussian Quadrature?

It gives **very accurate results** even with few evaluation points. For example:

* 2-point Gaussian Quadrature can exactly integrate all polynomials of degree ≤ 3.
* 3-point can exactly integrate degree ≤ 5.

---

## Example: 2-point Gaussian Quadrature

Let’s approximate:

$$
\int_{-1}^{1} x^2 \, dx
$$

### Step 1: Use the 2-point formula

$$
\int_{-1}^{1} f(x) \, dx \approx w_1 f(x_1) + w_2 f(x_2)
$$

From the Gaussian Quadrature table for **n = 2**:

* $x_1 = -\frac{1}{\sqrt{3}} \approx -0.577$
* $x_2 = +\frac{1}{\sqrt{3}} \approx +0.577$
* $w_1 = w_2 = 1$

### Step 2: Plug in the function $f(x) = x^2$

$$
f(x_1) = (-0.577)^2 \approx 0.333 \\
f(x_2) = (0.577)^2 \approx 0.333
$$

So,

$$
\int_{-1}^{1} x^2 dx \approx 1 \cdot 0.333 + 1 \cdot 0.333 = 0.666
$$

### Step 3: Exact answer for comparison

$$
\int_{-1}^{1} x^2 dx = \left[ \frac{x^3}{3} \right]_{-1}^{1} = \frac{1}{3} - ( -\frac{1}{3}) = \frac{2}{3} \approx 0.6667
$$

---

## 🔍 How Are Nodes ($x_i$) Calculated?

The $x_i$ values are the **roots of Legendre polynomials** $P_n(x)$.

### What Are Legendre Polynomials?

These are orthogonal polynomials defined on $[-1, 1]$. They satisfy the recurrence:

$$
(n+1) P_{n+1}(x) = (2n+1)x P_n(x) - n P_{n-1}(x)
$$

With:

* $P_0(x) = 1$
* $P_1(x) = x$

### Example: Derive $P_2(x)$

$$
3P_2(x) = 3x^2 - 1 \Rightarrow P_2(x) = \frac{1}{2}(3x^2 - 1)
$$

### Solve $P_2(x) = 0$ to find nodes

$$
\frac{1}{2}(3x^2 - 1) = 0 \Rightarrow x = \pm\frac{1}{\sqrt{3}}
$$

So, the 2-point nodes are:

* $x_1 = -\frac{1}{\sqrt{3}}$
* $x_2 = +\frac{1}{\sqrt{3}}$

---

## 📜 First Few Legendre Polynomials

| n | $P_n(x)$                         |
| - | -------------------------------- |
| 0 | $1$                              |
| 1 | $x$                              |
| 2 | $\frac{1}{2}(3x^2 - 1)$          |
| 3 | $\frac{1}{2}(5x^3 - 3x)$         |
| 4 | $\frac{1}{8}(35x^4 - 30x^2 + 3)$ |

---

```
import numpy as np
from numpy.polynomial.legendre import leggauss

# Define the function to integrate
def f(x):
    return x**2

# Number of Gauss points
n = 2

# Get nodes (x) and weights (w) for n-point Gaussian quadrature
x, w = leggauss(n)

# Compute the integral approximation
integral = sum(wi * f(xi) for xi, wi in zip(x, w))

print("Approximated integral:", integral)

