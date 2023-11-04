import asyncio
from time import sleep
from utils import Timer


async def async_say_hello():
    '''non blocking '''
    print('aw -> retrieving important data')
    await asyncio.sleep(4)
    return 'aw :: Hello!'


def sync_say_hello():
    print('bl -> retrieving important data')
    sleep(4)
    return 'bl :: Hello!'


async def main():
    with Timer():
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

        print('doing other stuff')  # the main() continues only AFTER res1, res2 and res3 are resolved
        print(f'\n{res1=}\n{res2=}\n{res3=}\n')


asyncio.run(main())
