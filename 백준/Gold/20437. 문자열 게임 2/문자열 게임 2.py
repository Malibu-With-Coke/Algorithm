import sys

input = sys.stdin.readline

n = int(input())


def solve():
    word = input().rstrip()
    num_duplicate = int(input())

    chr_count = {chr(i): [] for i in range(97, 123)}
    for idx, char in enumerate(word):
        chr_count[char].append(idx)

    max_gap = -1
    min_gap = 10001
    for count in chr_count.values():
        if len(count) < num_duplicate:
            continue

        search_max = len(count) - num_duplicate
        for i in range(0, search_max + 1):
            if max_gap < count[i + num_duplicate - 1] - count[i]:
                max_gap = count[i + num_duplicate - 1] - count[i]
            if min_gap > count[i + num_duplicate - 1] - count[i]:
                min_gap = count[i + num_duplicate - 1] - count[i]
    if max_gap == -1:
        print(-1)
    else:
        print(min_gap + 1, max_gap + 1)


for i in range(n):
    solve()
