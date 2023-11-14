import os
import time
import threading

print(f'pid: {os.getpid()}')


def work_hard(delay):
	print(f'Start working with delay {delay}')
	time.sleep(delay)
	# total_sum = sum([1**2, 10_000_000_000**2])
	# print(f'total_sum: {total_sum}')


start = time.time()
# synchronous exexution
# work_hard()
# work_hard()
# work_hard()

tr1 = threading.Thread(target=work_hard, args=(1,) )
tr2 = threading.Thread(target=work_hard, args=(1,))
tr3 = threading.Thread(target=work_hard, args=(1,))


tr1.start()
tr2.start()
tr3.start()

tr1.join()
tr2.join()
tr3.join()

end = time.time()
print(f'Time elapsed: {end-start}')


