import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    A = int(input_data[0])
    B = int(input_data[1])
    C = int(input_data[2])
    H = int(input_data[3])
    L = int(input_data[4])

    door_min = min(H, L)
    door_max = max(H, L)

    # Check all 3 possible faces of the mattress (AxB, AxC, BxC)
    # A face fits if its smaller dimension <= door_min AND its larger dimension <= door_max
    
    # Face 1: A x B
    face1_min = min(A, B)
    face1_max = max(A, B)
    
    # Face 2: A x C
    face2_min = min(A, C)
    face2_max = max(A, C)
    
    # Face 3: B x C
    face3_min = min(B, C)
    face3_max = max(B, C)

    if (face1_min <= door_min and face1_max <= door_max) or \
       (face2_min <= door_min and face2_max <= door_max) or \
       (face3_min <= door_min and face3_max <= door_max):
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    solve()