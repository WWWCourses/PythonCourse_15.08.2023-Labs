import threading
import time

def worker(x,y=None):
	tr_obj = threading.current_thread()
	print(f'{tr_obj}')
	time.sleep(1)


print(f'Main thread name: {threading.current_thread().name}')

start = time.time()
tr1 = threading.Thread(target=worker, name='TR1',args=(1,),kwargs={'y':2})
tr2 = threading.Thread(target=worker, name='TR2',args=(1,),kwargs={'y':2})
tr3 = threading.Thread(target=worker, name='TR3',args=(1,),kwargs={'y':2})

tr1.start() # worker(1, y=2)
tr2.start()
tr3.start()

tr1.join()
tr2.join()
tr3.join()

end = time.time()
print(f'time taken: {end-start}')

