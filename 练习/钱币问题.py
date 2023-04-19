# 求最小硬币数
def minMoney(arr: list[int], aim: int) -> int:
    dp = [aim + 1 for i in range(aim + 1)]
    dp[0] = 0
    for i in range(1, aim + 1):
        for j in arr:
            if i >= j:
                dp[i] = min(dp[i], dp[i - j] + 1)
    return dp[aim] if dp[aim] < aim + 1 else -1


arr = [2, 3, 5, 53]
aim = 54
print(minMoney(arr, aim))
