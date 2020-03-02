# import random module in order to have access to random

import random

random.seed()

# functions
def displayRules():
    print("-----       Welcome to Cee-lo!     ------")
    print("-----             Rules            ------")
    print("1.) You or CPU must reach 5 wins in order to end the game")
    print("2.) At the start of the game there is a coin toss to determine who goes first")
    print("3.) After each round alternate who goes first")
    print("4.) Getting a roll of 4-5-6 is an automatic win")
    print("5.) Getting a roll of 1-2-3 is an automatic loss")
    print("6.) Getting a roll with three of the same numbers (three of a kind) is considered a triple and is higher than a point")
    print("7.) Getting a roll with two of the same numbers (pair) is consider a point. The die with the number not within the pair is the point")
    print("8.) Getting a point does not take into consideration of how high the pair is only the point. Ex: 1-1-6 is higher than 6-6-1")
    print("9.) Getting any roll besides the above mentioned will result in a meaningless roll. The player or CPU than must roll again")
    print("10.) Draws do not count as either a win or loss")

def rollDice(List):
    # gets dice roll
    Die1 = random.randint(1,6)
    Die2 = random.randint(1,6)
    Die3 = random.randint(1,6)
    # adds dice roll to a list to sort
    List.append(Die1)
    List.append(Die2)
    List.append(Die3)
    List.sort()

# variables
playerWins = 0
CPUWins = 0
count = 0
playerTurn = 0
playerList = []
CPUList = []
pRollAgain = True
cRollAgain = True

displayRules()

# determine if either player or CPU goes first
print("Beginning coin toss...")
playerTurn = random.randint(0,1)
if playerTurn == 0:
    playerTurn = False
    print("CPU goes first!")
else:
    playerTurn = True
    print("Player goes first!")

while playerWins < 5 and CPUWins < 5:
    count += 1
    print(f"--------------- Round {count} ---------------")
    print("---------------------------------------")
    # If player's turn goes first
    if playerTurn == True:
        while pRollAgain == True:
            # get player's dice roll
            rollDice(playerList)
            playerDie3 = playerList.pop()
            playerDie2 = playerList.pop()
            playerDie1 = playerList.pop()
            print(f"Player's dice roll is: {playerDie1}-{playerDie2}-{playerDie3}")

            # possible outcomes

            # automatic win for player
            if playerDie1 == 4 and playerDie2 == 5 and playerDie3 == 6:
                print(f"Player automatically wins round {count}!")
                playerWins += 1
                pRollAgain = False

            # automatic loss for player
            elif playerDie1 == 1 and playerDie2 == 2 and playerDie3 == 3:
                print(f"Player automatically loses round {count}!")
                CPUWins += 1
                pRollAgain = False

            # triple for player
            elif playerDie1 == playerDie2 == playerDie3:
                print("Player has a triple!")
                while cRollAgain == True:
                    # gets CPU's dice roll
                    rollDice(CPUList)
                    CPUDie3 = CPUList.pop()
                    CPUDie2 = CPUList.pop()
                    CPUDie1 = CPUList.pop()
                    print(f"CPU's dice roll is: {CPUDie1}-{CPUDie2}-{CPUDie3}")

                    if CPUDie1 == 4 and CPUDie2 == 5 and CPUDie3 == 6:
                        print(f"CPU wins round {count}!")
                        CPUWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    elif CPUDie1 == 1 and CPUDie2 == 2 and CPUDie3 == 3:
                        print(f"Player wins round {count}!")
                        playerWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    elif CPUDie1 == CPUDie2 == CPUDie3:
                        if playerDie1 > CPUDie1:
                            print(f"Player wins round {count}!")
                            playerWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        elif CPUDie1 > playerDie1:
                            print(f"CPU wins round {count}!")
                            CPUWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        else:
                            print(f"Round {count} ends in a draw!")
                            pRollAgain = False
                            cRollAgain = False
            
                    elif CPUDie1 == CPUDie2 or CPUDie1 == CPUDie3 or CPUDie2 == CPUDie3:
                        print(f"Player wins round {count}!")
                        playerWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    else:
                        print("CPU has a meaningless roll. CPU most roll again!")

            # point for player
            elif playerDie1 == playerDie2:
                print(f"Player has a point of {playerDie3}!")
                while cRollAgain == True:
                    # gets CPU's dice roll
                    rollDice(CPUList)
                    CPUDie3 = CPUList.pop()
                    CPUDie2 = CPUList.pop()
                    CPUDie1 = CPUList.pop()
                    print(f"CPU's dice roll is: {CPUDie1}-{CPUDie2}-{CPUDie3}")

                    if CPUDie1 == 4 and CPUDie2 == 5 and CPUDie3 == 6:
                        print(f"CPU wins round {count}!")
                        CPUWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    elif CPUDie1 == 1 and CPUDie2 == 2 and CPUDie3 == 3:
                        print(f"Player wins round {count}!")
                        playerWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    elif CPUDie1 == CPUDie2 == CPUDie3:
                        print(f"CPU wins round {count}!")
                        CPUWins += 1
                        pRollAgain = False
                        cRollAgain = False
                    
                    elif CPUDie1 == CPUDie2:
                        if playerDie3 > CPUDie3:
                            print(f"Player wins round {count}!")
                            playerWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        elif CPUDie3 > playerDie3:
                            print(f"CPU wins round {count}!")
                            CPUWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        else:
                            print(f"Round {count} ends in a draw!")
                            pRollAgain = False
                            cRollAgain = False
                    
                    elif CPUDie2 == CPUDie3:
                        if playerDie3 > CPUDie1:
                            print(f"Player wins round {count}!")
                            playerWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        elif CPUDie1 > playerDie3:
                            print(f"CPU wins round {count}!")
                            CPUWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        else:
                            print(f"Round {count} ends in a draw!")
                            pRollAgain = False
                            cRollAgain = False
                    
                    else:
                        print("CPU has a meaningless roll. CPU most roll again!")
                    

        
            elif playerDie2 == playerDie3:
                print(f"Player has a point of {playerDie1}!")
                while cRollAgain == True:
                    # gets CPU's dice roll
                    rollDice(CPUList)
                    CPUDie3 = CPUList.pop()
                    CPUDie2 = CPUList.pop()
                    CPUDie1 = CPUList.pop()
                    print(f"CPU's dice roll is: {CPUDie1}-{CPUDie2}-{CPUDie3}")

                    if CPUDie1 == 4 and CPUDie2 == 5 and CPUDie3 == 6:
                        print(f"CPU wins round {count}!")
                        CPUWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    elif CPUDie1 == 1 and CPUDie2 == 2 and CPUDie3 == 3:
                        print(f"Player wins round {count}!")
                        playerWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    elif CPUDie1 == CPUDie2 == CPUDie3:
                        print(f"CPU wins round {count}!")
                        CPUWins += 1
                        pRollAgain = False
                        cRollAgain = False
                    
                    elif CPUDie1 == CPUDie2:
                        if playerDie1 > CPUDie3:
                            print(f"Player wins round {count}!")
                            playerWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        elif CPUDie3 > playerDie1:
                            print(f"CPU wins round {count}!")
                            CPUWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        else:
                            print(f"Round {count} ends in a draw!")
                            pRollAgain = False
                            cRollAgain = False
                    
                    elif CPUDie2 == CPUDie3:
                        if playerDie1 > CPUDie1:
                            print(f"Player wins round {count}!")
                            playerWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        elif CPUDie1 > playerDie1:
                            print(f"CPU wins round {count}!")
                            CPUWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        else:
                            print(f"Round {count} ends in a draw!")
                            pRollAgain = False
                            cRollAgain = False
                    
                    else:
                        print("CPU has a meaningless roll. CPU most roll again!")

            # meaningless roll for player
            else:
                print("Player has a meaningless roll. Player must roll again!")

    # ---------------------------------------------------------------------------------------------------
    # If CPU's turn goes first
    else:
        while cRollAgain == True:
            # get CPU's dice roll
            rollDice(CPUList)
            CPUDie3 = CPUList.pop()
            CPUDie2 = CPUList.pop()
            CPUDie1 = CPUList.pop()
            print(f"CPU's dice roll is: {CPUDie1}-{CPUDie2}-{CPUDie3}")

            # possible outcomes

            # automatic win for CPU
            if CPUDie1 == 4 and CPUDie2 == 5 and CPUDie3 == 6:
                print(f"CPU automatically wins round {count}!")
                CPUWins += 1
                cRollAgain = False

            # automatic loss for CPU
            elif CPUDie1 == 1 and CPUDie2 == 2 and CPUDie3 == 3:
                print(f"CPU automatically loses round {count}!")
                playerWins += 1
                cRollAgain = False

            # triple for CPU
            elif CPUDie1 == CPUDie2 == CPUDie3:
                print("CPU has a triple!")
                while pRollAgain == True:
                    # gets player's dice roll
                    rollDice(playerList)
                    playerDie3 = playerList.pop()
                    playerDie2 = playerList.pop()
                    playerDie1 = playerList.pop()
                    print(f"Player's dice roll is: {playerDie1}-{playerDie2}-{playerDie3}")

                    if playerDie1 == 4 and playerDie2 == 5 and playerDie3 == 6:
                        print(f"Player wins round {count}!")
                        playerWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    elif playerDie1 == 1 and playerDie2 == 2 and playerDie3 == 3:
                        print(f"CPU wins round {count}!")
                        CPUWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    elif playerDie1 == playerDie2 == playerDie3:
                        if CPUDie1 > playerDie1:
                            print(f"CPU wins round {count}!")
                            CPUWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        elif playerDie1 > CPUDie1:
                            print(f"Player wins round {count}!")
                            playerWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        else:
                            print(f"Round {count} ends in a draw!")
                            pRollAgain = False
                            cRollAgain = False
            
                    elif playerDie1 == playerDie2 or playerDie1 == playerDie3 or playerDie2 == playerDie3:
                        print(f"CPU wins round {count}!")
                        CPUWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    else:
                        print("Player has a meaningless roll. Player most roll again!")

            # point for CPU
            elif CPUDie1 == CPUDie2:
                print(f"CPU has a point of {CPUDie3}!")
                while pRollAgain == True:
                    # gets player's dice roll
                    rollDice(playerList)
                    playerDie3 = playerList.pop()
                    playerDie2 = playerList.pop()
                    playerDie1 = playerList.pop()
                    print(f"Player's dice roll is: {playerDie1}-{playerDie2}-{playerDie3}")

                    if playerDie1 == 4 and playerDie2 == 5 and playerDie3 == 6:
                        print(f"Player wins round {count}!")
                        playerWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    elif playerDie1 == 1 and playerDie2 == 2 and playerDie3 == 3:
                        print(f"CPU wins round {count}!")
                        CPUWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    elif playerDie1 == playerDie2 == playerDie3:
                        print(f"Player wins round {count}!")
                        playerWins += 1
                        pRollAgain = False
                        cRollAgain = False
                    
                    elif playerDie1 == playerDie2:
                        if CPUDie3 > playerDie3:
                            print(f"CPU wins round {count}!")
                            CPUWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        elif playerDie3 > CPUDie3:
                            print(f"Player wins round {count}!")
                            playerWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        else:
                            print(f"Round {count} ends in a draw!")
                            pRollAgain = False
                            cRollAgain = False
                    
                    elif playerDie2 == playerDie3:
                        if CPUDie3 > playerDie1:
                            print(f"CPU wins round {count}!")
                            CPUWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        elif playerDie1 > CPUDie3:
                            print(f"Player wins round {count}!")
                            playerWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        else:
                            print(f"Round {count} ends in a draw!")
                            pRollAgain = False
                            cRollAgain = False
                    
                    else:
                        print("Player has a meaningless roll. Player most roll again!")
                    

        
            elif CPUDie2 == CPUDie3:
                print(f"CPU has a point of {CPUDie1}!")
                while pRollAgain == True:
                    # gets player's dice roll
                    rollDice(playerList)
                    playerDie3 = playerList.pop()
                    playerDie2 = playerList.pop()
                    playerDie1 = playerList.pop()
                    print(f"Player's dice roll is: {playerDie1}-{playerDie2}-{playerDie3}")

                    if playerDie1 == 4 and playerDie2 == 5 and playerDie3 == 6:
                        print(f"Player wins round {count}!")
                        playerWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    elif playerDie1 == 1 and playerDie2 == 2 and playerDie3 == 3:
                        print(f"CPU wins round {count}!")
                        CPUWins += 1
                        pRollAgain = False
                        cRollAgain = False

                    elif playerDie1 == playerDie2 == playerDie3:
                        print(f"Player wins round {count}!")
                        playerWins += 1
                        pRollAgain = False
                        cRollAgain = False
                    
                    elif playerDie1 == playerDie2:
                        if CPUDie1 > playerDie3:
                            print(f"CPU wins round {count}!")
                            CPUWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        elif playerDie3 > CPUDie1:
                            print(f"Player wins round {count}!")
                            playerWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        else:
                            print(f"Round {count} ends in a draw!")
                            pRollAgain = False
                            cRollAgain = False
                    
                    elif playerDie2 == playerDie3:
                        if CPUDie1 > playerDie1:
                            print(f"CPU wins round {count}!")
                            CPUWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        elif playerDie1 > CPUDie1:
                            print(f"Player wins round {count}!")
                            playerWins += 1
                            pRollAgain = False
                            cRollAgain = False
                        else:
                            print(f"Round {count} ends in a draw!")
                            pRollAgain = False
                            cRollAgain = False
                    
                    else:
                        print("Player has a meaningless roll. Player most roll again!")

            # meaningless roll for CPU
            else:
                print("CPU has a meaningless roll. CPU must roll again!")
    
    # Changes who goes first for the next round and resets pRollAgain and cRollAgain
    if playerWins < 5 and CPUWins < 5:
        if playerTurn == True:
            playerTurn = False
            pRollAgain = True
            cRollAgain = True
            print("CPU now goes first in the next round")
            print("---------------------------------------")
        else:
            playerTurn = True
            pRollAgain = True
            cRollAgain = True
            print("Player now goes first in the next round")
            print("---------------------------------------")
    else:
        print("Game, Set, and Match!")

# Determines who wins!
if playerWins > CPUWins:
    print(f"Player won and finished the game in round: {count}!!!")
else:
    print(f"CPU won and finished the game in round: {count}!!!")