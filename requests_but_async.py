import asyncio
import requests

from utils import Timer


async def async_get(url):
    '''the atomic unit of work'''
    print(f'running async_get for {url=} ...')
    return await asyncio.to_thread(requests.get, url)


async def async_get_gather(url_list):
    '''asynchronously run async_get using async.gather method'''
    return await asyncio.gather(*[async_get(url) for url in url_list])


async def async_get_tasks(url_list):
    '''asynchronously run async_get creating task and awaiting them
    side by side'''
    tasks = [asyncio.create_task(async_get(url)) for url in url_list]
    res_list = [await task for task in tasks]

    return res_list


def blocking_requests_get(url_list):
    '''synchronously run requests.get'''
    response_list = [requests.get(url, timeout=5) for url in url_list]
    return response_list


async def main():
    '''the programm entry point'''
    with Timer():

        url1 = 'https://example.com'
        url2 = 'http://google.com'
        url3 = 'https://tusur.ru'
        url_list = [url1, url2, url3]

        res1, res2, res3 = await async_get_tasks(url_list)
        print(f'{res1.status_code=}\n{res2.status_code=}\n{res3.status_code=}')


asyncio.run(main())
