words = [input() for i in range(int(input()))]

answer = 0

def group_check(word):
    already_check = []
    last_word = ''
    for i in word:
        if i == last_word:
            continue
        elif i in already_check:
            return 0
        else:
            already_check.append(last_word)
            last_word = i
    return 1

for i in range(len(words)):
    answer += group_check(words[i])

print(answer)
