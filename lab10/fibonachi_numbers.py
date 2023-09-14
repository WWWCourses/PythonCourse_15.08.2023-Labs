# ------------------------------- With Iterator ------------------------------ #
# class Fibonachi:
# 	def __init__(self, limit):
# 		self.n1 = 0
# 		self.n2 = 1
# 		self.limit = limit


# 	def __iter__(self):
# 		return self

# 	def __next__(self):
# 		self.n1, self.n2 = self.n2, self.n1 + self.n2

# 		if self.n1<self.limit:
# 			return self.n1
# 		else:
# 			raise StopIteration



# fib_iterator = Fibonachi(30)

# print('Fib with Iterator')
# for num in fib_iterator:
# 	print(num, end=', ')


# -------------------------------- With Lists -------------------------------- #
print()
def make_fib_list(limit):
	# limit = 30
	l = []
	n1,n2 = 0,1
	while n2<limit:
		l.append(n2)
		n1, n2 = n2, n1+n2

	return l

fib_list = make_fib_list(30)

print('Fib with list')
for num in fib_list:
	print(num, end=', ')

print()

# ------------------------------ With Generator ------------------------------ #
def make_fib_generator(limit):
	n1,n2 = 0,1
	while n2<limit:
		yield n2
		n1, n2 = n2, n1+n2



fib_gen = make_fib_generator(30)

print('Fib with list')
for num in fib_gen:
	print(num, end=', ')