# --------------------------------- Задача 1. -------------------------------- #
# Да се напише програма, която да реализира генератор на четни числа.

# def evens_generator(max):
# 	el = 2
# 	while el<=max:
# 		yield el
# 		el+=2


# evens = evens_generator(10)
# print(list(evens))

### demo for generate list of evens:
# evens = list(range(2,11,2))
# evens = [el for el in range(2,11) if el%2==0]

# print(evens)

# --------------------------------- Задача 3. -------------------------------- #
# Да се напише програма, която да реализира генератор на прости числа

# helper function to check if number is prime
def is_prime(x):
	is_prime_fl = True

	# TODO: optimize...
	for el in range(2,x):
		if x%el==0:
			is_prime_fl = False
			break

	return is_prime_fl

# print( is_prime(7) )
# print( is_prime(8) )

def prime_generator(limit):
	for x in range(limit):
		if is_prime(x):
			yield x


# for el in prime_generator(10):
# 	print(el)



### demo for create list of primes
# primes = [x for x in range(10) if is_prime(x) ]
# print(primes)