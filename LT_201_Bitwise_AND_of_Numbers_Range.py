def rangeBitwiseAnd(left: int, right: int) -> int:
    shift = 0
    # Find the common prefix
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    # Shift the prefix back to its original position
    return left << shift

left = int(input("Enter Left number : "))
right = int(input("Enter Right number : "))
print(rangeBitwiseAnd(left, right))
