import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    prox = {}
    
    for _ in range(n):
        e, c, d = input().split()
        prox[int(e)] = (c, int(d))
    
    atual = 0
    res = []
    for _ in range(n):
        c, atual = prox[atual]
        res.append(c)
    
    sys.stdout.write(''.join(res))

if __name__ == "__main__":
    main()
