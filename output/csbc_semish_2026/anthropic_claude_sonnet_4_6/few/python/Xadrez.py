import sys
L, C = int(sys.stdin.readline()), int(sys.stdin.readline())
print(1 if (L + C) % 2 == 0 else 0)