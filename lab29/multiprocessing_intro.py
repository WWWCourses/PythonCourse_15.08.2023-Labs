import multiprocessing as mp
import time
import os



def calc_sum(start,end):
	total_sum = 0
	for num in range(start, end+1):
		total_sum += num**4
	print(f'total_sum: {total_sum}')

def worker():
	calc_sum(1,1_000_000)
	tr_obj = mp.current_process()
	print(f'{tr_obj}')


if __name__=="__main__":

	mp_pool = []
	processs_count = 5

	print(os.getpid(), '\n\n')
	print('START')
	start_time = time.perf_counter()
	for _ in range(processs_count):
		pr = mp.Process(target=worker)
		mp_pool.append(pr)
		print('Starting new process')
		pr.start()

	for pr in mp_pool:
		pr.join()


	end_time = time.perf_counter()
	print(f'TIME: {end_time-start_time}')