import threading
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor


class CalcSum:
	def __init__(self) -> None:
		pass

	def sequential(self, start, end):
		total_sum = 0

		total_sum += sum( list(range(start, end+1)) )
		print(f'Total sum in sequential: {total_sum}')

	def threads(self, start:int, end:int)->None:
		def __calc_sum( start:int, end:int)->None:
			global total_sum

			with l:
				total_sum = total_sum+ sum( list(range(start, end+1)) )

		l = threading.Lock()
		tr_pool = []
		args = ((start,end//2), (end//2+1,end))
		for arg in args:
			tr = threading.Thread(target=__calc_sum, args=arg)
			tr_pool.append(tr)
			tr.start()

		for tr in tr_pool:
			tr.join()

	def threadPool(self, start:int, end:int)->None:
		def __calc_sum( start:int, end:int)->None:
			print(f'start={start}, end={end}')
			global total_sum

			with l:
				total_sum = total_sum+ sum( list(range(start, end+1)) )

		l = threading.Lock()
		args = ((start,end//2), (end//2+1,end))
		# TODO as HW: fix errors
		with ThreadPoolExecutor(max_workers=5) as executor:
			tasks = executor.map(__calc_sum, (1,5))
			for task in tasks:
				task.result()





START = 1
END = 10

if __name__=='__main__':
	calc_sum =  CalcSum()

	calc_sum.sequential(START, END)

	total_sum = 0
	# calc_sum.threads(START, END)
	calc_sum.threadPool(START, END)
	print(f'Total sum in threads: {total_sum}')

