import string
import random

word_bank = ["smells", "it", "like", "Xbox", "is", "better", "than", "ps4", "AirPods", "Broke", "In", "here", 'sorry']
letters = string.ascii_letters
print(word_bank)
word = random.choice(word_bank)
print(word)

print(list(string.ascii_letters))
print(list(string.digits))
print(list(string.punctuation))

