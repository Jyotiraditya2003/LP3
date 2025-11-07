#0/1 knapsack using dp

values =[]
n = int(input("enter number of values:"))
for i in range(n):
    val = int(input(f"enter value {i+1}:"))
    values.append(val)
weights =[]
for i in range(n):
    wt = int(input(f"enter weight {i+1}:"))
    weights.append(wt)
capacity = int(input("enter capacity of knapsack:"))

def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0  for _ in range(capacity + 1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w],
                    values[i-1] + dp[i-1][w - weights[i-1]]
                )
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

if __name__ == "__main__":
#    values = [60, 100, 120]
#    weights = [10, 20, 30]
#    capacity = 50
    max_value = knapsack_01(values, weights, capacity)
    print("maximum value is:", max_value)

#TC o(nlogn)
#SC O(n)