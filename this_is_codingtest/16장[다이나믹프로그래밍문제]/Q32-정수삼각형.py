n = int(input())

dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            left_down = 0
        else:
            left_down = dp[i-1][j-1]
        if j == len(dp[i]) - 1:
            right_down = 0
        else:
            right_down = dp[i-1][j]
        dp[i][j] = dp[i][j] + max(left_down, right_down)

result = 0
for i in dp[n-1]:
    result = max(result, i)
print(result)