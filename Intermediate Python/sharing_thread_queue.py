from queue import Queue
from threading import Thread, Lock, current_thread

def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        t = Thread(target=worker, args=(q, lock))
        t.daemon = True # this thread dies when main thread dies
        t.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print('End')
    