# Newton-Raphson Method
The Newton-Raphson Method is an efficient numerical technique used to find approximate roots of real-valued equations.

## Formula
To solve the equation:
f(x) = 0
The iterative formula is:
### xₙ₊₁ = xₙ - f(xₙ) / f′(xₙ)
Where:
xₙ is the current approximation,
f(xₙ) is the function value at xₙ,
f′(xₙ) is the derivative of the function at xₙ.

## Requirements
1. The function f(x) must be differentiable.
2. The initial guess x₀ must be reasonably close to the actual root.
3. The derivative f′(xₙ) must not be zero.

### Steps
Start from an initial guess x₀.
Find the tangent at x₀.
Find where the tangent intersects the x-axis.
Use that intersection as the next guess.
Repeat until the value converges.

## Example: Square Root of 2
We want to find the root of:

```
f(x) = x² - 2
Derivative:
f′(x) = 2x
Step 1: Initial guess
x₀ = 1.5
Step 2: Iteration using the formula
x₁ = 1.5 - (1.5² - 2) / (2×1.5) = 1.4167

x₂ = 1.4167 - (1.4167² - 2) / (2×1.4167) ≈ 1.4143

Continues converging to √2 ≈ 1.4142
```
### How to Choose a Good Initial Guess
1. Plot the function and pick a point near where it crosses the x-axis.
2. Use the Intermediate Value Theorem to bracket the root.
3. Make sure f′(x₀) ≠ 0.
4. Check if values converge during early iterations.

### Warning Signs of a Bad Guess
1. Derivative is zero (f′(xₙ) = 0)
Values diverge or jump around
Convergence is too slow or oscillates


# Newton-Raphson Method in Python

```
def f(x):
    return x**2 - 2  

def df(x):
    return 2 * x     
def newton_raphson(x0, tol=1e-6, max_iter=10):
    print(f"Initial guess: x0 = {x0}")
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        
        if dfx == 0:
            print("Zero derivative. No solution found.")
            return None

        x1 = x0 - fx / dfx
        print(f"Iteration {i+1}: x = {x1:.6f}, f(x) = {f(x1):.6f}")
        
        if abs(x1 - x0) < tol:
            print("Converged.")
            return x1
        
        x0 = x1

    print("Did not converge.")
    return None

root = newton_raphson(1.5)
print(f"\nApproximate root: {root}")
```

```
def f(x):
    return x**2 - 2  

def df(x):
    return 2 * x     

def newton_raphson(x0, tol=1e-6, max_iter=10):
    print(f"Initial guess: x0 = {x0}")
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        
        if dfx == 0:
            print("Zero derivative. No solution found.")
            return None

        x1 = x0 - fx / dfx
        print(f"Iteration {i+1}: x = {x1:.6f}, f(x) = {f(x1):.6f}")
        
        if abs(x1 - x0) < tol:
            print("Converged.")
            return x1
        
        x0 = x1

    print("Did not converge.")
    return None

root = newton_raphson(1.5)
print(f"\nApproximate root: {root}")

```
