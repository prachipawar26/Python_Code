from multiprocessing import Pool # manages nultiple process

def cube(n):
    return n ** 3

def square(n):
    return [i * i for i in n]

if __name__ == "__main__":
    nums = range(10)
    pool = Pool()

    # map(), apply(), join(), close() ---> important methods of Pool
    
    # USE MAP: When you have a collection of data and want to process in parallel
    # This splits 'nums' across your 10 cores.
    cb = pool.map(cube, nums)

    # USE APPLY: When you want to run a single task once. 
    # Note: apply() is "blocking" (it stops the main script until it's done).
    sq = pool.apply(square, args=(nums,))

    pool.close() # always called before join()
    pool.join()

    print('Result cube: ', cb)
    print('Result square: ', sq)
