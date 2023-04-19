# 求组合数
def minMoney(arr: list[int], aim: int) -> int:
    dp = [0 for i in range(aim + 1)]
    dp[0] = 1
    for j in arr:
        for i in range(1, aim + 1):
            if i >= j:
                dp[i] += dp[i - j]
    return dp[aim]


arr = [2, 1, 5]
aim = 5
print(minMoney(arr, aim))
