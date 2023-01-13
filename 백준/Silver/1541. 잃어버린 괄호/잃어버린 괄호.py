import re

a = re.split('([-|+])',input())
# print(a)

buho = 1
sum = 0
for i in a:
    # if i == '+':
    if i == '-':
        buho = -1
    elif i == '+':
        continue
    else:
        sum += int(i) * buho

print(sum)

# 55-50+40