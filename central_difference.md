## Central Differences

### Concept

Forward and backward differences are first-order accurate approximations of a derivative. A better method is the **central difference**, which increases the accuracy by symmetrically evaluating points around `x`.

The central difference formula:

```
f'(x) ≈ [f(x + h/2) - f(x - h/2)] / h     
```

### Derivation Using Taylor Expansions

We expand `f(x + h/2)` and `f(x - h/2)`:

```
f(x + h/2) = f(x) + (h/2)f'(x) + (h^2/8)f''(x) + ...    
f(x - h/2) = f(x) - (h/2)f'(x) + (h^2/8)f''(x) - ...     
```

Subtracting and rearranging:

```
f'(x) ≈ [f(x + h/2) - f(x - h/2)] / h - (h^2/24)f'''(x) 
```

**Error Analysis**:

* Approximation error: \~ (h^2/24)|f'''(x)|
* Rounding error: \~ 2C|f(x)| / h
* Total error:

```
ε(h) = (2C * |f(x)|) / h + (h^2 / 24) * |f'''(x)|      
```

Minimizing error:

```
h = [12C * |f(x)| / |f'''(x)|]^(1/3)                 
ε = [108C^2 * |f(x)|^2 * |f'''(x)|]^(1/3)             
```

### Accuracy Comparison

* If `|f(x)| ≈ 1` and `|f'''(x)| ≈ 1`:

  * Optimal `h ≈ C^{1/3} ≈ 10^-5`
  * Optimal error `ε ≈ C^{2/3} ≈ 10^-7`

Thus, central difference is about 100× more accurate than forward/backward differences.

### Application to Sampled Data

When you only have values at intervals of `h`, you can't compute `f(x ± h/2)`.
Instead, use:

```
f'(x) ≈ [f(x + h) - f(x - h)] / (2h)                
```

* This uses 2h spacing, so error is larger than ideal central difference.
* But still better than forward/backward if `h` is small enough.

### Special Case

If you want the derivative at a point **between** samples (e.g., at `x = midpoint`), you can use the original:

```
f'(x) ≈ [f(x + h/2) - f(x - h/2)] / h
```

which gives the most accurate result with samples at `x ± h/2`.

### Example 5.4: Sampled Function Derivative

Given: `f(x) = 1 + tanh(2x)`

* Define `f(x)` in Python.
* Use central difference to approximate the derivative.
* Compare to the analytic derivative:

```
f'(x) = 2 * sech^2(2x)
```

``` 
import numpy as np
import matplotlib.pyplot as plt

# Define the function and its analytic derivative
def f(x):
    return 1 + np.tanh(2 * x)

def df_analytic(x):
    return 2 / np.cosh(2 * x)**2  # sech^2(2x)

# Central difference approximation
def df_numerical(x, h=1e-3):
    return (f(x + h) - f(x - h)) / (2 * h)

# Generate x values and compute derivatives
x_vals = np.linspace(-2, 2, 400)
df_exact = df_analytic(x_vals)
df_approx = df_numerical(x_vals)

# Plotting
plt.plot(x_vals, df_exact, label='Analytic Derivative', linewidth=2)
plt.plot(x_vals, df_approx, '--', label='Central Difference Approximation', linewidth=2)
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title("Example 5.4: Derivative of f(x) = 1 + tanh(2x)")
plt.legend()
plt.grid(True)
plt.show()
