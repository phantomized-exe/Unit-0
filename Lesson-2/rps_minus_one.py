'''
Name: Phann Boon
File: rps_minus_one.py
Description: Implements the Rock Paper Scissors Minus One
game from Squid Game
'''

'''
Pseudocode
Have computer pick two random "hands" of either rps
SET com_score, player_score to 0
STORE values in comp_hand somehow (you choose)
ASK user for their hands
STORE values in player_hand
ASK user which hand to keep
computer randomly chooses hand
EVALUATE who wins
UPDATE score
ASK if they want to continue or quit
IF quit, PRINT scores and END game
    ELSE play again
'''
def rps_minus_one():
    import random
    comp_score = 0
    player_score = 0
    continue_game = True
    while continue_game:
        comp_hand = []
        player_hand = []
        for i in range(2):
            comp_num = random.randint(1,3)
            if comp_num == 1:
                comp_hand.append("rock")
            elif comp_num == 2:
                comp_hand.append("paper")
            else:
                comp_hand.append("scissors")
        try:
            for i in range(2):
                player_num = int(input("Choose a hand:\n1. Rock\n2. Paper\n3. Scissors "))
                if player_num == 1:
                    player_hand.append("rock")
                elif player_num == 2:
                    player_hand.append("paper")
                else:
                    player_hand.append("scissors")
        except ValueError:
            print("Invalid choice.")
            continue
        print(f"The computer's hands are {comp_hand[0]} and {comp_hand[1]}. Your hands are {player_hand[0]} and {player_hand[1]}.")
        try:
            remove_hand = int(input(f"Choose hand to remove:\n1. {player_hand[0]}\n2. {player_hand[1]} "))
        except ValueError:
            print("Invalid choice.")
            continue
            player_hand.remove(player_hand[remove_hand-1])
        comp_num = random.randint(0,1)
        comp_hand.remove(comp_hand[comp_num])
        if comp_hand[0] == "rock":
            if player_hand[0] == "paper":
                print("You win because paper covers rock.")
                player_score += 1
            elif player_hand[0] == "rock":
                print("Nobody wins because both are rock.")
            else:
                print("The computer wins because rock smashes scissors.")
                comp_score += 1
        elif comp_hand[0] == "paper":
            if player_hand[0] == "scissors":
                print("You win because scissors cuts paper.")
                player_score += 1
            elif player_hand[0] == "paper":
                print("Nobody wins because both are paper.")
            else:
                print("The computer wins because paper covers rock.")
                comp_score += 1
        else:
            if player_hand[0] == "rock":
                print("You win because rock smashes scissors.")
                player_score += 1
            elif player_hand[0] == "scissors":
                print("Nobody wins because both are scissors.")
            else:
                print("The computer wins because scissors cuts paper.")
                comp_score += 1
        #try:
            #cont_game = int(input("Continue game?\n1. Yes\n2. No "))
        #except ValueError:
            #print("Invalid choice.")
            #continue
        cont_game = int(input("Continue game?\n1. Yes\n2. No "))
        if cont_game != 1:
            continue_game = False
            return f"Player score: {player_score}\nComputer score: {comp_score}"
        else:
            continue_game = True
            continue

print(rps_minus_one())



