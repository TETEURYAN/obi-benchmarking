import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # We need to choose a North-South street to widen
    # North-South streets run vertically
    # There are M+1 vertical streets (at positions 0, 1, ..., M)
    # But the interior streets (positions 1 to M-1) have blocks on both sides
    # We need to expropriate all blocks on ONE side of the chosen street
    
    # For a vertical street at position j (0-indexed, j from 0 to M):
    # - Left side: columns 0..j-1 (j columns)
    # - Right side: columns j..M-1 (M-j columns)
    # But we choose one side, so we pick min(sum of left side columns, sum of right side columns)
    # Wait, actually we need to expropriate ALL blocks on one side
    # The street at position j: left side has columns 0..j-1, right side has columns j..M-1
    # But for streets at position 0 or M, one side has 0 blocks
    
    # Actually, re-reading: "desapropriar todas as quadras de um dos lados da rua escolhida"
    # So for street j, we pick the cheaper side (left or right)
    
    # Compute column sums
    col_sum = [0] * M
    for i in range(N):
        for j in range(M):
            col_sum[j] += grid[i][j]
    
    # prefix sums
    prefix = [0] * (M + 1)
    for j in range(M):
        prefix[j+1] = prefix[j] + col_sum[j]
    
    total = prefix[M]
    
    min_cost = float('inf')
    # Streets at positions 1 to M-1 (interior streets)
    # For street at position j (1-indexed between columns j-1 and j):
    # Left side sum = prefix[j], Right side sum = total - prefix[j]
    for j in range(1, M):
        left = prefix[j]
        right = total - prefix[j]
        cost = min(left, right)
        if cost < min_cost:
            min_cost = cost
    
    print(min_cost)

main()