import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    x = list(map(int, input().split()))
    
    h = max(x)
    out = []
    
    for level in range(h, 0, -1):
        row = ['1' if xi >= level else '0' for xi in x]
        out.append(' '.join(row))
    
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
