import sys

A, B, C = map(int, sys.stdin.readline().split())
X, Y, Z = map(int, sys.stdin.readline().split())

print((X // A) * (Y // B) * (Z // C))