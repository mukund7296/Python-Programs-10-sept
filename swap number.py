"""Problem Solution

1. Take the values of both the elements from the user.
2. Store the values in separate variables.
3. Print the swapped values.
4. Exit.
"""

a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
a,b=b,a
print("a is:",a," b is:",b)