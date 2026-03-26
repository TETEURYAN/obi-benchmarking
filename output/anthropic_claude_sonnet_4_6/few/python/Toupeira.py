import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    S = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    edges = set()
    for _ in range(T):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        edges.add((min(x,y), max(x,y)))
    
    P = int(data[idx]); idx += 1
    count = 0
    
    for _ in range(P):
        N = int(data[idx]); idx += 1
        path = []
        for i in range(N):
            path.append(int(data[idx])); idx += 1
        
        valid = True
        for i in range(N-1):
            a = path[i]
            b = path[i+1]
            if (min(a,b), max(a,b)) not in edges:
                valid = False
                break
        
        if valid:
            count += 1
    
    print(count)

main()