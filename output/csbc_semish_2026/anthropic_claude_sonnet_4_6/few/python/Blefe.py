import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    A = []
    for i in range(N):
        A.append(int(data[idx])); idx += 1
    
    B = []
    for i in range(M):
        B.append(int(data[idx])); idx += 1
    
    # valid_set contains all numbers that can be played
    # Initially it's the set A, then grows as B elements are added
    valid_set = set(A)
    
    # We also need to track all numbers currently in B to compute sums
    b_so_far = []
    b_set = set()  # set of values in b_so_far for quick lookup
    
    first_invalid = None
    
    for val in B:
        # Check if val is valid: either in valid_set or is sum of two elements in b_so_far
        is_valid = False
        
        if val in valid_set:
            is_valid = True
        else:
            # Check if val = b_so_far[i] + b_so_far[j] for some i, j
            for x in b_so_far:
                needed = val - x
                if needed in b_set:
                    is_valid = True
                    break
        
        if not is_valid:
            first_invalid = val
            break
        
        # Add val to b_so_far and update valid_set with new sums
        # New sums: val + x for all x in b_so_far, and val + val
        new_sums = set()
        new_sums.add(val + val)
        for x in b_so_far:
            new_sums.add(val + x)
        
        b_so_far.append(val)
        b_set.add(val)
        valid_set.update(new_sums)
    
    if first_invalid is None:
        print("sim")
    else:
        print(first_invalid)

solve()