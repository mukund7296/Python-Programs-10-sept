"""
Problem Solution

1. Take a value from the user and store it in a variable n.
2. Use two for loop where the value of j ranges between the values of 0 and n-1 and value of i also ranges between 0 and n-1.
3. Print the value of 1 when i is equal to j and 0 otherwise.
4. Exit.
"""

n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()