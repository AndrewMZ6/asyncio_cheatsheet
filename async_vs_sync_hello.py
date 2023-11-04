'''
    In this file I compare three methods of "getting access":
        - blocking syncronous function
        - async with using asyncio.gather
        - async with using asyncio.create_task and await
'''
import asyncio
from time import sleep
from utils import Timer


async def async_say_hello():
    '''non blocking long operation'''
    print('aw -> retrieving important data')
    await asyncio.sleep(4)
    return 'aw :: Hello!'


def sync_say_hello():
    '''blocking long operation'''
    print('bl -> retrieving important data')
    sleep(4)
    return 'bl :: Hello!'


async def main():
    with Timer():
        print('work before await')

        # messages = await asyncio.gather(*[async_say_hello() for _ in range(4)])

        # tasks = [asyncio.create_task(async_say_hello()) for _ in range(4)]
        # messages = [await task for task in tasks]

        messages = [sync_say_hello() for _ in range(3)]
        res1, res2, res3 = messages

        # task1 = asyncio.create_task(async_say_hello())
        # task2 = asyncio.create_task(async_say_hello())
        # task3 = asyncio.create_task(async_say_hello())
        
        # res1 = await task1
        # res2 = await task2
        # res3 = await task3

        print('doing other stuff')  # the main() continues only AFTER res1, res2 and res3 are resolved
        print(f'\n{res1=}\n{res2=}\n{res3=}\n')


asyncio.run(main())


# OUTPUT for async versions:
# work before await
# aw -> retrieving important data
# aw -> retrieving important data
# aw -> retrieving important data
# doing other stuff
#
# res1='aw :: Hello!'
# res2='aw :: Hello!'
# res3='aw :: Hello!'
#
# total execution time: 4.01 seconds


# OUTPUT for blocking version:
# work before await
# bl -> retrieving important data
# bl -> retrieving important data
# bl -> retrieving important data
# doing other stuff
#
# res1='bl :: Hello!'
# res2='bl :: Hello!'
# res3='bl :: Hello!'
#
# total execution time: 12.04 seconds
