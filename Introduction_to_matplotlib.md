# 📘 Matplotlib
It is widely used in visualizing data, functions, and simulation results. It works seamlessly with NumPy and SciPy.

```python
import numpy as np
import matplotlib.pyplot as plt
```

---

## 1. Line Plot
- Plot a simple line graph
```python
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
```

---

## 2. Scatter Plot
- Plot discrete data points
```python
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])

plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
```

---

## 3. Bar Plot
- Plot vertical bars
```python
categories = ['A', 'B', 'C']
values = [5, 7, 3]

plt.bar(categories, values)
plt.title("Bar Plot")
plt.show()
```

---

## 4. Histogram
- Show distribution of data
```python
data = np.random.randn(1000)

plt.hist(data, bins=30, color='green')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

---

## 5. Multiple Lines in One Plot
```python
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.legend()
plt.title("Multiple Lines")
plt.grid(True)
plt.show()
```

---

## 6. Subplots
- Create multiple plots in a grid
```python
x = np.linspace(0, 10, 100)

y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title("Sine")

plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.title("Cosine")

plt.tight_layout()
plt.show()
```

---

## 7. Saving Figures
- Save plot to a file
```python
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.savefig("sine_wave.png")
```
---

