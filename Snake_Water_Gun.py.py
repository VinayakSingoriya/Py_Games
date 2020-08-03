import  random
print("GAME! GAME! GAME!\n")
i=0       #for condition
j=0       #for successfull attempt
k=0       #for unsucessfull attempt
l=0       #for draw a game
while i<5:
        # This will choose a random option
        list=["snake","water","gun"]
        choice=random.choice(list)
        # print(choice)snam

        # User input and check conditions

        print("Enter any one from snake,water,gun")
        user_input=input()
        if choice=="snake" and user_input=="water":
            print("computer:",choice,"||","yours:",user_input)
            print("you lose the game")
            k+=1
            i+=1

        elif choice=="snake" and user_input=="gun":
            print("computer:", choice, "||","yours:", user_input)
            print("congrats you have Won!!")
            i+=1
            j+=1
        elif choice=="snake" and user_input=="snake":
            print("computer:", choice, "||","yours:", user_input)
            print("Game drawn!!")
            l+=1
            i += 1

        elif choice=="water" and user_input=="snake":
            print("computer:", choice, "||","yours:", user_input)
            print("congrats you have Won")
            i += 1
            j += 1
        elif choice=="water" and user_input=="gun":
            print("computer:", choice, "||","yours:", user_input)
            print("you lose the game")
            k+=1
            i+=1
        elif choice=="water" and user_input=="water":
            print("computer:", choice, "||","yours:", user_input)
            print("Game drawn!!")
            l+=1
            i += 1
        elif choice=="gun" and user_input=="snake":
            print("computer:", choice, "||","yours:", user_input)
            print("you lose the game")
            k+=1
            i+=1
        elif choice=="gun" and user_input=="water":
            print("computer:", choice, "||","yours:", user_input)
            print("congrats you have Won")
            i += 1
            j += 1
        elif choice=="gun" and user_input=="gun":
            print("computer:", choice, "||","yours:", user_input)
            print("Game drawn!!")
            l+=1
            i+=1
        else:
            print("Invalid choice")
            k+=1
            i+=1
        print("---\nAttempt left-", 5 - i, ":")
print("\n-----------------------------")
print("Total attempts:",i)
print("Your Points:",j)
print("Computer Points:",k)
print("Game drawn:",l)
if j>k:
    print(">>Congrats,you have won the Game!!<<")
elif j==k:
    print(">>Game Drawn!!<<")
else:
    print(">>You lose the game!!<<")
print("\n-----------------------------")