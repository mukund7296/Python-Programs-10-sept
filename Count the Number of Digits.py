"""
Problem Solution

1. Take the value of the integer and store in a variable.
2. Using a while loop, get each digit of the number and increment the count each time a digit is obtained.
3. Print the number of digits in the given integer.
4. Exit.
"""

n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)