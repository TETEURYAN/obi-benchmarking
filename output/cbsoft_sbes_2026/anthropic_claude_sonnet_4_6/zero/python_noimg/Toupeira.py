import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    S = int(input_data[idx]); idx += 1
    T = int(input_data[idx]); idx += 1
    
    edges = set()
    for _ in range(T):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        edges.add((min(x,y), max(x,y)))
    
    P = int(input_data[idx]); idx += 1
    
    count = 0
    for _ in range(P):
        N = int(input_data[idx]); idx += 1
        saloes = []
        for i in range(N):
            saloes.append(int(input_data[idx])); idx += 1
        
        possible = True
        for i in range(N-1):
            a = saloes[i]
            b = saloes[i+1]
            if (min(a,b), max(a,b)) not in edges:
                possible = False
                break
        
        if possible:
            count += 1
    
    print(count)

main()