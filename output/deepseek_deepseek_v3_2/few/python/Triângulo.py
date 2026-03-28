
import sys

def can_form_triangle(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    varetas = list(map(int, data))
    
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                if can_form_triangle(varetas[i], varetas[j], varetas[k]):
                    print('S')
                    return
    print('N')

if __name__ == "__main__":
    solve()
