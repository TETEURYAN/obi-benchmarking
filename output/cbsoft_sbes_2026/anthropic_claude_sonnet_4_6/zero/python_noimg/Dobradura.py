import sys

def solve():
    n_test = 0
    for line in sys.stdin:
        N = int(line.strip())
        if N == -1:
            break
        n_test += 1
        # After N folds, the paper is folded 2*N times total (N times operation D, each D = 2 folds)
        # Each fold doubles the layers
        # After N operations of D (each D = 2 folds), we have 2^(2*N) = 4^N layers
        # The paper is a square folded into a smaller square
        # When we cut vertically and horizontally through the folded square,
        # we get pieces based on the grid created
        
        # Let's think about it:
        # N=0: no folding, cut vertical + horizontal = 4 pieces (2x2 grid)
        # But expected output for N=0 is 4, and N=1 is 9
        
        # For N=0: 4 pieces
        # For N=1: 9 pieces
        
        # Let me think more carefully.
        # Operation D: fold twice -> 4 layers, 1/4 size
        # After N operations: 4^N layers, size = original / 2^N x original / 2^N
        
        # When we cut the folded square with one vertical and one horizontal cut,
        # we cut through all layers.
        
        # The cuts divide the folded square into 4 pieces (2x2).
        # But when unfolded, each cut line corresponds to multiple cut lines in the original.
        
        # For N=0: 1 sheet, cut into 4 pieces -> 4
        # For N=1: folded once (operation D = 2 folds)
        #   After 1 fold (horizontal): 2 layers, half height
        #   After 2nd fold (vertical): 4 layers, quarter size
        #   Cut vertical and horizontal through the quarter
        #   The vertical cut in the quarter corresponds to 1 cut in original (the fold line + cut)
        #   Actually the cut creates lines in the original paper
        
        # Let me think in terms of grid lines:
        # After N operations, the paper is folded to 1/2^N of original in each dimension
        # The cut creates a grid of (2^N + 1) x (2^N + 1) points? No...
        
        # N=0: 2x2 = 4 pieces -> (1+1)*(1+1) = 4
        # N=1: 9 pieces -> 3x3 = 9 -> (2+1)*(2+1) = 9
        # N=2: would be (4+1)*(4+1) = 25?
        # Pattern: (2^N + 1)^2
        
        # Check: N=0: (1+1)^2 = 4 ✓
        # N=1: (2+1)^2 = 9 ✓
        
        pieces = (2**N + 1) ** 2
        
        print(f"Teste {n_test}")
        print(pieces)
        print()

solve()