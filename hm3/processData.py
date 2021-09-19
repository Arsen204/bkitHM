import json
import sys
from lab_python_fp.cmTimer1 import cmTimer1
from lab_python_fp.printResult import printResult
from lab_python_fp.unique import Unique
from lab_python_fp.genRandom import genGenerator


if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = '/Users/arsenvardumyan/bkitHM/hm3/data_row.json'


with open(path) as f:
    data = json.load(f)


@printResult
def f1(data):
    return sorted(Unique((data[x]["job-name"] for x, _ in enumerate(data)), ignoreCase=True), key=lambda x: x.lower())


@printResult
def f2(data):
    return list(filter(lambda x: x.startswith('программист'), data))


@printResult
def f3(data):
    return list(map(lambda x: x + " с опытом Python", data))


@printResult
def f4(data):
    salaris = genGenerator(len(data), 100000, 200000)
    return list(zip(data, salaris))


if __name__ == '__main__':
    with cmTimer1():
        f4(f3(f2(f1(data))))
