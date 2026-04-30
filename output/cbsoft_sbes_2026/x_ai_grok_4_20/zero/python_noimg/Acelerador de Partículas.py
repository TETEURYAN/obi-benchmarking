
D = int(input())

dist_to_accel = 3
circum = 8

if D == 6:
    print(1)
elif D == 7:
    print(2)
elif D == 8:
    print(3)
else:
    traveled_in_accel = D - dist_to_accel
    pos = traveled_in_accel % circum
    if pos == 0:
        print(3)
    elif pos <= 4:
        print(1)
    else:
        print(2)
