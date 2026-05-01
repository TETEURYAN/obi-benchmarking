
import sys

def main():
    data = sys.stdin.read().split()
    A = int(data[0])
    B = int(data[1])
    C = int(data[2])
    H = int(data[3])
    L = int(data[4])

    faces = [
        (A, B),
        (A, C),
        (B, C)
    ]

    for face in faces:
        a, b = face
        if (a <= H and b <= L) or (a <= L and b <= H):
            print('S')
            return
    print('N')

if __name__ == "__main__":
    main()
