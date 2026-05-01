import sys

data = sys.stdin.read().split()
a, b, c, d = int(data[0]), int(data[1]), int(data[2]), int(data[3])

# There are 3 ways to split 4 players into 2 teams of 2:
# (a,b) vs (c,d)
# (a,c) vs (b,d)
# (a,d) vs (b,c)

diff1 = abs((a + b) - (c + d))
diff2 = abs((a + c) - (b + d))
diff3 = abs((a + d) - (b + c))

print(min(diff1, diff2, diff3))