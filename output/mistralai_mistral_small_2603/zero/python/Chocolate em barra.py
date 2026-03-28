
N = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if x1 == x2:
    if (y1 <= N // 2 and y2 > N // 2) or (y2 <= N // 2 and y1 > N // 2):
        print('S')
    else:
        print('N')
elif y1 == y2:
    if (x1 <= N // 2 and x2 > N // 2) or (x2 <= N // 2 and x1 > N // 2):
        print('S')
    else:
        print('N')
else:
    print('N')
