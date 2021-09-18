from lab_python_fp.field import fieldGenerator
from lab_python_fp.genRandom import genGenerator
from lab_python_fp.unique import Unique
from lab_python_fp.sort import sortLambda
from lab_python_fp.printResult import printResult


@printResult
def fieldGeneratorTest():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
    ]

    return fieldGenerator(goods, 'title', 'color')


@printResult
def genRandomTest():
    test1 = genGenerator(5, 3, 10)
    test2 = genGenerator(10, 0, 100)
    test3 = genGenerator(2, -10, 10)
    return {"test1": test1, "test2": test2, "test3": test3}


@printResult
def uniqueTest():
    data1 = [1, 1, 1, 1, 4, 1, 2, 2, 2, 2, 2, 3]
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    try:
        unique = Unique(data1, ignoreCase=True)
        unique.printUnique()
    except Exception as e:
        print(e)

    try:
        unique = Unique(data2, ignoreCase=True)
        unique.printUnique()
    except Exception as e:
        print(e)

    try:
        unique = Unique(data2)
        unique.printUnique()
    except Exception as e:
        print(e)

    try:
        unique = Unique(data2, ignoreCase=43)
        unique.printUnique()
    except Exception as e:
        print(e)


@printResult
def sortTest():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    return sortLambda(data)


def main():
    fieldGeneratorTest()
    genRandomTest()
    uniqueTest()
    sortTest()


if __name__ == "__main__":
    main()
