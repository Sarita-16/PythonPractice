def fruitsCalculation(arr):
    totalSales = 0
    bestProduct = ''
    maxi = 0
    for tup in arr:
        mul = 1
        for i in tup:
            mul = tup[-2] * tup[-1]
            if mul > maxi:
                maxi = mul
                bestProduct = tup[0]
        totalSales = totalSales + mul

    avgSales = "{:.2f}".format(totalSales / len(arr))

    print("Total Sum : ", totalSales, ", Average Sales : ", avgSales, ", Best Product : ", bestProduct)


arr = []

while True:
    name, unit, cost = input().split()
    if name.lower() == 'q' or unit.lower() == 'q' or cost.lower() == 'q':
        break
    unit = float(unit)
    cost = float(cost)

    arr.append((name, unit, cost))  # Append a tuple of (name, unit, cost)

print("Array : ", arr)

fruitsCalculation(arr)
