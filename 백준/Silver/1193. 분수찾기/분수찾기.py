n = int(input())

down_to = 1
up_to = 2
add_num = 1

while not(down_to <= n< up_to):
    down_to += add_num
    add_num += 1
    up_to += add_num

molecule = n - down_to + 1
denominator = add_num - molecule + 1

if add_num % 2 == 0:
    print(f'{molecule}/{denominator}')
else:
    print(f'{denominator}/{molecule}')