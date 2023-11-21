import multiprocessing as mp

def increment(r):
  global x

  for _ in r:
    x+=1


  print(f"x in {mp.current_process().name}: {x}")


if __name__ == "__main__":
  x = 0

  pr1 = mp.Process(target=increment, args=(range(1000),))
  pr2 = mp.Process(target=increment, args=(range(1000),))

  pr1.start();pr2.start();
  pr1.join();pr2.join();


  print(f"x in {mp.current_process().name}: {x}")

  #OUTPUT
  # x in Process-1: 1000
  # x in Process-2: 1000
  # x in MainProcess: 0