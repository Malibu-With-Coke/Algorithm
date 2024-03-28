import sys

input = sys.stdin.readline

n_matrix, m_tree, k_year = map(int, input().split())
add_nutrient = [list(map(int, input().split())) for _ in range(n_matrix)]
tree_matrix = [[[] for _ in range(n_matrix)] for _ in range(n_matrix)]

for _ in range(m_tree):
    x, y, age = map(int, input().split())
    x -= 1
    y -= 1
    tree_matrix[x][y].append(age)

cur_nutrient = [[5 for _ in range(n_matrix)] for _ in range(n_matrix)]
for _ in range(k_year):

    next_breeding = []
    for i in range(n_matrix):
        for j in range(n_matrix):

            if len(tree_matrix[i][j]) != 0:
                tree_matrix[i][j].sort()
                new_tree = []
                next_add_nut = 0
                for tree_age in tree_matrix[i][j]:
                    if cur_nutrient[i][j] - tree_age >= 0:
                        cur_nutrient[i][j] -= tree_age
                        new_tree.append(tree_age + 1)
                        if (tree_age + 1) % 5 == 0:
                            next_breeding.append((i, j))
                    else:
                        next_add_nut += tree_age // 2

                tree_matrix[i][j] = new_tree
                cur_nutrient[i][j] += next_add_nut

    for x, y in next_breeding:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue

                if 0 <= dx + x < n_matrix and 0 <= dy + y < n_matrix:
                    tree_matrix[dx + x][dy + y].append(1)

    for i in range(n_matrix):
        for j in range(n_matrix):
            cur_nutrient[i][j] += add_nutrient[i][j]

rest_tree = 0
for i in range(n_matrix):
    for j in range(n_matrix):
        rest_tree += len(tree_matrix[i][j])

print(rest_tree)