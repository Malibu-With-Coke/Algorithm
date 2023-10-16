import sys
input = sys.stdin.readline

n = int(input())

INF = 10e9

def solve():
    num_files = int(input())

    files = list(map(int, input().split()))

    connetion_files = [[INF for _ in range(num_files)] for _ in range(num_files)]

    for i in range(num_files):
        connetion_files[i][i] = 0

    for gap in range(1, num_files):

        time_taken = sum(files[0 : gap])
        for start_idx in range(num_files - gap):
            
            end_idx = start_idx + gap
            time_taken += files[end_idx]
                        
            for mid_idx in range(start_idx, end_idx):
                connetion_files[start_idx][end_idx] = min(connetion_files[start_idx][end_idx], connetion_files[start_idx][mid_idx] +  connetion_files[mid_idx + 1][end_idx] + time_taken)
            time_taken -= files[start_idx]
    print(connetion_files[0][num_files - 1])


for i in range(n):
    solve()