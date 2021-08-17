#def new_func(player_1, player_2):
    #if player_1 == player_2:
        #print("This is a tie.")
    #else:
        #print("Someone won.")

play = input('Would you like to play Rock, Paper, Scissors? (Y/N): ')
while play != "N":
    player_1 = input('Player 1, choose Rock, Paper, or Scissors: ')
    player_2 = input('Player 2, choose Rock, Paper, or Scissors: ')
    if player_1 == player_2:
        print("This is a tie.")
    elif player_1.lower() == "rock" and player_2.lower() == "scissors":
        print("Player 1 won.")
    elif player_1.lower() == "rock" and player_2.lower() == "paper":
        print("Player 2 won.")
    elif player_1.lower() == "paper" and player_2.lower() == "rock":
        print("Player 1 won.")
    elif player_1.lower() == "paper" and player_2.lower() == "scissors":
        print("Player 2 won.")
    elif player_1.lower() == "scissors" and player_2.lower() == "paper":
        print("Player 1 won.")
    elif player_1.lower() == "scissors" and player_2.lower() == "rock":
        print("Player 2 won.")
    else:
        print("Someone won.")
    play = input('Would you like to play Rock, Paper, Scissors? (Y/N): ')



