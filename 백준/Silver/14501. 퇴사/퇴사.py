n = int(input())

d = {}
for i in range(1,n+1):
    during_days, payment = map(int, input().split())
    d[i] = [during_days, payment]

dp = [0 for i in range(n+2)]    # 0 ~ n+1

max_num = 0

for i in range(n, 0, -1):
    during_days, payment = d[i]

    if during_days + i > n+1:
        dp[i] = dp[i+1]
        continue
    
    dp[i] = max(dp[i+1], dp[i+during_days]+payment)
    if dp[i] > max_num:
        max_num = dp[i]

print(max_num)