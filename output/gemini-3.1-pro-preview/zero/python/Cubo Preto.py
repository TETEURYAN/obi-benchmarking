import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    
    zero_faces = (N - 2) ** 3
    one_face = 6 * ((N - 2) ** 2)
    two_faces = 12 * (N - 2)
    three_faces = 8
    
    print(zero_faces)
    print(one_face)
    print(two_faces)
    print(three_faces)

if __name__ == '__main__':
    main()