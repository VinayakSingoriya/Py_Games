n=13
print("Guess a number game!!\n")
for x in range(5):
    print("Note: You  have only",5-x, "chances to guess\n")
    print("Guess a number:")
    num=int(input())
    if num>13:
        print("Enter smaller number\n")
    elif num<13:
        print("Enter greater number\n")
    elif num==13:
        print("congrats Mr. Pycoder,you guessed it correctly in your",5-x,"attempt\n")
        break
print("GAME OVER")
