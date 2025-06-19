# Euler's Method - Markdown Notes

## ✨ What is Euler’s Method?

Euler’s Method is a numerical technique for solving first-order differential equations of the form:

$\frac{dx}{dt} = f(x, t)$

Given an initial condition:

$x(t = a) = x_0$

We use Euler's method to estimate the values of $x(t)$ at evenly spaced points.

---

## 🔹 Basic Idea

Using Taylor expansion:

$x(t+h) = x(t) + h \cdot \frac{dx}{dt} + \frac{h^2}{2!} \cdot \frac{d^2x}{dt^2} + \cdots$

Ignoring higher-order terms, we get:

$x(t+h) \approx x(t) + h \cdot f(x, t)$

This is the **Euler update rule**:

$x_{\text{next}} = x_{\text{current}} + h \cdot f(x_{\text{current}}, t_{\text{current}})$

---

## 📉 Python Code Example

```python
from math import sin
from numpy import arange
from pylab import plot, xlabel, ylabel, show

def f(x, t):
    return -x**3 + sin(t)

a = 0.0      # Start of interval
b = 10.0     # End of interval
N = 1000     # Number of steps
h = (b-a)/N  # Step size

x = 0.0      # Initial condition

tpoints = arange(a, b, h)
xpoints = []

for t in tpoints:
    xpoints.append(x)
    x += h * f(x, t)

plot(tpoints, xpoints)
xlabel("t")
ylabel("x(t)")
show()
```

---

## ⚡ Accuracy and Error

* **Each step error:** $\sim h^2$ (local error)
* **Total error:** $\sim h$ (global error)
* Smaller $h$ means better accuracy but more computation

### Error Formula (Approx):

$\text{Total Error} \approx h \cdot [f(x(b), b) - f(x(a), a)]$

---

## 🔶 Pros and Cons

| Feature             | Euler’s Method         | Runge-Kutta Method           |
| ------------------- | ---------------------- | ---------------------------- |
| Accuracy            | Low (error $\sim h$)   | High (e.g., RK4: $\sim h^4$) |
| Complexity          | Very simple            | More complex                 |
| Time per step       | Very fast              | Slightly slower              |
| Overall Performance | OK for rough estimates | Much better for precision    |


