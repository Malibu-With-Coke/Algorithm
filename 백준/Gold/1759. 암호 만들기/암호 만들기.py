l,c = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
used = [0 for _ in range(c)]

word = []
max = 0
before_max = 0
def password (num, idx):
    if num == l:
        vowels = 0
        consonants = 0
        check = 0
        for i in word:
            if i in ['a','e','i','o','u']:
                vowels += 1
            else:
                consonants += 1
        if vowels >= 1 and consonants >= 2:
            print(''.join(word))
        return
    else:
        for i in range(idx, c):
            word.append(arr[i])
            password(num+1, i+1)
            word.pop()

password(0, 0)