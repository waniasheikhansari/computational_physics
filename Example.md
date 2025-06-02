import numpy as np
import scipy.integrate as spi
import sympy as sp

def get_function():
    x = sp.symbols('x')
    expr = input("Enter the function f(x) using Python syntax (e.g., sin(x), x**2, exp(x)): ")
    try:
        parsed_expr = sp.sympify(expr)
        f = sp.lambdify(x, parsed_expr, modules=['numpy'])
        return f
    except (sp.SympifyError, NameError) as e:
        print(f"Error parsing the function: {e}")
        return get_function()

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h * (0.5*y[0] + np.sum(y[1:-1]) + 0.5*y[-1])

def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson's rule requires an even number of intervals.")
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h/3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

def romberg_integration(f, a, b):
    return spi.romberg(f, a, b)

def gaussian_quadrature(f, a, b, n):
    result, _ = spi.fixed_quad(f, a, b, n=n)
    return result

def main():
    f = get_function()
    a = float(input("Enter the lower limit (a): "))
    b = float(input("Enter the upper limit (b): "))
    n = int(input("Enter the number of intervals (n): "))

    print("\nChoose integration method:")
    print("1. Trapezoidal Rule")
    print("2. Simpson's Rule")
    print("3. Romberg Integration")
    print("4. Gaussian Quadrature")

    method = input("Enter the number corresponding to your choice: ")

    try:
        if method == '1':
            result = trapezoidal_rule(f, a, b, n)
        elif method == '2':
            result = simpsons_rule(f, a, b, n)
        elif method == '3':
            result = romberg_integration(f, a, b)
        elif method == '4':
            result = gaussian_quadrature(f, a, b, n)
        else:
            print("Invalid choice.")
            return
        print(f"\nResult of integration: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
