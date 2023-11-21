import queue

queue = queue.Queue()

queue.put(1)
queue.put(2)
queue.put(3)


el1 = queue.get()
el2 = queue.get()
el3 = queue.get()

print(el1,el2,el3)
