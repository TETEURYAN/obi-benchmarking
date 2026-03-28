import sys
import bisect

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    xs = [0] * n
    ys = [0] * n
    for i in range(n):
        xs[i] = int(next(it))
        ys[i] = int(next(it))
    
    penalties = [0] * n
    # Árvore de Fenwick (BIT) para contar quantos valores <= x
    # Como as distâncias são inteiras e podem ser grandes, vamos comprimir
    dists = []
    for i in range(n):
        xr = xs[i] + (penalties[i-1] if i > 0 else 0)
        yr = ys[i] + (penalties[i-1] if i > 0 else 0)
        d = xr*xr + yr*yr
        dists.append(d)
    
    # compressão de coordenadas
    sorted_dists = sorted(dists)
    uniq = []
    for d in sorted_dists:
        if not uniq or d != uniq[-1]:
            uniq.append(d)
    rank = {v: i+1 for i, v in enumerate(uniq)}  # BIT usa 1-indexado
    
    bit = [0] * (len(uniq) + 2)
    
    def bit_update(idx, delta):
        while idx < len(bit):
            bit[idx] += delta
            idx += idx & -idx
    
    def bit_query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        return s
    
    for i in range(n):
        xr = xs[i] + (penalties[i-1] if i > 0 else 0)
        yr = ys[i] + (penalties[i-1] if i > 0 else 0)
        d = xr*xr + yr*yr
        r = rank[d]
        # número de flechas anteriores com distância <= d
        penalties[i] = bit_query(r) - 1  # exclui a própria flecha atual (ainda não inserida)
        bit_update(r, 1)
    
    sys.stdout.write("\n".join(map(str, penalties)))

if __name__ == "__main__":
    main()