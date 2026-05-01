
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    X = int(input_data[0])
    Y = int(input_data[1])
    L1 = int(input_data[2])
    H1 = int(input_data[3])
    L2 = int(input_data[4])
    H2 = int(input_data[5])
    
    possible = False
    
    for w1, h1 in [(L1, H1), (H1, L1)]:
        for w2, h2 in [(L2, H2), (H2, L2)]:
            if w1 + w2 <= X and max(h1, h2) <= Y:
                possible = True
            if max(w1, w2) <= X and h1 + h2 <= Y:
                possible = True
                
    if possible:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    solve()
