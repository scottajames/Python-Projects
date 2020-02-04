#Word Jumble with hinting
#The player should be able to see the hint if he or she is stuck
#Add scoring system that rewards players who solve a jumble without asking for a hint

import random

LIST = ("Python", "Programming", "String", "Vector", "Array")
answer = random.choice(LIST).lower()
hint = answer[0:3]
score = 0

play = input("Would you like to play (yes/no) ")
while play == "yes":
    print("Okay your word is", (answer[::2]))
    print("If you want a hint just ask for one by typing 'hint'")
    question = input("What is the answer? ")
    if question == "hint":
        print("The first 3 letters are",hint)
        score-=50
    elif question == answer:
        print("Correct!")
        score+=100
        highscore = input("Checkout your score by typing 'score' ")
        if highscore == "score":
            print(score)
        else:
            print("Thanks for playing")
            input("\n Press enter to exit")
if play == "no":
    input("\n Press enter to exit")
