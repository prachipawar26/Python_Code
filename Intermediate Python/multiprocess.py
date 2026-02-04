from multiprocessing import Process, current_process
import os
import time

def squares():
    # Adding a print so we know the process started
    print(f"Child Process {os.getpid()} is starting...")
    for i in range(50):
        _ = i * i
        time.sleep(0.05)
    print(f"Child Process {os.getpid()} is finished.")

if __name__ == "__main__":
    print(f"Main Process ID: {os.getpid()}")
    
    num_processes = os.cpu_count()
    print(f"Detected {num_processes} CPU cores. Creating processes...")
    
    processes = []

    for i in range(num_processes):
        p = Process(target=squares)
        processes.append(p)
        p.start() # Starting them immediately in the first loop is also fine

    for p in processes:
        p.join()

    print("Main process: All children have finished. End.")