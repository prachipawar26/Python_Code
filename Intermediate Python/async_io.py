import asyncio as aio

async def fetch_data(delay):
    print('Fetching Data...')
    await aio.sleep(delay)
    print('Data Fetched!')
    return {"Data": "XYZ"}

async def main():
    print("Start of main co-routine")
    
    # This fires off fetch_data in the background!
    # It starts running, but main() keeps moving immediately.
    task = aio.create_task(fetch_data(5)) 
    
    print("I am doing other work while data fetches...")
    print("I can print this, do math, or start other tasks!")

    # NOW we wait, because we actually need the result to continue
    res = await task 
    
    print(f'Received Result: {res}')
    print("End of main co-routine")

# This creates the coroutine object but DOES NOT run the print statement
# Python will give you a warning here.
coro_object = main() 
print(f"Look, I'm an object: {coro_object}")

# This is the "Engine" that actually executes the code inside the object
aio.run(main())