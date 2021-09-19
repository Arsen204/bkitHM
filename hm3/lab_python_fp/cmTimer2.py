from contextlib import contextmanager
import time


@contextmanager
def cmTimer2():
    try:
        startTime = time.perf_counter()
        yield startTime

    finally:
        elapsedTime = time.perf_counter() - startTime

        print()
        print(
            f'\u001b[37mElapsed time: \u001b[1;35m{elapsedTime:5f}\u001b[37m seconds\u001b[0m')
        print()
