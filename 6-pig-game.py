import random as r

def roll():
    min_value = 1
    max_value = 6
    roll = r.randint(min_value, max_value)

    return roll

# value= roll()
# print(value) 

while True : 
    players = input("Enter the number of players (2 - 4) : ")
    if(players.isdigit()):
        players = int(players)
        if 1 <= players <= 4 :
            break
        else:
            print("Must be between 2 - 4 playerss.")
    else:
        print("Invalid so, try again ")

max_score = 50
players_scores = [0 for _ in range(players)]

print(players)
print(players_scores)

while max(players_scores) < max_score:
    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "turn has just started!")
        print("Your total store is", players_scores[player_index], "\n")
        current_score = 0

        while True:
            should_roll = input("Do you want to roll (y)? ")
            if should_roll.lower() != 'y':
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!") 
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
                
            print("Your score is:", current_score)

        players_scores[player_index] += current_score
        print("Your total score is:", players_scores[player_index])

max_score = max(players_scores)
winning_index = players_scores.index(max_score)
print("Player number", winning_index + 1, "is the winner with the score of: ", max_score)