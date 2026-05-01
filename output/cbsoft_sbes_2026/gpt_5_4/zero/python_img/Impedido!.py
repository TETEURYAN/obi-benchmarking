l, r, d = map(int, input().split())
print("S" if (r > 50 and l < r and r > d) else "N")