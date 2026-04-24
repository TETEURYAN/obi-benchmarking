import sys

def solve():
    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        X, Y = map(int, line1)
        
        line2 = sys.stdin.readline().split()
        L1, H1 = map(int, line2)
        
        line3 = sys.stdin.readline().split()
        L2, H2 = map(int, line3)
    except ValueError:
        return

    orientations1 = [(L1, H1), (H1, L1)]
    orientations2 = [(L2, H2), (H2, L2)]

    for w1, h1 in orientations1:
        for w2, h2 in orientations2:
            if (w1 + w2 <= X and max(h1, h2) <= Y) or \
               (max(w1, w2) <= X and h1 + h2 <= Y):
                print('S')
                return

    print('N')

if __name__ == '__main__':
    solve()