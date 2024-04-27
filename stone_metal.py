def stoneMetal(stone, metal):
    count = 0
    """ stone = stone.lower()           # convert all char of this string to lower case
    metal = metal.lower()           # convert all char of this string to lower case
    metal = ''.join(set(metal))     # convert the string to a set to remove duplicates, then join the char into a string"""
    for i in metal:
        for j in stone:
            if i == j:
                count = count+1

    return count

stone = input("Enter any stone names : ")
metal = input("Enter the metals name : ")
result = stoneMetal(stone, metal)
print('Total number of metal found in stone is : ', format(result))