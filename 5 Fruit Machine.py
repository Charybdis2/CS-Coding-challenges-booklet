#Fruit Machine Write a program to simulate a Fruit Machine that displays three symbols at random from Cherry, Bell, Lemon, Orange, Star, Skull.
#The player starts with £1 credit, with each go costing 20p. If the Fruit Machine “rolls” two of the same symbol, the user wins 50p. The player wins £1 for three of the same and £5 for 3 Bells.
#The player loses £1 if two skulls are rolled and all of his/her money if three skulls are rolled. The player can choose to quit with the winnings after each roll or keep playing until there is no money left.

import random
def roll(money):
    symbol = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
    slot = []
    money = money-20
    for a in range(3):
        slot += [symbol[random.randint(0, 5)]]
    money += check_symbol(slot, money)
    print(slot)
    return(money)

def count_symbol(slot, symbol):
    return len([s for s in slot if s == symbol])

def check_symbol(slot, money):
    one, two, three  = slot[0], slot[1], slot[2]
    if count_symbol(slot, one) == 3:
        if one == "Bell":
           return 500
        if one == 'Skull':
            return -money
        return 100
    
    if count_symbol(slot, 'Skull') == 2:
        return -100

    if count_symbol(slot, one) == 2 or count_symbol(slot, two) == 2:
        return 50
    return 0

money = 100
stop = ""
while money >= 20 and stop != "yes":
    
    money = roll(money)
    print(money)
    stop = (input("Would you like to stop? ")).lower()

