# 📌 Secant Method – Numerical Root Finding

The **Secant Method** is a numerical technique used to find an approximate root of a real-valued function \( f(x) \), where \( f(x) = 0 \).

---

## 📐 Formula

$$
x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}
$$


---

## 🔁 Steps

1. Choose initial values \( x_0 \) and \( x_1 \)
2. Compute the next approximation \( x_2 \)
3. Check if \( |f(x_2)| \) is within your tolerance
4. If not, repeat the process using:
   - \( x_{n-1} \gets x_n \)
   - \( x_n \gets x_{n+1} \)

---

## ✅ Advantages

- No need to compute derivatives (unlike Newton-Raphson)
- Often converges faster than the Bisection Method

---

## ⚠️ Limitations

- Can diverge if initial guesses are poor
- Not guaranteed to converge
- May fail near local extrema (flat slope)

---

## 🔧 Example: \( f(x) = x^2 - 4 \)

Let:
- \( x_0 = 1 \), \( f(x_0) = -3 \)
- \( x_1 = 3 \), \( f(x_1) = 5 \)

Apply the formula:

\[
x_2 = 3 - \frac{5(3 - 1)}{5 - (-3)} = 3 - \frac{10}{8} = 1.75
\]

So, the next approximation is \( x_2 = 1.75 \)

---

### Use the Secant Method when:
- You don't have or can't easily compute the derivative
- You have two decent initial guesses close to the root

---

```
def f(x):
    return x**2 - 2

def secant(x0, x1, tol=1e-6, max_iter=10):
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            print("Division by zero.")
            return None
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        print(f"Iter {i+1}: x = {x2:.6f}, f(x) = {f(x2):.6f}")
        if abs(f(x2)) < tol:
            return x2
        x0, x1 = x1, x2
    return x2

secant(1, 2)
```
