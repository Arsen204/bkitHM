import sys
import math


def getCoef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()

    try:
        coef = float(coef_str)
    except:
        while True:
            print(prompt)
            coef_str = input()

            try:
                coef = float(coef_str)
            except:
                continue
            break
    return coef


def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        if root > 0:
            result.append(math.sqrt(root))
            result.append(-math.sqrt(root))
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        if root1 > 0:
            result.append(math.sqrt(root1))
            result.append(-math.sqrt(root1))
        if root2 > 0:
            result.append(math.sqrt(root2))
            result.append(-math.sqrt(root2))
    return result


def main():
    a = getCoef(1, 'Введите коэффициент А:')
    b = getCoef(2, 'Введите коэффициент B:')
    c = getCoef(3, 'Введите коэффициент C:')

    roots = get_roots(a, b, c)

    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 2:
        print(f'Два корня: {roots[0], roots[1]}')
    elif len_roots == 4:
        print(f'Четыре корня: {roots[0], roots[1], roots[2], roots[3]}')


if __name__ == "__main__":
    main()
