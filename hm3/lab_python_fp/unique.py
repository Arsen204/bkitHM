

class Unique(object):
    def __init__(self, items, **kwargs):
        self.elements = {}
        ignoreCase = kwargs.get("ignoreCase")

        if ignoreCase == None:
            ignoreCase = False
        elif not isinstance(ignoreCase, bool):
            raise Exception(
                "\u001b[33mignoreCase\u001b[0m parameter is not of type \u001b[31mbool\u001b[0m")

        for item in items:
            if ignoreCase == True and isinstance(item, str):
                item = item.lower()

            self.elements[item] = item

        self.length = len(items)

    def __next__(self):
        return next(self.elements)

    def __iter__(self):
        return iter(self.elements)

    def printUnique(self):
        print("[", end="")
        print(*self.elements, sep=", ", end="")
        print("]")
