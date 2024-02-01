import sys

input = sys.stdin.readline

num_balls = int(input())
balls = input()

red_ball = balls.count("R")
blue_ball = num_balls - red_ball
ans = min(red_ball, blue_ball)
if red_ball == 0 or blue_ball == 0:
    print(0)
    exit(0)

left_side_ball = 0
for i in range(0, num_balls):
    if balls[i] != balls[0]:
        break
    left_side_ball += 1

right_side_ball = 0
for i in range(num_balls - 1, -1, -1):
    if balls[i] != balls[num_balls - 1]:
        break
    right_side_ball += 1

# print(left_side_ball, right_side_ball)
if balls[0] == "R":
    ans = min(red_ball - left_side_ball, ans)
else:
    ans = min(blue_ball - left_side_ball, ans)

if balls[num_balls - 1] == "R":
    ans = min(red_ball - right_side_ball, ans)
else:
    ans = min(blue_ball - right_side_ball, ans)

print(ans)