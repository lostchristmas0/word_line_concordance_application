def linearSearch(target, aList):
    """Returns the index position of target in aList or -1 if target
    is not in aList"""
    for position in range(len(aList)):
        if target == aList[position]:
            return position
    return -1
