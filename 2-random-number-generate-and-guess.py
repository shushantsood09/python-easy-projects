import random as r

# Randthe range won't include the upper value ehich mean it will generate numbers till 10 from 0


top_of_range = input("Type a number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Print type a number greater then 0 nect time.")
        quit()

else:
    print("Please type a number next time.")
    quit()

random_number = r.randrange(top_of_range)
print(random_number)

# print(top_of_range)

# randomNumber2 = r.randint(1, 11)
# # It will generate the result from 0 till 11. Mean it wil;l include 11 as well in the result.
# print(randomNumber2)

guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess.")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You are above the number")
    else:
        print("You are below the number")

print("You got it in", guesses, "guesses")
