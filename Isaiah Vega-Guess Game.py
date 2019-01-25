import random
random1 = random.randint(0, 10)
win = False
guess_left = 5


while guess_left > 0 and not win:
    guess_number = int(input("Guess a number between 0 to 100"))
    if guess_number > random1:
        print("Guess lower")
        guess_left -= 1
    elif guess_number < random1:
        print("Guess higher")
        guess_left -= 1
    elif guess_number == random1:
        print("You Win!")
        win = True
