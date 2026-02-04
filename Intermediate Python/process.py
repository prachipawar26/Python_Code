from multiprocessing import Process
import os

def squares(n):
    res = [x**2 for x in range(n)]
    print(res)

if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()


    # Create processes
    for i in range(num_processes):
        p = Process(target=squares, args=(10,))
        processes.append(p)

    """When a new process starts, it re-imports your script. Without the guard, 
    the child process tries to create its own child processes, leading to an infinite loop of process creation 
    until the system blocks it."""

    # Start
    for p in processes:
        p.start()
    
    for p in processes:
        p.join() # wait for a process to finish, blocking the main thread

    print('End Main')