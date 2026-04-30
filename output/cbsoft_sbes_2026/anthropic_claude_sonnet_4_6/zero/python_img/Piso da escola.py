L = int(input())
C = int(input())

# Type 1 tiles: full diamonds
# Interior full tiles
type1 = (2*L - 1) * (2*C - 1) // 2 + ... 

# Let me think carefully about this.
# The room is L x C meters.
# Each tile has diagonal of 1 meter, so side = 1/sqrt(2).
# Tiles are placed with diagonals aligned to room sides.
# 
# For L=3, C=5: type1=23, type2=12
# 
# The grid of tile centers forms a pattern.
# In a rotated grid, the number of full tiles and half tiles:
# 
# Looking at the pattern: tiles are arranged in a diamond grid.
# The room L x C with tiles of diagonal 1m:
# Along each dimension, we fit 2*L tiles diagonally (half-diagonal = 0.5m)
# 
# Type1 (full diamond): (2L-1)*(2C-1) - but need to check parity
# For L=3,C=5: (5)*(9) = 45... not matching
#
# Let me think differently.
# Number of full tiles = (L-1)*(C-1)*2 + ... 
# For L=3,C=5: type1=23, type2=12
# (2*3-1)*(2*5-1) = 5*9=45 total half-unit squares
# type1*2 + type2*1 + 4*(0.5) = L*C*4 (area in quarter units)
# Area = L*C = 15, each type1 has area 0.5, type2 has area 0.25, type3 has area 0.125
# 23*0.5 + 12*0.25 + 4*0.125 = 11.5 + 3 + 0.5 = 15 ✓
#
# Pattern: type2 = 2*(L-1) + 2*(C-1) = 2*(L+C-2)
# For L=3,C=5: 2*(3+5-2)=2*6=12 ✓
# For L=1,C=1: 2*(1+1-2)=0 ✓
#
# type1: from area equation:
# type1*0.5 = L*C - type2*0.25 - 4*0.125
# type1 = 2*L*C - type2*0.5 - 1
# For L=3,C=5: 2*15 - 12*0.5 - 1 = 30 - 6 - 1 = 23 ✓
# For L=1,C=1: 2*1 - 0 - 1 = 1 ✓

L = int(input())
C = int(input())

type2 = 2 * (L - 1) + 2 * (C - 1)
type1 = 2 * L * C - type2 // 2 - 1

print(type1)
print(type2)