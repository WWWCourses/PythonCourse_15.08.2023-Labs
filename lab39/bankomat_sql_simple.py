import mysql.connector

class MongoDB:
	def __init__(self,
				 host='localhost',
				 user='test',
				 password='test1234',
				 database='bankomatdb'):

		self.host = host
		self.user = user
		self.password = password
		self.database = database

	def create_accounts_table(self):
		# NOT IMLEMENTED
		sql = """"
			CREATE TABLE `accounts` (
				`id` int NOT NULL AUTO_INCREMENT,
				`client_name` varchar(255) NOT NULL,
				`pin` char(4) NOT NULL,
				`balance` decimal(10,2) NOT NULL,
				PRIMARY KEY (`id`)
			)
		"""

	def get_connection(self):
		return mysql.connector.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
		)

	def get_account_by_name(self, client_name: str):
		try:
			connection = self.get_connection()
			cursor = connection.cursor(dictionary=True)

			query = f"SELECT * FROM accounts WHERE client_name = '{client_name}' LIMIT 1;"
			cursor.execute(query)
			account_data = cursor.fetchone()
			print(f'account_data: {account_data}')

			cursor.close()
			connection.close()

			if account_data:
				return account_data
			else:
				raise Exception(f'Account for client {client_name} not found in the database.')
		except Exception as err:
			print(f'Error: {err}')

	def update_account_balance(self, account_id:int, new_balance:int):
		try:
			connection = self.get_connection()
			cursor = connection.cursor(dictionary=True)

			query = f"update accounts set balance={new_balance} where id = {account_id};"
			print(query)
			cursor.execute(query)
			connection.commit()

			cursor.close()
			connection.close()
		except Exception as err:
			print(f'Error: {err}')



class Bankomat():
	def __init__(self, name, account_data):
		self.name = name
		self.id = account_data['id']
		self.balance = account_data['balance']
		self.client_name = account_data['client_name']
		self.pin = account_data['pin']


	def check_balance(self):
		return f"Your current balance is {self.balance}."

	def check_pin(self, pin):
		self.pin = pin

	def deposit(self, amount):
		self.balance += amount
		return f"You have deposited {amount}. Your new balance is {self.balance}."

	def withdraw(self, amount):
		if amount > self.balance:
			return "Sorry, you do not have enough funds in your account."
		self.balance -= amount

		# update db:
		db.update_account_balance(account_id=self.id, new_balance=self.balance)

		return f"You have withdrawn {amount}. Your new balance is {self.balance}."


if __name__ == "__main__":
	db = MongoDB()

	### user login:
	name = input('Enter your name: ')
	account_data = db.get_account_by_name( name )

	if account_data['balance'] >0:
		print("'Your name is accepted'")
		bankomat = Bankomat('Bankomat1', account_data )
	else:
		print("Wrong name")
		exit()

	is_pin_correct = False
	for i in range(3):
		pin_input = input('Enter your pin: ')
		is_pin_correct = (pin_input==account_data['pin'])
		print(f'pin_input: {pin_input}')
		print(f"account_data['pin']: {account_data['pin']}")
		if is_pin_correct:
			break

	# show menu:
	if is_pin_correct:
		print('Login Successful')
		print("Make a choice - 1 to 3 or exit")
		print('1  Balance Inquiry')
		print('2  Withdraw')
		print('3  Deposit')

	# get user choice
	user_choice = 2
	if user_choice == 2:
		amount = 20
		bankomat.withdraw(amount)







