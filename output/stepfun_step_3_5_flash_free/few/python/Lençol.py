import sys

def can_cover(a, b, A, B):
    return (A <= a and B <= b) or (A <= b and B <= a)

def check_union(W, H, A1, B1, A2, B2):
    h_max1 = 0
    if W <= A1:
        h_max1 = max(h_max1, B1)
    if W <= B1:
        h_max1 = max(h_max1, A1)
    h_max2 = 0
    if W <= A2:
        h_max2 = max(h_max2, B2)
    if W <= B2:
        h_max2 = max(h_max2, A2)
    if h_max1 > 0 and h_max2 > 0:
        low = max(1, H - h_max2)
        high = min(h_max1, H - 1)
        if low <= high:
            return True

    w_max1 = 0
    if H <= A1:
        w_max1 = max(w_max1, B1)
    if H <= B1:
        w_max1 = max(w_max1, A1)
    w_max2 = 0
    if H <= A2:
        w_max2 = max(w_max2, B2)
    if H <= B2:
        w_max2 = max(w_max2, A2)
    if w_max1 > 0 and w_max2 > 0:
        low = max(1, W - w_max2)
        high = min(w_max1, W - 1)
        if low <= high:
            return True

    return False

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    A1, B1, A2, B2, A, B = map(int, data)
    if can_cover(A1, B1, A, B) or can_cover(A2, B2, A, B):
        print('S')
        return
    if check_union(A, B, A1, B1, A2, B2) or check_union(B, A, A1, B1, A2, B2):
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()