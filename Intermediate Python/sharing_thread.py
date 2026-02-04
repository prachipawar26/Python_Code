from threading import Thread, Lock
import time

val = 0

def increase(lock):
    global val
    
    # lock.acquire()
    # local_var = val
    # local_var += 1
    # time.sleep(0.2)
    # val = local_var
    # lock.release()

    # or use context manager
    with lock:
        local_var = val
        local_var += 1
        time.sleep(0.2)
        val = local_var

if __name__ == "__main__":
    lock = Lock()
    print(f'Start value = {val}')

    # race condition will occur - two or more threads look to modify variable
    # prevent race condition use lock
    t1 = Thread(target=increase, args=(lock,))
    t2 = Thread(target=increase, args=(lock,))
    t3 = Thread(target=increase, args=(lock,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print(f'End value = {val}')
