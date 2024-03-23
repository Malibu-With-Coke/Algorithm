import sys

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


def calculate_point(team_lst):
    sum_point = 0
    for i in range(len(team_lst)):
        a_player = team_lst[i]
        for j in range(i + 1, len(team_lst)):
            b_player = team_lst[j]
            sum_point += matrix[a_player][b_player] + matrix[b_player][a_player]
    return sum_point


half_n = n // 2
already_used = [False] * n
min_gap = 10e10


def make_combine(cnt, idx, team_lst):
    if cnt == half_n:
        team_a_point = calculate_point(team_lst)

        other_team_lst = []
        for i in range(n):
            if not already_used[i]:
                other_team_lst.append(i)

        team_b_point = calculate_point(other_team_lst)

        global min_gap
        min_gap = min(abs(team_a_point - team_b_point), min_gap)
        return

    for i in range(idx, n):
        if not already_used[i]:
            team_lst.append(i)
            already_used[i] = True

            make_combine(cnt + 1, i + 1, team_lst)

            team_lst.pop()
            already_used[i] = False


make_combine(0, 0, [])
print(min_gap)
