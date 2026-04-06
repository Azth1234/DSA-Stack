def count_ways(coins, amount):
    n = len(coins)
    
    # dp[i] = number of ways to make sum i
    dp = [0] * (amount + 1)
    dp[0] = 1   # one way to make 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]


# Example
coins = [1, 2, 3]
amount = 4

print("Number of ways:", count_ways(coins, amount))