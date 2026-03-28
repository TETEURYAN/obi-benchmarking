import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        Q = int(next(iterator))
    except StopIteration:
        return

    # Precompute prefix sums
    # prefix[i] stores the sum of the first i digits
    prefix_sum = [0] * (N + 1)
    
    for i in range(1, N + 1):
        try:
            digit = int(next(iterator))
            prefix_sum[i] = prefix_sum[i-1] + digit
        except StopIteration:
            break
            
    results = []
    
    # Process queries
    for _ in range(Q):
        try:
            L = int(next(iterator))
            R = int(next(iterator))
            
            k = R - L + 1
            
            # If interval length is 1, potential is 0
            if k == 1:
                results.append("0")
                continue
                
            interval_sum = prefix_sum[R] - prefix_sum[L-1]
            
            # Potential formula: 11 * (k - 1) * interval_sum
            potential = 11 * (k - 1) * interval_sum
            results.append(str(potential))
            
        except StopIteration:
            break
            
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()