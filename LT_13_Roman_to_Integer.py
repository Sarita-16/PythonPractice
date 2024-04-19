def romanToInt(roman):
    romanNum = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    result = 0
    preVal = 0
    for i in roman:
        val = romanNum[i]
        if val > preVal:
            result = result + val - 2 * preVal
        else:
            result = result + val
        preVal = val
    return result


r = input("Enter Roman numerals : ")
roman = r.upper()
result = romanToInt(roman)
print(r," : ",result)