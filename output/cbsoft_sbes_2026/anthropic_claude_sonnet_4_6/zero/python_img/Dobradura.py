import sys

def solve():
    # When N=0: no folding, cut gives 4 pieces -> output 4
    # When N=1: one fold operation D (fold twice), then cut
    # Let's think about it:
    # N=0: original sheet, cut vertically and horizontally -> 4 pieces
    # But output says N=0 gives 4, N=1 gives 9
    
    # Let me think more carefully.
    # Each fold operation D folds the paper twice (once horizontally, once vertically)
    # resulting in 1/4 the size with 4 layers.
    
    # After N fold operations:
    # - The paper has 4^N layers
    # - We cut with one vertical and one horizontal cut
    # - This creates a grid of cuts through all layers
    
    # For N=0: 1 layer, cut gives 4 pieces -> 4
    # For N=1: 4 layers, but the pieces depend on how folds interact with cuts
    
    # Let me think differently.
    # After N folds of operation D, the folded square has dimensions (1/2^N) of original in each direction.
    # The cuts go through the middle of the folded square.
    
    # For N=0: cut through middle of original -> 4 pieces
    # For N=1: fold once (D operation = 2 folds), then cut
    #   After D: paper is folded in half horizontally then vertically
    #   Cut through middle of folded piece
    #   The vertical cut corresponds to 2 cuts on original (at 1/4 and 3/4? or at 1/2?)
    #   The horizontal cut similarly
    
    # Actually let me think in terms of lines on original paper.
    # Each fold doubles the number of cut lines in that direction.
    # After N fold operations (each fold = 1 horizontal + 1 vertical fold):
    # In each direction, number of cut lines = 2^N
    # Number of pieces = (2^N + 1)^2... wait
    # N=0: (1+1)^2 = 4 ✓
    # N=1: (2+1)^2 = 9 ✓
    # N=2: (4+1)^2 = 25
    
    # So formula: (2^N + 1)^2
    
    test_num = 1
    for line in sys.stdin:
        n = int(line.strip())
        if n == -1:
            break
        pieces = (2**n + 1) ** 2
        print(f"Teste {test_num}")
        print(pieces)
        print()
        test_num += 1

solve()