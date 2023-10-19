from functools import reduce
import time


def calc_sum_1(start,end):
	return reduce( lambda a,b: a+b, range(start, end+1) )

def calc_sum_2(start, end):
	total = 0
	for el in range(start,end+1):
		total+=el

	return total

# t1_start = time.time()
# print( calc_sum_1(1,10_000_000) ) #
# t1_end = time.time()

# t2_start = time.time()
# print( calc_sum_2(1,10_000_000) ) #
# t2_end = time.time()

# print(f'calc_sum_1 time: {t1_end-t1_start}')
# print(f'calc_sum_2 time: {t2_end-t2_start}')

print('Hi')
time.sleep(2)
print('Buy')