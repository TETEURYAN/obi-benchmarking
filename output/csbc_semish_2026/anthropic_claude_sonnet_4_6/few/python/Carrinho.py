import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    D = float(data[idx]); idx += 1
    
    batteries = []
    for _ in range(N):
        P = float(data[idx]); idx += 1
        C = float(data[idx]); idx += 1
        batteries.append((P, C))
    
    # batteries are in strictly increasing order of position
    # Add destination as a virtual point
    # positions: batteries[0..N-1], destination at D
    
    positions = [b[0] for b in batteries]
    charges = [b[1] for b in batteries]
    
    # dp[i] = minimum time to reach position positions[i] (or D if i==N)
    # We have N battery positions + destination D
    # At each battery position, we can pick up that battery (or not)
    # We can only change speed when swapping battery
    # Key insight: between two consecutive battery swaps, we travel at constant speed
    # If we use battery with charge C over distance d, time = d/V, and constraint: d <= C/V => V <= C/d
    # To minimize time d/V, maximize V, so V = C/d, time = d/(C/d) = d^2/C
    
    # But we can combine multiple battery segments if we don't swap
    # Wait - we can only change speed when swapping battery
    # So between swaps, speed is constant
    # If we have battery with charge C and travel distance d at speed V:
    # constraint: d <= C/V => V <= C/d
    # time = d/V, minimized when V is maximized = C/d
    # minimum time for segment = d^2/C
    
    # But we might skip some batteries along the way
    # If we pick up battery at position i and next swap at position j (skipping batteries in between),
    # we travel distance = positions[j] - positions[i] with charge charges[i]
    # time = (positions[j] - positions[i])^2 / charges[i]
    
    # We need DP:
    # dp[i] = min time to reach node i (0-indexed battery positions, N = destination)
    # Nodes: 0..N-1 are battery positions, node N is destination D
    
    # From node i, we can go to any node j > i (next battery or destination)
    # using battery charges[i], distance = pos[j] - pos[i]
    # time contribution = (pos[j] - pos[i])^2 / charges[i]
    
    # But wait - we might carry a battery from earlier and not swap at intermediate positions
    # Actually when we pass a battery we CAN choose not to swap
    # So from position i (where we last swapped), we can go directly to any future position j
    # using the battery we currently have (charges[i])
    
    INF = float('inf')
    
    # Extended positions including destination
    ext_pos = positions + [D]
    ext_n = N + 1  # indices 0..N, where N is destination
    
    dp = [INF] * ext_n
    dp[0] = 0.0
    
    for i in range(N):
        if dp[i] == INF:
            continue
        c = charges[i]
        for j in range(i+1, ext_n):
            dist = ext_pos[j] - ext_pos[i]
            time = (dist * dist) / c
            if dp[i] + time < dp[j]:
                dp[j] = dp[i] + time
    
    print(f"{dp[N]:.3f}")

solve()