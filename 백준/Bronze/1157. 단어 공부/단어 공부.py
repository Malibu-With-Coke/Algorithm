word = input()

count = [0 for _ in range(26)]

max_num = 0
max_index = 0
check = 1

for i in range(len(word)):
    num= ord(word[i])
    if (num>=97):
        num -= 32
    count[num-65] += 1
    if (max_num < count[num-65]):
        max_num = count[num-65]
        max_index = num
        check = 0
    elif (max_num == count[num-65]):
        check = 1

if (check):
    print("?")
else:
    print(chr(max_index))