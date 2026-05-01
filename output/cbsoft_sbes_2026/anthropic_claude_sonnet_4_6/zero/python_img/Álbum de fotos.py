def can_fit(px, py, w1, h1, w2, h2):
    # Try all orientations of both photos
    # Photo 1 can be (w1,h1) or (h1,w1)
    # Photo 2 can be (w2,h2) or (h2,w2)
    orientations1 = [(w1, h1), (h1, w1)]
    orientations2 = [(w2, h2), (h2, w2)]
    
    for a1, b1 in orientations1:
        for a2, b2 in orientations2:
            # Try placing side by side horizontally: photos placed left-right
            # Photo1 takes a1 width, Photo2 takes a2 width
            # Total width = a1 + a2, each must fit in height
            if a1 + a2 <= px and b1 <= py and b2 <= py:
                return True
            if a1 + a2 <= py and b1 <= px and b2 <= px:
                return True
            # Try placing stacked vertically: photos placed top-bottom
            if b1 + b2 <= py and a1 <= px and a2 <= px:
                return True
            if b1 + b2 <= px and a1 <= py and a2 <= py:
                return True
    
    return False

line1 = input().split()
X, Y = int(line1[0]), int(line1[1])
line2 = input().split()
L1, H1 = int(line2[0]), int(line2[1])
line3 = input().split()
L2, H2 = int(line3[0]), int(line3[1])

if can_fit(X, Y, L1, H1, L2, H2):
    print('S')
else:
    print('N')