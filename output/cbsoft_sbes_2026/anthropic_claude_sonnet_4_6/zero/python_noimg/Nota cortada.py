B = int(input())
T = int(input())

# The note is 160 wide and 70 tall
# The cut goes from point B on the base to point T on the top
# Felix gets the left piece, Marzia gets the right piece

# The left piece is a trapezoid with parallel sides B (bottom) and T (top), height 70
# Area of left piece = (B + T) / 2 * 70
# Total area = 160 * 70

# Left area = (B + T) / 2 * 70
# Total area = 160 * 70
# Half total area = 80 * 70

# Felix wins if (B + T) / 2 > 80, i.e., B + T > 160
# Marzia wins if (B + T) / 2 < 80, i.e., B + T < 160
# Lost if B + T == 160

s = B + T

if s > 160:
    print(1)
elif s < 160:
    print(2)
else:
    print(0)