import numpy as np
import sympy as sp
from scipy.integrate import romberg

# Symbol for parsing the function
x = sp.Symbol('x')

def get_function_input():
    expr_str = input("Enter the function in terms of x (e.g., 2*x**2 + 3*x + 1): ")
    try:
        expr = sp.sympify(expr_str)
        f = sp.lambdify(x, expr, modules=['numpy'])
        return f, expr
    except Exception:
        print("Invalid function. Please try again.")
        return get_function_input()

def trapezoidal_rule(f, a, b, n=100):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return h * result

def simpson_rule(f, a, b, n=100):
    if n % 2:
        n += 1  # Simpson’s rule requires even number of intervals
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        factor = 4 if i % 2 else 2
        result += factor * f(a + i * h)
    return h * result / 3

def gaussian_quadrature(f, a, b, n=2):
    [xi, wi] = np.polynomial.legendre.leggauss(n)
    result = 0
    for i in range(n):
        x_trans = ((b - a) / 2) * xi[i] + (b + a) / 2
        result += wi[i] * f(x_trans)
    return (b - a) / 2 * result

def romberg_integration(f, a, b):
    return romberg(f, a, b, show=False)

def main():
    print("Numerical Integration Tool")
    f, expr = get_function_input()

    a = float(input("Enter the lower limit of integration: "))
    b = float(input("Enter the upper limit of integration: "))

    print("\nChoose numerical method:")
    print("1. Trapezoidal Rule")
    print("2. Simpson's Rule")
    print("3. Gaussian Quadrature (2-point)")
    print("4. Romberg Integration")

    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == '1':
        result = trapezoidal_rule(f, a, b)
        method = "Trapezoidal Rule"
    elif choice == '2':
        result = simpson_rule(f, a, b)
        method = "Simpson's Rule"
    elif choice == '3':
        result = gaussian_quadrature(f, a, b)
        method = "Gaussian Quadrature (2-point)"
    elif choice == '4':
        result = romberg_integration(f, a, b)
        method = "Romberg Integration"
    else:
        print("Invalid choice.")
        return

    print(f"\nMethod Used: {method}")
    print(f"Function: {expr}")
    print(f"Integral from {a} to {b} ≈ {result:.6f}")

if __name__ == "__main__":
    main()
    
