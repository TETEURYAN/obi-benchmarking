import sys

def solve():
    data = sys.stdin.read().split()
    test_num = 0
    results = []
    for token in data:
        n = int(token)
        if n == -1:
            break
        test_num += 1
        # After N doublings, the paper has 2^N layers in each direction (4^N total layers)
        # The paper is folded 2^N times in each direction
        # When we cut vertically and horizontally through the center:
        # Each cut through k layers produces k+1 pieces in that dimension
        # But we need to think about it differently
        #
        # After N operations of D (fold vertically then horizontally):
        # The paper has 2^N folds in x-direction and 2^N folds in y-direction
        # Number of layers = 4^N
        #
        # When N=0: no folding, 1 sheet. Cut vertically and horizontally -> 4 pieces? But output says 4.
        # When N=1: output says 9.
        #
        # N=0: 4 pieces
        # N=1: 9 pieces
        #
        # Let's think: after N doublings, in each direction we have 2^N segments.
        # A cut in one direction through a folded paper with 2^N layers creates cuts at multiple positions.
        # 
        # For N=0: 1x1 grid of paper, one vertical cut + one horizontal cut = 4 pieces
        # For N=1: after folding once (2 layers in each direction)
        #   The vertical cut goes through 2 layers -> creates cuts at 2 positions in original
        #   The horizontal cut goes through 2 layers -> creates cuts at 2 positions in original
        #   Original paper divided into 3x3 = 9 pieces
        #
        # Pattern: (2^N + 1)^2
        # N=0: (1+1)^2 = 4 ✓
        # N=1: (2+1)^2 = 9 ✓
        
        pieces = (2**n + 1) ** 2
        results.append((test_num, pieces))
    
    output = []
    for i, (num, pieces) in enumerate(results):
        output.append(f"Teste {num}")
        output.append(str(pieces))
        output.append("")
    
    print('\n'.join(output))

solve()