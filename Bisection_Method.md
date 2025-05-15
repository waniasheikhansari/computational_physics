# 📘 Bisection Method – Computing Physics Notes

## 📌 What is the Bisection Method?

The **Bisection Method** is a numerical technique to find **roots** of a **continuous** function. A *root* is a value of \( x \) where:

\[
f(x) = 0
\]

---

## ✅ Conditions for Bisection Method

- The function \( f(x) \) must be **continuous** on the interval \([a, b]\).
- The function must satisfy:
  
\[
f(a) \cdot f(b) < 0
\]

This means \( f(a) \) and \( f(b) \) have **opposite signs**, so the graph must cross the x-axis between them (by the **Intermediate Value Theorem**).

---

## 🔁 Bisection Algorithm Steps

1. Choose initial interval \([a, b]\) such that \( f(a) .f(b) < 0 \).
2. Compute midpoint:

\[c = \frac{a + b}{2}\]

3. Evaluate \( f(c) \):
   - If \( f(c) = 0 \), then \( c \) is the root.
   - If \( f(a) \cdot f(c) < 0 \), the root lies in \([a, c]\), so update \( b = c \).
   - If \( f(c) \cdot f(b) < 0 \), the root lies in \([c, b]\), so update \( a = c \).
4. Repeat steps until \( |b - a| \) is less than the desired tolerance.

---

## ✍️ Example: Find Root of \( f(x) = x^2 - 4 \)

We want to find a root in \([1, 3]\):

### Step 1: Check signs
\[
f(1) = 1^2 - 4 = -3 \\
f(3) = 9 - 4 = 5 \\
f(1) \cdot f(3) = -15 < 0 \quad \Rightarrow \text{Valid interval}
\]

### Step 2: Iterations

| Iteration | a   | b   | c = (a+b)/2 | f(c)          | Interval Selected |
|-----------|-----|-----|-------------|----------------|------------------|
| 1         | 1   | 3   | 2.0         | \( f(2) = 0 \) | Root found       |

🎉 **Root is exactly at** \( x = 2 \)

---

## 🧠 Why Do We Multiply \( f(a) \cdot f(b) \) or \( f(a) \cdot f(c) \)?

To check if the function **changes sign** between two points:
- If product is **negative** → signs are opposite → **root exists** between them
- If product is **positive** → no root in that subinterval

---

## 📎 Applications

Used in:
- Physics (motion, energy)
- Engineering (equilibrium, design)
- Computing (when algebraic solutions are hard)
- Anywhere numerical solutions to \( f(x) = 0 \) are needed

---

## 📂 Source Code (Python)

```python
def f(x):
    return x**2 - 4

def bisection(a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return None
    
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

root = bisection(1, 3)
print(f"Root found: {root}")
```

## 🎯 Bisection Method Example – Projectile Motion

We solve for the time \( t \) when a projectile hits the ground using:

\[
h(t) = 50t - 4.9t^2
\]

We want \( h(t) = 0 \) (i.e., when the height becomes zero).

---

### 🐍 Python Code

```python
def h(t):
    return 50*t - 4.9*t**2

def bisection(a, b, tol=1e-6):
    if h(a) * h(b) >= 0:
        return None

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if h(c) == 0:
            return c
        elif h(a) * h(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

root = bisection(1, 20)
print(f"Projectile hits ground at t ≈ {root:.6f} seconds")
