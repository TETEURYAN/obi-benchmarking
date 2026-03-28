import sys
from bisect import bisect_left, bisect_right

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    X = [int(data[idx+i]) for i in range(n)]; idx += n
    H = [int(data[idx+i]) for i in range(n)]; idx += n
    
    # For each domino i, if knocked right, it covers [X[i], X[i]+H[i]]
    # We need to find how many dominoes fall in total (chain reaction)
    
    # Process from right to left using memoization
    # For domino i, the reach is X[i] + H[i]
    # It directly knocks dominoes j where X[j] in [X[i], X[i]+H[i]]
    # But those also extend the reach
    
    # We'll store for each domino i:
    # - count[i]: number of dominoes that fall when i is knocked
    # - max_reach[i]: the maximum right position reached when i is knocked
    
    # Process right to left
    count = [1] * n
    max_reach = [X[i] + H[i] for i in range(n)]
    
    # For each domino i (right to left), find all dominoes it can knock
    # using the extended reach
    
    for i in range(n-2, -1, -1):
        # Current reach starts as X[i] + H[i]
        reach = X[i] + H[i]
        
        # Find first domino to the right of i that X[j] <= reach
        # j starts at i+1
        j = i + 1
        
        while j < n and X[j] <= reach:
            # domino j falls
            if max_reach[j] > reach:
                reach = max_reach[j]
            j += 1
        
        # j is now the first domino that doesn't fall
        # count[i] = j - i (number of dominoes including i itself)
        count[i] = j - i
        max_reach[i] = reach
    
    # But this is O(N^2) in worst case. We need to optimize.
    # Let's use a smarter approach: jump pointers
    # Actually, let's redo with the jump approach
    
    # Reset
    count = [1] * n
    max_reach = [X[i] + H[i] for i in range(n)]
    
    for i in range(n-2, -1, -1):
        reach = X[i] + H[i]
        j = i + 1
        
        while j < n and X[j] <= reach:
            if max_reach[j] > reach:
                reach = max_reach[j]
            # Jump: skip all dominoes that j already accounts for
            # j's count tells us how many fall from j
            # next unprocessed is j + count[j]... wait no
            # We need to jump to the next domino not covered by j's chain
            j_next = i + 1
            # Actually let's use the jump: after processing j, 
            # the next candidate is j + count[j] if we stored it right
            # But count[j] = number falling from j, so next is j+count[j]
            # Let me restructure
            break
        
        count[i] = j - i
        max_reach[i] = reach
    
    # Let me do it properly with jumping
    count = [1] * n
    max_reach = [X[i] + H[i] for i in range(n)]
    
    for i in range(n-2, -1, -1):
        reach = X[i] + H[i]
        j = i + 1
        
        while j < n and X[j] <= reach:
            if max_reach[j] > reach:
                reach = max_reach[j]
            j += count[j]  # jump over all dominoes that j would knock
        
        count[i] = j - i
        max_reach[i] = reach
    
    sys.stdout.write(' '.join(map(str, count)) + '\n')

main()