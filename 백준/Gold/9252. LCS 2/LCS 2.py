import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

word1_len = len(word1)
word2_len = len(word2)

dp = [[0 for _ in range(word2_len+1)] for _ in range(word1_len+1)]
word = [["" for _ in range(word2_len+1)] for _ in range(word1_len+1)]

for i in range(1, word1_len+1):
    for j in range(1, word2_len+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            word[i][j] = word[i-1][j-1] + word1[i-1]
        else:
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                word[i][j] = word[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
                word[i][j] = word[i][j-1]

print(dp[word1_len][word2_len])
if word[word1_len][word2_len] != "":
    print(word[word1_len][word2_len])