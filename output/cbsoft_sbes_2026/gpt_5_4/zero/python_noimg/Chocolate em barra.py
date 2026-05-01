n = int(input().strip())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

metade = n // 2

if (x1 <= metade < x2) or (x2 <= metade < x1) or (y1 <= metade < y2) or (y2 <= metade < y1):
    print("S")
else:
    print("N")