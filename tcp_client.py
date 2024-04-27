import asyncio


async def tcp_echo_client(message):
	"""An example TCP client"""
	reader, writer = await asyncio.open_connection(
		'1.1.1.1', 443)

	print(f'send: {message!r}')
	writer.write(message.encode())
	await writer.drain()

	data = await reader.read(1000)
	print(f'received: {data.decode()!r}')

	print('closing the connection')
	writer.close()
	await writer.wait_closed()

asyncio.run(tcp_echo_client('hey'))


# EXECUTION RESULTS
#
# send: 'hey'
# received: 'HTTP/1.1 400 Bad Request\r\nServer: cloudflare\r\nDate: Sat, 27 Apr 2024 22:54:58 GMT\r\nContent-Type: text/html\r\nContent-Length: 155\r\nConnection: close\r\nCF-RAY: -\r\n\r\n<html>\r\n<head><title>400 Bad Request</title></head>\r\n<body>\r\n<center><h1>400 Bad Request</h1></center>\r\n<hr><center>cloudflare</center>\r\n</body>\r\n</html>\r\n'
# closing the connection
# [Finished in 703ms]
