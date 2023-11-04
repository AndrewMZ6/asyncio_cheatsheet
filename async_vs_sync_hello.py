import asyncio
from time import sleep, perf_counter


async def async_say_hello():
    print('aw -> retrieving important data')
    await asyncio.sleep(4)
    return 'aw :: Hello!'


def sync_say_hello():
    print('bl -> retrieving important data')
    sleep(4)
    return 'bl :: Hello!'


async def main():
    start = perf_counter()
    print('work before await')

    # messages = await asyncio.gather(*[async_say_hello() for _ in range(4)])

    # tasks = [asyncio.create_task(async_say_hello()) for _ in range(4)]
    # messages = [await task for task in tasks]

    # messages = [sync_say_hello() for _ in range(4)]

    task1 = asyncio.create_task(async_say_hello())
    task2 = asyncio.create_task(async_say_hello())
    task3 = asyncio.create_task(async_say_hello())
    
    res1 = await task1
    res2 = await task2
    res3 = await task3
    # task = asyncio.create_task(async_say_hello())
    # res = await task

    # res = sync_say_hello()

    print('doing other stuff')  # the main() continues ofny AFTER res1, res2 and res3 are resolved
    
    # print(*[message for message in messages])
    print(f'\n{res1=}\n{res2=}\n{res3=}\n')
    print(f'total amount of time {perf_counter() - start:.2f} seconds')


asyncio.run(main())
