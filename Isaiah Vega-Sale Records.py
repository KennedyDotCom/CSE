import csv

with open('Sales Records.csv', 'r') as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        if row[2] == 'Fruits':
            if row[13] == 'Profit':
