import csv
digit_len = 16


def num_len(num: str):
    if len(str(num)) == digit_len:
        return True
    return False


def last_num(num):
    lnum = int(num[15])
    return lnum


def reverse(num: str):
    print(num)
    return num[::-1]


reverse()

def validate(num: str):
    if first_num_even(num) and second_num_odd(num):
        return True
    return False

def reversed_version(num: str)




def valid1(num: str):
    reversed_version = reverse(num)
    for i in num: reversed_version:

def first_num_even(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False

def second_num_odd(num: str):
    second_num = int(num[1])
    if second_num % 2 == 1:
        return True
    return False

with open('Book1.csv', 'r') as old_csv:
    with open('MyNewFile.csv', 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print('Processing...')

        for row in reader:
            old_number = row[0]  # String
            if validate(old_number):
                writer.writerow(row)
        print('OK')




