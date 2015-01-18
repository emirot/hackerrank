__author__ = 'nolanemirot'


def quickSort(ent):
    if(len(ent) <= 1):
        return ent

    before = []
    after = []
    within = []
    pivot = ent[0]
    for el in ent:
        if el < pivot:
            before.append(el)
        elif el > pivot:
            after.append(el)
        else:
            within.append(el)
        before = quickSort(before)
        within = quickSort(within)
        after = quickSort(after)
    return before + within + after


if __name__ == '__main__':
    print(quickSort([13,4,3,5,65,324,4234,32,12,454]))