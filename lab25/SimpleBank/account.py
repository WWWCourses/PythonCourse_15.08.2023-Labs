from db import DB

class Account:
	account_number = 1

	def __init__(self, client_id:int, pin:str, balance:float=0.0)->None:
		self.client_id = client_id
		self.balance = balance
		self.pin = pin
		self.number = Account.account_number
		Account.account_number += 1


class Bank:
	def __init__(self) -> None:
		self.accounts = db.accounts_from_csv() or []

	def create_demo_accounts(self):
		accounts = []

		for i in range(1,4):
			client_id = i
			balance = 0.0
			pin = f'{i:04}'
			account = Account(client_id, pin, balance)
			accounts.append(account)


db = DB()
print(db.accounts_from_csv())