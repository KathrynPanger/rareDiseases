def onlyInts(list):
    integerList = []
    for item in list:
        try:
            int(item)
            integerList.append(item)
        except:
            continue
    return integerList