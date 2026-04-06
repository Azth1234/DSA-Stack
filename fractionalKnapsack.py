def fractional_knapsack(weights, profits, capacity):
    n = len(weights)

    # Calculate profit/weight ratio
    items = []
    for i in range(n):
        items.append((profits[i]/weights[i], weights[i], profits[i]))

    # Sort by ratio in descending order
    items.sort(reverse=True)

    total_profit = 0
    w = 0

    for ratio, weight, profit in items:
        if w + weight <= capacity:
            total_profit += profit
            w = w + weight
        else:
            remain = capacity - w
            total_profit += ratio * remain
            break

    return total_profit


weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

print("Maximum Profit:", fractional_knapsack(weights, profits, capacity))