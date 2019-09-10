"""
Problem Solution

1. Take in the first, second and third number and store it in separate variables.
2. Then append all the three numbers to the list.
3. Use three for loops and print the digits in the list if none of their indexes are equal to each other.
4. Exit.
"""

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]

d.append(a)
d.append(b)
d.append(c)
print(d)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])