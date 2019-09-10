"""
Problem Solution

1. Take in the upper range and lower range limit from the user.
2. Take in the number to be divided by from the user.
3. Using a for loop, print all the factors which is divisible by the number.
4. Exit.


lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)
        """
A=int(input("Enter lower range limit:"))
B=int(input("Enter upper range limit:"))
C=int(input("Enter the number to be divided by:"))
for i in range(A,B+1):
    if i%C==0:
        print(i)