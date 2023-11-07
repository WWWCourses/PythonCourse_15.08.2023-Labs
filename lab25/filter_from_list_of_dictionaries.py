users = [
	{
		'name':'Ivan',
		'pincode':456,
		'balance':1000
	},
	{
		'name':'Kalin',
		'pincode':123,
		'balance':500
	},
	{
		'name':'Ivan',
		'pincode':456,
		'balance':1000
	}
]

def variant0(users, name):
	for user in users:
		if user['name']==name:
			return user

	return False


def varaint1(users,name):
	# def myFilter(el):
		# 	# print(el)
		# 	# if el["name"]==user_name:
		# 	# 	return True
		# 	# else:
		# 	# 	return False

		# 	# ternary operator
		# 	return True if el["name"]==user_name else False


		res = next(filter(
			lambda el:True if el["name"]==user_name else False ,
			users)
		)
		print(res)

def variant2(users,name):
	return [user for user in users if user['name']==name ][0]



user = variant2(users,'Kalin')
# print(user)

pin = 123

if user['pincode']==pin:
	print('OK')
else:
	print('Not OK')


