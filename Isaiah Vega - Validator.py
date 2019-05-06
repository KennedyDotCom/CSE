import csv
digit_len = 16


def num_len(num: str):
    if len(str(num)) == digit_len:
        return True
    return False


def last_num(num):
    digit_len.remove(15)


def reverse(num: str):
    print(num)
    return num[::-1]


reverse()


def validate(num: str):
    if validate(num):






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

