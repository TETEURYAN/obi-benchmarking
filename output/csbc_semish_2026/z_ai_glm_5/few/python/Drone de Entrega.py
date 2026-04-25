import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    A = int(input_data[0])
    B = int(input_data[1])
    C = int(input_data[2])
    H = int(input_data[3])
    L = int(input_data[4])

    w_min = min(H, L)
    w_max = max(H, L)

    # Check face A x B
    if max(A, B) <= w_max and min(A, B) <= w_min:
        print("S")
        return

    # Check face A x C
    if max(A, C) <= w_max and min(A, C) <= w_min:
        print("S")
        return

    # Check face B x C
    if max(B, C) <= w_max and min(B, C) <= w_min:
        print("S")
        return

    print("N")

if __name__ == "__main__":
    solve()