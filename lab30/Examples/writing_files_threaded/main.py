import time
import threading

def write_file(filename):
	print(f'creting file: {filename}')
	char_number = 300 * 1024 * 1024
	with open(filename, "w") as f:
		f.write('a'*char_number)


if __name__=="__main__":
	base_filename = 'test'
	filename_suffix = 1

	start = time.time()
	for n in range(5):
		write_file(base_filename + str(filename_suffix))
		filename_suffix+=1

	end = time.time()
	print(f'Seq Time taken: {end-start}')

	threads_pool = []
	start = time.time()
	for n in range(5):
		tr = threading.Thread(target=write_file, args=(base_filename + str(filename_suffix),))
		filename_suffix+=1
		threads_pool.append(tr)
		tr.start()

	for tr in threads_pool:
		tr.join()

	end = time.time()
	print(f'Threaded Time taken: {end-start}')



