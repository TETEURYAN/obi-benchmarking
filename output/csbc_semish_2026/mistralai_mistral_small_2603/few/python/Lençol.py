
import sys

def main():
    data = sys.stdin.read().split()
    A1, B1, A2, B2, A, B = map(int, data)

    def check(a, b):
        if (a == A and b == B) or (a == B and b == A):
            return True
        if a > A or b > B:
            return False
        if (a == A and (b + B2) == B) or (a == A and (B2 + b) == B):
            return True
        if (b == A and (a + B2) == B) or (b == A and (B2 + a) == B):
            return True
        if (a + A2 == A and b == B) or ((A2 + a) == A and b == B):
            return True
        if (b + A2 == A and a == B) or ((A2 + b) == A and a == B):
            return True
        if (a + A2 == A and b + B2 == B) or ((A2 + a) == A and (B2 + b) == B):
            return True
        if (a + B2 == A and b + A2 == B) or ((B2 + a) == A and (A2 + b) == B):
            return True
        return False

    if check(A1, B1) or check(B1, A1) or check(A2, B2) or check(B2, A2):
        print('S')
    else:
        print('N')

if __name__ == "__main__":
    main()
