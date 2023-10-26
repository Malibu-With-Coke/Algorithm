import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break


def postorder (start_idx, end_idx):
    if start_idx > end_idx:
        return
    if start_idx == end_idx:
        print(tree[start_idx])
        return
    
    mid_idx = end_idx + 1
    for idx in range(start_idx + 1, end_idx + 1):
        if tree[start_idx] < tree[idx]:
            mid_idx = idx
            break


    postorder(start_idx + 1, mid_idx - 1)
    postorder(mid_idx, end_idx)

    print(tree[start_idx])

postorder(0, len(tree) - 1)