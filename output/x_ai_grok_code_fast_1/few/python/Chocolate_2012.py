import sys

L = int(sys.stdin.read())

def count_pieces(s):
    if s < 2:
        return 1
    return 4 * count_pieces(s // 2)

print(count_pieces(L))