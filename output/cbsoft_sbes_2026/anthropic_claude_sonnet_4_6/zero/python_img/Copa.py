import math

K = int(input())
L = int(input())

def group(pos, size):
    return (pos - 1) // size

k_group_8 = group(K, 2)
l_group_8 = group(L, 2)

if k_group_8 == l_group_8:
    print("oitavas")
else:
    k_group_4 = group(K, 4)
    l_group_4 = group(L, 4)
    if k_group_4 == l_group_4:
        print("quartas")
    else:
        k_group_2 = group(K, 8)
        l_group_2 = group(L, 8)
        if k_group_2 == l_group_2:
            print("semifinal")
        else:
            print("final")