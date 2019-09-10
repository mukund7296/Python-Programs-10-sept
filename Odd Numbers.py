"""
Problem Solution

1. Take in the upper range limit and the lower range limit and store it in separate variables.
2. Use a for-loop ranging from the lower range to the upper range limit.
3. Then use an if statement if check whether the number is odd or not and print the number.
4. Exit.
"""

lower=int(input("Enter the lower limit for the range:"))
upper=int(input("Enter the upper limit for the range:"))
for i in range(lower,upper+1,2):
    print(i)

   # or

for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)