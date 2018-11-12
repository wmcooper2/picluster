#!/usr/bin/env python3
"""Threading tutorial from sentdex;
    https://www.youtube.com/watch?v=NwH0HvMI4EA

"""


import threading as th
import time
from queue import Queue

print_lock = th.Lock()
def exampleJob(worker):
    time.sleep(0.5)
    with print_lock:
        print(th.current_thread().name, worker)

def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()


q = Queue()
for x in range(10):
    t = th.Thread(target=threader)
    t.daemon=True   #dies when main thread dies
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()

end = time.time()
print("time taken", str(end-start))

