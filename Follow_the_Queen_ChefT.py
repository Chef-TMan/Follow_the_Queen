# We will be making a favorite street game called follow thw queen.
# Each hand is an automatic bet of $20, so choose the right card or lose your money
# just like the street game, you can leave when you win or keep playing..

import random

cards = ["Queen of Hearts", "Jack of Hearts", "King of Hearts"]
random.shuffle(cards)
print(" Wanna win $20 the easy way? ")

while cards:
    draw = input(
        "Time to find the Queen of Hearts! Place your $20 on the table!  If you want to chicken out, enter Q. ")
    if draw == "Q":
        break
    else:
        card = random.choice(cards)
        print("Your card is the:", card)
    while True:
        QH = str("Queen of Hearts")
        if card == QH:
            print("You win $20!")
            break
        else:
            print("Sorry, you lost! Thanx for the $20")
            break
