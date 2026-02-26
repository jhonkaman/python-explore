# Run: python3 operators/assignment_operators.py
# Assignment Operators Examples
# Assignment operators assign values to variables

# Simple assignment
x = 10
print("x =", x)

# Multiple assignment
a, b, c = 1, 2, 3
print("a =", a, ", b =", b, ", c =", c)

# Addition assignment (+=)
x = 10
x += 5  # Equivalent to x = x + 5
print("x += 5:", x)  # 15

# Subtraction assignment (-=)
x = 10
x -= 3  # Equivalent to x = x - 3
print("x -= 3:", x)  # 7

# Multiplication assignment (*=)
x = 10
x *= 2  # Equivalent to x = x * 2
print("x *= 2:", x)  # 20

# Division assignment (/=)
x = 10
x /= 2  # Equivalent to x = x / 2
print("x /= 2:", x)  # 5.0

# Floor division assignment (//=)
x = 10
x //= 3  # Equivalent to x = x // 3
print("x //= 3:", x)  # 3

# Modulus assignment (%=)
x = 10
x %= 3  # Equivalent to x = x % 3
print("x %= 3:", x)  # 1

# Exponent assignment (**=)
x = 2
x **= 3  # Equivalent to x = x ** 3
print("x **= 3:", x)  # 8

# Swapping values
x = 5
y = 10
x, y = y, x
print("After swap: x =", x, ", y =", y)
