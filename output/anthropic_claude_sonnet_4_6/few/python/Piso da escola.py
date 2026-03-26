import sys

data = sys.stdin.read().split()
L = int(data[0])
C = int(data[1])

# For a room of L x C meters with diagonal-aligned tiles:
# Each meter of length/width corresponds to a diagonal grid
# 
# Looking at the pattern:
# For L=3, C=5: type1=23, type2=12
# For L=1, C=1: type1=1, type2=0
#
# The tile has diagonal 1 meter, so side = 1/sqrt(2)
# The grid is rotated 45 degrees
#
# In the diagonal grid pattern:
# - Interior full tiles (type 1): (2*L-1)*(2*C-1) - but need to figure out pattern
# 
# Let's think in terms of the diagonal grid:
# The room L x C, with tiles aligned diagonally
# Number of type1 tiles = (2L-1)*(2C-1) - something
# 
# For L=1,C=1: type1=1, type2=0
# (2*1-1)*(2*1-1) = 1. Correct!
#
# For L=3,C=5: (2*3-1)*(2*5-1) = 5*9 = 45. But answer is 23.
# 
# Let me think differently.
# In a diagonal tiling of L x C room:
# The diagonal grid has (2L+1) x (2C+1) points roughly
# 
# Actually let's think: type1 = (L-1)*(C-1)*2 + (L-1) + (C-1) + 1?
# For L=1,C=1: 0+0+0+1=1 ✓
# For L=3,C=5: 2*2*4 + 2 + 4 + 1 = 16+7=23 ✓
#
# So type1 = 2*(L-1)*(C-1) + (L-1) + (C-1) + 1
#           = 2*(L-1)*(C-1) + L + C - 1
#
# For type2:
# For L=1,C=1: 0
# For L=3,C=5: 12
# type2 = 2*(L-1) + 2*(C-1)?
# = 2*2 + 2*4 = 4+8=12 ✓
# For L=1,C=1: 0+0=0 ✓
#
# So type2 = 2*(L-1) + 2*(C-1) = 2*(L+C-2)

type1 = 2*(L-1)*(C-1) + (L-1) + (C-1) + 1
type2 = 2*(L-1) + 2*(C-1)

print(type1)
print(type2)