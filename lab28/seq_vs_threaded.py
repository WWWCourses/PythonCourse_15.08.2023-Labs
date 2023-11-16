import threading
import time
import os

def worker():
	tid = threading.current_thread().name

	# do some hard and time consuming work:
	# create list of 10 elements 1,2, ... 10
	l = list(range(1,100_000_000))
	# print the sum of squares of l elements:
	sum_of_squares = sum([el**2 for el in l])


	print(f"Worker {tid} sum_of_squares = {sum_of_squares}")



print(f'Process ID: {os.getpid()}')
#################################################
# Sequential Processing:
#################################################
t = time.time()
worker()
worker()
print("Sequential Processing took:",time.time() - t,"\n")

#################################################
# Multithreaded Processing:
#################################################
tmulti = time.time()
tr1 = threading.Thread(target=worker, name='TR1')
tr2 = threading.Thread(target=worker, name='TR2')

tr1.start();tr2.start()
tr1.join(); tr2.join()
print("Multithreaded Processing took:",time.time() - tmulti)