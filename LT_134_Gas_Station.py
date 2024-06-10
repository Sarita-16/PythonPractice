def canCompleteCircuit(gas, cost):
    n = len(gas)

    total_gas = sum(gas)
    total_cost = sum(cost)

    if total_gas < total_cost:
        return -1

    tank = 0
    start_station = 0

    for i in range(n):
        tank += gas[i] - cost[i]

        if tank < 0:
            start_station = i + 1
            tank = 0

    return start_station

gas = list(map(int, input("Enter gas nums : ").split()))
cost = list(map(int, input("Enter costs : ").split()))
print(canCompleteCircuit(gas, cost))
