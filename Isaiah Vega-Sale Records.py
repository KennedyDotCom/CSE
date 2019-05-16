import csv

with open('Sales Records.csv', 'r') as old_csv:
    reader = csv.reader(old_csv)
    print('processing')
    a_item_type = []
    for row in reader:
        if row[0] == 'Region':
            continue

        item_type = row[2]
        total_profit = round(float(row[13]))
        if item_type not in a_item_type:
            a_item_type[item_type] = total_profit
        else:
            a_item_type[item_type] += total_profit

    print(a_item_type)
    print("Successful")
    print('the item with most profit is')
