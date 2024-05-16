def hIndex(citations):
    citations = sorted(citations)
    length = len(citations)

    for i, j in enumerate(citations):
        if length - i <= j:
            return length - i

    return 0

citations = [3,0,6,1,5]
print("H-Index : ", hIndex(citations))