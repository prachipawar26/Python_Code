from multiprocessing import Process, Array, Lock
# Sharing data within processes is difficult as each process is in different memory space
# They need special shared memory objects ---> Value, Array
import os
import time

def add_100(n, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(n)):
            with lock:
                n[i] += 1

if __name__ == "__main__":
    shared_arr = Array('i', [0, 1, 2, 3, 4]) # Array('data type', list)
    print('Shared array at start: ', shared_arr[:])

    lock = Lock()

    # race condition might happend if no Lock used
    p1 = Process(target=add_100, args=(shared_arr, lock))
    p2 = Process(target=add_100, args=(shared_arr, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Shared array at end: ', shared_arr[:])
