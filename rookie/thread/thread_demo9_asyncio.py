import asyncio
import time

'''
同步协程
'''


async def greet(delay, msg):
    await asyncio.sleep(delay)
    print('hello', msg)


async def main():
    print("开始执行")
    start_time = time.time()

    await greet(1, 'bill')
    await greet(2, 'mike')

    print('运行时间：', time.time() - start_time)
    print('运行结束')


asyncio.run(main())
