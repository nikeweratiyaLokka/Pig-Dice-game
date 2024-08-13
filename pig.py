import random

#Gets a value between 1 and 6
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    
    return roll

#Gets the number of players
while True:
    players = int(input("Enter the number of players: "))
    if 2 <= players <= 4:
        break
    else:
        print("num of players is invalid, should be between 2-4")
 
 
max_score = 20


#Arrays for the scores and player names
player_scores = [0 for _ in range(players)]
player_names = [None for _ in range(players)]
for i in range(len(player_names)):
    player_names[i] = input(f"Enter player {i+1}'s name\n ")




while max(player_scores) < max_score:
    for i in range(len(player_scores)):
        print(f"\n{player_names[i]}'s turn\n")
        current_score = 0
        
        
        #Current user begins their turn
        while True:
            player_roll = input("roll ?(y)" )
            if player_roll.lower() != "y":
                break
            
            value = roll()
            
            #If the value is 1, the score resets for the current player
            if value == 1:
                print("You rolled a 1. Score reset")
                current_score = 0
                break 
            else:
                print(f"You rolled a:{value}")
                current_score += value
            
            print(f"Your score is: {current_score}")
        
        player_scores[i] += current_score
        print()
        for i in range(players):
            print(f"{player_names[i]} : {player_scores[i]}")
        
    
    
        
    
    


