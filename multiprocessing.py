Multiprocessing is a way how multiple processes can run together in Python.
The main difference between multithreading and multiprocessing is that for separate processes different addressspace or
memoryspace is provided such that process runs as part of it and can't share the data or variables directly.
They will need to use inter process communication techniques like files, queues etc. to transfer data between processes.

In multithreading, all the three processes will run in the same addressspace utilising the same memory etc so the data or 
variables can be shared across as well.

import multiprocessing
import time
def calc_sq_nos(nums):
  for n in nums:
    time.sleep(5)
    print(n*n)

def calc_cube_nos(nums):
  for n in nums:
    time.sleep(5)
    print(n*n*n)
  
if __name__ == "__main__":
  arr1 = [1,2,7,9]
  p1 = multiprocessing.Process(target = calc_sq_nos, args = (arr1,))
  p2 = multiprocessing.Process(target = calc_cube_nos, args = (arr1,))
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  

Note -  In Windows task manager, we can see that it will run three processes - main, p1 and p2.


