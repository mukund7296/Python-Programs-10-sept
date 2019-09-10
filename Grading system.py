"""Problem Description

The program takes in the marks of 5 subjects and displays the grade.
Problem Solution

1. Take in the marks of 5 subjects from the user and store it in different variables.
2. Find the average of the marks.
3. Use an else condition to decide the grade based on the average of the marks.
4. Exit.

"""
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=int(sub1+sub2+sub3+sub4+sub4)/5
if (avg>=90):
    print("Grade: A")
elif (avg>=80 and avg <=90):
    print("Grade: B")
elif (avg>=70 and avg <=80):
    print("Grade: C")
elif (avg>=60 and avg <=70):
    print("Grade: D")
else:
    print("Grade: F")
print("Average marks in Percentage :",avg,"%")