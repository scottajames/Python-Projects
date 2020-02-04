#A program that prints a list of words in random order
#doesn't print the words more than once

import random

list = ["python", "programming", "computer", "database", "list"]
random.shuffle(list)
print(list)
