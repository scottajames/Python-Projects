#Game where computer picks a random word and the player has to guess that word
#The computer tells the player how many letters are in that word
#Player gets five chances to ask if a letter is in the word
#Computer can only respond with yes or no

import random

LIST = ["Python", "Programming", "String", "Vector", "Array"]
answer = random.choice(LIST).lower()
letters = "abcdefghijklmnopqrstuvwxyz"
letterGuess = ""
answerGuess = ""
tries = 0
score = 0


print("There are ",len(answer),"letters in the word")

while  answerGuess != answer:
    letterGuess = input("What letter do you think is in the word? ").lower()
    tries+=1
    if letterGuess in answer:
        print("Yes")
    else:
        print("No")
    if tries == 6:
        break;
    elif tries >= 5:
        answerGuess = input("What do you think the word is? ").lower()
        tries+=1
        if answerGuess == answer:
            score+=100
            print("Correct! your score is: ", score)
        else:
            print("Wrong! why not try again?")
            score-=5
            print("Your score is", score)
