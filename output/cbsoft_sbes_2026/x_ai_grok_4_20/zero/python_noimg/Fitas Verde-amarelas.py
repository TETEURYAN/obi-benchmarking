
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
grid = []
index = 2
for i in range(N):
    row = data[index]
    grid.append(list(row))
    index += 1

# Create land grid: 1 if '#', 0 otherwise
land = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i][j] == '#':
            land[i][j] = 1

# Directions for 4-connectivity
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to check if two land cells are adjacent
def is_adj(i1, j1, i2, j2):
    return abs(i1 - i2) + abs(j1 - j2) == 1

# We'll model this as a graph where each "maximal segment" is a node
# But to minimize number of tapes = number of segments used
# Actually, since each connected component of land in a certain way...

# The key is that green (horizontal) and yellow (vertical) cannot be adjacent
# So, if two land cells are adjacent horizontally, they cannot be covered by different colors if one is vertical tape and other horizontal.
# A horizontal tape (green) covers a sequence in a row.
# But the constraint is between cells: if two cells are neighbors (share side), and one is covered by green, other by yellow, forbidden.

# So, if two land cells share a side, they cannot have different colors.
# Because if one is in a green tape, it's covered by green, other by yellow -> forbidden.

# Therefore, all land cells that are 4-connected must have the SAME color!
# Is that true? No, because the color is per tape, but a cell covered by green means it's part of some horizontal tape.

# Every land cell must be covered by exactly one tape: either a green (horizontal) or yellow (vertical).

# If a cell is covered by a green tape, it means that tape is horizontal, so the entire tape is in one row.

# The constraint is only that no green-covered cell is adjacent (4-dir) to a yellow-covered cell.

# So, the coloring of cells with two colors: G or Y, such that:
# - All G cells in same row that are contiguous (with only land? no, the tape covers contiguous cells, but since only land needs cover, and tapes cannot cover sea I think? Wait.

# The rule: "All land cells must be covered, all sea must be uncovered."
# And "each cell is completely covered or completely uncovered"

# So tapes can only be placed over land cells. If a tape covers a segment, that segment must be all land, because if it includes sea, that sea would be covered, which is forbidden.

# Yes, important: a tape (green or yellow) can only cover a contiguous sequence of land cells, because if it covers a sea, that sea cell would be covered, violation.

# So, each tape corresponds exactly to a maximal or subsegment of consecutive land cells in a row (for green) or in a column (for yellow).

# But since we can choose any length, but to minimize number, we will always cover maximal possible? Not necessarily, because of constraints.

# The constraint between colors.

# If two land cells are adjacent (share side), then:
# - If they are horizontal neighbors, they could be in same green tape, or in different green tapes (but that would be more tapes), or one in green one in yellow but then if one is green and one is yellow, and they are neighbors, forbidden.

# So if two land cells are horizontal neighbors, they cannot be one green and one yellow.

# Similarly for vertical neighbors.

# So in other words, if two land cells are 4-adjacent, they cannot have different colors.

# Therefore, within each 4-connected component of land cells, ALL cells must have the SAME color!

# Because connectivity is transitive.

# Yes! The land forms connected components (4-connected), and each such component must be colored entirely green or entirely yellow.

# Now, if a component is colored green, that means every cell in it must be covered by a horizontal (green) tape.

# Since the component may have multiple cells in same row, but to cover with horizontal tapes, in each row, the cells of this component in that row must be covered by green tapes.

# But since they are connected (possibly through other rows), but for covering, since tapes are per row for green.

# To cover a cell with green, it must be part of some horizontal tape in its row.

# But since the whole component is green, all cells are green.

# The number of green tapes needed for a component colored green is the number of "horizontal segments" in that component.

# That is, for each row, look at the consecutive land cells belonging to this component in that row; each run of consecutive cells in a row counts as one green tape (we can cover the whole run with one tape).

# Similarly, if colored yellow, number of vertical segments in columns.

# Yes.

# So, first, we need to find all 4-connected components of land ('#').

# For each such component, we have two choices: color it green or yellow.

# If green, cost = number of horizontal runs in the component.
# A horizontal run: in each row, for the cells in this component, group by consecutive in row.

# Since the component may have gaps? No, if there is a gap in a row, but connected through other path, but if there are two separate # in same row not adjacent, but connected via other rows, then they are in same component, but to cover with green, since they are not contiguous in the row (there is sea or nothing between), we cannot cover them with one tape; we need separate tapes for each disjoint segment in that row.

# Yes, so number of maximal contiguous horizontal segments within the component.

# Similarly for vertical.

# Then, for each component, we can choose to assign it to green, cost = num_h_segments, or yellow, cost = num_v_segments, and take the min for that component.

# Then, total min tapes is sum over all components of min(h_seg, v_seg) for that component.

# Is that correct?

# Is there any interaction between components? The constraint only applies if two cells from different components are adjacent.

# But if two land cells are adjacent, they would be in the SAME component! Because 4-connected component.

# So, no two land cells from different components are adjacent.

# Therefore, no constraint between different components.

# Yes! So they are independent.

# Perfect.

# So, the problem reduces to: find all 4-connected components of '#'.

# For each, compute number of horizontal runs and vertical runs within it.

# Then, for each component, add min(num_horizontal_runs, num_vertical_runs) to the answer.

# That should be the minimum number of tapes.

# Let's verify with the sample.

# First sample:

# 4 7

# ##..###

# ..#...#

# #####.#

# #..#..#

# Let's see the land positions.

# Row 0: # # . . # # #

# Row 1: . . # . . . #

# Row 2: # # # # # . #

# Row 3: # . . # . . #

# Now, let's find connected components.

# There seems to be one big component on the left and some on right? Let's see.

# Actually, looking at the picture (though not shown), but output is 8.

# Let's compute.

# I need to implement this logic.

# But first, is this correct?

# In the third sample:

# 6x5

# .....

# ..###

# ..###

# ..###

# ..###

# .....

# So a 4x3 rectangle of # in the middle.

# It's one connected component.

# Horizontal runs: in each of 4 rows, there is one run of 3 consecutive #. So 4 horizontal runs.

# Vertical runs: in each of 3 columns, there is one run of 4 consecutive #. So 3 vertical runs.

# min(4,3)=3, and sample output is 3. Yes! Matches. Probably using 3 vertical tapes.

# Second sample:

# 1 9

# ...####.#

# One row: positions 3,4,5,6 are #, then 8 is #.

# Two components: one with 4 #, one with 1 #.

# For the 4#: horizontal runs=1, vertical runs=4 (since 1 row), min(1,4)=1

# For the single: min(1,1)=1

# Total 2, matches sample output 2.

# First sample output 8, presumably correct.

# Another sample 4 output 7, seems good.

# Last one looks like letters or something, output 18.

# Perfect.

# Now, what if a component has weird shape, like two horizontal segments connected by a vertical.

# For example, like a U shape.

# Then horizontal runs would be 3 (two on bottom, one on top? etc.), vertical would be 2, etc.

# Yes, and since we choose all green or all yellow for the component.

# Is it always optimal to color whole component one color? Yes, because as we established, must be same color due to adjacency constraints.

# Excellent.

# Now, to implement, since N,M<=1000, NM=1e6, ok.

# We will do DFS or BFS to find components.

# Since N*M=1e6, need to be careful with recursion depth, so better use iterative DFS or BFS.

# I'll use BFS.

# For each component, while discovering the cells, I can collect all cells in the component.

# Then, to count horizontal runs: group cells by row, and for each row, sort the columns, and count how many groups of consecutive cols.

# Similarly for vertical: group by col, for each col sort rows, count consecutive groups.

# Since |component| total over all is <=1e6, it's fine.

# Time: O(NM log?) but if I sort per row, but since per component, if I collect list of (i,j), then use dict of lists or array of lists.

# Since N<=1000, I can use list of lists.

from collections import deque, defaultdict

visited = [[False] * M for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(M):
        if land[i][j] == 1 and not visited[i][j]:
            # new component
            component = []
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                component.append((x, y))
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and land[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            
            # Now compute h_runs and v_runs
            row_cols = [[] for _ in range(N)]
            col_rows = [[] for _ in range(M)]
            for x, y in component:
                row_cols[x].append(y)
                col_rows[y].append(x)
            
            h_runs = 0
            for r in range(N):
                if row_cols[r]:
                    cols = sorted(row_cols[r])
                    h_runs += 1
                    for k in range(1, len(cols)):
                        if cols[k] != cols[k-1] + 1:
                            h_runs += 1
            
            v_runs = 0
            for c in range(M):
                if col_rows[c]:
                    rows = sorted(col_rows[c])
                    v_runs += 1
                    for k in range(1, len(rows)):
                        if rows[k] != rows[k-1] + 1:
                            v_runs += 1
            
            ans += min(h_runs, v_runs)

print(ans)
