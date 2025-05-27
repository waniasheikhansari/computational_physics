# Romberg Integration

##  What is Romberg Integration?

Romberg Integration is a **numerical integration technique** that improves upon the **trapezoidal rule** by using **Richardson extrapolation** to accelerate convergence.

It gives **very accurate results** with relatively **few function evaluations**, especially for **smooth functions**.

---

## Why Use Romberg Integration?

-  It **reuses** trapezoidal approximations at smaller step sizes.
-  It applies **Richardson extrapolation** to eliminate errors.
-  It is faster and more accurate than the trapezoidal or Simpson’s rule alone.
---

## Where is Romberg Integration Used?

- In **scientific computing** for accurate definite integrals.
- In **physics and engineering** simulations.
- In **machine learning** and **probability** when analytical integration is hard.
- When you need **high precision integration** of smooth functions.

---

## How Does It Work?

Romberg Integration builds a **triangular table** \( R_{n,m} \) using:
1. The **trapezoidal rule** to compute initial approximations.
2. **Richardson extrapolation** to combine results and remove error.

### Formula:
![Romberg Formula](https://latex.codecogs.com/png.image?\dpi{150}R_{n,m}=\frac{4^mR_{n,m-1}-R_{n-1,m-1}}{4^m-1})

---

## Example

Let's integrate the function f(x) = 1 ⁄ (1 + x²) from 0 to 1.

```python
import numpy as np

def f(x):
    return 1 / (1 + x**2)

def trapezoidal(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])

def romberg(f, a, b, max_level=5):
    R = np.zeros((max_level, max_level))
    for i in range(max_level):
        n = 2**i
        R[i, 0] = trapezoidal(f, a, b, n)
        for j in range(1, i + 1):
            R[i, j] = (4**j * R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)
    return R

# Run Romberg integration
a, b = 0, 1
R = romberg(f, a, b, max_level=5)

# Print table
import pandas as pd
romberg_table = pd.DataFrame(R)
print(romberg_table.round(8))
