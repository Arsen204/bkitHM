import random


def genGenerator(num_count, begin, end):
    return (random.randint(begin, end) for _ in range(num_count))
