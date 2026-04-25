import sys

# Increase recursion depth just in case, though we use an iterative approach
sys.setrecursionlimit(2000)

def solve():
    # Read all input from stdin at once
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Create an iterator to parse tokens sequentially
    iterator = iter(input_data)
    
    try:
        # First token is N (integer)
        N = int(next(iterator))
        # Second token is F (float)
        F = float(next(iterator))
    except StopIteration:
        return

    # Read the N areas
    areas = []
    for _ in range(N):
        try:
            areas.append(int(next(iterator)))
        except StopIteration:
            break
            
    # If N=1, no divisions needed, tax is 0
    if N == 1:
        print("0.00")
        return

    # To handle the circular arrangement, we duplicate the array.
    # This allows us to treat any circular segment as a linear segment
    # in the duplicated array.
    A = areas + areas
    
    # Compute prefix sums for O(1) range sum queries.
    # P[i] stores the sum of elements A[0]...A[i-1].
    P = [0] * (2 * N + 1)
    for i in range(2 * N):
        P[i+1] = P[i] + A[i]

    # Helper function to get sum of A[i...j] inclusive
    def get_sum(i, j):
        return P[j+1] - P[i]

    # DP table: dp[i][j] stores the minimum tax to split the linear
    # segment A[i...j] into individual lots.
    # Initialize with 0.0 (base case: length 1 segments have 0 cost).
    dp = [[0.0] * (2 * N) for _ in range(2 * N)]

    # Fill DP table for segments of length 2 up to N-1.
    # We only need up to N-1 because the first cut always breaks the circle
    # into two parts, each with size < N.
    for length in range(2, N):
        for i in range(2 * N):
            j = i + length - 1
            # Ensure we stay within bounds of the duplicated array
            if j >= 2 * N:
                break
            
            min_cost = float('inf')
            
            # Try all possible positions k to make a cut between A[k] and A[k+1]
            for k in range(i, j):
                sum_left = get_sum(i, k)
                sum_right = get_sum(k+1, j)
                
                # Cost of this cut is F * max(area_left, area_right)
                cut_cost = F * max(sum_left, sum_right)
                
                # Total cost is cut cost + cost to solve subproblems
                total_cost = cut_cost + dp[i][k] + dp[k+1][j]
                
                if total_cost < min_cost:
                    min_cost = total_cost
            
            dp[i][j] = min_cost

    # Now handle the first cut which breaks the circle.
    # We iterate over all possible segments that can be separated.
    total_area = P[N]
    min_total_tax = float('inf')
    
    for i in range(N):
        for length in range(1, N):
            j = i + length - 1
            
            # The segment to separate is A[i...j]
            sum_seg = get_sum(i, j)
            
            # The remaining part is the rest of the circle.
            sum_rest = total_area - sum_seg
            
            # Cost of the first division
            cost_first = F * max(sum_seg, sum_rest)
            
            # Cost to further split the separated segment
            cost_seg = dp[i][j]
            
            # Cost to further split the remaining segment
            # The remaining segment in the duplicated array is A[j+1 ... i+N-1]
            rest_start = j + 1
            rest_end = i + N - 1
            cost_rest = dp[rest_start][rest_end]
            
            current_total = cost_first + cost_seg + cost_rest
            
            if current_total < min_total_tax:
                min_total_tax = current_total

    # Print the result formatted to 2 decimal places
    print("%.2f" % min_total_tax)

if __name__ == '__main__':
    solve()