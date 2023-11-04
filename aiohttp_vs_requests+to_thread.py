import asyncio
import aiohttp
import requests

from utils import Timer, async_timeit


async def async_aiohttp_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            r = resp.status


    return r


async def async_get(url):
    '''the atomic unit of work'''
    print(f'running async_get for {url=} ...')
    return await asyncio.to_thread(requests.get, url)


async def async_get_gather(url_list):
    '''asynchronously run async_get using async.gather method'''
    return await asyncio.gather(*[async_get(url) for url in url_list])


@async_timeit
async def main():
    url1 = 'https://example.com'
    url2 = 'http://google.com'
    url3 = 'https://tusur.ru'
    url_list = [url1, url2, url3]
    
    with Timer('aiohttp'):
        res = await asyncio.gather(*[async_aiohttp_get(url) for url in url_list])
        for i in res:
            print(i)

    with Timer('requests'):
        res = await async_get_gather(url_list)
        for i in res:
            print(i.status_code)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # some weired thing for aiohttp to work
asyncio.run(main())

# OUTPUT:
#
# 200
# 200
# 200
# total execution time aiohttp: 1.21 seconds
# running async_get for url='https://example.com' ...
# running async_get for url='http://google.com' ...
# running async_get for url='https://tusur.ru' ...
# 200
# 200
# 200
# total execution time requests: 1.08 seconds
