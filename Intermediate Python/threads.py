from threading import Thread

def squares(n):
    res = [x**2 for x in range(n)]
    print(res)

if __name__ == "__main__":
    threads = []
    num_threads = 10

    # Create threads
    for i in range(num_threads):
        t = Thread(target=squares, args=(10,))
        threads.append(t)

    # Start
    for t in threads:
        t.start()
    
    # 11 threads under a process is created

    for t in threads:
        t.join() # wait for a threads to finish, blocking the main thread

    print('End Main')