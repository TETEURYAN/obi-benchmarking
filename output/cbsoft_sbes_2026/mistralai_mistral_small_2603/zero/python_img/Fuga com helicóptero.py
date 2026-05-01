
H, P, F, D = map(int, input().split())

if D == 1:
    if F < H:
        if P > F and P < H:
            print('N')
        else:
            print('S')
    else:
        if P > F or P < H:
            print('N')
        else:
            print('S')
else:
    if F > H:
        if P < F and P > H:
            print('N')
        else:
            print('S')
    else:
        if P < F or P > H:
            print('N')
        else:
            print('S')
