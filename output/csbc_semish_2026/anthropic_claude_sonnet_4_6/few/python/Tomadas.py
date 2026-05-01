import sys

def max_outlets(strips):
    # We have 4 strips and 1 wall outlet
    # We need to connect them optimally to maximize notebooks
    # Each strip plugged in uses 1 socket from its host, provides its Ti sockets
    # We want to maximize total available sockets for notebooks
    
    # Try all permutations of how to chain the strips
    # The wall outlet has 1 socket. We plug strips into available sockets.
    # Strategy: plug all 4 strips in a chain or tree structure
    # 
    # The optimal strategy: plug strips into each other to maximize free sockets
    # We have 1 wall socket. We can plug one strip there (uses 1 wall socket, gains T1 sockets)
    # Then plug remaining strips into those sockets (each uses 1 socket)
    # 
    # We want to find the arrangement that maximizes total free sockets
    # 
    # Let's think: if we plug k strips total, we use k sockets (one per strip plugged in)
    # and gain sum of their Ti sockets. Net gain = sum(Ti) - k
    # Plus the original 1 wall socket minus 1 used = 0 wall sockets free
    # Total notebooks = sum(Ti for plugged strips) - (number of strips plugged) + (1 - 1 if we plug into wall)
    # 
    # Actually: start with 1 free socket (wall)
    # Plug a strip: -1 socket used, +Ti sockets gained. Net: Ti - 1 new sockets
    # We want to plug all 4 strips if beneficial (Ti >= 2, which is always true since Ti >= 2)
    # 
    # So we should always plug all 4 strips.
    # The order matters for whether we CAN plug them all.
    # 
    # With 1 wall socket, plug strip with most sockets first to have room for others.
    # But since Ti >= 2, after plugging first strip we have Ti >= 2 sockets,
    # enough to plug remaining 3 strips (need 3 sockets, Ti >= 2... wait Ti could be 2)
    # 
    # If first strip has 2 sockets, we can plug 2 more strips into it.
    # Those strips provide more sockets for the 4th.
    # 
    # Let's just try all 4! = 24 permutations and simulate greedily
    
    from itertools import permutations
    
    best = 0
    
    for perm in permutations(strips):
        # Try to plug all strips; simulate with available sockets
        # available = current free sockets
        available = 1  # wall outlet
        total_sockets = 0
        
        # We'll try a greedy: plug strips one by one
        # But order within perm matters
        # Actually let's try: plug them in given order
        avail = 1
        plugged = []
        remaining = list(perm)
        
        # Keep trying to plug strips as long as we have free sockets
        changed = True
        while changed and remaining:
            changed = False
            for i, t in enumerate(remaining):
                if avail > 0:
                    avail -= 1  # use one socket to plug this strip
                    avail += t  # gain t sockets
                    remaining.pop(i)
                    changed = True
                    break
        
        # avail now = free sockets = number of notebooks
        if not remaining:
            best = max(best, avail)
    
    # Also try not plugging some strips (but since Ti>=2, always beneficial)
    # Actually let's also consider all subsets
    from itertools import permutations as perms
    
    # The simulation above with all permutations should cover it
    # But let me redo more carefully: try all orderings
    
    best2 = 0
    for perm in permutations(strips):
        avail = 1
        for t in perm:
            if avail > 0:
                avail = avail - 1 + t
            else:
                break
        best2 = max(best2, avail)
    
    return max(best, best2)

data = sys.stdin.read().split()
strips = [int(x) for x in data[:4]]
print(max_outlets(strips))