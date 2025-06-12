# Gaussian Elimination Method

Gaussian Elimination is a method for solving systems of linear equations. It involves two key steps:

1. **Forward Elimination**: Transform the system into an upper triangular matrix.
2. **Backsubstitution**: Solve the resulting system from bottom to top.

---

### Step 1: Forward Elimination

We transform the system $A\vec{x} = \vec{b}$ into upper triangular form:

* Eliminate all elements below the main diagonal.
* Use row operations (swap, scale, subtract):

  * Multiply a row by a non-zero constant.
  * Add/subtract rows.

### Step 2: Backsubstitution

With the matrix in upper triangular form, solve for variables from last to first:

$$
\begin{align*}
    a_{nn}x_n &= b_n \\
    a_{n-1,n-1}x_{n-1} + a_{n-1,n}x_n &= b_{n-1} \\
    &\vdots \\
    a_{11}x_1 + \ldots + a_{1n}x_n &= b_1
\end{align*}
$$

---

## Important Concepts

* **Pivot Element**: The diagonal element used to eliminate below it.
* **Singular Matrix**: If any pivot becomes 0 and cannot be swapped, the system may have no or infinite solutions.
* **Partial Pivoting**: Row swaps to place the largest absolute value on the diagonal to reduce numerical errors.

---

## Example

Given:

$$
A = \begin{bmatrix} 2 & 1 & 4 & 1 \\
                    3 & 4 & -1 & -1 \\
                    1 & -4 & 1 & 5 \\
                    2 & -2 & 1 & 3 \end{bmatrix},
\quad
v = \begin{bmatrix} -4 \\ 3 \\ 9 \\ 7 \end{bmatrix}
$$

### Step 1: Forward Elimination

After applying Gaussian elimination, you get:

$$
A' = \begin{bmatrix} 1 & * & * & * \\
                     0 & 1 & * & * \\
                     0 & 0 & 1 & * \\
                     0 & 0 & 0 & 1 \end{bmatrix},
\quad
v' = \begin{bmatrix} v_0' \\ v_1' \\ v_2' \\ v_3' \end{bmatrix}
$$

### Step 2: Backsubstitution

$$
\begin{align*}
z &= 1 \\
y &= -2 \\
x &= -1 \\
w &= 2
\end{align*}
$$

**Final Answer**: $x = [2, -1, -2, 1]$

---

## Python Implementation

```python
from numpy import array, empty

A = array([[ 2, 1, 4, 1],
           [ 3, 4, -1, -1],
           [ 1, -4, 1, 5],
           [ 2, -2, 1, 3]], float)

v = array([-4, 3, 9, 7], float)
N = len(v)

# Gaussian Elimination
for m in range(N):
    div = A[m, m]
    A[m, :] /= div
    v[m] /= div
    for i in range(m+1, N):
        mult = A[i, m]
        A[i, :] -= mult * A[m, :]
        v[i] -= mult * v[m]

# Backsubstitution
x = empty(N, float)
for m in range(N-1, -1, -1):
    x[m] = v[m]
    for i in range(m+1, N):
        x[m] -= A[m, i] * x[i]

print("Solution:", x)
```
# Dry Run
Matrix \$A\$ and vector \$v\$:

```
A = [
 [ 2,  3,  1,  2],
 [ 1,  4, -4, -2],
 [ 4, -1,  1,  1],
 [ 1, -1,  5,  3]
]
v = [-4, 3, 9, 7]
```

---

## Step 1: Gaussian Elimination

### Pivot Row m = 0

* Pivot: A\[0]\[0] = 2
* Normalize row 0:

```
A[0] = [1, 0.5, 2, 0.5]
v[0] = -2
```

* Eliminate below:

  * i = 1:

    * mult = 1 → A\[1] -= 1 \* A\[0], v\[1] += 2 → 9
    * `A[1] = [0, 2.5, -7, -2.5]`
  * i = 2:

    * mult = 4 → A\[2] -= 4 \* A\[0], v\[2] = 9 + 8 = 17
    * `A[2] = [0, -3, -7, -1]`
  * i = 3:

    * mult = 1 → A\[3] -= 1 \* A\[0], v\[3] = 7 + 2 = 9
    * `A[3] = [0, -1.5, 3, 2.5]`

### Pivot Row m = 1

* Pivot: A\[1]\[1] = 2.5
* Normalize:

```
A[1] = [0, 1, -2.8, -1]
v[1] = 3.6
```

* Eliminate:

  * i = 2:

    * mult = -3 → A\[2] += 3 \* A\[1], v\[2] += 3 \* 3.6 = 27.8
    * `A[2] = [0, 0, -15.4, -4]`
  * i = 3:

    * mult = -1.5 → A\[3] += 1.5 \* A\[1], v\[3] += 1.5 \* 3.6 = 14.4
    * `A[3] = [0, 0, -1.2, 1]`

### Pivot Row m = 2

* Pivot: A\[2]\[2] = -15.4
* Normalize:

```
A[2] = [0, 0, 1, ~0.26]
v[2] = -1.805
```

* Eliminate:

  * i = 3:

    * mult = -1.2 → A\[3] += 1.2 \* A\[2], v\[3] += 1.2 \* -1.805 = \~12.235
    * `A[3] = [0, 0, 0, 1.312]`

### Pivot Row m = 3

* Normalize:

```
A[3] = [0, 0, 0, 1]
v[3] = ~9.327
```

---

## Step 2: Back Substitution

* x\[3] = v\[3] = \~9.327
* x\[2] = v\[2] - A\[2]\[3] \* x\[3] = -1.805 - (0.26 \* 9.327) ≈ -4.229
* x\[1] = v\[1] - A\[1]\[2]\*x\[2] - A\[1]\[3]\*x\[3] = 3.6 - (-2.8 \* -4.229) - (-1 \* 9.327) = -1
* x\[0] = v\[0] - A\[0]\[1]*x\[1] - A\[0]\[2]*x\[2] - A\[0]\[3]*x\[3] = -2 - 0.5*(-1) - 2*(-4.229) - 0.5*9.327 ≈ 2

---

## Solution:

```
x = [2, -1, -2, 1]
```


