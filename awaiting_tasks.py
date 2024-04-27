import asyncio


async def my_coro():
	print('starting my_coro')
	await asyncio.sleep(3)
	print('finishing my_coro')

async def main():
	task = asyncio.create_task(my_coro())	# my_coro   is function;  
	await task								# my_coro() is coroutine;

if __name__ == '__main__':
	asyncio.run(main())
	

# execution results
# starting my_coro
# finishing my_coro
# [Finished in 3.1s]