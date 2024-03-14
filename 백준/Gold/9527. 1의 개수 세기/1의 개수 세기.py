import sys

input = sys.stdin.readline

n, m = map(int, input().split())

psum = [0 for _ in range(55)]
psum[1] = 1

for i in range(2, 55):
    psum[i] = psum[i - 1]
    psum[i] += pow(2, i - 1) + (i - 1) * pow(2, i - 2)


def get_cum_sum(num):
    cnt = 0
    bin_num = bin(num)[2:]
    length = len(bin_num)
    for i in range(length):
        if bin_num[i] == "1":
            val = length - i - 1
            cnt += psum[val]
            cnt += num - 2**val + 1
            num = num - 2**val
    return cnt


print(get_cum_sum(m) - get_cum_sum(n - 1))