userName = input("Type your name : ")
print("Welcome", userName, "to this adventure!")

answer = input("You are on a dirt road it came to an end and you can go left and right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You came to a river, you can walk around it or swim accross? Type walk to walk around or swim to swim accross: ").lower()
    if answer == "swim":
        print("You swim accross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else :
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You came to a bridge, do you wnt to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)").lower()
        if answer == 'yes':
            print('You talk to stanger and you won!')
        elif answer == 'no':
            print('You ignore the stranger and they are offended and you lose.')
        else:
            print("Not a valid option. You lose.")

    else :
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print("Thank you for trying", userName)