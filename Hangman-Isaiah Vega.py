import string
import random

word_bank = ["Xbox", "how", "than", "ps4", "is", "today", "superior", "better", "help", "but", "pc", 'more']
letters = string.ascii_letters
word = random.choice(word_bank)
print(word)
guesses_left = 8
letters_guessed = []

while guesses_left >= 1:
    guessed_letter = input("Guess a letter: ")
    letters_guessed.append(guessed_letter)
    print(letters_guessed)
    