import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A, B, C = map(int, data[:3])
    H, L = map(int, data[3:5])
    
    dims = [A, B, C]
    dims.sort()
    # As duas menores dimensões do colchão
    x, y = dims[0], dims[1]
    
    # Dimensões da porta
    door_dims = sorted([H, L])
    door_h, door_w = door_dims[0], door_dims[1]
    
    if x <= door_h and y <= door_w:
        print('S')
    else:
        print('N')

if __name__ == "__main__":
    main()