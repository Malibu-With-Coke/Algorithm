n = int(input())
arr_len = int(input())
arr = input()

i, ans, count = 0, 0, 0
while i < (arr_len - 1):
    if arr[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == n:
            ans += 1
            count -= 1
    else:
        i += 1
        count = 0

print(ans)