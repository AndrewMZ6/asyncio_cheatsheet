import asyncio
import aiohttp
import requests

from utils import Timer, async_timeit


async def async_aiohttp_get(url: str) -> int:
    '''making aiohttp get requests and returning
       status code
    '''
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            r = resp
    return r


async def async_get(url: str) -> asyncio.coroutine:
    '''the atomic unit of work'''
    return await asyncio.to_thread(requests.get, url)


async def async_get_gather(url_list: str) -> asyncio.Task:
    '''asynchronously run async_get using async.gather method'''
    return await asyncio.gather(*[async_get(url) for url in url_list])



async def main():
    url1 = 'https://example.com'
    url2 = 'http://google.com'
    url3 = 'https://tusur.ru'
    url_list = [url1, url2, url3]
    
    with Timer('aiohttp'):
        print('')
        res = await asyncio.gather(*[async_aiohttp_get(url) for url in url_list])
        for i in res:
            print(f'aiohttp -> status code {i.status} for url {i.url}')

    with Timer('requests'):
        print('')
        res = await async_get_gather(url_list)
        for i in res:
            print(f'requests -> status code {i.status_code} for url {i.url}')
            


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # some weired thing for aiohttp to work
asyncio.run(main())

# Execution results

# aiohttp -> status code 200 for url https://example.com
# aiohttp -> status code 200 for url http://www.google.com/
# aiohttp -> status code 200 for url https://tusur.ru/ru
# total execution time aiohttp: 0.99 seconds

# requests -> status code 200 for url https://example.com/
# requests -> status code 200 for url http://www.google.com/
# requests -> status code 200 for url https://tusur.ru/ru
# total execution time requests: 1.13 seconds
# [Finished in 2.7s]
