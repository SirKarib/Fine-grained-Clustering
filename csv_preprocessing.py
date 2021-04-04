import csv

with open('export_file.csv', encoding="UTF-8", newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)
