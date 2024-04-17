def BTBS(prices):
    bp = prices[0]
    p = 0
    for i in range(1, len(prices)):
        if prices[i] < bp:
            bp = prices[i]
        p = max(p, prices[i] - bp)
    return p

n = int(input("Enter how many numbers you want to insert : "))
prices = []
for i in range(n):
    prices.append(int(input()))
print("Maximum profit : ", BTBS(prices))