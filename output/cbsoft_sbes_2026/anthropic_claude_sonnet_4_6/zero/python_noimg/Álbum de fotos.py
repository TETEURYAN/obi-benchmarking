def fits(pw, ph, fw, fh):
    # Check if photo (fw x fh) fits in page (pw x ph)
    return fw <= pw and fh <= ph

def can_place(px, py, l1, h1, l2, h2):
    # Try all 4 orientations for each photo (2 x 2 = 4 combinations)
    orientations1 = [(l1, h1)]
    if l1 != h1:
        orientations1.append((h1, l1))
    
    orientations2 = [(l2, h2)]
    if l2 != h2:
        orientations2.append((h2, l2))
    
    for (w1, h1_) in orientations1:
        for (w2, h2_) in orientations2:
            # Try placing side by side horizontally: photo1 on left, photo2 on right
            # Both must fit in height, combined width must fit
            # Option 1: side by side horizontally
            if w1 + w2 <= px and max(h1_, h2_) <= py:
                return True
            # Option 2: stacked vertically
            if max(w1, w2) <= px and h1_ + h2_ <= py:
                return True
    
    return False

line1 = input().split()
px, py = int(line1[0]), int(line1[1])
line2 = input().split()
l1, h1 = int(line2[0]), int(line2[1])
line3 = input().split()
l2, h2 = int(line3[0]), int(line3[1])

if can_place(px, py, l1, h1, l2, h2):
    print('S')
else:
    print('N')