words = input()

stack = []
mul = 1
answer = 0

for i in range(len(words)):
    if words[i] == '(':
        stack.append(words[i])
        mul *= 2
    elif words[i] == '[':
        stack.append(words[i])
        mul *= 3
    elif words[i] == ')':
        if(stack and stack[-1] == '('):
            if(words[i-1] == '('):
                answer += mul
        else:
            answer = 0
            break
        mul /= 2
        stack.pop()
    elif words[i] == ']':
        if(stack and stack[-1] == '['):
            if(words[i-1] == '['):
                answer += mul
        else:
            answer = 0
            break
        mul /= 3
        stack.pop()

if stack:
    answer = 0
print(int(answer))