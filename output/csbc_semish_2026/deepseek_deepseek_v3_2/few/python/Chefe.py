import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    I = int(next(it))
    
    age = [0] * (N + 1)
    for i in range(1, N + 1):
        age[i] = int(next(it))
    
    parent = [0] * (N + 1)
    children = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        x = int(next(it))
        y = int(next(it))
        parent[y] = x
        children[x].append(y)
    
    # mapeamento inicial: empregado i está na posição i
    pos_to_emp = list(range(N + 1))
    emp_to_pos = list(range(N + 1))
    
    def swap_employees(a, b):
        if a == b:
            return
        pa = pos_to_emp[a]
        pb = pos_to_emp[b]
        pos_to_emp[a], pos_to_emp[b] = pb, pa
        emp_to_pos[pa], emp_to_pos[pb] = b, a
    
    def get_youngest_manager(e):
        pos = emp_to_pos[e]
        visited = [False] * (N + 1)
        stack = [pos]
        visited[pos] = True
        best = float('inf')
        
        while stack:
            cur_pos = stack.pop()
            cur_emp = pos_to_emp[cur_pos]
            for child in children[cur_emp]:
                child_pos = emp_to_pos[child]
                if not visited[child_pos]:
                    visited[child_pos] = True
                    stack.append(child_pos)
                    if age[child] < best:
                        best = age[child]
        return best if best != float('inf') else '*'
    
    out_lines = []
    for _ in range(I):
        cmd = next(it)
        if cmd == 'T':
            a = int(next(it))
            b = int(next(it))
            # trocar as posições de a e b
            pos_a = emp_to_pos[a]
            pos_b = emp_to_pos[b]
            swap_employees(pos_a, pos_b)
        else:  # 'P'
            e = int(next(it))
            res = get_youngest_manager(e)
            out_lines.append(str(res))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()