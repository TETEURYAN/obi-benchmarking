d = int(input().strip())
r = d % 400
print(min(r, 400 - r))