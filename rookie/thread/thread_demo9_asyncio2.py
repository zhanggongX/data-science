import asyncio
import time

'''
异步协程
'''


async def greet(delay, msg):
    await asyncio.sleep(delay)
    print('hello', msg)


async def main():
    print("开始执行")
    start_time = time.time()

    task1 = asyncio.create_task(greet(1, 'bill'))
    task2 = asyncio.create_task(greet(2, 'mike'))

    await task1
    await task2

    print('运行时间：', time.time() - start_time)
    print('运行结束')


asyncio.run(main())
