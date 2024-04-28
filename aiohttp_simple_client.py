import asyncio
import aiohttp


url = 'tusur.ru'
requests_times = 100

async def get_status_code(url):
	async with aiohttp.ClientSession() as session:   				# establishing connection session
		async with session.get(f'https://{url}') as response:
			print(f'status code for "{url}" is {response.status}')


async def main():
	await asyncio.gather(*[get_status_code(url) for i in range(requests_times)])


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # to prevent RuntimeErrors on "windows"
asyncio.run(main())


# Execution results for 4 requests
#
# status code for "tusur.ru" is 200
# status code for "tusur.ru" is 200
# status code for "tusur.ru" is 200
# status code for "tusur.ru" is 200
# [Finished in 1.1s]


# Execution results for 40 requests
#
# status code for "tusur.ru" is 200
# ...
# status code for "tusur.ru" is 200
# [Finished in 3.1s]


# Execution results for 100 requests
#
# status code for "tusur.ru" is 200
# ...
# status code for "tusur.ru" is 200
# [Finished in 5.4s]
