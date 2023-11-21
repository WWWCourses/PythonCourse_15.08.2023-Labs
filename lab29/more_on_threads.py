import threading
import time
import os


def calc_sum(start,end):
	global total_sum
	total_sum= 0
	for num in range(start, end+1):
		total_sum += num**4
	print(f'total_sum: {total_sum}')

def worker():
	calc_sum(1,10_000_000)
	tr_obj = threading.current_thread()
	print(f'{tr_obj}')


threading_pool = []
threads_count = 5

print(os.getpid(), '\n\n')
print('START')
start_time = time.perf_counter()
for _ in range(threads_count):
	tr = threading.Thread(target=worker)
	threading_pool.append(tr)
	print('Starting new thread')
	tr.start()

for tr in threading_pool:
	tr.join()


end_time = time.perf_counter()
print(f'TIME: {end_time-start_time}')






