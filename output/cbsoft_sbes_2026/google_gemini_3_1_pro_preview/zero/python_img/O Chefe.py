
import sys

sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    out = []
    
    while True:
        try:
            N_str = next(iterator)
        except StopIteration:
            break
        N = int(N_str)
        M = int(next(iterator))
        I = int(next(iterator))
        
        ages = [0] * (N + 1)
        for i in range(1, N + 1):
            ages[i] = int(next(iterator))
            
        adj = [[] for _ in range(N + 1)]
        for _ in range(M):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[v].append(u)
            
        reach = [0] * (N + 1)
        computed = [False] * (N + 1)
        
        def get_reach(u):
            if computed[u]:
                return reach[u]
            ans = 0
            for v in adj[u]:
                ans |= (1 << v) | get_reach(v)
            reach[u] = ans
            computed[u] = True
            return ans
            
        for i in range(1, N + 1):
            if not computed[i]:
                get_reach(i)
                
        pos = list(range(N + 1))
        emp = list(range(N + 1))
        
        for _ in range(I):
            op = next(iterator)
            if op == 'T':
                A = int(next(iterator))
                B = int(next(iterator))
                pA = pos[A]
                pB = pos[B]
                
                pos[A] = pB
                pos[B] = pA
                emp[pA] = B
                emp[pB] = A
            elif op == 'P':
                E = int(next(iterator))
                pE = pos[E]
                mask = reach[pE]
                
                if mask == 0:
                    out.append("*")
                else:
                    min_age = 1000
                    temp = mask
                    while temp > 0:
                        lsb = temp & -temp
                        idx = lsb.bit_length() - 1
                        age = ages[emp[idx]]
                        if age < min_age:
                            min_age = age
                        temp ^= lsb
                    out.append(str(min_age))
                    
    if out:
        sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
