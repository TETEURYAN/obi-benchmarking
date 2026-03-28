import sys
sys.setrecursionlimit(200000)

def prime_factors(x):
    res = set()
    d = 2
    while d * d <= x:
        if x % d == 0:
            res.add(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        res.add(x)
    return res

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
    
    def _push(self, node, left, right):
        if self.lazy[node]:
            self.tree[node] = self.lazy[node] * (right - left + 1)
            if left != right:
                self.lazy[node*2] = self.lazy[node]
                self.lazy[node*2+1] = self.lazy[node]
            self.lazy[node] = 0
    
    def update(self, l, r, val):
        self._update(1, 0, self.n-1, l, r, val)
    
    def _update(self, node, left, right, ql, qr, val):
        self._push(node, left, right)
        if qr < left or right < ql:
            return
        if ql <= left and right <= qr:
            self.lazy[node] = val
            self._push(node, left, right)
            return
        mid = (left + right) // 2
        self._update(node*2, left, mid, ql, qr, val)
        self._update(node*2+1, mid+1, right, ql, qr, val)
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]
    
    def query(self, l, r):
        return self._query(1, 0, self.n-1, l, r)
    
    def _query(self, node, left, right, ql, qr):
        self._push(node, left, right)
        if qr < left or right < ql:
            return 0
        if ql <= left and right <= qr:
            return self.tree[node]
        mid = (left + right) // 2
        return self._query(node*2, left, mid, ql, qr) + self._query(node*2+1, mid+1, right, ql, qr)

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    arr = [int(next(it)) for _ in range(N)]
    
    max_val = 10**9
    prime_limit = int(max_val**0.5) + 5
    is_prime = [True] * (prime_limit + 1)
    primes = []
    for i in range(2, prime_limit + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, prime_limit + 1, i):
                is_prime[j] = False
    
    def get_factors(x):
        res = set()
        for p in primes:
            if p * p > x:
                break
            if x % p == 0:
                res.add(p)
                while x % p == 0:
                    x //= p
        if x > 1:
            res.add(x)
        return res
    
    seg_trees = {}
    prime_to_idx = {}
    idx_counter = 0
    for i in range(N):
        facs = get_factors(arr[i])
        for p in facs:
            if p not in prime_to_idx:
                prime_to_idx[p] = idx_counter
                idx_counter += 1
    
    seg_list = [SegmentTree(N) for _ in range(idx_counter)]
    for i in range(N):
        facs = get_factors(arr[i])
        for p in facs:
            idx = prime_to_idx[p]
            seg_list[idx].update(i, i, 1)
    
    out_lines = []
    for _ in range(M):
        t = int(next(it))
        if t == 1:
            I = int(next(it)) - 1
            V = int(next(it))
            old_facs = get_factors(arr[I])
            for p in old_facs:
                idx = prime_to_idx[p]
                seg_list[idx].update(I, I, 0)
            arr[I] = V
            new_facs = get_factors(V)
            for p in new_facs:
                if p not in prime_to_idx:
                    prime_to_idx[p] = idx_counter
                    seg_list.append(SegmentTree(N))
                    idx_counter += 1
                idx = prime_to_idx[p]
                seg_list[idx].update(I, I, 1)
        else:
            E = int(next(it)) - 1
            D = int(next(it)) - 1
            total = 0
            length = D - E + 1
            total = length * (length + 1) // 2
            for seg in seg_list:
                cnt = seg.query(E, D)
                if cnt > 0:
                    total -= cnt * (cnt - 1) // 2
            out_lines.append(str(total))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()