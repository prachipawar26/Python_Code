from queue import Queue

if __name__ == "__main__":
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)

    print(q.get())
    print(q.empty())

    q.task_done() # always call ---> tells that processing is done
    q.join() # blocks main thread until all elements in queue are processed