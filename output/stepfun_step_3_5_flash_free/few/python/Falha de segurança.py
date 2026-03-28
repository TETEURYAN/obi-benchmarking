import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    senhas = data[1:1+n]
    
    S_set = set(senhas)
    contador = defaultdict(int)
    
    for s in senhas:
        L = len(s)
        vistos = set()
        for i in range(L):
            for j in range(i+1, L+1):
                t = s[i:j]
                if t in S_set and t not in vistos:
                    contador[t] += 1
                    vistos.add(t)
    
    total = 0
    for s in senhas:
        total += contador[s] - 1
    
    print(total)

if __name__ == "__main__":
    main()