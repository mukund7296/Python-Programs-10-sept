"""Problem Solution

1. Take the value of the integer and store in a variable.
2. Using a while loop, get each digit of the number and store the reversed number in another variable.
3. Print the reverse of the number.
4. Exit.
"""
n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)