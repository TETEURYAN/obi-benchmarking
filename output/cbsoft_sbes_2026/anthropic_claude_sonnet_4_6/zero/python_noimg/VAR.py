Looking at the problem:

- The judge is at (0,0)
- The field is 16m x 8m rectangle
- From the examples: (-6,6) and (8,2) are inside; (-4,10) and (6,-2) are outside

From the figure description, the judge is at corner (0,0), and the field extends to 16m x 8m. Looking at the examples:
- (8,2) is inside → x goes from some negative to positive, y from 0 to 8
- (-6,6) is inside → x can be negative
- (6,-2) is outside → y=-2 is outside
- (-4,10) is outside → y=10 is outside

The field is 16m wide and 8m tall. Judge at (0,0). The field seems to span x from -8 to 8 (16m wide) and y from 0 to 8 (8m tall).

Check: (-6,6) → x in [-8,8], y in [0,8] → inside ✓
(8,2) → x in [-8,8], y in [0,8] → inside ✓
(-4,10) → y=10 > 8 → outside ✓
(6,-2) → y=-2 < 0 → outside ✓
(6,-2) test case → N ✓
(8,2) test case → S ✓

x = int(input())
y = int(input())

if -8 <= x <= 8 and 0 <= y <= 8:
    print('S')
else:
    print('N')