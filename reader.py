import csv

with open("aita_top.csv", 'r', encoding="utf8") as file:

    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)
