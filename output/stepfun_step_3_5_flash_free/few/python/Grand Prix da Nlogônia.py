import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); M = int(next(it))
    planos = []
    for _ in range(M):
        u = int(next(it)); L = int(next(it)); R = int(next(it))
        planos.append((u, L, R))
    
    def tem_ciclo(k):
        intervals = [[] for _ in range(N+1)]
        for i in range(k):
            u, L, R = planos[i]
            intervals[u].append((L, R))
        
        pai = list(range(N+2))
        estado = [0] * (N+1)
        ptr = [0] * (N+1)
        
        def find(x):
            root = x
            while pai[root] != root:
                root = pai[root]
            while pai[x] != x:
                nxt = pai[x]
                pai[x] = root
                x = nxt
            return root
        
        def union(x, y):
            x = find(x)
            y = find(y)
            if x != y:
                pai[x] = y
        
        pilha = []
        for i in range(1, N+1):
            if estado[i] == 0:
                estado[i] = 1
                pilha.append(i)
                while pilha:
                    u = pilha[-1]
                    while ptr[u] < len(intervals[u]):
                        L, R = intervals[u][ptr[u]]
                        v = find(L)
                        while v <= R:
                            if estado[v] == 0:
                                estado[v] = 1
                                pilha.append(v)
                                break
                            elif estado[v] == 1:
                                return True
                            else:
                                v = find(v)
                        if v > R:
                            ptr[u] += 1
                        else:
                            break
                    else:
                        estado[u] = 2
                        pilha.pop()
                        union(u, u+1)
        return False
    
    low, high = 1, M
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if tem_ciclo(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    print(ans if ans != -1 else -1)

if __name__ == "__main__":
    main()