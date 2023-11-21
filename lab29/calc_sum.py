import multiprocessing as mp

START = 1
END = 10

def split_interval():
	# TODO
    pass

def calc_sum(arg):
	print(mp.current_process().name)
	start = arg[0]
	end = arg[1]
	total_sum = sum(range(start, end+1))
	return total_sum


if __name__ == "__main__":
	pool = mp.Pool(processes=2)
	total_sum_list = pool.map(calc_sum, ((1,5),(6,10)))
	pool.close()
	pool.join()
	print(f'Total sum: {sum(total_sum_list)}')



