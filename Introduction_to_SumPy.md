# 📘 SymPy
It allows for algebraic manipulations, calculus, equation solving, and symbolic integration/differentiation, making it valuable in theoretical and computational physics.

```python
import sympy as sp
```

---

## 1. Symbols
- Define symbolic variables
```python
x, y = sp.symbols('x y')
```

---

## 2. sp.expand()
- Expand algebraic expressions
```python
expr = (x + 2)**2
print(sp.expand(expr))
```

---

## 3. sp.factor()
- Factor algebraic expressions
```python
expr = x**2 + 2*x + 1
print(sp.factor(expr))
```

---

## 4. sp.simplify()
- Simplify expressions
```python
expr = (x**2 - 1)/(x - 1)
print(sp.simplify(expr))
```

---

## 5. sp.solve()
- Solve equations
```python
equation = sp.Eq(x**2 - 2, 0)
solutions = sp.solve(equation, x)
print(solutions)
```

---

## 6. sp.diff()
- Differentiate expressions
```python
expr = sp.sin(x)*sp.exp(x)
print(sp.diff(expr, x))
```

---

## 7. sp.integrate()
- Integrate expressions
```python
expr = x * sp.exp(x)
indefinite = sp.integrate(expr, x)
definite = sp.integrate(expr, (x, 0, 1))

print("Indefinite:", indefinite)
print("Definite:", definite)
```

---

## 8. sp.limit()
- Compute limits
```python
expr = sp.sin(x)/x
limit_val = sp.limit(expr, x, 0)
print(limit_val)
```

---

## 9. sp.series()
- Taylor/Maclaurin series expansion
```python
expr = sp.sin(x)
series = sp.series(expr, x, 0, 6)
print(series)
```

---

## 10. sp.lambdify()
- Convert symbolic expressions to numerical functions
```python
f = sp.lambdify(x, sp.sin(x) + x**2)
print(f(2.0))
```
---

