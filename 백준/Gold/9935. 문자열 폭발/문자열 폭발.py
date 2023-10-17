import sys
input = sys.stdin.readline

word = list(input().rstrip())
boom_word = list(input().rstrip())
boom_last_word = boom_word[-1]
bomm_word_len = len(boom_word)
stack = []

for i in word:
    stack.append(i)
    
    while stack and stack[-1] == boom_last_word and len(stack) >= bomm_word_len:
        check = True
        for idx, boom_chr in enumerate(boom_word):
            if stack[-bomm_word_len + idx] != boom_chr:
                check = False
                break
        if not check:
            break

        for _ in range(bomm_word_len):
            stack.pop()



print(*stack if stack else "FRULA",sep="")
