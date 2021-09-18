
def fieldGenerator(items, *args):
    assert len(args) > 0

    result = []

    for item in items:
        temp = {}
        for arg in args:
            value = item.get(arg)
            if value != None:
                temp.update({arg: value})
        if temp:
            if len(args) == 1:
                result.append(temp[arg])
            else:
                result.append(temp)

    return result
