import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    E = int(next(it))
    I = int(next(it))
    V = int(next(it))
    adj_forward = [[] for _ in range(E)]
    pred = [[] for _ in range(E)]
    indegree = [0] * E
    for _ in range(I):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj_forward[a].append(b)
        pred[b].append(a)
        indegree[b] += 1
    iniciais = [int(next(it)) - 1 for _ in range(V)]
    adj_prime = [lst[:] for lst in adj_forward]
    for b in range(E):
        if indegree[b] == 1:
            a = pred[b][0]
            adj_prime[b].append(a)
    reach = [0] * E
    for i in range(E):
        reach[i] = (1 << i)
        for v in adj_prime[i]:
            reach[i] |= (1 << v)
    for k in range(E):
        for i in range(E):
            if reach[i] & (1 << k):
                reach[i] |= reach[k]
    F_mask = reach
    T_mask = 0
    Q = deque()
    for x in iniciais:
        if not (T_mask >> x) & 1:
            T_mask |= (1 << x)
            Q.append(x)
    while Q:
        b = Q.popleft()
        for c in adj_forward[b]:
            if not (T_mask >> c) & 1:
                T_mask |= (1 << c)
                Q.append(c)
        if indegree[b] == 1:
            a = pred[b][0]
            if not (T_mask >> a) & 1:
                T_mask |= (1 << a)
                Q.append(a)
        if indegree[b] > 1:
            inter = F_mask[pred[b][0]]
            for a in pred[b][1:]:
                inter &= F_mask[a]
            novos = inter & ~T_mask
            if novos:
                T_mask |= novos
                temp = novos
                while temp:
                    lsb = temp & -temp
                    pos = (lsb.bit_length() - 1)
                    Q.append(pos)
                    temp -= lsb
    saida = []
    for i in range(E):
        if (T_mask >> i) & 1:
            saida.append(str(i + 1))
    print(' '.join(saida))

if __name__ == '__main__':
    main()