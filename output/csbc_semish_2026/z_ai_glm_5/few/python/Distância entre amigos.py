import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n_str = next(iterator)
        N = int(n_str)
    except StopIteration:
        return

    # max_val stores the maximum of (A_k - k) found so far (for k < current i)
    # We initialize it to negative infinity
    max_val = float('-inf')
    
    # ans stores the maximum distance found so far
    ans = float('-inf')
    
    # Iterate through buildings using 0-based index
    for i in range(N):
        try:
            ai_str = next(iterator)
            ai = int(ai_str)
        except StopIteration:
            break
        
        # Calculate the term for the current building as the right endpoint (j)
        # The term is (A_j + j)
        term_plus = ai + i
        
        # Calculate potential maximum distance ending at current building i
        # We want max of (A_k - k) + (A_i + i) for k < i
        # Note: For i=0, max_val is -inf, so current_dist remains -inf (or very small)
        # which is correct as there is no k < 0.
        current_dist = max_val + term_plus
        
        if current_dist > ans:
            ans = current_dist
        
        # Update max_val with the current building as a potential left endpoint
        # The term is (A_i - i)
        term_minus = ai - i
        
        if term_minus > max_val:
            max_val = term_minus
            
    print(ans)

if __name__ == '__main__':
    solve()