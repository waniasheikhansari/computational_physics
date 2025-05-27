# Higher Order Integration

Higher order integration methods provide more accurate numerical integration by reducing the error term more effectively than basic methods like the trapezoidal rule. These methods use higher-degree polynomial interpolation or extrapolation techniques to approximate the integral.

---

## What is Higher Order Integration?

- **Order** refers to the degree of accuracy of a numerical integration method.
- Higher order methods have error terms that shrink faster as the step size \( h \) decreases.
- They typically approximate the integrand using higher-degree polynomials or combine simpler methods with extrapolation.

---

## Common Numerical Integration Methods and Their Order

| Method              | Interpolation Type            | Polynomial Degree | Error Order       | Notes                             |
|---------------------|------------------------------|-------------------|-------------------|----------------------------------|
| Trapezoidal Rule    | Linear interpolation          | 1 (straight line) | \(O(h^2)\)        | Simple, but less accurate         |
| Simpson's Rule      | Quadratic interpolation       | 2 (parabola)      | \(O(h^4)\)        | More accurate for smooth functions|
| Romberg Integration | Polynomial extrapolation      | Based on trapezoidal | Improves order by repeated extrapolation | Uses Richardson extrapolation to accelerate convergence |
| Gaussian Quadrature | Optimized polynomial points   | Varies            | Very high order   | Uses optimal points for polynomials |

---

# Higher Order Integration Example

## Example: Comparing Trapezoidal Rule and Simpson’s Rule

Integrate the function  
f(x) = 1 / (1 + x²)  
over the interval [0, 1].

---

### Exact value:

The integral is  
∫₀¹ 1/(1+x²) dx = arctan(1) - arctan(0) = π/4 ≈ 0.7854

---

### Trapezoidal Rule (1 interval):

Approximate using  
T = (1/2) × [f(0) + f(1)] = (1/2) × [1 + 0.5] = 0.75

Error ≈ 0.0354

---

### Simpson’s Rule (2 intervals):

Step size h = (1 - 0) / 2 = 0.5, and  
S = (h/3) × [f(0) + 4 × f(0.5) + f(1)]

Calculate function values:  
f(0) = 1  
f(0.5) = 1 / (1 + 0.5²) = 0.8  
f(1) = 0.5

So,  
S = (0.5 / 3) × [1 + 4 × 0.8 + 0.5] = (0.5 / 3) × 4.7 = 0.7833

Error ≈ 0.0021

---

Simpson’s rule provides a much better approximation than the trapezoidal rule for the same number of intervals because it uses quadratic interpolation rather than linear.


Simpson’s rule is more accurate because it uses **quadratic interpolation** rather than linear.

---

## Interpolation in Numerical Integration

- **Trapezoidal Rule:** Uses **linear interpolation** between points.
- **Simpson’s Rule:** Uses **quadratic interpolation** (fitting a parabola).
- **Romberg Integration:** Uses **polynomial extrapolation** on integral estimates to increase accuracy.




