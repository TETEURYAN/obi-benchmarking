import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    pins = [int(data[i+2]) for i in range(n)]
    
    # diff[i] = pins[i] - M (how much each pin needs to change)
    # Each operation: choose consecutive pair (i, i+1), add +1 or -1 to both
    # We need to find minimum number of operations
    
    # Let's think of it as: let x[i] be the net number of operations applied to pair (i, i+1)
    # positive means increase, negative means decrease
    # Then pin[0] changes by x[0]
    # pin[i] changes by x[i-1] + x[i] for 0 < i < n-1
    # pin[n-1] changes by x[n-2]
    
    # We need: pins[i] + change[i] = M
    # change[i] = M - pins[i] = -diff[i] where diff[i] = pins[i] - M
    
    # So:
    # x[0] = -diff[0]
    # x[i-1] + x[i] = -diff[i]  =>  x[i] = -diff[i] - x[i-1]
    # x[n-2] = -diff[n-1]
    
    # The total number of moves is sum of |x[i]|
    # x[0] is determined by diff[0], then x[1] by diff[1] and x[0], etc.
    # But x[0] = -diff[0] is fixed! Let's verify with test cases.
    
    # Actually x[0] can be any value, and then x[1] = -diff[1] - x[0], etc.
    # Wait, no. x[0] = change needed for pin[0] = M - pins[0]
    # Because pin[0] is only affected by operation on pair (0,1), so x[0] = M - pins[0]
    
    # Then x[1] = (M - pins[1]) - x[0]
    # x[2] = (M - pins[2]) - x[1]
    # ...
    # This is fully determined. The total moves = sum |x[i]|
    
    # Let's verify with test 1: pins = [45,45,55,55], M=50
    # need = [5, 5, -5, -5]
    # x[0] = 5
    # x[1] = 5 - 5 = 0
    # x[2] = -5 - 0 = -5
    # total = |5| + |0| + |-5| = 10 ✓
    
    # Test 2: pins = [84,39,17,72,94], M=84
    # need = [0, 45, 67, 12, -10]
    # x[0] = 0
    # x[1] = 45 - 0 = 45
    # x[2] = 67 - 45 = 22
    # x[3] = 12 - 22 = -10
    # total = 0 + 45 + 22 + 10 = 77 ✓
    
    need = [m - pins[i] for i in range(n)]
    
    total = 0
    x_prev = need[0]
    total += abs(x_prev)
    
    for i in range(1, n-1):
        x_cur = need[i] - x_prev
        total += abs(x_cur)
        x_prev = x_cur
    
    print(total)

solve()