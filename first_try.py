import csv

with open('export_file.csv.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)
