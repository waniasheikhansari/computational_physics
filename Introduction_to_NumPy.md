# 📘 NumPy 
NumPy is a core library for numerical and scientific computing in Python. It provides support for arrays, mathematical operations, and various tools required in computational physics.
---

## 1. np.array
- Create an array from a list

```python
import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
```
## 2. np.zeros(n) 
Create an array of zeros
```
z = np.zeros(4)
print(z)
```
## 3. np.ones(n) 
Create an array of ones
```
o = np.ones(3)
print(o)
```
## 4. np.linspace(start, stop, num) 
Create evenly spaced numbers
```
x = np.linspace(0, 10, 5)
print(x)
```
## 5. np.arange(start, stop, step)
Range of numbers
```
r = np.arange(0, 10, 2)
print(r)
```
## 6. np.reshape(array, new_shape)
Reshape an array
```
a = np.array([1, 2, 3, 4, 5, 6])
reshaped = a.reshape(2, 3)
print(reshaped)
```
## 7. np.sum(array) 
Sum of elements
```
arr = np.array([1, 2, 3])
print(np.sum(arr))
```
## 8. np.mean(array) 
Mean value
```
arr = [2,4,9,0,5]
print(np.mean(arr))
```
## 9. np.std(array) 
Standard deviation
```
print(np.std(arr))
```
## 10. np.min(array) and np.max(array)
Min/Max values
```
print(np.min(arr))
print(np.max(arr))
```
## 11. np.dot(a, b) 
Dot product
```
a = np.array([1, 2])
b = np.array([3, 4])
print(np.dot(a, b))
```

## 12. Math functions
np.sin, np.cos, np.exp, np.sqrt
```
x = np.array([0, np.pi/2, np.pi])
print(np.sin(x))
print(np.cos(x))

x = np.array([0, 1, 2])
print(np.exp(x))

x = np.array([1, 4, 9])
print(np.sqrt(x))
```
## 13. np.log(array)
Natural logarithm
```
x = np.array([1, np.e, np.e**2])
print(np.log(x))
```
## 14. Element-wise operations
```
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
print(a * b)
```
## 15. Indexing and slicing
```
a = np.array([10, 20, 30, 40])
print(a[0])     # First element
print(a[-1])    # Last element
print(a[1:3])   # Slice from index 1 to 2
```
## 16. Shape and size
```
a = np.array([[1, 2], [3, 4]])
print(a.shape)
print(a.size)
```
## 17. Transpose of array
```
a = np.array([[1, 2], [3, 4]])
print(a.T)
```
## 18. Random numbers
```
print(np.random.rand(3))          # Random floats
print(np.random.randint(1, 10, 3)) # Random integers
```
## 19. Identity matrix
```
print(np.eye(3))
```
## 20. Diagonal elements
```
a = np.array([[1, 2], [3, 4]])
print(np.diag(a))
```
## 21. Flatten array
```
a = np.array([[1, 2], [3, 4]])
print(a.flatten())
```
