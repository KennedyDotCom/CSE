import random

rounds_max_money = 0
money = 15
rounds = 0
max_money = 15
while money > 0:
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    # print(dice_1, dice_2)

    round += 1

    money -= 1

    if dice_1 + dice_2 == 7:
        money += 5
        print("You did it, You have", money, "dollars now")
        if money > max_money:
            max_money = money
    elif dice_1 + dice_2 < 7:
        print("You lost , Yo now have", money, "dollar")
print("you lasted", round, "rounds")
print("You had", max_money, "dollars")
# print("You had", round_max_money, "round with max money")
