# Get user input for integer and floating-point numbers
a = float(input("Enter a number (a): "))
b = float(input("Enter another number (b): "))
c = int(input("Enter an integer (c): "))

# Perform arithmetic operations
sum_ab = a + b
sum_ac = a + c
sum_bc = b + c
difference_ab = a - b
difference_ac = a - c
difference_bc = b - c
product_ab = a * b
product_ac = a * c
product_bc = b * c
quotient_ab = a / b
quotient_ac = a / c
quotient_bc = b / c
modulus_ab = a % b
modulus_ac = a % c
modulus_bc = b % c
exponentiation_ab = a ** b
exponentiation_ac = a ** c
exponentiation_bc = b ** c

# Print the results
print("a + b =", sum_ab)
print("a + c =", sum_ac)
print("b + c =", sum_ac)
print("a - b =", difference_ab)
print("a - c =", difference_ac)
print("b - c =", difference_bc)
print("a * b =", product_ab)
print("a * c =", product_ac)
print("b * c =", product_bc)
print("a / b =", quotient_ab)
print("a / c =", quotient_ac)
print("b / c =", quotient_bc)
print("a % b =", modulus_ab)
print("a % c =", modulus_ac)
print("b % c =", modulus_bc)
print("a ** b =", exponentiation_ab)
print("a ** c =", exponentiation_ac)
print("b ** c =", exponentiation_bc)

# Use built-in functions for numerical operations
absolute_c = abs(c)
rounded_b = round(b)
max_value = max(a, b, c)
min_value = min(a, b, c)

print("Absolute value of c:", absolute_c)
print("Rounded value of b:", rounded_b)
print("Max value:", max_value)
print("Min value:", min_value)

# Import the math module for more advanced math operations
import math

square_root_a = math.sqrt(a)
logarithm_base_10_a = math.log10(a)
factorial_c = math.factorial(abs(c))

print("Square root of a:", square_root_a)
print("Logarithm base 10 of a:", logarithm_base_10_a)
print(f"Factorial of |c| ({abs(c)}):", factorial_c)
