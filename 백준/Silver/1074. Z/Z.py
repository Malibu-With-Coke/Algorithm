n, r, c = map(int, input().split())
# arr = [[0 for _ in range(pow(2,n))] for _ in range(pow(2,n))]

def sol (n, r, c):
    if n == 0:
        return 0
    else:
        return 2*(r%2)+(c%2) + 4*sol(n-1, int(r/2), int(c/2))
    
print(sol(n,r,c))

































# r += 1 
# c += 1
# answer = 0

# def z (num, x, y):
#     if num <= 0:
#         return
#         # global count
#         # arr[y][x] = count
#         # count += 1
#     else:
#         global answer
#         print(answer)
#         x_ = x//2
#         y_ = y//2
#         print(x, y, x_, y_)
#         mul = (2**(num-1))**2
#         print("mul: ",mul)
#         if (x - 2*x_ < c <= x- x_ and y - 2*y_ < r <= y- y_):
#             print("1")
#             z (num-1, x_, y_)
#         elif (x - x_ < c <= x and y - 2*y_ < r <= y- y_):
#             print("2")
#             answer += mul
#             z (num-1, x, y_)
#         elif (x - 2*x_ < c <= x- x_ and y - y_ < r <= y):
#             print("3")
#             answer += 2*mul
#             z (num-1, x_, y)
#         elif (x - x_ < c <= x and y - y_ < r <= y):
#             print("4")
#             answer += 3*mul
#             z (num-1, x, y)

# z (n, pow(2, n), pow(2, n))

# print (answer)