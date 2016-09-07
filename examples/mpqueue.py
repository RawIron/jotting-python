import multiprocessing as mp
import Queue
import time


def worker(q):
  event_available = True
  while event_available:
    try:
      event = q.get(True, 1)
      print event
    except Queue.Empty:
      event_available = False


q = mp.Queue()

p = mp.Process(target=worker, args=(q,))
p.start()

for _ in range(1000):
  q.put({"id": 1})

q.close()
q.join_thread()

p.join()
