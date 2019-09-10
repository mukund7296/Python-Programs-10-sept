"""
Problem Description

The program takes two numbers and prints the quotient and remainder.
Problem Solution

1. Take in the first and second number and store it in separate variables.
2. Then obtain the quotient using division and the remainder using modulus operator.
3. Exit.
"""

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
quotient=a//b
remainder=a%b
print("Quotient is:",quotient)
print("Remainder is:",remainder)