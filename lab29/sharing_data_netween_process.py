import multiprocessing as mp
import time

def increment(n, q):
	x = q.get()
	for _ in range(n):
		x+=1
	q.put(x)

	print(f'x in {mp.current_process().name}: {x}')


if __name__=="__main__":
	x = 0
	q = mp.Queue()
	q.put(x)

	process_pool = []
	process_count = 2
	for _ in range(process_count):
		pr = mp.Process(target=increment, args=(1000,q))
		process_pool.append(pr)
		pr.start()

	for pr in process_pool:
		pr.join()

	print(f'x in main: {q.get()}')


