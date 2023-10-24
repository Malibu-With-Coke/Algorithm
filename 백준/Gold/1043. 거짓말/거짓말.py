import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lier = list(map(int, input().split()))
num_lier = lier[0]
if num_lier == 0:
    print(m)
    exit()

group = {i : set() for i in range(1, n + 1)}

tell_true_people = {i : False for i in range(1, n + 1)}

parties = [list(map(int, input().split())) for _ in range(m)]

for idx, party in enumerate(parties):
    for i in range(1, party[0]):
        for j in range(i + 1, party[0] + 1):
            group[party[i]].add(party[j])
            group[party[j]].add(party[i])

from collections import deque

deq = deque()    
for i in range (1, num_lier + 1):
    deq.append(lier[i])
    tell_true_people[lier[i]] = True
    

while deq:
    person = deq.popleft()
    
    for friend in group[person]:
        if not tell_true_people[friend]:
            tell_true_people[friend] = True
            deq.append(friend)

ans = 0 

for party in parties:
    
    check = True

    for idx in range(1, party[0] + 1):
        if tell_true_people[party[idx]]:
            check = False
            break
    
    if check:
        ans += 1

print(ans)