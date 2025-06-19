# Second-Order Runge-Kutta Method 

While Euler's method uses a **first-order Taylor expansion**, we can try to increase accuracy by using higher-order terms. However, directly using Taylor series requires derivatives of $f$, which may not be explicitly available or convenient to compute.

The **second-order Runge-Kutta method**, also known as the **midpoint method**, avoids the need for explicit derivatives and offers **much better accuracy** than Euler's method.

---

## Concept

Euler's method uses the slope at $t$ to estimate $x(t + h)$:

$x(t + h) = x(t) + h \cdot f(x, t)$

Second-order Runge-Kutta improves this by using the slope at the **midpoint** $t + h/2$.

---

##  Step-by-Step Algorithm

Let:

* $k_1 = h \cdot f(x, t)$
* $k_2 = h \cdot f(x + 0.5 \cdot k_1, t + 0.5 \cdot h)$
* $x(t + h) = x(t) + k_2$

This is the **midpoint method** — second-order Runge-Kutta:

```math
\begin{aligned}
k_1 &= h \cdot f(x, t) \\
k_2 &= h \cdot f\left(x + \frac{1}{2}k_1, t + \frac{1}{2}h\right) \\
x_{\text{next}} &= x + k_2
\end{aligned}
```

---

##  Accuracy

* Local error: $\mathcal{O}(h^3)$
* Global error: $\mathcal{O}(h^2)$
* Much better than Euler (which has global error $\mathcal{O}(h)$)

Although we approximate $x(t + h/2)$ using Euler's method, it does **not degrade** the overall accuracy — proven by Taylor expansion.

---

##  Python Code Example

```python
from math import sin
from numpy import arange
from pylab import plot, xlabel, ylabel, show

def f(x, t):
    return -x**3 + sin(t)

a = 0.0
b = 10.0
N = 10  # Try 10, 20, 50, 100
h = (b - a) / N

x = 0.0
xpoints = []
tpoints = arange(a, b, h)

for t in tpoints:
    xpoints.append(x)
    k1 = h * f(x, t)
    k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
    x += k2

plot(tpoints, xpoints)
xlabel("t")
ylabel("x(t)")
show()
```

---

##  Visual Comparison

* Run with **N = 10, 20, 50, 100**
* Results show that small N (10 or 20) is inaccurate
* For N = 50 and N = 100, the solution **converges**
* Accuracy with N = 100 is similar to Euler's method with N = 1000

