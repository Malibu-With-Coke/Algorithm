N = input()
break_num = int(input())
if(break_num > 0):
    broken = input().split()
else:
    broken = []

def confirms(num):  # Check for duplication
    # print(list(set(list(map(str, num)) + broken)))
    # print(list(map(str, num)) + broken)
    temp = list(set(map(str, num)))
    # print(temp)
    # print(list(set(temp + broken)))
    # print(temp + broken)
    if len(list(set(temp + broken))) == len((temp + broken)):
        # print(list(set(temp + broken)).sort())
        # print((temp + broken).sort())
        return True
    else:
        return False

if (break_num == 10):
    print(abs(100-int(N)))
    exit()
# print(confirms(N))
if (confirms(N) or N == "100"):
    if (N == "100"):
        print(0)
    else:
        print(min(len(N),abs(100-int(N))))
    exit()

answer = 0

ud = -1
n = int(N)
while(True):
    # print(ud)
    if (n+ud <0):
        ud *= -1
        continue
    if confirms(str(n + ud)):
        break
    if ud > 0:
        ud += 1
    ud *= -1

print(min(len(str(n+ud))+abs(ud),abs(100-n)))
# print(abs(100-n))
# print(1)
# print(ud)