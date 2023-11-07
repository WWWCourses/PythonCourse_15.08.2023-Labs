import csv

class DB:
	def __init__(self) -> None:
		pass

	def accounts_to_csv(self, accounts)->None:
		filename='accounts.csv'
		fields=['client_id', 'balance', 'pin', 'number']

		with open(filename, 'w') as f:
			writer = csv.DictWriter(f, fieldnames = fields)

			# writing headers (field names)
			writer.writeheader()

			# writing data rows
			for account in accounts:
				writer.writerow(account.__dict__)

	def accounts_from_csv(self):
		filename='accounts.csv'
		accounts = []

		with open(filename, 'r', newline='') as f:
			reader = csv.DictReader(f)
			for row in reader:
				accounts.append(row)


		return accounts