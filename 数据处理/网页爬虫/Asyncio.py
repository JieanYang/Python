
# normal way 
# import time


# def job(t):
#     print('Start job ', t)
#     time.sleep(t)               # wait for "t" seconds
#     print('Job ', t, ' takes ', t, ' s')
    

# def main():
#     [job(t) for t in range(1, 3)]
    
    
# t1 = time.time()
# main()
# print("NO async total time : ", time.time() - t1)


# Asyncio
import asyncio
import time

async def job(t):
    print('Start job ', t)
    await asyncio.sleep(t)          # wait for "t" seconds, it will look for another job while await
    print('Job ', t, ' takes ', t, ' s')
    

async def main(loop):
    tasks = [loop.create_task(job(t)) for t in range(1, 3)]     # just create, not run job
    await asyncio.wait(tasks)                                   # run jobs and wait for all tasks done

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()                          # Ipython notebook gives error if close loop
print("Async total time : ", time.time() - t1)