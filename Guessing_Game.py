#modify the guess my number game so that the player has a limited number of guesses
#if the player fails to guess in time the program should display an appropriately
#chastising message

import random

print("Guess the Number!")
print("Its Between 1 and 100!")
print("You have 3 Tries!")

number = random.randint(1, 10)
tries = 0


while tries != 3:
    guess = int(input("\nGuess The Number \n"))
    tries+=1

    if guess < number:
        print("The Number Is Higher!")

    elif guess > number:
        print("The Number Is Lower!")


    elif guess == number:
        print("You Win!")
        break
