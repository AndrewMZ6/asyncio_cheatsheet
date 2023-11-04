from time import perf_counter
import asyncio


class Timer:
    '''
        Convenience class for measuring time
        during asyncio and threading experiments.

        Usage example:
        >>> with Timer():
        >>>     run some stuff
        >>>
        ... total execution time: x seconds
    '''

    def __init__(self):
        self.start = perf_counter()
        self.end = None
        self.total_time = None

    def __enter__(self, *args):
        return self

    def __exit__(self, *args):
        self.end = perf_counter()
        self.total_time = self.end - self.start
        print(f'total execution time: {self.total_time:.2f} seconds')


async def async_delay(n: int, name: str = 'default') -> int:
    '''
        Convenience function for immitating
        long running non blocking operations

        Usage exmaple:
        >>> await async_delay(5)
        or
        >>> await async_delay(3, 'my_delay')
    '''
    print(f'delay {name} is sleeping for {n} seconds')
    await asyncio.sleep(n)
    print(f'delay {name} finished sleeping')
    return n
