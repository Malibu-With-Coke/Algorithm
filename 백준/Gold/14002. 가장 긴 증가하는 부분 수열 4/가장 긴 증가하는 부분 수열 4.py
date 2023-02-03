n = int(input())

arr = list(map(int, input().split()))

dp_inc = [0 for i in range(n)]
previous_num = {i : -1 for i in range(n)}
max_index = 0

for i in range(0,n,1):
    for j in range(0,i,1):
        if arr[i] > arr[j] and dp_inc[i] < dp_inc[j]:
            dp_inc[i] = dp_inc[j]
            previous_num[i] = j
    dp_inc[i] += 1
    if dp_inc[max_index] < dp_inc[i]:
        max_index = i


idx = max_index
ans = []
while True:
    ans.append(str(arr[idx]))
    idx = previous_num[idx]
    if idx == -1:
        break

print(dp_inc[max_index])
for i in range(len(ans)-1,-1,-1):
    print(ans[i], end=" ")
print()