
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    pieces = {}
    for _ in range(n):
        parts = input().split()
        e, c, d = int(parts[0]), parts[1], int(parts[2])
        pieces[e] = (c, d)
    
    result = []
    current = 0
    for _ in range(n):
        c, d = pieces[current]
        result.append(c)
        current = d
    
    print(''.join(result))

main()
