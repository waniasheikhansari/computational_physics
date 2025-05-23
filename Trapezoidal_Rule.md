# 📐 Trapezoidal Rule – Numerical Integration

## 🧮 What is the Trapezoidal Rule?

The **Trapezoidal Rule** is a numerical method to estimate the **definite integral** of a function `f(x)` over an interval `[a, b]`.  
It approximates the area under the curve using **trapezoids** instead of rectangles.

---

## 🔢 Formula (Single Interval)

<pre> ∫ᵃᵇ f(x) dx ≈ (b - a)/2 × [f(a) + f(b)] </pre>
---

## 🧠 Composite Trapezoidal Rule (Multiple Intervals)

Divide `[a, b]` into `n` equal subintervals of width:

$h = \frac{b - a}{n}$


Then the approximation becomes:

$$
\int_a^b f(x) \, dx \approx \frac{h}{2} \left[ f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]
$$


Where:
- \( x_0 = a \), \( x_n = b \)  
- xᵢ = a + i · h  for i = 1, 2, ..., n−1


---

## 📊 Example: ∫₀¹ x² dx using n = 4

Let \( f(x) = x^2 \), \( a = 0 \), \( b = 1 \), and \( n = 4 \)

### Step-by-step:

- \( h = (1 - 0)/4 = 0.25 \)
- \( x_i = 0, 0.25, 0.5, 0.75, 1 \)
- \( f(x_i) = 0, 0.0625, 0.25, 0.5625, 1 \)

$$
\int_0^1 x^2 \, dx \approx \frac{0.25}{2} \left[ 0 + 2(0.0625 + 0.25 + 0.5625) + 1 \right] = 0.34375
$$


### ✅ Exact value:

<pre> ∫₀¹ x² dx = 1/3 ≈ 0.3333 </pre>
---
```
def f(x):
    return x**2

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        result += 2 * f(x_i)

    result *= h / 2
    return result

# Example
a = 0
b = 2
n = 4

approx = trapezoidal_rule(f, a, b, n)
print(f"Approximate integral using Trapezoidal Rule: {approx}")

```
---
## 📈 Visualization (Python Code)

```python
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**2
a, b = 0, 1
n = 4
x = np.linspace(a, b, 100)
y = f(x)

x_axis = np.linspace(a, b, n + 1)
y_axis = f(x_axis)


plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b', label='$f(x) = x^2$', linewidth=2)  # Smooth curve
plt.plot(x_axis, y_axis, 'ro', label='Sample points')  # Sample points

for i in range(n):
    xs = [x_axis[i], x_axis[i], x_axis[i+1], x_axis[i+1]]
    ys = [0, y_axis[i], y_axis[i+1], 0]
    plt.fill(xs, ys, 'skyblue', edgecolor='black', alpha=0.5)

plt.title("Trapezoidal Rule Approximation of $\\int_0^1 x^2 dx$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()


h = (b - a) / n
trapezoidal_approx = (y_axis[0] + y_axis[-1] + 2 * np.sum(y_points[1:-1])) * h / 2
print("Trapezoidal Rule Approximation:", trapezoidal_approx)



