"""Problem Solution

1. Take the number of elements to be stored in the list as input.
2. Use a for loop to input elements into the list.
3. Calculate the total sum of elements in the list.
4. Divide the sum by total number of elements in the list.
5. Exit.


n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Element element "))
    a.append(elem)
    avg = sum(a) / n

print("Average of elements in the list", round(avg, 2))

"""
user=int(input("How many elemnts you want to enter :-"))
box=[]
for i in range(0,user):
    user1=int(input("Enter your elemnts to add in list :- "))
    box.append(user1)
    avg=sum(box)/user
print("Avg of these numbers are",round(avg,2))