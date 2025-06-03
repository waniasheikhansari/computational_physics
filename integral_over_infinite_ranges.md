**INTEGRALS OVER INFINITE RANGES**

In physics and applied math, we often deal with integrals over infinite limits, such as:

$\int_0^\infty f(x)\, dx$

Standard numerical methods don’t directly apply to these because they can't handle infinite limits. **Solution**: change the variable to transform the infinite range into a finite one.

---

### Common Change of Variables

**1. From 0 to ∞**

Use: $x = \frac{z}{1 - z} \Rightarrow dx = \frac{dz}{(1 - z)^2}$

Then:
$\int_0^\infty f(x)\, dx = \int_0^1 f\left(\frac{z}{1 - z}\right) \frac{dz}{(1 - z)^2}$

You can then use standard methods like trapezoidal, Simpson's rule, or **Gaussian quadrature**.

**2. From a to ∞**

Use: $x = a + \frac{z}{1 - z} \Rightarrow dx = \frac{dz}{(1 - z)^2}$

$\int_a^\infty f(x)\, dx = \int_0^1 f\left(a + \frac{z}{1 - z}\right) \frac{dz}{(1 - z)^2}$

**3. From −∞ to ∞**

Split into two parts or use:
$x = \tan\left(\frac{\pi(z - 0.5)}{2}\right) \Rightarrow dx = \frac{\pi}{2 \cos^2\left(\frac{\pi(z - 0.5)}{2}\right)} dz$

Then:
$\int_{-\infty}^\infty f(x)\, dx = \int_0^1 f(x(z)) \cdot \frac{\pi}{2 \cos^2\left(\frac{\pi(z - 0.5)}{2}\right)} dz$

---

### Example (Gaussian Quadrature)

Evaluate:
$\int_0^\infty e^{-x^2} dx$

Change variable: $x = \frac{z}{1 - z}$

Then the integral becomes:
$\int_0^1 \frac{e^{-\left(\frac{z}{1 - z}\right)^2}}{(1 - z)^2} dz$

Use Gaussian quadrature with 50 points, and you'll get:
$\approx 0.886226925 \quad \text{(matches known value)}$

This shows **how effective** these change-of-variable methods are.

```
# Example 5.3: Compute the integral of exp(-x^2) from 0 to infinity using Gaussian quadrature

from gaussxw import gaussxwab
from math import exp

def f(z):
    return exp(-z**2 / (1 - z)**2) / (1 - z)**2
N = 50

a = 0.0
b = 1.0
x, w = gaussxwab(N, a, b)
s = 0.0
for k in range(N):
    s += w[k] * f(x[k])

print("Integral ≈", s) 
