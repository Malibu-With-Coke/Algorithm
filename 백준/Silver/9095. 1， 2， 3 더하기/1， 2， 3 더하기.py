n = int(input())

dp = {1:1, 2:2, 3:4}

def solve(num):
    if num in dp:
        return dp[num]
    else:
        dp[num] = solve(num-1) + solve(num-2) + solve(num-3) 
        return dp[num]

for _ in range(n):
    num = int(input())
    print(solve(num))