import sys

input = sys.stdin.readline

n, m, l, num_stars = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(num_stars)]

ans = 0
for i in range(num_stars):
    for j in range(num_stars):
        left_upper_x = min(stars[i][0], stars[j][0])
        left_upper_y = min(stars[i][1], stars[j][1])
        cnt = 0
        for k in range(num_stars):
            if (
                left_upper_x <= stars[k][0] <= left_upper_x + l
                and left_upper_y <= stars[k][1] <= left_upper_y + l
            ):
                cnt += 1

        ans = max(ans, cnt)

print(num_stars - ans)
