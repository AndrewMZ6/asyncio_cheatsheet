# Convenience function for measuring time
# during asyncio and threading experiments
from time import perf_counter


class Timer:

    def __init__(self):
        self.start = perf_counter()
        self.end = None
        self.total_time = None

    def __enter__(self, *args):
        return self

    def __exit__(self, *args):
        self.end = perf_counter()
        self.total_time = self.end - self.start
        print(f'total execution time {self.total_time:.2f} seconds')