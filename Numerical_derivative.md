# Numerical Derivatives

Numerical differentiation is the process of estimating the derivative of a function using its values at certain points. It's the numerical opposite of integration.

---

## Why Are Numerical Derivatives Less Common?

1. **Simplicity**: The techniques are straightforward.
2. **Analytical Availability**: If a function is known, we can differentiate it exactly.
3. **Stability Issues**: Numerical derivatives can be unstable and prone to large errors.

However, they're essential in some fields like solving **partial differential equations**.

---

## Basic Derivative Definition

In calculus, the derivative of a function $f(x)$ is:

```
df/dx = lim(h -> 0) [f(x + h) - f(x)] / h
```

In numerical methods, we approximate this with a small `h`.

---

## Forward Difference Method

Approximates the derivative at a point `x`:

```
df/dx ≈ [f(x + h) - f(x)] / h
```

* Measures slope in the **forward (positive)** direction from `x`.
* This is known as the **forward difference**.

---

## Backward Difference Method

Approximates the derivative at a point `x`:

```
df/dx ≈ [f(x) - f(x - h)] / h
```

* Measures slope in the **backward (negative)** direction from `x`.
* This is known as the **backward difference**.

---

## Comparison and Use

| Situation                      | Method               |
| ------------------------------ | -------------------- |
| General use                    | Either               |
| Function domain has a boundary | Use forward/backward |
| Discontinuity at `x`           | Choose carefully     |

Both methods give similar results in most cases. However, at domain boundaries or discontinuities, only one may be usable.

---

## ⚠️ Choosing the Step Size `h`

* Too **large**: High **truncation error**.
* Too **small**: High **round-off error**.

Best value for `h` balances these errors.

---

## Geometric Interpretation

The derivative is the slope of the curve `f(x)` at point `x`.

* **Forward difference**: Slope of the secant line from `x` to `x + h`
* **Backward difference**: Slope of the secant line from `x - h` to `x`

---

## Example 

```python
import numpy as np

def f(x):
    return np.sin(x)

def forward_diff(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

def backward_diff(f, x, h=1e-5):
    return (f(x) - f(x - h)) / h

x = np.pi / 4
print("Forward Difference:", forward_diff(f, x))
print("Backward Difference:", backward_diff(f, x))
print("Exact Derivative (cos):", np.cos(x))
```
---
# Errors in Numerical Derivatives

When computing derivatives using **forward** or **backward differences**, the results are not perfectly accurate. There are two key sources of error:

1. **Rounding Error:** Caused by limitations in computer precision (discussed in Section 4.2).
2. **Approximation Error:** Because we cannot actually take the limit $h \to 0$, we only approximate the derivative.

Unlike numerical integration (where rounding errors are often negligible), both error types play significant roles when computing numerical derivatives.

---

## Forward Difference Error Analysis

We analyze errors using the **Taylor expansion**:

$$
f(x + h) = f(x) + h f'(x) + \frac{h^2}{2} f''(x) + \dots
$$

Rearranging:

$$
\frac{f(x + h) - f(x)}{h} = f'(x) + \frac{h}{2} f''(x) + \dots \tag{5.90}
$$

### Approximation Error

* Neglecting higher-order terms introduces **approximation error**.
* To leading order:

$$
\text{Approximation Error} \approx \frac{h}{2} |f''(x)|
$$

So, **smaller** $h$ leads to **more accuracy**, up to a point.

### Rounding Error

If $h$ is too small:

* $f(x + h)$ and $f(x)$ become very close.
* Subtracting nearly equal numbers causes large **rounding errors**.

From Section 4.2:

* Let $C$ be the relative error constant (typically $C \approx 10^{-16}$ in Python).
* Then:

$$
\text{Rounding Error} \approx \frac{2C |f(x)|}{h}
$$

---

## Total Error

Let total error $\epsilon$ be the sum of rounding and approximation errors:

$$
\epsilon(h) = \frac{2C |f(x)|}{h} + \frac{h}{2} |f''(x)| \tag{5.91}
$$

To find optimal $h$, minimize $\epsilon(h)$:

$$
\frac{d\epsilon}{dh} = -\frac{2C |f(x)|}{h^2} + \frac{1}{2} |f''(x)| = 0
$$

Solving gives:

$$
h = \sqrt{\frac{4C |f(x)|}{|f''(x)|}} \tag{5.93}
$$

### Final Error Estimate

Substitute optimal $h$ into error formula:

$$
\epsilon = \sqrt{4C |f(x)| |f''(x)|} \tag{5.94}
$$

If $f(x)$ and $f''(x) \approx 1$:

* $h \approx \sqrt{C} \approx 10^{-8}$
* $\epsilon \approx 10^{-8}$

---


