import sys

def solve():
    input_data = list(map(int, sys.stdin.read().split()))
    
    if not input_data:
        return

    a, b, c, d = input_data
    
    # True Coral (V): Pattern ...BVBPBVBP...
    # Indices 0, 2 are same color (B).
    # Indices 1, 3 are different colors (V, P).
    # So, for a slice of 4 [x0, x1, x2, x3]:
    # True Coral condition: x0 == x2 and x1 != x3
    
    # False Coral (F): Pattern ...BVPBVPBVP...
    # Sequence: B, V, P, B, V, P...
    # Indices:
    # 0: B
    # 1: V
    # 2: P
    # 3: B
    # Here, x0 == x3 (B).
    # x1 and x2 are distinct from x0 and each other?
    # The problem guarantees it's either V or F.
    # False Coral condition: x0 == x3.
    
    if a == c and b != d:
        print("V")
    else:
        print("F")

if __name__ == "__main__":
    solve()