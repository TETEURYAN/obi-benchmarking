import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    N = int(next(iterator))
    X1 = int(next(iterator))
    Y1 = int(next(iterator))
    X2 = int(next(iterator))
    Y2 = int(next(iterator))
    
    mid = N // 2
    
    # Check horizontal cut (rows)
    # One sticker in rows 1 to mid, the other in rows mid+1 to N
    horizontal_possible = (X1 <= mid and X2 > mid) or (X1 > mid and X2 <= mid)
    
    # Check vertical cut (columns)
    # One sticker in cols 1 to mid, the other in cols mid+1 to N
    vertical_possible = (Y1 <= mid and Y2 > mid) or (Y1 > mid and Y2 <= mid)
    
    if horizontal_possible or vertical_possible:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()