import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    X, Y = int(data[0]), int(data[1])
    L1, H1 = int(data[2]), int(data[3])
    L2, H2 = int(data[4]), int(data[5])
    
    orientations1 = [(L1, H1), (H1, L1)]
    orientations2 = [(L2, H2), (H2, L2)]
    
    for w1, h1 in orientations1:
        for w2, h2 in orientations2:
            # Tenta colocar lado a lado (horizontalmente)
            if (w1 + w2 <= X and max(h1, h2) <= Y) or (w1 + w2 <= Y and max(h1, h2) <= X):
                print('S')
                return
            # Tenta colocar um sobre o outro (verticalmente)
            if (max(w1, w2) <= X and h1 + h2 <= Y) or (max(w1, w2) <= Y and h1 + h2 <= X):
                print('S')
                return
                
    print('N')

solve()