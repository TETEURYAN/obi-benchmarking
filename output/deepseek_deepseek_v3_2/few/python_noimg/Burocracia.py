import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx]); idx += 1
    p = [0] * (N + 1)
    p[1] = 1
    for i in range(2, N + 1):
        p[i] = int(data[idx]); idx += 1
    
    Q = int(data[idx]); idx += 1
    
    # Compression structure: parent after compression
    comp = [0] * (N + 1)
    for i in range(1, N + 1):
        comp[i] = p[i]
    
    # Precompute binary lifting arrays
    logN = 0
    while (1 << logN) <= N:
        logN += 1
    up = [[0] * (logN + 1) for _ in range(N + 1)]
    for v in range(1, N + 1):
        up[v][0] = comp[v]
    for k in range(1, logN + 1):
        for v in range(1, N + 1):
            up[v][k] = up[up[v][k-1]][k-1]
    
    answers = []
    for _ in range(Q):
        t = int(data[idx]); idx += 1
        if t == 1:
            v = int(data[idx]); idx += 1
            k = int(data[idx]); idx += 1
            # Binary lifting query
            cur = v
            for i in range(logN + 1):
                if (k >> i) & 1:
                    cur = up[cur][i]
            answers.append(cur)
        else:
            v = int(data[idx]); idx += 1
            # Reestruturação: todos abaixo de v se tornam filhos diretos de v
            comp[v] = v
            up[v][0] = v
            for k in range(1, logN + 1):
                up[v][k] = up[up[v][k-1]][k-1]
    
    sys.stdout.write("\n".join(map(str, answers)))

if __name__ == "__main__":
    solve()