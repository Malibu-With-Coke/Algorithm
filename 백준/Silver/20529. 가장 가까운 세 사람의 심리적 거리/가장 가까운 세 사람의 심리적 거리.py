import sys
input = sys.stdin.readline

from itertools import combinations

n = int(input())

def compare(person1, person2):
    count = 0
    for i in range(4):
        if person1[i] != person2[i]:
            count += 1
    
    return count

def solve():
    _ = int(input())
    people = list(map(str, input().split()))
    mbti = {}
    for a in "I", "E":
        for b in "N", "S":
            for c in "T", "F":
                for d in "J", "P":
                    temp = a+b+c+d
                    mbti[temp] = 0

    numberOfCases = 0
    cases = []    
    
    for person in people:
        if mbti[person] < 3:
            mbti[person] += 1
            cases.append(person)

    com_case = combinations(cases, 3)

    ans = sys.maxsize

    for case in com_case:
        a, b, c = case
        diff = 0

        diff += compare(a, b)
        diff += compare(b, c)
        diff += compare(a, c)
        
        ans = min(diff, ans)
    

    print(ans)
    
for _ in range(n):
    solve()