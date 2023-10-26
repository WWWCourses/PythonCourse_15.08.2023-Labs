import csv

with open('./datasets/drinks.csv', newline='') as csvfile:
	drinks = csv.reader(csvfile, delimiter=',', quotechar='"')

	for row in drinks:
		print(row)

