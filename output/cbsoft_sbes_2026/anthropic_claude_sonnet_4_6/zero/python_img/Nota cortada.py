B = int(input())
T = int(input())

# The note is 160 x 70
# Cut goes from (B, 0) at base to (T, 70) at top
# Left piece (Felix) is a trapezoid with parallel sides B and T, height 70
# Area of left piece = (B + T) / 2 * 70
# Total area = 160 * 70
# Half area = 80 * 70

left_area = (B + T) * 70  # multiplied by 2 to avoid fractions
total_area = 160 * 70 * 2  # also multiplied by 2
half_area = total_area // 2  # = 160 * 70

if left_area > half_area:
    print(1)
elif left_area < half_area:
    print(2)
else:
    print(0)