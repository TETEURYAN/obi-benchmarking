import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    turns = []
    for _ in range(M):
        turns.append(int(data[idx])); idx += 1
    
    # We need to track which original positions survive all turns.
    # After each turn with Ti, positions that are multiples of Ti are removed.
    # The list is then compacted.
    
    # Key insight: We can represent the surviving set as a set of "gaps" or
    # track the mapping from current position to original position.
    # 
    # But N can be up to 1e9, so we can't store all elements.
    # 
    # We need to figure out which original indices survive.
    # 
    # After turn with T, from a list of size L, we remove floor(L/T) elements
    # (those at positions T, 2T, 3T, ...).
    # The survivors are those NOT at multiples of T.
    # 
    # We can represent the current list implicitly.
    # 
    # Think of it this way: we need to find the mapping from "current position"
    # to "original position" after all turns.
    # 
    # We only need the first 10000 survivors.
    # 
    # Approach: simulate but represent the list as a function.
    # 
    # After processing turns, we need to find the k-th element (for k=1..10000).
    # 
    # We can compute: given a current position p after all turns, what is the original index?
    # 
    # We process turns in reverse: given position p in the final list,
    # find position in the list before the last turn, etc.
    # 
    # Before turn i (with value T), the list had size L_prev.
    # After turn i, size L_after = L_prev - floor(L_prev / T).
    # 
    # Given position p (1-indexed) in the list after turn i,
    # find position q in the list before turn i:
    # The survivors are positions not divisible by T.
    # The p-th survivor: we need to find the p-th number in {1..L_prev} not divisible by T.
    # 
    # In each block of T consecutive positions, T-1 survive.
    # full_blocks = (p-1) // (T-1)
    # remainder = (p-1) % (T-1) + 1  (position within the block, 1-indexed)
    # q = full_blocks * T + remainder
    # But we must ensure remainder != T (it won't be since remainder <= T-1)
    
    # Compute sizes at each step
    sizes = [N]
    for t in turns:
        prev = sizes[-1]
        removed = prev // t
        sizes.append(prev - removed)
    
    final_size = sizes[-1]
    count = min(final_size, 10000)
    
    output = []
    for p in range(1, count + 1):
        # p is position in final list, trace back through turns
        pos = p
        for i in range(M - 1, -1, -1):
            t = turns[i]
            # pos is position in list after turn i
            # find position in list before turn i (size = sizes[i])
            # p-th element not at multiple of t
            # In blocks of t: (t-1) survivors per block
            full_blocks = (pos - 1) // (t - 1)
            remainder = (pos - 1) % (t - 1) + 1
            pos = full_blocks * t + remainder
        output.append(pos)
    
    sys.stdout.write('\n'.join(map(str, output)) + '\n')

solve()