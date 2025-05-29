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
```
### Example 
Evaluate the integral:

∫[1 to 3] (2x² + 3x + 1) dx

using **2-point Gaussian quadrature**.

---

## Step 1: Gauss-Legendre Nodes and Weights (n = 2)

For 2-point Gauss quadrature on [-1, 1]:

- Nodes:
  ξ₁ = -1/√3 ≈ -0.57735  
  ξ₂ = +1/√3 ≈ +0.57735

- Weights:
  w₁ = 1  
  w₂ = 1

---

## Step 2: Transform Interval [1, 3] to [-1, 1]

Use the transformation:

x = ((b - a) / 2) * ξ + (b + a) / 2  
x = ((3 - 1) / 2) * ξ + (3 + 1) / 2  
x = ξ + 2

So:

- x₁ = -1/√3 + 2 ≈ 1.42265  
- x₂ = +1/√3 + 2 ≈ 2.57735

---

## Step 3: Evaluate the Function at Transformed Nodes

f(x) = 2x² + 3x + 1

- f(x₁) ≈ f(1.42265) ≈ 9.316  
- f(x₂) ≈ f(2.57735) ≈ 22.021

---

## Step 4: Apply Gaussian Quadrature Formula

∫[1 to 3] f(x) dx ≈ (b - a)/2 * [ w₁ * f(x₁) + w₂ * f(x₂) ]  
                 ≈ (3 - 1)/2 * [9.316 + 22.021]  
                 ≈ 1 * 31.337  
                 ≈ **31.34**

---

## Final Answer

Approximate value: **31.34**

```
import numpy as np

# Function to integrate
def f(x):
    return x**4 - 2*x + 1

x_nodes, w_weights = np.polynomial.legendre.leggauss(3)

a, b = 0, 2
def transform(x):
    return 0.5*(b - a)*x + 0.5*(b + a)

integral = 0.5 * (b - a) * np.sum(w_weights * f(transform(x_nodes)))

print(f"Gaussian quadrature approximation (n=3): {integral}")
```
