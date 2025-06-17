# Eigenvalues and Eigenvectors — Computational Physics (Mark Newman)

## 1. Introduction

Eigenvalues and eigenvectors are fundamental concepts in linear algebra, with deep applications in physics, especially in classical mechanics, quantum mechanics, and electromagnetism. These concepts help us understand how a physical system behaves under transformations represented by matrices.

---

## 2. What Are Eigenvalues and Eigenvectors?

Let $A$ be an $N \times N$ matrix. An eigenvector $\mathbf{v}$ of $A$ is a non-zero vector such that:

$A \mathbf{v} = \lambda \mathbf{v}$

Here:

* $\mathbf{v}$: Eigenvector
* $\lambda$: Eigenvalue corresponding to $\mathbf{v}$

### Interpretation:

* The eigenvector $\mathbf{v}$ maintains its direction when acted upon by matrix $A$.
* The eigenvalue $\lambda$ represents the **scaling factor** by which the eigenvector is stretched or compressed.

### In Physics:

* **Classical Mechanics**: Vibrational modes of a system
* **Quantum Mechanics**: Allowed energy levels
* **Electromagnetism**: Field propagation in media

---

## 3. Properties of Eigenvectors for Symmetric Matrices

For a real symmetric matrix $A$:

* There are $N$ eigenvectors for an $N \times N$ matrix.
* Eigenvectors $\mathbf{v}_i$ and $\mathbf{v}_j$ are **orthogonal** if $i \neq j$:
  $\mathbf{v}_i \cdot \mathbf{v}_j = 0$
* They are usually **normalized**:
  $\| \mathbf{v}_i \| = 1$

---

## 4. Matrix Formulation

We can write all eigenvalue equations together:
$AV = VD$
Where:

* $V$ is the matrix of eigenvectors (as columns)
* $D$ is a diagonal matrix of eigenvalues
* $V$ is orthogonal $(V^T = V^{-1})$

---

## 5. The QR Algorithm (Numerical Method)

The **QR algorithm** is a powerful numerical method for calculating the eigenvalues and eigenvectors of a real symmetric matrix.

### Step-by-step Breakdown:

1. Start with a real symmetric matrix $A$.

2. Perform the QR decomposition:
   $A = QR$

   * $Q$: orthogonal matrix
   * $R$: upper triangular matrix

3. Reverse the multiplication:
   $A_1 = RQ$

4. Repeat the process:

   * Decompose $A_1 = Q_2 R_2$
   * $A_2 = R_2 Q_2$
   * Continue iterating...

5. After $k$ steps:
   $A_k = (Q_k \dots Q_1)^T A (Q_k \dots Q_1) \rightarrow D$ (diagonal)

6. Define:
   $V = Q_1 Q_2 \dots Q_k$

7. Then:
   $AV = VD$

   * Columns of $V$: Eigenvectors
   * Diagonal elements of $D$: Eigenvalues

---

## 6. Python Implementation (Using NumPy)

### Calculate Eigenvalues and Eigenvectors:

```python
from numpy import array
from numpy.linalg import eigh

A = array([[1, 2],
           [2, 1]], float)

x, V = eigh(A)

print("Eigenvalues:", x)
print("Eigenvectors:\n", V)
```

### Output:

```
Eigenvalues: [-1.  3.]
Eigenvectors:
[[-0.7071  0.7071]
 [ 0.7071  0.7071]]
```

### Calculate Only Eigenvalues (Faster):

```python
from numpy.linalg import eigvalsh

x = eigvalsh(A)
print("Eigenvalues:", x)
```

---

## 7. QR Algorithm Example (Manual Implementation)

### Example Matrix:

$A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$

### Python Code:

```python
import numpy as np

def qr_decomposition(A):
    n = A.shape[0]
    Q = np.zeros_like(A)
    R = np.zeros((n, n))
    
    for i in range(n):
        v = A[:, i]
        for j in range(i):
            R[j, i] = np.dot(Q[:, j], A[:, i])
            v = v - R[j, i] * Q[:, j]
        R[i, i] = np.linalg.norm(v)
        Q[:, i] = v / R[i, i]
    return Q, R

def qr_algorithm(A, iterations=100):
    A_k = A.copy()
    n = A.shape[0]
    V = np.eye(n)
    for _ in range(iterations):
        Q, R = qr_decomposition(A_k)
        A_k = R @ Q
        V = V @ Q
    return A_k, V

A = np.array([[2, 1], [1, 2]], dtype=float)
D, V = qr_algorithm(A, iterations=100)

print("Diagonal Matrix (Eigenvalues):\n", D)
print("Matrix V (Eigenvectors):\n", V)
```

This implementation manually computes QR decomposition using the Gram-Schmidt process and iterates the QR algorithm.

---

## 8. Notes

* `eigh()` and `eigvalsh()` assume the matrix is symmetric or Hermitian.
* Only the lower triangle of the matrix is used. The upper triangle is ignored.
* For complex Hermitian matrices, the functions assume the upper triangle is the complex conjugate of the lower.
* For general matrices (not symmetric), use `eig()` and `eigvals()`.

---
