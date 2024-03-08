# File: S112_A1_T2_3_20230756.py. 

""" is a two-player mathematical subtraction game.
 It is played by two people with a pile of coins (or other tokens) between them.
The players take turns removing coins from the pile, always removing a non-zero square number of coins.
 The game is usually played as a normal play game, which means that the player who removes the last coin wins.
 It is an impartial game, meaning that the set of moves available from any position does not depend on whose turn it is.
 """

# Author: Amar yasser brahim20230756

# ID: 20230756

import random
import math

# The function's task is to ensure that the number is square
def is_squar (x):
    if (math.sqrt(x) == int(math.sqrt(x))):
        return True
    else:
        return False
        
# The function's task is to ensure that the number is valid,
# such as being a square, being a negative number, or being zero
def validity (coins_number,player_number):
    if player_number <= coins_number and is_squar(player_number) and coins_number > 0  and player_number > 0 :
        return True
    else:
        return False
    
def the_game(number_of_coins):
        while True:
            try:
                player1_number = int(input("player1 choose a number: "))
            except:
                print(" Please enter an valid number")
                continue

            while not validity(number_of_coins, player1_number):
                try:
                    player1_number = int(input("please enter a valid number: "))
                except:
                    print(" Please enter a valid number")
                    continue

            number_of_coins -= player1_number
        # In this step, the number of coins for player1 is updated with each move
            print("  =====================")
            print("number of coins now is", number_of_coins)
            print("  =====================")

            if number_of_coins == 0:
                print ("        player1 wins")
                break
            
            player2_number = int(input("player2 choose a number :") )

            while  not validity(number_of_coins,player2_number):
                player2_number = int(input("please enter a valid number :"))

            number_of_coins -= player2_number
            
        # In this step, the number of coins for player2 is updated with each move
            print("  =====================")
            print("number of coins now is", number_of_coins)
            print("  =====================")

            if number_of_coins == 0:
                print ("       player2 wins")
                break

        print("==============================================")
        if(input("press \"A\" to exit or press any key to play again\n==============================================\n").upper() == "A"):
            exit()
            
while True:
    choice = input("Do you want to enter the number yourself or have it chosen randomly? (enter 'A' or 'B'): ").upper()
    if choice == 'A':
        while True:
            number = (input("Enter the starting number of coins: "))
            if(number.isdigit and not is_squar(eval(number)) and eval(number) > 0):
                the_game(int(number))
                break
            else:
                print("please enter a valid number")
                continue
    elif choice == 'B':
        number = random.randint(1, 1000) 
        print("Randomly chosen number is:", number)
        the_game(number)
    else:
        print("Invalid choice. Please enter either 'manual' or 'random'.\n")
        continue