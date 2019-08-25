import csv
with open('selectColumn.csv','rb') as csvfile:
 reader = csv.reader(csvfile)
 rows= [row[2] for row in reader]
print rows

## Method-2
with open('selectColumn.csv','rb') as csvfile:
 reader = csv.DictReader(csvfile)
 column = [row['Age'] for row in reader]
print column