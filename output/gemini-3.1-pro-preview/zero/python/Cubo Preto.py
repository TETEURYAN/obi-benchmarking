
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    zero_faces = (n - 2) ** 3
    one_face = 6 * ((n - 2) ** 2)
    two_faces = 12 * (n - 2)
    three_faces = 8
    
    print(zero_faces)
    print(one_face)
    print(two_faces)
    print(three_faces)

if __name__ == '__main__':
    main()
