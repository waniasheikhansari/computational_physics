# Types of Errors: Round-off and Truncation Errors

In numerical analysis and computing, errors can occur during calculations due to the limitations of representing numbers and performing arithmetic operations. These errors can be categorized into two primary types: **round-off errors** and **truncation errors**.

## 1. **Round-off Errors**

### **Definition**:
Round-off errors arise when a number is approximated to a limited number of digits, as most computers cannot represent numbers with infinite precision.

### **Cause**:
This error occurs because floating-point numbers (the way computers represent real numbers) have limited precision. For example, when a number is too large or too small to be exactly represented, it is rounded to the nearest representable number.

### **Example**:
For instance, the number \( \frac{1}{3} \) in decimal is a repeating decimal:

# 📉 Truncation Errors – A Short Guide

## 🔍 What is a Truncation Error?
A **truncation error** occurs when a mathematical process (like a series, integral, or derivative) is **approximated** by cutting off part of the computation.

> It is the difference between the exact mathematical value and the approximation.

---

## 🧠 Common Causes
- Approximating an **infinite series** with a finite number of terms  
- Using **finite differences** to approximate derivatives  
- **Numerical integration** (e.g., trapezoidal or Simpson’s rule)

---

## ✍️ Example

Approximating `e^x` using a Taylor Series:

