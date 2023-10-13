import sys
input = sys.stdin.readline

string = str(input().rstrip())
n = int(input())
li = [list(input().split()) for _ in range(n)]

count_string = len(string)
alp = [[0 for _ in range (count_string + 1)] for _ in range(26)]

def alpha_to_idx (alphabet):
    return ord(alphabet) - ord('a')

for idx, chr in enumerate(string):
    alp[ord(chr) - 97][idx] += 1

    for i in range(26):
        alp[i][idx] += alp[i][idx-1]
        
for i in range(n):
    c, s, e = li[i]
    c = ord(c) - 97
    s = int(s)
    e = int(e)
    print(alp[c][e] - alp[c][s - 1])
