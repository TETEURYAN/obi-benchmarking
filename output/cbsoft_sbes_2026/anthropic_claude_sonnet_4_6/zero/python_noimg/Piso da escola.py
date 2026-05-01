L = int(input())
C = int(input())

# Each lajota type 1 is a square with 1m diagonal, so side = 1/sqrt(2)
# When placed with diagonals aligned to walls, they form a grid pattern
# 
# For a room L x C:
# Type 1 (full diamond): 
# Type 2 (half diamond - triangle):
# Type 3 (quarter diamond): always 4 (corners)
#
# Looking at the pattern:
# For L=3, C=5: type1=23, type2=12
# For L=1, C=1: type1=1, type2=0
#
# The grid of diamonds: when you tile with diamonds (squares rotated 45°)
# with diagonal = 1m, the grid has (2L-1)*(2C-1) positions in a checkerboard-like pattern
# but we need to think carefully.
#
# With diagonal=1, side=sqrt(2)/2
# In a rotated grid, for room L x C:
# The number of full tiles (type1) in interior
# The number of half tiles (type2) on edges
#
# Let's think of it as a grid of size (2L+1) x (2C+1) points
# where diamonds fit at integer+half positions
#
# Actually, let's derive from examples:
# L=3, C=5: type1=23, type2=12
# L=1, C=1: type1=1, type2=0
#
# For L=1,C=1: 1 full, 0 half, 4 quarter
# For L=3,C=5: 23 full, 12 half, 4 quarter
#
# Pattern for type2 (edge halves): 2*(L-1) + 2*(C-1) = 2*(L+C-2)
# L=3,C=5: 2*(3+5-2)=12 ✓
# L=1,C=1: 2*(1+1-2)=0 ✓
#
# Pattern for type1:
# L=3,C=5: 23
# L=1,C=1: 1
# 
# type1 = (2L-1)*(2C-1) - 2*(L-1)*(C-1) ... let's check
# L=3,C=5: (5)*(9) - 2*2*4 = 45-16=29 no
#
# type1 = 2*L*C - L - C + 1? 
# L=3,C=5: 30-3-5+1=23 ✓
# L=1,C=1: 2-1-1+1=1 ✓
# 
# So type1 = 2*L*C - L - C + 1

type1 = 2*L*C - L - C + 1
type2 = 2*(L + C - 2)

print(type1)
print(type2)