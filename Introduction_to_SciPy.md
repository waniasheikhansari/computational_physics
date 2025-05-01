# 📘 SciPy
It provides tools for optimization, integration, interpolation, linear algebra, signal processing, and solving differential equations—essential in computational physics.

```python
import numpy as np
import scipy
```

---

## 1. scipy.optimize.root_scalar
- Find the root of a scalar function
```python
result = scipy.optimize.root_scalar(lambda x: x**2 - 2, bracket=[1, 2])
print(result.root)
```

## 2. scipy.optimize.newton
- Use Newton-Raphson method to find roots
```python
root = scipy.optimize.newton(lambda x: x**2 - 2, x0=1.5)
print(root)
```

## 3. scipy.integrate.quad
- Perform definite integration
```python
result, error = scipy.integrate.quad(lambda x: x**2, 0, 1)
print(result)
```

## 4. scipy.integrate.dblquad
- Perform double integration over a region
```python
result, error = scipy.integrate.dblquad(lambda x, y: x * y, 0, 1, lambda x: 0, lambda x: 1)
print(result)
```

## 5. scipy.integrate.solve_ivp
- Solve ordinary differential equations (ODEs)
```python
def dydt(t, y):
    return -2 * y

solution = scipy.integrate.solve_ivp(dydt, (0, 5), [1])
print(solution.y)
```

## 6. scipy.linalg.solve
- Solve linear system Ax = b
```python
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = scipy.linalg.solve(A, b)
print(x)
```

## 7. scipy.linalg.inv
- Find the inverse of a matrix
```python
A = np.array([[1, 2], [3, 4]])
print(scipy.linalg.inv(A))
```

## 8. scipy.linalg.eig
- Compute eigenvalues and eigenvectors
```python
A = np.array([[4, -2], [1, 1]])
values, vectors = scipy.linalg.eig(A)
print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)
```

## 9. scipy.fft.fft and scipy.fft.ifft
- Fast Fourier Transform and its inverse
```python
x = np.array([1, 2, 3, 4])
fft_result = scipy.fft.fft(x)
ifft_result = scipy.fft.ifft(fft_result)
print("FFT:", fft_result)
print("Inverse FFT:", ifft_result)
```

## 10. scipy.constants
- Access physical and mathematical constants
```python
print("Pi:", scipy.constants.pi)
print("Speed of light (m/s):", scipy.constants.c)
print("Gravitational constant:", scipy.constants.G)
```
---


