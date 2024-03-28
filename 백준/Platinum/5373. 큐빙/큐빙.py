import sys

input = sys.stdin.readline


def turn_face(face, clock_turn=True):
    if clock_turn:
        next_face = [
            " ",
            face[7],
            face[4],
            face[1],
            face[8],
            face[5],
            face[2],
            face[9],
            face[6],
            face[3],
        ]
    else:
        next_face = [
            " ",
            face[3],
            face[6],
            face[9],
            face[2],
            face[5],
            face[8],
            face[1],
            face[4],
            face[7],
        ]
    return next_face


def turn_clock(part_1, part_2, part_3, part_4):
    temp = part_1
    part_1 = part_2
    part_2 = part_3
    part_3 = part_4
    part_4 = temp


def turn_reverse_clock(part_1, part_2, part_3, part_4):
    temp = part_1
    part_1 = part_4
    part_4 = part_3
    part_3 = part_2
    part_2 = temp


def front_turn(clock_turn=True):
    global LF, UF, RF, DF, FF, BF
    FF = turn_face(FF, clock_turn)
    if clock_turn:
        temp0, temp1, temp2 = UF[7], UF[8], UF[9]
        UF[7], UF[8], UF[9] = LF[9], LF[6], LF[3]
        LF[9], LF[6], LF[3] = DF[3], DF[2], DF[1]
        DF[3], DF[2], DF[1] = RF[1], RF[4], RF[7]
        RF[1], RF[4], RF[7] = temp0, temp1, temp2
    else:
        temp0, temp1, temp2 = UF[7], UF[8], UF[9]
        UF[7], UF[8], UF[9] = RF[1], RF[4], RF[7]
        RF[1], RF[4], RF[7] = DF[3], DF[2], DF[1]
        DF[3], DF[2], DF[1] = LF[9], LF[6], LF[3]
        LF[9], LF[6], LF[3] = temp0, temp1, temp2


def down_turn(clock_turn=True):
    global LF, UF, RF, DF, FF, BF
    DF = turn_face(DF, clock_turn)
    if clock_turn:
        temp0, temp1, temp2 = FF[7], FF[8], FF[9]
        FF[7], FF[8], FF[9] = LF[7], LF[8], LF[9]
        LF[7], LF[8], LF[9] = BF[3], BF[2], BF[1]
        BF[3], BF[2], BF[1] = RF[7], RF[8], RF[9]
        RF[7], RF[8], RF[9] = temp0, temp1, temp2
    else:
        temp0, temp1, temp2 = FF[7], FF[8], FF[9]
        FF[7], FF[8], FF[9] = RF[7], RF[8], RF[9]
        RF[7], RF[8], RF[9] = BF[3], BF[2], BF[1]
        BF[3], BF[2], BF[1] = LF[7], LF[8], LF[9]
        LF[7], LF[8], LF[9] = temp0, temp1, temp2


def back_turn(clock_turn=True):
    global LF, UF, RF, DF, FF, BF
    BF = turn_face(BF, clock_turn)
    if clock_turn:
        temp0, temp1, temp2 = DF[7], DF[8], DF[9]
        DF[7], DF[8], DF[9] = LF[1], LF[4], LF[7]
        LF[1], LF[4], LF[7] = UF[3], UF[2], UF[1]
        UF[3], UF[2], UF[1] = RF[9], RF[6], RF[3]
        RF[9], RF[6], RF[3] = temp0, temp1, temp2
    else:
        temp0, temp1, temp2 = DF[7], DF[8], DF[9]
        DF[7], DF[8], DF[9] = RF[9], RF[6], RF[3]
        RF[9], RF[6], RF[3] = UF[3], UF[2], UF[1]
        UF[3], UF[2], UF[1] = LF[1], LF[4], LF[7]
        LF[1], LF[4], LF[7] = temp0, temp1, temp2


def up_turn(clock_turn=True):
    global LF, UF, RF, DF, FF, BF
    UF = turn_face(UF, clock_turn)
    if clock_turn:
        temp0, temp1, temp2 = BF[7], BF[8], BF[9]
        BF[7], BF[8], BF[9] = LF[3], LF[2], LF[1]
        LF[3], LF[2], LF[1] = FF[3], FF[2], FF[1]
        FF[3], FF[2], FF[1] = RF[3], RF[2], RF[1]
        RF[3], RF[2], RF[1] = temp0, temp1, temp2
    else:
        temp0, temp1, temp2 = BF[7], BF[8], BF[9]
        BF[7], BF[8], BF[9] = RF[3], RF[2], RF[1]
        RF[3], RF[2], RF[1] = FF[3], FF[2], FF[1]
        FF[3], FF[2], FF[1] = LF[3], LF[2], LF[1]
        LF[3], LF[2], LF[1] = temp0, temp1, temp2


def right_turn(clock_turn=True):
    global LF, UF, RF, DF, FF, BF
    RF = turn_face(RF, clock_turn)
    if clock_turn:
        temp0, temp1, temp2 = UF[3], UF[6], UF[9]
        UF[3], UF[6], UF[9] = FF[3], FF[6], FF[9]
        FF[3], FF[6], FF[9] = DF[3], DF[6], DF[9]
        DF[3], DF[6], DF[9] = BF[3], BF[6], BF[9]
        BF[3], BF[6], BF[9] = temp0, temp1, temp2
    else:
        temp0, temp1, temp2 = UF[3], UF[6], UF[9]
        UF[3], UF[6], UF[9] = BF[3], BF[6], BF[9]
        BF[3], BF[6], BF[9] = DF[3], DF[6], DF[9]
        DF[3], DF[6], DF[9] = FF[3], FF[6], FF[9]
        FF[3], FF[6], FF[9] = temp0, temp1, temp2


def left_turn(clock_turn=True):
    global LF, UF, RF, DF, FF, BF
    LF = turn_face(LF, clock_turn)
    if clock_turn:
        temp0, temp1, temp2 = UF[1], UF[4], UF[7]
        UF[1], UF[4], UF[7] = BF[1], BF[4], BF[7]
        BF[1], BF[4], BF[7] = DF[1], DF[4], DF[7]
        DF[1], DF[4], DF[7] = FF[1], FF[4], FF[7]
        FF[1], FF[4], FF[7] = temp0, temp1, temp2

    else:
        temp0, temp1, temp2 = UF[1], UF[4], UF[7]
        UF[1], UF[4], UF[7] = FF[1], FF[4], FF[7]
        FF[1], FF[4], FF[7] = DF[1], DF[4], DF[7]
        DF[1], DF[4], DF[7] = BF[1], BF[4], BF[7]
        BF[1], BF[4], BF[7] = temp0, temp1, temp2


for _ in range(int(input())):
    number_spin = int(input())
    spins = list(input().split())

    LF = [" "] + ["g"] * 9
    UF = [" "] + ["w"] * 9
    FF = [" "] + ["r"] * 9
    RF = [" "] + ["b"] * 9
    BF = [" "] + ["o"] * 9
    DF = [" "] + ["y"] * 9

    for spin in spins:
        if spin[1] == "+":
            rotate_dir = True
        else:
            rotate_dir = False

        if spin[0] == "L":
            left_turn(rotate_dir)
        if spin[0] == "R":
            right_turn(rotate_dir)
        if spin[0] == "F":
            front_turn(rotate_dir)
        if spin[0] == "U":
            up_turn(rotate_dir)
        if spin[0] == "B":
            back_turn(rotate_dir)
        if spin[0] == "D":
            down_turn(rotate_dir)

    print(UF[1] + UF[2] + UF[3])
    print(UF[4] + UF[5] + UF[6])
    print(UF[7] + UF[8] + UF[9])
