import csv

# user,pincode,balance
# Kalin,123,500
# Ivan,456,1000


def list_of_lists_to_csv(data, filename, fieldsname):
	with open(filename, 'w', newline='') as f:
		writer = csv.writer(f)

		writer.writerow(fieldsname)
		writer.writerows(data)


def list_of_dicts_to_csv(data, filename, fieldnames):
		with open(filename, 'w', newline='') as f:
			writer = csv.DictWriter(f, fieldnames=fieldnames)
			writer.writeheader()
			for el in data:
				writer.writerow(el)

def csv_to_list_of_dicts(filename):
	users = []

	with open(filename, 'r', newline='') as f:
		reader = csv.DictReader(f)
		for row in reader:
			users.append(row)

	return users




def get_user():
	# user_name = input('Enter a name: ')
	user_name = 'Kalin'
	users = csv_to_list_of_dicts('user_accounts_list.csv')
	# print(users)

	res = next(filter(
		lambda el:True if el["name"]==user_name else False ,
		users)
	)
	print(res)





columns = ['name','pincode','balance']
get_user()

# data_list = [
# 	['Kalin',123,500],
# 	['Ivan',456,1000]
# ]

# data_dict = [
# 	{
# 		'name':'Kalin',
# 		'pincode':123,
# 		'balance':500
# 	},
# 	{
# 		'name':'Ivan',
# 		'pincode':456,
# 		'balance':1000
# 	}
# ]

# list_of_lists_to_csv(data_list, 'user_accounts_list.csv', columns)
# list_of_dicts_to_csv(data_dict, 'user_accounts_dict.csv', columns)
