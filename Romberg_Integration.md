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
# Romberg Integration Example

We want to approximate the integral:

```
∫₀¹ 1 / (1 + x²) dx
```

This is the integral of:

```
f(x) = 1 / (1 + x²)
```

The exact value is:

```
arctan(1) - arctan(0) = π / 4 ≈ 0.7854
```

---

## Step 1: Trapezoidal Approximation (Level 0)

We start with one trapezoid:

```
R(0, 0) = (1 - 0)/2 * [f(0) + f(1)]
        = 1/2 * [1 + 1/2]
        = 0.75
```

---

## Step 2: Two Intervals (Level 1)

Evaluate at midpoint `x = 0.5`:

```
f(0.5) = 1 / (1 + 0.25) = 0.8

R(1, 0) = 1/4 * [f(0) + 2*f(0.5) + f(1)]
        = 1/4 * [1 + 2*0.8 + 0.5]
        = 1/4 * 3.1 = 0.775
```

---

## Step 3: Romberg Extrapolation

Apply Richardson extrapolation:

```
R(1, 1) = (4^1 * R(1,0) - R(0,0)) / (4^1 - 1)
        = (4 * 0.775 - 0.75) / 3
        = (3.1 - 0.75) / 3
        = 0.7833
```

---

## Romberg Table (Partial)

| n | m | R(n, m) |
| - | - | ------- |
| 0 | 0 | 0.7500  |
| 1 | 0 | 0.7750  |
| 1 | 1 | 0.7833  |

---

## ✅ Final Approximate Value

```
R(1, 1) ≈ 0.7833
Exact value = π / 4 ≈ 0.7854
```



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
