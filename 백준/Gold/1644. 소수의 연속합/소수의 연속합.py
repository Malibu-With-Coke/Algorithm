import sys

input = sys.stdin.readline

num = int(input())
if num == 1:
    print(0)
    exit(0)

def sieve_of_eratosthenes(n):  # get prime numbers.
    import math
    nums = [True for _ in range(n + 1)]
    nums[1] = False

    for erase in range(2, int(math.sqrt(n))+1):
        if not nums[erase]:
            continue
        temp = erase * 2
        while temp <= n:
            if nums[temp]:
                nums[temp] = False
            temp += erase

    ret = []
    for prime in range(1, n + 1):
        if nums[prime]:
            ret.append(prime)

    return ret


prime_nums = sieve_of_eratosthenes(num)
length_pn = len(prime_nums)
end_idx = 0
sum = prime_nums[0]
ans = 0

for start_idx in range(length_pn):

    while sum < num and end_idx < length_pn - 1:
        end_idx += 1
        sum += prime_nums[end_idx]

    if sum == num:
        ans += 1

    sum -= prime_nums[start_idx]

print(ans)