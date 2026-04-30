import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    X, Y = int(input_data[0]), int(input_data[1])
    L1, H1 = int(input_data[2]), int(input_data[3])
    L2, H2 = int(input_data[4]), int(input_data[5])
    
    for w1, h1 in ((L1, H1), (H1, L1)):
        for w2, h2 in ((L2, H2), (H2, L2)):
            if w1 + w2 <= X and max(h1, h2) <= Y:
                print('S')
                return
            if w1 + w2 <= Y and max(h1, h2) <= X:
                print('S')
                return
                
    print('N')

if __name__ == '__main__':
    main()