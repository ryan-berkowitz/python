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
    else:
        print("Someone won.")
    play = input('Would you like to play Rock, Paper, Scissors? (Y/N): ')



