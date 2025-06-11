# Higher-Order Approximations for Derivatives

This explains how we can improve numerical derivative approximations by fitting higher-order polynomials to data points around the point of interest. It is based on the discussion in *Computational Physics* by Mark Newman.

* Instead of using just two points (as in forward, backward, or central difference), fit a polynomial (quadratic, cubic, etc.) to several points near the point where the derivative is needed.
* Higher-order fits can reduce approximation error.

---

## Basic Case: Quadratic Approximation

Assume we're estimating $f'(0)$ using a quadratic polynomial:

$y = ax^2 + bx + c$

Choose 3 symmetric points: $x = -h, 0, +h$.

### Equations from data:

```
a h^2 - b h + c = f(-h)
c = f(0)
a h^2 + b h + c = f(h)
```

Subtracting the first and third equations:

```
2bh = f(h) - f(-h)  =>  b = [f(h) - f(-h)] / (2h)


```

Since $b = f'(0)$, we get:

### Central Difference Formula:

$$
\frac{df}{dx} \approx \frac{f(x+h) - f(x-h)}{2h}
$$

> Note: Even with a quadratic fit, the result is the same as the central difference. No improvement yet.

---

## Going Beyond: Higher-Order Fits

Using more points and fitting higher-degree polynomials (cubic, quartic, etc.) does give better derivative estimates.

* **Cubic Fit**: Requires 4 points (e.g., $-3h, -h, h, 3h$)
* **Quartic Fit**: Requires 5 points (e.g., $-2h, -h, 0, h, 2h$)

### Method:

1. Write polynomial $P(x) = a_n x^n + \dots + bx + c$
2. Plug in known function values at sampled points.
3. Solve the resulting system for coefficient $b$, which is $f'(x)$.
4. Final formula is a weighted sum of function values, divided by $h$.

---

## Table 5.1

| Degree  | Sample Points (centered at 0) | Coefficients (example form)               | Error Order |
| ------- | ----------------------------- | ----------------------------------------- | ----------- |
| Linear  | $-h, h$                       | $[f(h) - f(-h)] / 2h$                     | $O(h^2)$    |
| Cubic   | $-3h, -h, h, 3h$              | $[-f(3h) + 9f(h) - 9f(-h) + f(-3h)] / 8h$ | $O(h^4)$    |
| Quartic | $-2h, -h, 0, h, 2h$           | More complex...                           | $O(h^4)$    |

---

## Final Notes

* In most practical cases, central difference is good enough.
* Higher-order methods become useful when high accuracy is needed and more data is available.
* Always balance **approximation error** with **rounding error** by choosing a suitable $h$.

---

