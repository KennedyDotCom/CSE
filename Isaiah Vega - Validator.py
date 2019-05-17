import csv
digit_len = 16








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

