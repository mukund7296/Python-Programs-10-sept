
i=0
while i <5:
    guess = 7
    user = int(input("Enter your guess number between 1 to 10 :- "))
    if guess==user:
        print("You have won this \"Game\" Attempt Number",i+1)
        break
    elif guess>=user:
        print("Too Low,Attempt Number ",i+1)
    elif guess<=user:
        print("Too High ,Attempt Number ",i+1)
    i=i+1
if guess!=user:
        print("You lost \"Game\"")