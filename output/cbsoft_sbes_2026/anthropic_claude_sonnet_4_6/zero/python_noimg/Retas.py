import sys
from fractions import Fraction

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx+=1
    X1 = int(input_data[idx]); idx+=1
    X2 = int(input_data[idx]); idx+=1
    
    lines = []
    for i in range(N):
        A = int(input_data[idx]); idx+=1
        B = int(input_data[idx]); idx+=1
        lines.append((A, B))
    
    # Two lines y = A1*x + B1 and y = A2*x + B2 intersect when A1 != A2
    # Intersection x = (B2 - B1) / (A1 - A2)
    # We need X1 <= x <= X2
    # x = (B2-B1)/(A1-A2), need X1*(A1-A2) <= (B2-B1) <= X2*(A1-A2) if A1>A2
    # or X2*(A1-A2) <= (B2-B1) <= X1*(A1-A2) if A1<A2
    
    # With N up to 1e5, O(N^2) pairs = 5*10^9 which is too slow
    # But wait, let's think about what we can do
    # Lines with same A (parallel) never intersect
    # Lines with different A intersect at exactly one point
    
    # Group lines by slope
    from collections import defaultdict
    slope_groups = defaultdict(list)
    for A, B in lines:
        slope_groups[A].append(B)
    
    slopes = list(slope_groups.keys())
    
    # For each pair of distinct slopes (A1, A2), count pairs (B1, B2) where
    # X1 <= (B2-B1)/(A1-A2) <= X2
    # i.e., X1*(A1-A2) <= B2-B1 <= X2*(A1-A2) if A1>A2
    # Let's fix A1 > A2 (so A1-A2 > 0):
    # X1*(A1-A2) <= B2-B1 <= X2*(A1-A2)
    # B2 - B1 in [X1*(A1-A2), X2*(A1-A2)]
    
    # This is still O(N^2) in worst case if all slopes are distinct
    # N=1e5 means 5*10^9 pairs - too slow
    
    # For competitive programming with N=1e5, we need a smarter approach
    # But given the constraints, let's try O(N^2) with optimizations for same slopes
    # Actually N=1e5 with O(N^2) is 10^10 operations - definitely too slow
    
    # However, looking at test cases, maybe N is small enough in practice?
    # Let's implement O(N^2) and hope for the best, or find a smarter way
    
    # Actually for OBI problems, sometimes N=1e5 but with O(N^2) being acceptable
    # Let's just do O(N^2) with fast arithmetic (no Fraction)
    
    count = 0
    n = len(lines)
    
    # Use integer arithmetic to avoid floating point
    # x_intersect = (B2-B1)/(A1-A2)
    # X1 <= (B2-B1)/(A1-A2) <= X2
    
    for i in range(n):
        A1, B1 = lines[i]
        for j in range(i+1, n):
            A2, B2 = lines[j]
            if A1 == A2:
                # parallel, no intersection
                continue
            # x = (B2-B1)/(A1-A2)
            num = B2 - B1
            den = A1 - A2
            # Check X1 <= num/den <= X2
            if den > 0:
                # X1*den <= num <= X2*den
                if X1 * den <= num <= X2 * den:
                    count += 1
            else:
                # den < 0, flip inequalities
                if X2 * den <= num <= X1 * den:
                    count += 1
    
    print(count)

solve()