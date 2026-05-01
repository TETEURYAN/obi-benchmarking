
k = int(input())
l = int(input())

if k > l:
    k, l = l, k

if k <= 8 and l <= 8:
    if (k + 7) // 8 == (l + 7) // 8:
        print("oitavas")
    else:
        print("quartas")
elif k <= 8 and l > 8:
    if (k + 3) // 4 == (l + 3) // 4 - 2:
        print("semifinal")
    else:
        print("final")
else:
    if (k + 7) // 8 == (l + 7) // 8:
        print("oitavas")
    elif (k + 3) // 4 == (l + 3) // 4:
        print("quartas")
    else:
        print("semifinal")
