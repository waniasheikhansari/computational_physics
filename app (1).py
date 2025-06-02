
import streamlit as st
import numpy as np
import sympy as sp
import scipy.integrate as spi

def parse_function(expr):
    x = sp.symbols('x')
    try:
        parsed_expr = sp.sympify(expr)
        f = sp.lambdify(x, parsed_expr, modules=['numpy'])
        return f, None
    except Exception as e:
        return None, str(e)

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h * (0.5*y[0] + np.sum(y[1:-1]) + 0.5*y[-1])

def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson's rule requires even number of intervals.")
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h/3 * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]) + y[-1])

def romberg_integration_verbose(f, a, b, max_order=5):
    R = np.zeros((max_order, max_order))
    output = []
    for k in range(max_order):
        n = 2**k
        R[k, 0] = trapezoidal_rule(f, a, b, n)
        for j in range(1, k+1):
            R[k, j] = (4**j * R[k, j-1] - R[k-1, j-1]) / (4**j - 1)
        output.append([round(R[k, i], 6) for i in range(k+1)])
    return R[max_order-1, max_order-1], output

def gaussian_quadrature_verbose(f, a, b, max_n):
    results = []
    for n in range(1, max_n+1):
        res, _ = spi.fixed_quad(f, a, b, n=n)
        results.append((n, round(res, 6)))
    return results

st.title("📐 Numerical Integration Calculator")

expr = st.text_input("Enter the function f(x):", value="sin(x)")
a = st.number_input("Lower limit (a):", value=0.0)
b = st.number_input("Upper limit (b):", value=np.pi)
n = st.number_input("Number of intervals / points (n):", min_value=1, value=6, step=1)

method = st.selectbox("Choose integration method", [
    "Trapezoidal Rule",
    "Simpson's Rule",
    "Romberg Integration",
    "Gaussian Quadrature"
])

if st.button("Compute"):
    f, error = parse_function(expr)
    if error:
        st.error(f"Invalid function: {error}")
    else:
        try:
            if method == "Trapezoidal Rule":
                result = trapezoidal_rule(f, a, b, int(n))
                st.success(f"Trapezoidal Rule Result: {result:.6f}")
            elif method == "Simpson's Rule":
                result = simpsons_rule(f, a, b, int(n))
                st.success(f"Simpson's Rule Result: {result:.6f}")
            elif method == "Romberg Integration":
                result, table = romberg_integration_verbose(f, a, b, max_order=int(n))
                st.success(f"Romberg Final Result: {result:.6f}")
                st.subheader("Romberg Table:")
                for i, row in enumerate(table):
                    st.write(f"R[{i}]: {row}")
            elif method == "Gaussian Quadrature":
                results = gaussian_quadrature_verbose(f, a, b, max_n=int(n))
                st.success(f"Gaussian Quadrature (n={n}) Result: {results[-1][1]}")
                st.subheader("All Iterations:")
                for ni, val in results:
                    st.write(f"n = {ni} → {val}")
        except Exception as e:
            st.error(f"Error: {e}")
