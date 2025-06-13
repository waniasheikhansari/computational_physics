
## LU Decomposition and Gaussian Elimination

Gaussian elimination solves systems of linear equations by converting a matrix into an upper-triangular form, then solving via backsubstitution. However, this process can be reformulated using **matrix operations** to make it more systematic and efficient, especially when solving multiple systems with the same matrix.

### The Matrix Multiplication Representation

Each elimination step in Gaussian elimination corresponds to multiplying by a **lower-triangular matrix**. For instance, in the second step, where we eliminate the second column below the diagonal:

```math
L_1 = \begin{bmatrix}
1 & 0 & 0 & 0 \\
-b_{10} & 1 & 0 & 0 \\
-b_{20} & 0 & 1 & 0 \\
-b_{30} & 0 & 0 & 1
\end{bmatrix}
```

This matrix, when multiplied by the original matrix `A`, performs the first elimination.

Subsequent elimination steps introduce additional lower-triangular matrices `L2`, `L3`, etc., each responsible for zeroing out below-diagonal elements in their respective columns.

### Full Elimination as Matrix Multiplication

The result of complete Gaussian elimination is:

```math
L_3 L_2 L_1 L_0 A = U
```

Where `U` is an upper-triangular matrix.

If we apply the same transformations to the right-hand side vector `v`, we get:

```math
L_3 L_2 L_1 L_0 A x = L_3 L_2 L_1 L_0 v
```

Let:

* `L = (L_3 L_2 L_1 L_0)^{-1}` (product of inverse lower-triangular matrices)
* `U = L_3 L_2 L_1 L_0 A`

Then:

```math
LU = A
```

This is the **LU decomposition**: expressing `A` as the product of a lower-triangular matrix `L` and an upper-triangular matrix `U`.

---

## Solving Ax = v Using LU Decomposition

We solve the system in two steps:

1. **Forward substitution**:
   Solve `Ly = v`
2. **Back substitution**:
   Solve `Ux = y`

This approach is efficient because:

* `L` and `U` are triangular matrices
* You can reuse `L` and `U` for different vectors `v`

### Example

Assume:

```math
L = \begin{bmatrix}
1 & 0 & 0 \\
l_{10} & 1 & 0 \\
l_{20} & l_{21} & 1
\end{bmatrix},
U = \begin{bmatrix}
u_{00} & u_{01} & u_{02} \\
0 & u_{11} & u_{12} \\
0 & 0 & u_{22}
\end{bmatrix}
```

To solve `Ax = v`:

* First compute `y` from `Ly = v` using forward substitution
* Then compute `x` from `Ux = y` using back substitution

---

## Advantages of LU Decomposition

* Efficient for solving multiple systems with the same matrix but different right-hand sides
* Captures all elimination steps in matrices `L` and `U`
* Avoids recomputation of the decomposition

---

## Pivoting and Stability

To ensure numerical stability, LU decomposition should include **partial pivoting**:

* Swap rows so that pivot elements are as far from zero as possible
* Prevents division by small numbers

Standard practice: **LU decomposition with partial pivoting**

---

## Python Implementation

Using `numpy.linalg.solve`:

```python
from numpy.linalg import solve
x = solve(A, v)
```

This uses LU decomposition internally to efficiently solve the system.

For more control:

* Use `scipy.linalg.lu` to compute `L` and `U` separately
* Useful when solving multiple systems with the same `A`

More resources:

* [scipy.org](https://www.scipy.org)

---

## Summary

* Gaussian elimination can be represented using matrix multiplication
* LU decomposition expresses a matrix `A` as a product `LU`
* Solving `Ax = v` becomes two simpler steps: `Ly = v`, then `Ux = y`
* LU is widely used and implemented in numerical libraries like NumPy and SciPy
* Always use pivoting to ensure numerical stability
