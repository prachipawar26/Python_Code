from multiprocessing import Process, Value, Lock
# Sharing data within processes is difficult as each process is in different memory space
# They need special shared memory objects ---> Value, Array
import os
import time

def add_100(n, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            n.value += 1

if __name__ == "__main__":
    shared_val = Value('i', 0) # Value('data type', start_value)
    print('Shared value at start: ', shared_val.value)

    lock = Lock()

    # race condition might happend if no Lock used
    p1 = Process(target=add_100, args=(shared_val, lock))
    p2 = Process(target=add_100, args=(shared_val, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Shared value at end: ', shared_val.value)
