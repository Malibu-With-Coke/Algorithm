h, w = map(int, input().split())

chess = [list(input()) for i in range(h)]

w_chess = "WBWBWBWB"
b_chess = "BWBWBWBW"
min_count = 999999


for i_ in range(h-7):
    for j_ in range(w-7):
        check = 1
        count1 = 0
        count2 = 0
        # print(check)
        for i in range(i_, i_+8):
            for j in range(j_, j_+8):
                if(check == 1):
                    if(chess[i][j] != w_chess[j-j_]):
                        # print(i,"-",j)
                        count1 += 1
                    elif(chess[i][j] != b_chess[j-j_]):
                        count2 += 1
                else:
                    if(chess[i][j] != b_chess[j-j_]):
                        count1 += 1
                    elif(chess[i][j] != w_chess[j-j_]):
                        count2 += 1
            check *= -1
        if (min_count > min(count1, count2)):
            min_count = min(count1, count2)

print(min_count)
        