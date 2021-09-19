
from sys import argv


def printResult(func):
    def wrapper(*args):
        print(f'\n\u001b[1;34;4m{func.__name__}\u001b[0m\n')

        result = func(*args)

        if isinstance(result, list):
            for elem in result:
                print(elem)
        elif isinstance(result, dict):
            for k, v in result.items():
                print(f"{k} = {v}")
        elif result:
            print(result)

        return result
    return wrapper
