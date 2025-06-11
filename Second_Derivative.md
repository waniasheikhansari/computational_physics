# Numerical Approximation of the Second Derivative

## Overview

This note explains how to approximate the second derivative of a function numerically using finite difference methods. We'll use the central difference formula and analyze its error.

---

## Formula for the Second Derivative

The second derivative is defined as the derivative of the first derivative:

```
f''(x) = d/dx [f'(x)]
```

Using the central difference method for the first derivative, we can write:

```
f'(x + h/2) ≈ [f(x + h) - f(x)] / h
f'(x - h/2) ≈ [f(x) - f(x - h)] / h
```

Now apply the central difference formula again:

```
f''(x) ≈ [f(x + h) - 2f(x) + f(x - h)] / h^2
```

This is the standard second-order central difference approximation.

---

## Taylor Expansion and Error Analysis

Using Taylor expansions:

```
f(x + h) = f(x) + h f'(x) + (h^2/2) f''(x) + (h^3/6) f'''(x) + (h^4/24) f⁽⁴⁾(x) + ...
f(x - h) = f(x) - h f'(x) + (h^2/2) f''(x) - (h^3/6) f'''(x) + (h^4/24) f⁽⁴⁾(x) - ...
```

Adding both:

```
f(x + h) + f(x - h) = 2f(x) + h^2 f''(x) + (h^4/12) f⁽⁴⁾(x) + ...
```

Solving for f''(x):

```
f''(x) ≈ [f(x + h) - 2f(x) + f(x - h)] / h^2 + O(h^2)
```

So the **truncation error** is of order `h^2`, with leading term:

```
error ≈ (h^2 / 12) * f⁽⁴⁾(x)
```

---

## Rounding Error

Each function evaluation has a rounding error of roughly `C * |f(x)|`.

* Three function calls → worst-case total error in numerator: `≈ 4C * |f(x)|`
* Total rounding error:

```
error ≈ (4C * |f(x)|) / h^2
```

---

## Total Error and Optimal h

Combining both sources:

```
Total Error e(h) = A * h^2 + B / h^2
```

Where:

* `A = (1/12) * |f⁽⁴⁾(x)|`
* `B = 4C * |f(x)|`

To minimize the total error, differentiate with respect to `h`, set to zero:

```
d(e)/dh = 2A * h - 2B / h^3 = 0
→ Optimal h = (B / A)^(1/4)
```

Substituting back gives minimum error:

```
e_min = 2 * sqrt(A * B)
```

If `f(x)` and `f⁽⁴⁾(x)` are of order 1:

```
e_min ≈ sqrt(C)
```

Which is typically \~1e-8 in double precision.

---

## Conclusion

* The central difference approximation for the second derivative is simple and widely used.
* It has an error of order `h^2`.
* Rounding error also plays a role and limits precision.
* The method is roughly as accurate as forward/backward difference for first derivatives.
* Higher-order formulas exist but are not covered here.

---

> 📘 **Equation Reference:** Eq. (5.109), (5.110), (5.111), (5.113), (5.114), (5.115) from the textbook.
