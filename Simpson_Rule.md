# Simpson’s Rule for Numerical Integration

## Introduction

Simpson’s Rule is a numerical method to approximate the definite integral of a function:

\[
\int_a^b f(x) \, dx
\]

It works by approximating the function \( f(x) \) using **parabolas** (quadratic polynomials) instead of straight lines, which often results in a more accurate approximation than the trapezoidal rule.

---

## Why Use Simpson’s Rule?

- Provides higher accuracy by fitting parabolas to the curve.
- More efficient: fewer points needed for desired accuracy.
- Works best for smooth functions.
- Requires an **even number** of subintervals.

---

## The Formula

Divide the interval \([a, b]\) into \(n\) equal subintervals (where \(n\) is even), each of width:

\[
h = \frac{b - a}{n}
\]

The approximate integral is:

\[
\int_a^b f(x) \, dx \approx \frac{h}{3} \left[ f(x_0) + 4 \sum_{\text{odd } i} f(x_i) + 2 \sum_{\text{even } i} f(x_i) + f(x_n) \right]
\]

Where:
- \(x_0 = a\), \(x_n = b\)
- \(x_i = a + i \cdot h\)
- The sums are over the function values at odd and even indexed points respectively, excluding the first and last.

---

## Step-by-Step Calculation

1. **Divide the interval** \([a,b]\) into \(n\) equal parts, where \(n\) is even.
2. **Calculate the step size**:

   \[
   h = \frac{b - a}{n}
   \]

3. **Calculate the sample points**:

   \[
   x_i = a + i \times h, \quad i=0,1,2,\ldots,n
   \]

4. **Evaluate the function** at each \(x_i\):

   \[
   y_i = f(x_i)
   \]

5. **Apply Simpson’s Rule formula**:

   \[
   \text{Integral} \approx \frac{h}{3} \left( y_0 + 4(y_1 + y_3 + \cdots + y_{n-1}) + 2(y_2 + y_4 + \cdots + y_{n-2}) + y_n \right)
   \]

---

## Example Calculation

Estimate \(\int_0^1 x^2 \, dx\) with \(n=4\):

- \(a=0\), \(b=1\), \(n=4\) (even)
- \(h = \frac{1-0}{4} = 0.25\)
- Points: \(x_0=0\), \(x_1=0.25\), \(x_2=0.5\), \(x_3=0.75\), \(x_4=1\)
- Function values:  
  \(f(0)=0^2=0\)  
  \(f(0.25)=(0.25)^2=0.0625\)  
  \(f(0.5)=(0.5)^2=0.25\)  
  \(f(0.75)=(0.75)^2=0.5625\)  
  \(f(1) = 1^2=1\)

Apply formula:

\[
\begin{aligned}
\int_0^1 x^2 dx &\approx \frac{0.25}{3} \left[ 0 + 4(0.0625 + 0.5625) + 2(0.25) + 1 \right] \\
&= \frac{0.25}{3} \left[ 0 + 4(0.625) + 0.5 + 1 \right] \\
&= \frac{0.25}{3} \left[ 0 + 2.5 + 0.5 + 1 \right] \\
&= \frac{0.25}{3} \times 4 \\
&= \frac{1}{3} \approx 0.3333
\end{aligned}
\]

This matches the exact value of \(\frac{1}{3}\).

---

## Python Code Example

```python
import numpy as np

def f(x):
    return x**2

a, b = 0, 1
n = 4  # must be even

x_points = np.linspace(a, b, n + 1)
y_points = f(x_points)

h = (b - a) / n

simpson_approx = (h / 3) * (y_points[0] + 
                            4 * np.sum(y_points[1:n:2]) +  # odd indices
                            2 * np.sum(y_points[2:n-1:2]) +  # even indices
                            y_points[n])

print("Simpson's Rule Approximation:", simpson_approx)
print("Exact value:", 1/3)
