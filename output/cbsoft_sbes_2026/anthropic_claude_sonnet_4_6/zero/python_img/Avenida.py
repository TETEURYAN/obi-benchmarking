D = int(input())
r = D % 400
print(min(r, 400 - r))