import sys

def can_make(a1, b1, a2, b2, A, B):
    # Try all orientations of both pieces
    pieces1 = [(a1, b1), (b1, a1)]
    pieces2 = [(a2, b2), (b2, a2)]
    
    # Case 1: single piece covers the sheet (no seam needed)
    for (x1, y1) in pieces1:
        if x1 >= A and y1 >= B:
            return True
    for (x2, y2) in pieces2:
        if x2 >= A and y2 >= B:
            return True
    
    # Case 2: two pieces joined with a seam parallel to one side
    # Seam parallel to B side (vertical seam): pieces placed side by side horizontally
    # piece1 width w1, piece2 width w2, w1+w2 >= A, both heights >= B
    # Seam parallel to A side (horizontal seam): pieces placed side by side vertically
    # piece1 height h1, piece2 height h2, h1+h2 >= B, both widths >= A
    
    for (x1, y1) in pieces1:
        for (x2, y2) in pieces2:
            # Horizontal join: x1 + x2 >= A, y1 >= B, y2 >= B
            if x1 + x2 >= A and y1 >= B and y2 >= B:
                return True
            # Vertical join: y1 + y2 >= B, x1 >= A, x2 >= A
            if y1 + y2 >= B and x1 >= A and x2 >= A:
                return True
    
    return False

data = sys.stdin.read().split()
a1, b1, a2, b2, A, B = int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5])

if can_make(a1, b1, a2, b2, A, B):
    print("S")
else:
    print("N")