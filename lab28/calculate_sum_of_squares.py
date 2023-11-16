# --------------- TASK: print the sum of squares of l elements: -------------- #
import time
from threading import Thread, current_thread



# start = time.perf_counter()
# l = list(range(1,5_000_000))
# sum_of_squares = sum([el**2 for el in l])
# end = time.perf_counter()

# print(f'Time taken: {end-start}')

class MyThread(Thread):
	def __init__(self, target, args ):
		 super().__init__(target=target, args=args)
		 self.return_value = None

	def run(self):
		self.return_value = self._target(*self._args)

	def join(self):
		super().join()
		return self.return_value

def calculate_sum_of_squares(start, end):
	"""	calculate_sum_of_squares
	Args:
		start (_type_): start number, inclusive
		end (_type_): end number, inclusive
	"""
	sum_of_squares = sum([el**2 for el in range(start, end+1)])
	tid = current_thread().name
	print(f'{tid}: sum_of_squares={sum_of_squares}')
	return sum_of_squares



if __name__=="__main__":
	N = 10_000_000

	### Sequential:
	# start = time.perf_counter()
	# sum1 = calculate_sum_of_squares(1,int(N/2))
	# sum2 = calculate_sum_of_squares(int(N/2)+1, N)
	# end = time.perf_counter()
	# print(f'Sum of squares = {sum1+sum2}')
	# print(f'Time: {end-start}')

	### Threaded:
	start = time.perf_counter()
	tr1 = MyThread(target=calculate_sum_of_squares, args=(1,int(N/2)))
	tr2 = MyThread(target=calculate_sum_of_squares, args=(int(N/2)+1, N))
	tr1.start()
	tr2.start()
	sum1 = tr1.join()
	sum2 = tr2.join()

	end = time.perf_counter()
	print(f'Sum of squares = {sum1+sum2}')
	print(f'Time: {end-start}')


