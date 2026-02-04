from multiprocessing import Process, Lock, Queue

def squares(n, queue):
    for i in n:
        queue.put(i * i)

def negative(n, queue):
    for i in n:
        queue.put(-1 * i)

if __name__ == "__main__":
    n = range(5)
    q = Queue()

    p1 = Process(target=squares, args=(n, q))
    p2 = Process(target=negative, args=(n, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty(): 
        print(q.get())
