n = int(input())
num = 1
count = 1

while True:
    if n <= num:
        print(count)
        break

    num += 6 * count
    count += 1