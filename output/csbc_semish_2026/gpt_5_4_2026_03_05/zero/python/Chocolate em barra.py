n = int(input().strip())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

half = n // 2

ok = ((x1 <= half < x2) or (x2 <= half < x1) or
      (y1 <= half < y2) or (y2 <= half < y1))

print('S' if ok else 'N')