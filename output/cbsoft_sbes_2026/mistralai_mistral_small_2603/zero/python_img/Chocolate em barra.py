t(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if x1 == x2:
    meio = n // 2
    if (y1 <= meio and y2 > meio) or (y2 <= meio and y1 > meio):
        print('S')
    else:
        print('N')
elif y1 == y2:
    meio = n // 2
    if (x1 <= meio and x2 > meio) or (x2 <= meio and x1 > meio):
        print('S')
    else:
        print('N')
else:
    print('N')
