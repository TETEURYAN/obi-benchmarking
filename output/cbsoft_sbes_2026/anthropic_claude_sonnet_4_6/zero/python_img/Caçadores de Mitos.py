import sys
input = sys.stdin.readline

def main():
    n = int(input())
    seen = set()
    result = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if (x, y) in seen:
            result = 1
        else:
            seen.add((x, y))
    print(result)

main()