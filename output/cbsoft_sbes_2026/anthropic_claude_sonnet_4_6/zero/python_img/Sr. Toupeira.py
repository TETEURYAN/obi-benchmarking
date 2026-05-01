import sys
input = sys.stdin.readline

def main():
    S, T = map(int, input().split())
    edges = set()
    for _ in range(T):
        x, y = map(int, input().split())
        edges.add((min(x,y), max(x,y)))
    
    P = int(input())
    count = 0
    for _ in range(P):
        line = list(map(int, input().split()))
        n = line[0]
        saloes = line[1:]
        possible = True
        for i in range(n-1):
            a, b = saloes[i], saloes[i+1]
            if (min(a,b), max(a,b)) not in edges:
                possible = False
                break
        if possible:
            count += 1
    
    print(count)

main()