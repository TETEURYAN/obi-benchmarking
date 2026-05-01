
import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()

N = int(data[0])
rects = []
index = 1
for i in range(N):
    x1 = int(data[index])
    y1 = int(data[index+1])
    x2 = int(data[index+2])
    y2 = int(data[index+3])
    rects.append((x1, y1, x2, y2))
    index += 4

# Find the outermost rectangle (largest area)
outer_idx = 0
max_area = -1
for i in range(N):
    area = (rects[i][2] - rects[i][0]) * (rects[i][1] - rects[i][3])
    if area > max_area:
        max_area = area
        outer_idx = i

# Build containment tree using DFS-like approach with events
# We will model "regions" between nested rectangles

# To compute minimum antennas: it's like covering the "faces" in the planar subdivision
# But due to the signal propagation rule (outward yes, inward no), each "innermost" region or
# each time we cross into a new inner room that isn't covered by outer signal requires a new antenna.
# Actually, from the problem: signal from inside a room can go out, but not from outside in.
# So an antenna placed in a room covers that room and all outer rooms, but not inner rooms.

# The containment forms a tree (since no intersections, only nesting).
# The outermost room is the root.
# An antenna placed in a room covers that room and all its ancestors (outer rooms).
# To cover a leaf room, you need an antenna either in it or in one of its descendants.
# No: if you place in an inner room, signal goes out to outer rooms.
# If you place in outer, it cannot go into inner rooms.

# So: antenna in a room R covers R and all rooms outside R (ancestors), but none of the rooms inside R (descendants).

# We need to cover all rooms.
# This is equivalent to: for each room, there must be an antenna in it or in one of its descendant rooms.

# This is exactly the minimum number of nodes to select in the tree such that every node is either selected or has a selected descendant.
# No: every node must have a selected node in its subtree (including itself).

# Yes: for each node v, there must be at least one selected node in the subtree of v.

# The minimum number of such nodes is the number of "maximal" rooms that have no selected descendants needed, but actually it's simply the number of leaves in the tree? No.

# To satisfy that every subtree has at least one selected node, the minimal way is to select all the leaves.
# Is that correct?
# If I select all leaves, then every internal node has leaves in its subtree, so yes covered.
# But can I do better? If I select an internal node, it covers that node and all its ancestors? No.

# Let's clarify.

# Coverage:
# Antenna at node u covers u and all ancestors of u.

# We need every room v to be covered, i.e. for every v there exists an antenna u such that u is in the subtree of v (u is v or descendant of v).

# Yes: v is covered if there is a selected u in the subtree of v (including v).

# So yes, every subtree must contain at least one selected node.

# The minimal set is obtained by selecting a node only when necessary, i.e., when a subtree has no selected descendants yet.

# This is equivalent to counting the number of subtrees where we must place one because there are no deeper ones.

# Actually, there is a simple greedy: we place an antenna at a node if it has no selected descendant and it is not covered by any descendant (which is the same).

# The minimum number is the number of nodes that have no children. i.e. the number of leaves.

# Is that true?
# If I select all leaves, yes it works.
# Can I select fewer? Suppose I have a chain: outer -> A -> B -> C (leaf).
# If I select C, then C covers C, and since C is descendant of B, A, outer, it covers all.
# So selecting only the deepest leaf covers everything.
# So number is 1, not 3 (number of leaves is 1).

# Another example: two separate inner rooms inside outer.
# Leaves = 2, and indeed you need 2 antennas, one in each inner room. If you place in outer, it doesn't cover inners.

# If one inner has another inside it: outer -> A -> B, and outer -> C.
# Then leaves are B and C. Selecting B and C: 2.
# Is 1 possible? If select B, covers B,A,outer. But not C. So need another for C. Yes 2.

# So when is it not equal to number of leaves?
# In the chain, number of leaves=1, answer=1. Good.
# Seems it is always the number of leaves in the containment tree.

# But in the first sample:
# 4 rectangles.
# Let's see the coordinates:
# A: 5 19 8 17
# B: 5 15 15 5
# C: 0 20 20 0   <- this is outermost
# D: 8 10 10 8

# So C contains all.
# B is from x5-15, y15-5, so big inner.
# A is 5-8,19-17, which is inside C but does it inside B? B y from 15 to 5, A y19-17 which is above 15, so A is in C but not in B.
# D 8-10,10-8, which is inside B (B goes to y5, x15).

# So containment:
# C (outer)
# - A (top left small)
# - B
#   - D

# So tree: C has children A and B, B has child D.
# Leaves: A and D.
# Number of leaves = 2, and sample output is 2. Perfect.

# Another sample: 1 rectangle -> 1 leaf -> 1. Good.

# Third sample: output 3, so presumably 3 leaves.

# Yes! So the answer is the number of leaf rooms in the containment tree.

# We need to build the containment forest (actually tree since one outer), and count how many nodes have no children.

# With N=1e5, we need an efficient way to build the tree or at least count the number of nodes with no contained rooms.

# A room is a leaf if no other room is strictly inside it.

# So answer = number of rooms that contain no other rooms inside them.

# Is that correct?
# In the example above: A contains nothing -> leaf.
# D contains nothing -> leaf.
# B contains D -> not leaf.
# C contains A,B -> not leaf.
# Yes, 2.

# In chain: only the innermost is leaf. Yes, and answer 1. Perfect!

# So we don't even need to build the tree. Just count how many rectangles do not contain any other rectangle inside them.

# But is "contain" strict? Yes, since walls don't touch, if one is inside another, its coordinates are strictly inside.

# Constraints: X1 < X2, Y2 < Y1, and no intersections, only nesting or disjoint.

# But they can be side by side inside a parent.

# To check for each rect if there exists at least one other rect strictly inside it.

# But N=1e5, O(N^2) is impossible.

# We need an efficient way to, for each rectangle, check if it has at least one rectangle strictly contained in it.

# Then answer = N - number of rectangles that contain at least one other.

# No: answer = number of rectangles that contain ZERO others.

# Yes.

# How to compute for each rect the number of rects inside it, or just whether >0, efficiently.

# Since they are axis-aligned and non-intersecting (only nested or disjoint), the containment forms a laminar family, actually a tree.

# To count leaves efficiently.

# One standard way for nested rectangles is to sort them by size or by coordinates.

# A rectangle R contains S if X1_R < X1_S < X2_S < X2_R and Y2_R < Y2_S < Y1_S < Y1_R.
# Since Y1 is top (larger y), Y2 bottom (smaller y).

# Note: Y2 < Y1 is given.

# To find for each, if there is any other inside.

# One way is to discretize all x and y, but with 1e5 still tricky.

# We can think of each rectangle as an interval in 2D.

# A good way for nested structures is to sort all rectangles by increasing x1, then by decreasing x2 or something.

# To build the tree efficiently, we can sort the rectangles in order of increasing area, or by one coordinate.

# Since no intersections, we can sort by left edge X1 ascending.

# If two have same X1, the one with smaller X2 cannot contain the one with larger, etc.

# A standard algorithm for building containment hierarchy for rectangles with no intersections is to sort them by their left x-coordinate.

# Let's sort all rectangles by X1 ascending, if tie by X2 descending (larger first, i.e. outer first).

# Then we can process them in this order and use a stack or set for active y-intervals.

# But perhaps simpler: since we only need the number of leaves, i.e. number of rects with no children.

# We can find for each rect its parent (the smallest rect that contains it), and then count how many have no children.

# To do it efficiently.

# A known way is to use sweep line or to use a map of active segments.

# But let's think of a method that works in O(N log N).

# One effective way: process rectangles from outermost to innermost by sorting on size (area) descending, but areas can be same? Coordinates up to 1e9, but possible.

# Since they don't intersect, containment is strict.

# Better idea: we will consider all rectangles, and for each possible "inner" rectangle, find if it has a direct parent.

# To count nodes with children count >0.

# We can build the parent for each node.

# How to find the immediate container for each rectangle efficiently.

# Algorithm:
# - Sort all rectangles by increasing X1 (left edge).
# - Use a data structure that maintains the "active" possible parents, sorted by their Y intervals.

# As we sweep from left to right, when we encounter a new rectangle's left side, we query the smallest rectangle that contains its y-range.

# Since they are nested or disjoint, it works.

# We need a way to, for a given rectangle, find which one is the tightest that contains it.

# Let's define a way to compare which one contains another.

# Here is a working O(N log N) method using sorting and a Fenwick/segment tree for "has child".

# But perhaps overkill. Let's search for "count leaf rectangles in nested structure".

# Since it's a tree, number of leaves = (N + 1 - number of internal nodes with children), but not helpful.

# Note that every non-leaf has at least one child, so number of leaves = N - (number of non-leaves).

# Still need to find non-leaves.

# A rectangle is non-leaf if it contains at least one other.

# To check existence of contained rect.

# We can use 2D data structure: for each rect, store its (X1, Y1) or something.

# To check if a rect R contains any other S:
# exists S where X1_R < X1_S and X2_S < X2_R and Y2_R < Y2_S and Y1_S < Y1_R.

# So X1_S > X1_R, X2_S < X2_R, Y2_S > Y2_R, Y1_S < Y1_R.

# This is a 4-dimensional query.

# With N=1e5 we need coordinate compression and some offline processing.

# One standard way for offline containment counting is to sort by one dimension and use DS on others.

# Let's sort all rectangles by increasing X1.

# Then, as we process from left to right (increasing X1), the possible containers for current rect must have smaller X1 (already processed), and larger X2 and appropriate Y.

# But for a current S, its containers have X1 < X1_S and X2 > X2_S.

# So when processing S, not all possible containers are known if we go by X1, because a container with larger X1 cannot exist (since X1_container < X1_S to contain it).

# If A contains B then X1_A < X1_B < X2_B < X2_A, so indeed X1_A < X1_B, so containers have smaller X1.

# Perfect. So sort rectangles in increasing order of X1.

# We will process them from smallest X1 to largest (outer ones tend to have smaller X1).

# When we process a rectangle S, all possible containers have already been processed (smaller X1).

# Now, among the processed ones that have X2 > X2_S and Y1 > Y1_S and Y2 < Y2_S, we need to see if any such exists.

# But to mark that a container "has a child", we need to notify the containers that they have something inside.

# But since we only care if a rect has at least one inside, we can, when processing S, find the *immediate* container (the one with largest X1 or smallest area among those that contain it), and mark that immediate parent as having a child.

# But even if not immediate, any container would be marked, but since we only need existence, if I can mark all possible? Too many.

# We only need to mark that there is something inside, so if I can find at least one container for S, then all its containers actually have something inside, but I need to mark them.

# But that's not efficient.

# If a rect has a direct child, then it is non-leaf, and all its ancestors are also non-leaf.

# So the non-leaves are exactly the ancestors of all leaves.

# But to count leaves, perhaps it's easier to build the tree by finding parent of each, then count nodes with no children.

# Yes, and since it's a tree, we can do that.

# To find the parent of each rectangle (the innermost rectangle that contains it, or the direct container).

# The direct parent is the one that contains it and has no other between them.

# But for counting leaves we don't need direct, but to build adjacency list we need parents or children.

# To find for each rect its parent.

# When processing in order of increasing X1, for current S, we want to find the "active" container with the smallest X2 that is still > X2_S, or something? To get the tightest.

# We can maintain the currently "open" rectangles (processed but not yet "closed" by their X2), and keep their Y intervals in a way that we can query the smallest interval that contains the current Y interval of S.

# Yes, this is a classic technique for nested structures using a segment tree or a set of intervals.

# Since Y coordinates are up to 2*1e5 distinct after compression.

# Let's implement it.

# We will treat the rectangles as "events".

# But a proven method for building the containment tree for axis-aligned rectangles with no crossings is:

# 1. Collect all X coordinates, sort and compress.
# But perhaps:

# Let's sort the rectangles by their left X1 ascending. If X1 equal, put the one with smaller width first or handle ties carefully. But since no touch, X1 are distinct likely but not guaranteed.

# Coordinates can be same? Constraints don't say unique.

# But "Não há nenhum tipo de interseção entre os retângulos", so no overlapping or touching walls.

# So they are strictly nested or strictly disjoint.

# So if two have same X1, they cannot contain each other nor intersect, so they are disjoint in Y.

# To handle:

# We will create list of all rectangles with their index.

rect_list = []
for i in range(N):
    x1, y1, x2, y2 = rects[i]
    rect_list.append((x1, y2, y1, x2, i))  # x1, bottom, top, x2, idx

# Sort by x1 ascending, if tie by x2 ascending (smaller first, inner might have larger x1 but wait)
rect_list.sort()

# We will use a Fenwick or segment tree that stores, for Y, the "current active container" with the smallest x2 or something.

# To find if a rect is a leaf, we can count how many rects have children.

# Let's use a different approach that is simpler to code and works in O(N log N).

# We will process all rectangles sorted by increasing (X1), and use a set of active Y-intervals with their corresponding rectangle's "id" and X2.

# We maintain a set of candidate parents, ordered by their Y1 or use a tree map.

# A common way is to use a segment tree where each leaf is a Y coordinate (compressed), and we store in each segment the rectangle that "covers" that Y range with the current active innermost rectangle.

# When we "open" a rectangle (at its X1), we update the Y range [Y2, Y1] with the current rectangle id as the current container.

# But since we process by increasing X1, when we reach a new rectangle S, we can query what is the current container at some point inside S, say at its bottom or a representative Y.

# Since the active container at any Y is the innermost (most recent, smallest X1? No.

# Because we process by increasing X1, the latest one that covers a Y is the one with largest X1 (most inner so far).

# Yes! That's perfect.

# The most recently updated (largest X1) rectangle that covers a particular Y point is the innermost one containing that point.

# So, for a new rectangle S, if I query any point strictly inside S, say the midpoint of its Y or just query the min or max in its Y range, but to check if it is contained in some previous, I can query the current "owner" of its interior.

# If the current owner of its interior is some rectangle P, then P is the immediate container of S.

# Then we can set parent[S] = P, and we know P has a child.

# Yes!

# To detect leaves, we can have a has_child array, and when we assign a child to P, we mark has_child[P] = True.

# Then at the end, count how many have has_child False.

# The outermost has no parent, when we process it, there should be no previous owner.

# Yes.

# Now, to implement this we need a segment tree that can:
# - Update a range [Y2+eps, Y1-eps] with a new rectangle id (meaning this rect is now the innermost for that y range).
# - Query a single point or a range to get the current id.

# Since when we add a rectangle, it covers its entire interior, and because no intersections, the Y ranges of sibling rectangles don't overlap.

# So we can compress all Y coordinates.

all_y = set()
for r in rects:
    all_y.add(r[1])  # y1 top
    all_y.add(r[3])  # y2 bottom

y_list = sorted(all_y)
y_to_idx = {y: i+1 for i, y in enumerate(y_list)}  # 1-based for segtree
Y = len(y_list)

# Segment tree: each position will store the current innermost rectangle index.
# We need to support range update (set whole range to a value), and point query.

# Lazy propagation segment tree for range set update, point query.

class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [-1] * (4 * n)   # -1 means no container
        self.lazy = [-2] * (4 * n)   # -2 means no lazy

    def _push(self, node, start, end):
        if self.lazy[node] != -2:
            self.tree[node] = self.lazy[node]
            if start != end:
                self.lazy[2*node] = self.lazy[node]
                self.lazy[2*node+1] = self.lazy[node]
            self.lazy[node] = -2

    def update_range(self, node, start, end, l, r, val):
        self._push(node, start, end)
        if start > end or start > r or end < l:
            return
        if l <= start and end <= r:
            self.lazy[node] = val
            self._push(node, start, end)
            return
        mid = (start + end) // 2
        self.update_range(2*node, start, mid, l, r, val)
        self.update_range(2*node+1, mid+1, end, l, r, val)
        # Since it's set update, no need to combine tree[node]

    def query_point(self, node, start, end, idx):
        self._push(node, start, end)
        if start == end:
            return self.tree[node]
        mid = (start + end) // 2
        if idx <= mid:
            return self.query_point(2*node, start, mid, idx)
        else:
            return self.query_point(2*node+1, mid+1, end, idx)

# Note: because rectangles don't touch, we need to be careful with the Y indices.
# We will map the intervals to the discrete points between the Y lines.
# Since we only query inside, we can update from y_to_idx[y2]+1 to y_to_idx[y1]-1, assuming there are discrete y's inside.

# But if two y's are consecutive in sorted list with no other y between, then there might be no integer point between them.

# To handle this properly, we should compress the *gaps*.

# A better way: since we only care about the nesting, we can associate each possible "horizontal strip" .

# But to make it simple and correct, let's collect all unique Y, sort them.
# The possible "representative" points for a room are between its Y2 and Y1.

# For a rectangle with bottom y2, top y1, any y strictly >y2 and <y1 can be used.

# In discrete, after sorting y_list, for a rect, its y-range in compressed is from rank(y2) to rank(y1).

# We will make the segment tree on the *intervals* between the sorted y's.

# That is, there are Y-1 "atomic" horizontal slabs.

# We build segtree with Y-1 leaves, each representing the open interval (y_list[i], y_list[i+1]).

# Then, a rectangle covering from y2 to y1 will cover all slabs where the interval is strictly inside (y2, y1).

# So for a rect, left_idx = y_to_idx[y2]   # rank starting from 0 actually let's redefine.

y_coords = sorted(list(all_y))
m = len(y_coords)
# map y to rank 0 to m-1
y_rank = {y_coords[i]: i for i in range(m)}

# The atomic segments are 0 to m-2, representing space between y_coords[i] and y_coords[i+1]

# A rectangle with bottom=y2, top=y1 covers atomic segments j where y_coords[j] > y2 and y_coords[j+1] < y1.

# i.e. j where y_rank[y2] < j and j < y_rank[y1]-1 ? Let's say.

# rank_bottom = y_rank[y2]
# rank_top = y_rank[y1]
# Then it covers atomic slabs from rank_bottom to rank_top-2 inclusive? 

# The slabs j (between y_coords[j] and y_coords[j+1]) is inside the rect if y2 < y_coords[j] and y_coords[j+1] < y1.

# Since y_coords increasing, this is j > rank(y2) and j+1 < rank(y1), i.e. j >= rank(y2)+1 and j <= rank(y1)-2

# Yes.

# So if rank(y1) - rank(y2) <= 2, then there is no atomic slab strictly inside? But since no touching, if a rect exists, there should be space.

# But there might be no other y coords between y2 and y1, then rank(y1)-rank(y2)=1, then no j satisfying j>= r2+1 and j <= r1-2.

# This is a problem if there are no other horizontal lines inside a room.

# In that case, there is still "space" inside, but no discrete slab.

# To handle this, we need to always have at least one representative for each possible room.

# A simpler way is to use all the Y coordinates as points, but update the *closed*? But since walls don't touch, the y1 and y2 are unique? Not necessarily.

# Many rooms can share same y if they don't touch.

# This is getting complicated.

# Let's use a different strategy that is easier to implement correctly.

# Since N=1e5, but perhaps we can find all possible "parent" relationships in smart way.

# Another observation: because it's a tree, the number of leaves can be computed by counting how many rectangles are not the immediate container of any other.

# But let's look at the sample.

# A better and simpler way: we can model it as finding "maximal" elements under containment.

# The leaves are the minimal elements under the containment partial order (the ones that contain nothing).

# To count how many rectangles are minimal (not containing any other).

# To do this efficiently, we can use a data structure to keep track of "covered" areas or something.

# Let's try to implement using 2D structure for "is there any point inside".

# But since they are rectangles, we can add the "inner" rectangles as events.

# Here's a working method:

# We will sort all rectangles by their X1 ascending.

# We will maintain a set of "active" inner boundaries, but use a Fenwick tree or segtree on Y to keep track of whether a certain Y range has been "occupied" by an inner rectangle.

# Specifically:

# When we process a rectangle, we query if there is any previously placed inner rectangle whose entire body is inside this one.

# But it's tricky.

# Let's go back to the segment tree idea but fix the representative issue.

# Solution: instead of using gaps, we will add all four corners or use dynamic opening, but easier: since coordinates are large but we can compress all Y, and for each rectangle we will pick a representative Y that is unique to it or.

# Notice that because rectangles don't touch, for any rectangle, its (X1, Y1), (X1, Y2) etc are unique in some sense.

# A practical way that works: we can associate each rectangle with its bottom-left corner or a unique identifier inside it.

# Since no two rectangles touch or intersect, all the X and Y are such that we can pick for each rectangle a unique X and unique Y inside it that is not on any wall.

# But in code it's hard without discretization of all.

# Since we only need to know if a rectangle has something inside it, we can "place" a point inside each rectangle, for example at ( (x1+x2)/2 , (y1+y2)/2 ), but since coords are int, we can assume they are distinct.

# But in code we can't really place floating points.

# The containment of rectangles can be determined by checking if one point is inside another, but for counting we need data structure.

# Let's do the following: we will treat each rectangle as inserting its "presence" at its X2.

# Sort by X2 or use offline.

# Let's look for "minimum number of wifi antennas" or realize from the problem that the answer is the number of rooms that have no rooms inside them, i.e. the leaves.

# Yes.

# To count how many rectangles contain no other rectangles.

# So we need to find the number of rectangles that are "empty".

# To compute this, we can for each possible inner rect, "mark" its parent as having a child.

# So if we can find for each rect its immediate parent, then we can mark that parent.

# To find the immediate parent efficiently.

# The standard way is using a stack or a tree with y intervals.

# Let's implement an active set sorted by Y.

# We will process the rectangles in order of increasing X1.

# We will maintain a list or a balanced tree of "active" rectangles (those whose X2 has not been "passed" yet), but since we don't have sweep line on x, it's not.

# Since all X are different in practice, but to make it work we need a sweep line on X.

# Let's implement a sweep line.

# We will have vertical events at every X coordinate (all X1 and X2).

# But with 1e5 it's 2e5 events.

# At each X = X1 of a rect, we "open" the rectangle (add its Y interval).

# At X = X2 of a rect, we "close" it.

# To detect containment, it's a bit different.

# The containment tree can be built by maintaining the active Y-intervals in a way that they are nested.

# Since the family is laminar, the active Y intervals at any time are nested or disjoint.

# We can maintain a stack of active intervals.

# But perhaps for our purpose, we can do:

# Create events:
# - For each rect, an "open" event at x = X1, with its y1, y2, id, type=open
# - a "close" event at x = X2, with y1,y2, id, type=close

# Sort all events by x ascending. If same x, process opens before closes? But since no touching, X1 and X2 are all distinct across all.

# The problem says "paredes das salas não se tocam", so no two walls touch, so all X coordinates of vertical walls are distinct, same for horizontal? Anyway, all X1, X2 are distinct.

# So all 2N x-coords are unique.

# Sort events by x ascending.

# We will maintain a data structure for the "current active rooms" sorted by their Y interval.

# Specifically, we can use a sorted list or a balanced binary tree (in python we can use sortedcontainers or just since N large, better use a Fenwick for min or something).

# The idea is when we open a new room (at its left wall), we look for the smallest active room that contains this new room's Y interval. That will be its parent.

# Then we mark that parent as having a child.

# To do this, we need a way to query, given a [y2, y1], what is the active rectangle with the smallest height that completely contains [y2,y1].

# This requires an interval tree or a segment tree with min "size" or id.

# This is getting quite complex for a contest problem, although possible.

# Let's see the constraints again: N <= 10^5, so we need O(N log N).

# Let's think of the tree structure.

# Since one rectangle is the outermost, and others are inside.

# Let's assign each rect an index from 0 to N-1.

# To find which ones are leaves, i.e. which ones have no rect inside them.

# A rect i is not a leaf if there exists j such that rect i contains rect j.

# i contains j if x1i < x1j and x2j < x2i and y2i < y2j and y1j < y1i.

# To count the number of i that have no such j.

# This is equivalent to counting the number of i where there is no j "dominated" in 4 dimensions.

# This is a classic 4D dominance query, but we can reduce dimensions by sorting.

# Let's sort all rectangles by x1 ascending. As established earlier, if i contains j then x1i < x1j, so i appears before j in this order.

# So we process the rectangles from left to right (potential containers first).

# When we process a potential inner rect j, we want to query if there is any previous i with x2i > x2j, y2i < y2j, y1i > y1j.

# If yes, then j is contained in at least one, so the containers will have children.

# But we need to mark the containers as non-leaf.

# When we find that j is contained in some i's, we need to mark those i's as non-leaf.

# But which one? All of them, but we only need to mark that they have at least one.

# So we need a way to "tag" all possible containers of j as non-leaf.

# That is difficult.

# Instead, if we can find the *innermost* container of j (the one with the largest x1, or the most specific), then that innermost one definitely gets a child, and since ancestors also get it indirectly, but for our purpose since we only mark has_child, if I mark only the immediate parent, then the ancestors won't be marked yet.

# That won't work for has_child if I only mark immediate.

# If I only want the count of leaves, and leaves are those with has_child=False at the end, I must mark *all* ancestors as having child.

# So if I mark only the immediate, I need to propagate up the tree.

# So we need the tree anyway.

# So let's build the parent array.

# If when adding j, I can find its *immediate* container (the current innermost active container that contains its Y range), then I can set parent[j] = that_container, and later we can build the children list, and then count how many have 0 children.

# Yes, this works.

# To do this with segment tree, we can have a segment tree on compressed Y, and store in each range the *current innermost* rectangle that covers that Y range.

# When we "open" a rectangle, we update its entire Y range with its own id, meaning now the innermost for that range is this rect.

# When we query for a new rect, before updating, we query what is the current innermost in its interior Y range. That will be its parent.

# Then we update the range with the new id.

# The key is: we must process in order of increasing X1, and we must make sure that we only query after all possible outer have been opened, which is guaranteed.

# But when do we close them? In this approach, we never close because once a rectangle is opened, as we move right, its "innermost" status remains until a inner one is opened inside it.

# Since we only open and never have to remove because X2 is larger, when we reach an inner one, its X1 is larger, so we are to the right, but the outer is still "active" because its X2 is even larger.

# The order we open them is by X1, and an outer has smaller X1 so opened before, and when we open an inner, the outer is already in the segtree covering a large range, and the query for the inner will return the outer (or a more inner one if there are multiple levels).

# If there is already a more inner one opened before (with X1 between the outer and current), then it would have updated the range.

# But since if there was one in between, it would be the immediate.

# Yes, it works because of the nesting property: you cannot have overlapping Y ranges that are not nested.

# So the active updates are always proper.

# Now, about the discrete Y: since we update the *range* corresponding to the interior, we need to have enough resolution.

# Let's make the segment tree on all unique Y coordinates, but update from rank(y2) to rank(y1), but query a point that is strictly inside.

# To make it work even if no y coords inside, we can query the rank of y2 + 1 or something, but since it's discrete, let's add a little trick.

# We will compress all Y, but the segment tree will be on 0 to m-1, representing the Y coords themselves.

# But since walls don't touch, no two rectangles share the same horizontal wall, so all y1 and y2 are unique! Is that true?

# The problem says "As paredes das salas não se tocam." which means the walls do not touch each other.

# So no two walls share any segment, so all horizontal wall y-coordinates may be shared only if their x-ranges don't touch, but actually y can be same if they are at same height but separated in x.

# For example two rooms side by side can have same top y.

# So y1 can be same for different rects.

# So y_coords can repeat but set removes duplicates.

# For a room, to query if it has something inside, but for parent finding, if I update the points from rank(y2) to rank(y1), including the boundaries, it might be incorrect if another room has same y.

# But because they don't touch, if two rooms have same y1, their x ranges don't cause issue.

# To make it safe, let's do the following:

# We will use the segment tree on the sorted unique Y, with size m.

# For a rectangle with y2, y1, we will update the range rank(y2)+1 to rank(y1)-1 with the id.

# This represents the strict interior Y values.

# Then, to query the parent of a new rectangle, we need to query if there is any value in rank(y2)+1 to rank(y1)-1.

# If the range is empty (rank(y1)-rank(y2) < 2), then this room has no interior points in the discrete set, meaning no other wall inside it in Y, so it can only contain rectangles that have no horizontal walls inside either.

# If there is a rectangle inside it, that inner one would have its own y1,y2 strictly between, so it would have added its own y's to the set.

# Important: if there is any rectangle inside, its y1 and y2 are strictly between the outer's y2 and y1, so they are in the all_y set, and rank(y2_outer) < rank(y2_inner) < rank(y1_inner) < rank(y1_outer), so there are at least the inner's y's in between, so the range rank(y2)+1 to rank(y1)-1 will include at least rank of inner y2 and y1.

# So if there is any inner rect, there will be at least 2 discrete Y points strictly inside, so the update range will be non-empty.

# If a rect has no inner rect, then there might be no Y coords between its y2 and y1, so rank(y1) = rank(y2) + 1, then the update range rank(y2)+1 to rank(y1)-1 = r+1 to r is empty.

# In that case, for query, if the range to query is empty, then it has no parent? No, it must have a parent unless it is the outermost.

# For the outermost, its range will include all other y's.

# For a leaf rect with no other y coords between its y2 and y1, its query range is empty.

# So we cannot query an empty range.

# This is the problem.

# To fix this, we need to have at least one representative "slot" for every possible rectangle, even if no other lines inside it.

# One way is to associate each rectangle with a unique "id" or a unique position in Y for its "body".

# We can add, for each rectangle, two special Y values: its own "center" or just make sure every interval has a private leaf.

# A simple fix: we can make the segment tree leaves correspond to the rectangles themselves, but that is not straightforward.

# Another way: we can assign each rectangle a unique "probe point" in Y, for example we can sort the Y and also include "mid" points conceptually by making the ranks have enough space.

# Here's a good fix: instead of compressing only the existing Y, we can give each rectangle its own representative Y value that is guaranteed to be inside it and not on any wall.

# For example, we can collect all Y, but for each rect we can use a Y = (y1 + y2) / 2 but since we need integer for map, it's not good for segment tree.

# We can discretize by ranking all the boundary Y, but for each rect, we will query a specific location that is "owned" by it.

# Perhaps a different approach.

# Let's assign each rectangle a unique id from 0 to N-1, and we will use a map from Y to active rect, but since Y is 1e9 we can't.

# Since N=1e5, we can use a dynamic segment tree or just use a set of active intervals.

# Since the active Y intervals are laminar (nested or disjoint), we can maintain a sorted list or a tree of the current active Y segments, each associated with the rect that owns it.

# We can use a python dict or better, use a sorted list of active "boundaries".

# But in python, with N=1e5, we need log^2 or better.

# Let's use a Fenwick tree for "last update" with coordinate compression on all Y.

# Let's solve the empty range problem.

# Solution: we will add, for every rectangle, its "own" Y representative as y2 + 1 or something, but since coords are up to 1e9, we can create a list of all relevant Y for discretization including a unique probe for each rect.

# Specifically:

# - Collect all y1 and y2.
# - For each rect, add a unique probe y = y2 + (y1 - y2) // 2 + 1 or just add a distinct value for each, but to keep order, we need to insert a unique value between y2 and y1 for each rect.

# But to do it, we can collect all y1, y2, and also for each rect add a probe value like a tuple (y, type, rect_id) but it's complicated.

# Since we only use the ranks for range, we can create a list of events for Y.

# Let's do this: we will create a list of all unique Y from y1 and y2.

# Then sort them.

# Then, for the segment tree, we will build it with 2*m leaves or something.

# A simple and common trick is to map each possible "open interval" between sorted y's to a leaf, and also map the points themselves if needed.

# But for each rectangle, its "interior" will cover at least the open intervals inside it.

# For a leaf rectangle with no other y coords inside, its interior still has open intervals between its y2 and y1.

# So if I make the segment tree on the *gaps*, i.e. m-1 leaves, then for a rect with rank_bottom = r2, rank_top = r1, it covers gaps r2 to r1-1 (the gaps from after y[r2] to before y[r1]).

# The gaps index from 0 to m-2.

# Then, to update a rect, we update the gap range from r2 to r1-2 (0-based gaps).

# Gap k is between y_coords[k] and y_coords[k+1].

# This gap is inside the rect if y2 < y_coords[k] and y_coords[k+1] < y1, i.e. k >= r2 and k < r1-1, i.e. from r2 to r1-2 inclusive.

# If r1 = r2 + 1, then from r2 to r2-1 which is empty.

# So for leaf rooms that have no other Y coords inside their Y range, the range is empty, so we cannot update or query them.

# This happens when a room has no other room's wall inside its Y range.

# In that case, to represent that there is "space" for that room, we need to have a representative for that room even if no other lines.

# One way is to, for each rectangle, introduce a unique "private" Y coordinate inside it, guaranteed to be between its y2 and y1 and not equal to any other.

# Since all y are integers, we can, but to keep the order, we can collect triples: for boundaries we have (y, 0, id), for probes we have (y_probe, 1, id) where y_probe = y2 + 1 if possible, but to avoid collision we can use a list and sort all.

# But since we only need relative order, we can create a list of all Y events:

all_y_events = []
for i, (x1, y1, x2, y2) in enumerate(rects):
    all_y_events.append((y2, 0, 0, i))   # bottom wall, type 0
    all_y_events.append((y1, 0, 2, i))   # top wall, type 2
    # add a probe point strictly inside
    probe = y2 + 1 if y1 > y2 + 1 else (y2 + y1) // 2   # safe since y1 > y2
    all_y_events.append((probe, 1, 1, i))  # probe, type 1

# Then sort by y, then by type so that bottom < probe < top
all_y_events.sort()

# Now create a mapping from each unique position to a dense index, but only the probes and walls get indices.

y_compressed = []
last = None
for event in all_y_events:
    y = event[0]
    if y != last:
        y_compressed.append(y)
        last = y

# But this may still have duplicate if probes collide, but unlikely but to make unique per probe we can make probe depend on id.

# This is messy because y are up to 1e9, adding 1 may collide with other walls.

# To avoid any collision, we can discretize without using actual values, by sorting all the boundary and probe events with proper ordering.

# We don't need the actual y values, we need the order.

# So let's create a list of all "points" with their type.

# We will have a list of tuples: (y, type, rect_id)
# Where type = 0 for bottom, type = 1 for probe, type = 2 for top.

# Then sort by y ascending, if y equal, bottoms first (0), then probes (1), then tops (2).

# This way even if y values are same, the order is maintained correctly for containment (a bottom cannot be at same y as another's probe if they don't touch).

# But if two different y's are equal, the sort will put them together but with type.

# Then we can assign dense ranks to *only the probe points*, or to all.

# For the segment tree, we only need leaves for the probe points, because the probes are guaranteed to be strictly inside their own rectangle and no wall on them.

# So each rectangle has exactly one unique probe point that lies strictly inside it.

# Then, the segment tree can be built on these N probe points, sorted by their Y.

# But to do range update, we need that the probes of inner rectangles have Y between the y2 and y1 of outer.

# So if I sort all the probe points by their Y value, then for a rectangle, its range in the probe-sorted list is all probes with Y > y2 and Y < y1.

# To update a range, I need to update all probes that are inside this rect.

# But that's not what we want for the "current owner".

# The idea of the segment tree is to have the Y space discretized by all relevant points (probes), and the current owner is written on the probes that are inside the current rect.

# When I open a rect, I update all the probe points that are strictly inside it with my id.

# Then, when I want to know the parent of a new rect S, I can query any probe point that is inside S; the current owner of that probe will be the innermost rect that contains that probe, hence contains S (since the probe is inside S).

# Yes! Perfect.

# And since each rect has its own probe inside it, when we process S, we can query the owner of *its own probe*.

# That is brilliant and solves all issues.

# So let's implement that.

# Step 1: for each rect, choose a probe Y that is strictly between y2 and y1.
# Since y are integers from -1e9 to 1e9, we can safely choose probe_y = y2 + (y1 - y2) // 2 + (1 if (y1 - y2) % 2 == 0 else 0) or simply y2 + 1 if y1 > y2+1 else y2 + 0.5 but since we only compare, we can use fractions or just use a pair (y, offset).

# To make it simple in code, we will create a list of all "Y events" for sorting:

events_for_y = []
for i in range(N):
    x1, y1, x2, y2 = rects[i]
    events_for_y.append((y2, 0, i))   # 0 = bottom
    events_for_y.append((y1, 2, i))   # 2 = top
    # probe with type 1
    events_for_y.append((y2, 1, i))   # use same y as bottom but type 1, but to make it > bottom, we will sort properly

# To ensure probe is > y2 and < y1, we will use a tuple (y, type, i) where type for bottom=0, probe=1, top=2, and for probe we use the average or we can use a secondary key.

# If I put the probe as (y2, 1, i), when sorting by (y, type), the bottom (y2,0,i) comes before probe (y2,1,i), then top is at y1 > y2.

# But is the probe at "y2" but after bottom, so any comparison " > y2 " will include it.

# For an outer rect with smaller y2, it will contain this probe if its y2 < y2_inner and its y1 > y1_inner.

# Since the probe has y=y2_inner, and outer y2 < y2_inner, so y2_outer < probe_y = y2_inner < y1_inner < y1_outer, yes it is inside.

# For the rect itself, its bottom is = probe_y, but since we query after, and we consider strict > y2.

# But in practice for the ordering it works as long as we are consistent.

# Let's define the sort key as (y, type, i), with type 0=bottom, 1=probe, 2=top.

# So for a single rect, bottom comes first, then its probe at same y, then when y increases to y1 the top.

# Now, to assign ranks only to the probes.

probe_rank = [-1] * N
sorted_events = sorted(events_for_y, key=lambda e: (e[0], e[1], e[2]))
rank_counter = 0
for event in sorted_events:
    y, typ, idx = event
    if typ == 1:  # probe
        probe_rank[idx] = rank_counter
        rank_counter += 1

# Now we have N unique ranks from 0 to N-1 for the probes, sorted by their effective Y position.

# The segment tree will have N leaves, each corresponding to one probe.

# When we open rectangle i, we need to update all probes that are strictly inside i, i.e. whose probe_y > y2 and probe_y < y1.

# But to do that in range, the probe_rank is already sorted by that order, so the probes inside i are a consecutive range in the probe_rank?

# Is it consecutive?

# Yes, because the sorting is by increasing y, so all probes with y in (y2, y1) will be between the first probe >y2 and last <y1, and since they are sorted, yes it's a consecutive range in the sorted probe list.

# But to find the left and right of the range for a particular rect, we need to know the lowest rank where the probe is > y2 and < y1.

# So we need to find the smallest rank whose corresponding probe y > y2, and the largest whose probe y < y1.

# This requires either having the sorted probe list with their y, or binary search.

# So let's create a list of probes: for each rect its (probe_y, probe_rank, rect_id)

# Since we used (y2,1) for probe, the effective probe y is y2 for all, but that is wrong because all probes would have same y as their bottom, so ordering between different rects at same y2 would be by id, which is arbitrary and wrong.

# This breaks the ordering.

# Example: if one rect has y2=0, y1=10, another has y2=5, y1=6, then the probe for first should be say at 5, second at 5.5.

# If I set probe for first as (0,1), it would come before the second's bottom at (5,0).

# So the order would be wrong.

# To fix, we must choose a probe y that is strictly greater than y2 and less than y1, and different from all other y's if possible.

# Since y are integers, for probe we can use y = y2 + 1, but to avoid collision with other y= y2+1 that might be a wall of another, we can use a very fine resolution by using tuples.

# Let's represent every Y position as a tuple.

# We will not use integer y for sorting, but create custom events with proper ordering.

# All events are of three types for each rect:
# 1. Bottom of rect i: position = y2, type='bottom', rect=i
# 2. Probe of rect i: position = (y2 + y1) / 2.0 , type='probe', rect=i
# 3. Top of rect i: position = y1, type='top', rect=i

# Then we sort all these 3N events by their position (float is ok in python for sorting since no precision issue as all are integers or .5).

# Since all original y are integers, (y2+y1)//2 is integer or .5, and since y1 > y2, and integers, it will be strictly between.

# And since no walls at .5, and different rects if have same average it doesn't matter as long as consistent, but if two probes have same position it is ok for sorting as we can break ties by type or id.

# But in practice for containment, if two probes have same y it means their y ranges overlap in a way, but since no intersection it should not happen or it's fine.

# Let's do it with floats for sorting.

probes = [0] * N
events = []
for i in range(N):
    x1, y1, x2, y2 = rects[i]
    events.append((y2, 0, i))      # 0 = bottom
    mid = (y2 + y1) / 2
    events.append((mid, 1, i))     # 1 = probe
    events.append((y1, 2, i))      # 2 = top
    probes[i] = mid

events.sort(key=lambda e: (e[0], e[1], e[2]))  # sort by pos, then type, then rect id

# Now assign ranks to probes only
probe_to_rank = [-1] * N
r = 0
for pos, typ, idx in events:
    if typ == 1:
        probe_to_rank[idx] = r
        r += 1

# Now probe_to_rank[idx] is the leaf in segtree for that rect's probe, from 0 to N-1, sorted by increasing Y.

# For a given rectangle i, to update all probes inside it, we need the range of ranks where the probe's pos is > rect.y2 and < rect.y1.

# Since the events are sorted, the probes inside will be consecutive in the rank.

# To find the leftmost rank where probe pos > y2, and rightmost where probe pos < y1.

# We can precompute for each rect the range [L, R] such that all probes with rank in [L, R] are inside the rect.

# How? We can, while having the sorted events, but for each rect we can binary search the first and last.

# Since N=1e5, we can precompute the L and R for each rect by binary search on the sorted probe list.

# First let's create a list of the probe positions in sorted order.

sorted_probe_pos = [0.0] * N
sorted_probe_id = [0] * N
idx = 0
for pos, typ, rid in events:
    if typ == 1:
        sorted_probe_pos[idx] = pos
        sorted_probe_id[idx] = rid
        idx += 1

# Now for each rectangle i, we can binary search the lowest index L such that sorted_probe_pos[L] > rects[i][3] (y2)
# and the highest index R such that sorted_probe_pos[R] < rects[i][1] (y1), then the range is L to R inclusive.

# If no such, then L > R.

# Since every rect has its own probe inside it, for itself, there will be at least its own probe in that range.

from bisect import bisect_left, bisect_right

def get_update_range(i):
    y2 = rects[i][3]
    y1 = rects[i][1]
    # first probe with pos > y2
    L = bisect_left(sorted_probe_pos, y2 + 1e-9)
    # first probe with pos >= y1 , so < y1 is before it
    R = bisect_left(sorted_probe_pos, y1 - 1e-9) - 1
    return L, R

# Yes! bisect_left on the sorted_probe_pos.

# Now we can create for each rect its update_L, update_R
update_ranges = [get_update_range(i) for i in range(N)]

# Now, the segtree will be on 0 to N-1 (probe ranks)

# Each leaf corresponds to a probe of some rect.

# The value in the segtree will be the id of the innermost rectangle covering that probe.

tree = SegTree(N)

# We need to process the rects in order of increasing X1
order = list(range(N))
order.sort(key=lambda k: rects[k][0])

has_child = [False] * N

for k in order:  # process in increasing X1
    L, R = update_ranges[k]
    if L > R:
        # no space, should not happen
        parent = -1
    else:
        # query any point in [L, R], say L
        parent = tree.query_point(1, 0, N-1, L)
    if parent != -1:
        has_child[parent] = True
    # now update the range with our own id
    if L <= R:
        tree.update_range(1, 0, N-1, L, R, k)

# Now, the outermost should have parent = -1, and if it has children, has_child will be set.

# Finally, the number of leaves is the number of rects with has_child[i] == False

ans = sum(1 for b in has_child if not b)
print(ans)

# Let's check with the sample.

# Sample 1:
# rect 0: 5 19 8 17   y2=17, y1=19
# rect 1: 5 15 15 5    y2=5, y1=15
# rect 2: 0 20 20 0    y2=0, y1=20
# rect 3: 8 10 10 8    y2=8, y1=10

# Outermost is 2.

# Probes:
# rect0 probe ~18
# rect1 probe ~10
# rect2 probe ~10
# rect3 probe ~9

# y values: bottoms 17,5,0,8 ; tops 19,15,20,10 ; probes ~18,10,10,9

# Sorted positions approx: 0(bottom2), 5(b1), 8(b3), 9(p3), 10(p1 and p2?), 15(t1), 17(b0), 18(p0), 19(t0), 20(t2)

# So sorted probes order: p3(~9), p1(~10), p2(~10), p0(~18)

# Assume order p3, p1, p2, p0 or depending on exact mid and tie break.

# For rect2 (outer y2=0 y1=20), L=0, R=3, covers all probes.

# For rect1 (y2=5 y1=15), probes >5 and <15: p3(9), p1(10). p2 is at 10 but p2 is the outer's probe at 10, but 10<15 yes.

# Outer probe at (0+20)/2 = 10, rect1 probe at (5+15)/2=10, same.

# So same position, but in sorting we have tie broken by type then id.

# But in any case, for rect1, probes inside it should be only those with y in (5,15), so p3(~9) is inside rect1? Let's see if rect1 contains rect3.

# rect1: x 5 to 15, y 5 to 15
# rect3: x 8 to 10, y 8 to 10 -> yes, 5<8<10<15 and 5<8<10<15 yes.

# rect2 contains all.

# rect0: x5-8 y17-19, which is above, y from 17 to 19, not inside rect1 (which only to 15).

# So probes: p3 is inside rect1 and rect2.
# p0 is inside rect2 only.
# p1 (rect1's own probe at 10) is inside rect2 and inside itself? But when querying we query before update.

# p2 at 10 is inside rect2, is it inside rect1? 10 is =10, but since mid of outer is 10, and rect1 y1=15 >10, y2=5<10, yes 10 is inside rect1 too.

# So it works.

# When processing in order of X1:
# rect2 has X1=0, first.
# L,R for it = all 0-3, query on empty segtree -> -1, no parent, then update all 0-3 with id=2.

# Next, rect0 and rect1 have X1=5, rect3 has X1=8.

# Assume we process rect0 (id0) and rect1(id1), order between them depends on index or we sorted by x1 only, if same x1 we need stable or add tie breaker.

# In code above, order = list(range(N)); order.sort(key=lambda k: rects[k][0])

# If X1 same, smaller index first.

# So id0 then id1 (both X1=5), then id3 (X1=8).

# First id=0, rect0: y2=17, y1=19, so probes >17 and <19: p0(~18). So L and R only the last rank (3).

# Query at that position: currently it is 2 (outer), so parent=2, has_child[2] = True.
# Then update that position (rank 3) with 0.

# Next id=1, rect1 y2=5 y1=15, probes >5 <15: p3(9), p1(10), p2(10). Assume ranks 0,1,2.
# Query say at rank 0 (p3), current value is 2, so parent=2, has_child[2]=True.
# Then update ranks 0,1,2 with id=1.

# Note that p2 was updated to 1, but p2 is outer's probe at 10, which is inside rect1, yes correct because rect1 is inside outer.

# Next, id=3, X1=8, y2=8 y1=10, probes >8 <10 : p3(~9), rank 0.
# Query rank 0: now it has been updated by rect1 to 1.
# So parent = 1, has_child[1] = True.
# Then update rank 0 with 3.

# Now has_child: index 0: False, 1: True (has 3), 2: True (has 0 and 1), 3: False.

# So has_child False for 0 and 3, i.e. 2 leaves. Perfect! Matches sample.

# Excellent.

# Now let's check if there was a probe for outer that got updated by inner: yes p2 got updated to 1, but when we queried for others it was before or after correctly.

# When we queried for rect0 at its probe rank 3, it was still 2, because rect1 updated only 0-2, not 3. Perfect, because rank 3 is at 18, which is not inside rect1 (15).

# Yes!

# This works.

# If two probes have exactly same pos, in this case p1 and p2 both at 10.0, in sorted_probe_pos they will be in order of when we added in events.sort, which depends on rect id in tie breaker.

# But in bisect it uses the pos, so as long as we use > y2 and < y1 with epsilon it should be fine.

# In the get_update_range, since we use bisect_left with y2 + 1e-9 and y1 - 1e-9, for y2=5, >5.000... will include 9,10,10,18? No for this rect y1=15, <15-eps will include up to 10 but not 18.

# Yes.

# For rect0 y1=19 y2=17, >17 will get the 18, <19 gets it.

# Perfect.

# Now for the outermost in single rect case, it will query -1, has_child false, ans=1. Good.

# This should work.

# We need to implement the SegTree carefully.

# In the SegTree, since it's range assign (set update), and query point, the code I wrote earlier with tree[node] = val when pushing is correct for set.

# In the __init__ we have tree = [-1]* (4*N), lazy=[-2]*(4*N)

# In _push, if lazy != -2, set tree[node] = lazy, and if not leaf propagate to children, then reset lazy.

# In update, if fully covered, set lazy and push immediately.

# In query, always push down.

# Yes, it should work even though we don't maintain min or sum, just the set value, so when we set a range, the tree[node] represents the set value if the whole segment is set to same.

# Yes, this is standard lazy set update for assignment.

# One small fix: in the _push, if we set tree[node] = lazy[node], but if the node represents a range, and we have set it, it's ok because when we query we will push all the way.

# Yes.

# Let's write the code.

# Also, in case L > R, for outermost it is not, since it covers its own probe.

# In single rect, L to R includes its own probe, query gets -1, good. Then update with its id, but no more.

# Perfect.

# Now, if two rects are disjoint in Y but same X1 order, it works because their probe ranges don't overlap.

# Yes.

# This solves the problem.

# Let's handle the case where y1 - y2 == 1, mid = y2 + 0.5, and no other integer there, but since we use float in sorting it's fine, and bisect uses the float values.

# Yes.

# In python bisect on list of floats is fine.

# Now, to make it fully integer, we could have used (2*y) to avoid floats, but floats are safe here because all operations are simple averages of ints.

# Since all y are int, mid = (y1 + y2)/2 is either int or x.5, and different rects having same mid is ok.

# Yes.

# Let's write the full code.

import sys
from bisect import bisect_left

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1
rects = []
for i in range(N):
    x1 = int(data[index])
    y1 = int(data[index+1])
    x2 = int(data[index+2])
    y2 = int(data[index+3])
    rects.append((x1, y1, x2, y2))
    index += 4

if N == 0:
    print(0)
    sys.exit()

# events for y sorting: (pos, type, rect_id)
events = []
for i in range(N):
    y1 = rects[i][1]
    y2 = rects[i][3]
    events.append((y2, 0, i))        # bottom
    events.append(((y1 + y2) / 2, 1, i))  # probe
    events.append((y1, 2, i))        # top

events.sort(key=lambda x: (x[0], x[1], x[2]))

# build sorted_probe_pos and probe_to_rank
sorted_probe_pos = []
probe_id_from_rank = []
probe_rank = [-1] * N
r = 0
for pos, t, iid in events:
    if t == 1:
        sorted_probe_pos.append(pos)
        probe_id_from_rank.append(iid)
        probe_rank[iid] = r
        r += 1

# precompute update ranges for each rect
update_ranges = []
for i in range(N):
    y2 = rects[i][3]
    y1 = rects[i][1]
    # L = first index where sorted_probe_pos[L] > y2
    L = bisect_left(sorted_probe_pos, y2 + 1e-9)
    # R = last index where sorted_probe_pos[R] < y1
    R = bisect_left(sorted_probe_pos, y1 - 1e-9) - 1
    update_ranges.append((L, R))

class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [-1] * (4 * n)
        self.lazy = [-2] * (4 * n)

    def _push(self, node, start, end):
        if self.lazy[node] != -2:
            self.tree[node] = self.lazy[node]
            if start != end:
                self.lazy[node*2] = self.lazy[node]
                self.lazy[node*2+1] = self.lazy[node]
            self.lazy[node] = -2

    def update_range(self, node, start, end, l, r, val):
        self._push(node, start, end)
        if start > end or start > r or end < l:
            return
        if l <= start and end <= r:
            self.lazy[node] = val
            self._push(node, start, end)
            return
        mid = (start + end) // 2
        self.update_range(node*2, start, mid, l, r, val)
        self.update_range(node*2+1, mid+1, end, l, r, val)
        # no need to pull since it's assignment only

    def query_point(self, node, start, end, idx):
        self._push(node, start, end)
        if start == end:
            return self.tree[node]
        mid = (start + end) // 2
        if idx <= mid:
            return self.query_point(node*2, start, mid, idx)
        else:
            return self.query_point(node*2+1, mid+1, end, idx)

if N == 1:
    print(1)
    sys.exit()

st = SegTree(N)
order = list(range(N))
order.sort(key=lambda i: rects[i][0])

has_child = [False] * N

for i in order:
    L, R = update_ranges[i]
    if L <= R:
        # query its own probe or any in range, use the probe of this rect
        my_probe_rk = probe_rank[i]
        # but only if my_probe_rk is in [L,R], it should be
        parent = st.query_point(1, 0, N-1, my_probe_rk)
        if parent != -1:
            has_child[parent] = True
        st.update_range(1, 0, N-1, L, R, i)

ans = sum(not h for h in has_child)
print(ans)
```

This code correctly computes the number of leaf rectangles in the containment tree, which is the minimum number of antennas needed. It uses a segment tree with lazy propagation for range assignment and a discretization of probe points inside each rectangle to handle the nesting queries efficiently in O(N log N) ti