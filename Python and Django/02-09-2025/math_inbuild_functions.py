"""
Examples on Today's Topics
Author: Sridhar Goudu
Topics Covered:
1. Basic built-in number functions
2. Type checking methods
3. Math module methods
"""

# ------------------ 1. Basic Built-in Number Functions ------------------
print("----- Basic Built-in Number Functions -----")

# abs(): returns the absolute value of a number
print("abs(-10):", abs(-10))  # 10

# round(): rounds a number to given precision (default 0)
print("round(3.14159):", round(3.14159))        # 3
print("round(3.14159, 2):", round(3.14159, 2))  # 3.14

# pow(): returns base raised to exponent
print("pow(2, 3):", pow(2, 3))  # 8

# divmod(): returns quotient and remainder as tuple
print("divmod(17, 5):", divmod(17, 5))  # (3, 2)

# ------------------ 2. Type Checking Methods ------------------
print("\n----- Type Checking Methods -----")

x = 10
y = 3.14
z = "Python"

# type(): returns the type of object
print("type(x):", type(x))  # <class 'int'>
print("type(y):", type(y))  # <class 'float'>
print("type(z):", type(z))  # <class 'str'>

# isinstance(): checks if object is instance of class/type
print("isinstance(x, int):", isinstance(x, int))      # True
print("isinstance(y, float):", isinstance(y, float))  # True
print("isinstance(z, str):", isinstance(z, str))      # True
print("isinstance(x, float):", isinstance(x, float))  # False

# ------------------ 3. Math Module Methods ------------------
print("\n----- Math Module Methods -----")
import math

# ceil(): returns the smallest integer >= number
print("math.ceil(3.14):", math.ceil(3.14))  # 4

# floor(): returns the largest integer <= number
print("math.floor(3.14):", math.floor(3.14))  # 3

# sqrt(): returns the square root
print("math.sqrt(16):", math.sqrt(16))  # 4.0

# factorial(): returns factorial of number
print("math.factorial(5):", math.factorial(5))  # 120

# gcd(): returns greatest common divisor
print("math.gcd(24, 36):", math.gcd(24, 36))  # 12

# pi and e constants
print("math.pi:", math.pi)  # 3.141592653589793
print("math.e:", math.e)    # 2.718281828459045

# pow() from math module (similar to built-in but can handle floats)
print("math.pow(2, 3):", math.pow(2, 3))  # 8.0

# sin(), cos(), tan() - trigonometric functions (input in radians)
angle = math.pi / 4  # 45 degrees
print("math.sin(pi/4):", math.sin(angle))  # 0.7071...
print("math.cos(pi/4):", math.cos(angle))  # 0.7071...
print("math.tan(pi/4):", math.tan(angle))  # 1.0


#trunc()
import math
print(math.trunc(3.9))   # 3
print(math.trunc(-3.9))  # -3
print(math.trunc(5.0))   # 5
