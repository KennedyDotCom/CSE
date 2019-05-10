import csv

with open('Sales Records.csv', 'r') as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        Profit = row[13]
        Items = row[2:8]
        print(Items)
        print(Profit)
