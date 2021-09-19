import time


class cmTimer1():
    def __enter__(self):
        self._start_time = time.perf_counter()
        return self._start_time

    def __exit__(self, type, value, traceback):
        del type, value, traceback

        elapsedTime = time.perf_counter() - self._start_time
        self._start_time = None

        print()
        print(
            f'\u001b[37mElapsed time: \u001b[1;35m{elapsedTime:5f}\u001b[37m seconds\u001b[0m')
        print()
