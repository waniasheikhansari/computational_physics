# 📘 SciPy
It provides tools for optimization, integration, interpolation, linear algebra, signal processing, and solving differential equations—essential in computational physics.

---

## 1. scipy.optimize.root_scalar
- Find the root of a scalar function
```python
from scipy.optimize import root_scalar

result = root_scalar(lambda x: x**2 - 2, bracket=[1, 2])
print(result.root)
```

## 2. scipy.optimize.newton
- Use Newton-Raphson method to find roots
```python
from scipy.optimize import newton

root = newton(lambda x: x**2 - 2, x0=1.5)
print(root)
```

## 3. scipy.integrate.quad
- Perform definite integration
```python
from scipy.integrate import quad

result, error = quad(lambda x: x**2, 0, 1)
print(result)
```

## 4. scipy.integrate.dblquad
- Perform double integration over a region
```python
from scipy.integrate import dblquad

result, error = dblquad(lambda x, y: x * y, 0, 1, lambda x: 0, lambda x: 1)
print(result)
```

## 5. scipy.integrate.solve_ivp
- Solve ordinary differential equations (ODEs)
```python
from scipy.integrate import solve_ivp

def dydt(t, y):
    return -2 * y

solution = solve_ivp(dydt, (0, 5), [1])
print(solution.y)
```

## 6. scipy.linalg.solve
- Solve linear system Ax = b
```python
from scipy.linalg import solve
import numpy as np

A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = solve(A, b)
print(x)
```

## 7. scipy.linalg.inv
- Find the inverse of a matrix
```python
from scipy.linalg import inv
import numpy as np

A = np.array([[1, 2], [3, 4]])
print(inv(A))
```

## 8. scipy.linalg.eig
- Compute eigenvalues and eigenvectors
```python
from scipy.linalg import eig
import numpy as np

A = np.array([[4, -2], [1, 1]])
values, vectors = eig(A)
print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)
```

## 9. scipy.fft.fft and scipy.fft.ifft
- Fast Fourier Transform and its inverse
```python
from scipy.fft import fft, ifft
import numpy as np

x = np.array([1, 2, 3, 4])
fft_result = fft(x)
ifft_result = ifft(fft_result)
print("FFT:", fft_result)
print("Inverse FFT:", ifft_result)
```

## 10. scipy.constants
- Access physical and mathematical constants
```python
from scipy.constants import pi, c, G

print("Pi:", pi)
print("Speed of light (m/s):", c)
print("Gravitational constant:", G)
```
---



