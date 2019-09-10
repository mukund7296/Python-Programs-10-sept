"""
Problem Solution

1. Take the value of the integer and store in a variable.
2. Using a while loop, get each digit of the number and add the digits to a variable.
3. Print the sum of the digits of the number.
4. Exit.
"""

n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)