🔹 What is a Queue?
A queue is a FIFO (First-In-First-Out) data structure. Python provides a built-in queue module that supports multi-threaded programming with safe and efficient queues.

 Types of Queues in Python (queue module)

Queue.Queue – FIFO queue
LifoQueue – LIFO queue (stack)
PriorityQueue – retrieves entries in priority order


import queue

# Create a FIFO queue
q = queue.Queue()

# Add items
q.put("apple")
q.put("banana")
q.put("cherry")

# Remove items
print(q.get())  # Output: apple
print(q.get())  # Output: banana
print(q.get())  # Output: cherry


Method                 Description
put(item)              Adds item to the queue
get()                  Removes and returns an item
empty()                Returns True if queue is empty
full()                 Returns True if queue is full
qsize()                Returns the approximate size of the queue
put_nowait(item)       Non-blocking version of put()
get_nowait()           Non-blocking version of get()
task_done()            Indicates that a formerly enqueued task is complete
join()                 Blocks until all items in the queue have been processed


---------------------------------------------
Use Case 1: Producer-Consumer Problem
----------------------------------------------

import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)
        time.sleep(1)

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consuming {item}")
        q.task_done()

# Start threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
q.put(None)  # Signal consumer to exit
t2.join()

-------------------------------------------
Use Case 2: Task Queue with Worker Threads
-------------------------------------------

import threading
import queue

task_queue = queue.Queue()

def worker():
    while True:
        task = task_queue.get()
        if task is None:
            break
        print(f"Processing {task}")
        task_queue.task_done()

# Start worker threads
threads = []
for _ in range(3):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

# Add tasks
for i in range(10):
    task_queue.put(f"Task-{i}")

# Stop workers
for _ in threads:
    task_queue.put(None)

# Wait for all threads to finish
for t in threads:
    t.join()

----------------------------------------------
 Summary
----------------------------------------------

Use queue.Queue for thread-safe FIFO operations.
Use LifoQueue for stack-like behavior.
Use PriorityQueue for tasks with priorities.
Ideal for multi-threaded applications like web crawlers, task schedulers, or producer-consumer systems.



-------------------------------------------------------
Multiprocessing using a shared variable queue
-------------------------------------------------------

 
import multiprocessing
import time

def calc_sq_nums(nums,q):
    for n in nums:
        q.put(n*n)
    
if __name__ == "__main__":
    nums = [ 2,4,5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target = calc_sq_nums, args=(nums,q))
    p.start()
    p.join()
    while q.empty() is False:
        print(q.get())









