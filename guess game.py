#guess game
guess=7
for i in range(0,5):
    user = int(input("Enter your guess number between 1 to 10 :- "))
    if user==guess:
        print("You have Won this game in Attempt Number :",i+1)
        break
    elif user>=guess:
        print("Too Big ,Attempt Number :-",i+1)
    elif user<=guess:
        print("Too Small, Attempt Number :-",i+1)
if guess!=user:
    print("You lost \"Game\"")



