L, R, D = map(int, input().split())
print("S" if (R > 50) and (L < R) and (R > D) else "N")