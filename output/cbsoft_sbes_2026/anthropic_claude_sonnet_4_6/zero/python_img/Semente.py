import sys

def solve():
    input_data = sys.stdin.read().split()
    F = int(input_data[0])
    R = int(input_data[1])
    positions = [int(x) for x in input_data[2:2+R]]
    
    # Binary search on the answer
    def check(days):
        # Check if after 'days' days, the entire tape is covered
        # Each drop at position p covers [p - days, p + days]
        # We need to cover [1, F]
        covered_up_to = 0  # rightmost position covered so far
        for p in positions:
            left = p - days
            right = p + days
            if left <= covered_up_to + 1:
                # This drop extends coverage
                if right > covered_up_to:
                    covered_up_to = right
            else:
                # There's a gap
                return False
            if covered_up_to >= F:
                return True
        return covered_up_to >= F
    
    lo, hi = 0, F
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)

solve()