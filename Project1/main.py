# Copyright 2022 PI515

import random
keepAsking = True
while keepAsking:
    num = input('Type a number for an upper bound: ')
    if num.isdigit() == True:
        print("Let's play!")
        num = int(num)
        keepAsking = False
        print(num)
        # something about the loop condition
    else:
        print("Invalid input. Try again.")

secret = random.randint(1, num)
guess = None
count = 0

while guess != secret:
    guess = input("Type a number between 1 and " + str(num) + ": ")
    if guess.isdigit():
        guess = int(guess)
        if guess == secret: # can't always be wrong
      
         print("You got it! it took you", count, "guesses")
          
        else:
            print("Try again.")
            count += 1
        # what else?


