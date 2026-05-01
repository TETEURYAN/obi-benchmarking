
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

# Build containment tree using adjacency list (parent -> children)
children = [[] for _ in range(N)]
parent = [-1] * N

def contains(i, j):
    r1 = rects[i]
    r2 = rects[j]
    return r1[0] <= r2[0] and r1[2] >= r2[2] and r1[3] <= r2[3] and r1[1] >= r2[1]

for i in range(N):
    for j in range(N):
        if i != j and contains(i, j):
            if parent[j] == -1 or contains(i, parent[j]):
                parent[j] = i

for i in range(N):
    if parent[i] != -1:
        children[parent[i]].append(i)

# Now we need to compute for each subtree the minimum antennas
# Each node can be covered by an antenna inside it or from its parent (outside)
# But signal from outside cannot enter, so if a node places an antenna, it covers itself and all descendants
# If not, each child must be covered independently (by their own subtrees)

# We will use tree DP
# dp[u][0]: min antennas in subtree u, without placing antenna in u (so all children must cover themselves)
# dp[u][1]: min antennas in subtree u, placing antenna in u (covers u and all descendants, so 1 + 0 for children)

INF = 10**9
dp = [[INF, INF] for _ in range(N)]

def dfs(u):
    # If leaf
    dp[u][1] = 1
    if not children[u]:
        dp[u][0] = 0  # can be covered by parent
        return
    
    sum_child_0 = 0
    sum_child_1 = 0
    must_place = False
    for v in children[u]:
        dfs(v)
        sum_child_0 += dp[v][0]
        sum_child_1 += dp[v][1]
    
    # If we place antenna in u, it covers everything, children don't need to place anything
    dp[u][1] = 1
    
    # If we don't place in u, then each child must be covered by their own subtree (dp[v][1] or dp[v][0] if they can be covered by u, but since u doesn't place, they can't)
    # Since signal from u (outside child) cannot enter child, if u does not place antenna, each child must place at least one in its own subtree.
    # So dp[u][0] = sum over children of min antennas needed in child's subtree when child is not covered from outside, i.e. must cover itself.
    # For a child v, to cover v's region, since u doesn't place, v must have an antenna inside its own "influence", meaning we must take dp[v][1] ? No.
    
    # Let's rethink.
    
    # An antenna placed in a room u covers:
    # - The entire room u
    # - All rooms inside u (recursively), because from inside to outside is allowed? Wait, let's read the problem again.
    
    # "o sinal wifi é capaz de atravessar as paredes quando vem de dentro para fora, mas estranhamente não atravessa as paredes quando vem de fora para dentro das salas"
    
    # So signal goes from inside a room to outside, but not from outside to inside.
    
    # That means:
    # - If you place an antenna inside a room, the signal will fill that room and all outer rooms (because it can go out), but cannot go into inner rooms? Wait, that seems opposite of intuition.
    
    # Let's look at the description carefully.
    
    # "o sinal wifi é capaz de atravessar as paredes quando vem de dentro para fora, mas estranhamente não atravessa as paredes quando vem de fora para dentro das salas"
    
    # So if the antenna is inside a room, the signal can go out through the walls to the outer area.
    # But if the antenna is in the outer area, it cannot go into the inner room.
    
    # So an antenna placed in a room covers:
    # - Its own room
    # - All outer regions (the "outside" of this room)
    # - But does NOT cover any inner rooms (nested inside it).
    
    # But the figure is not shown, but from the description: "a figura mostra duas posições possíveis para uma antena, mostrada como um círculo, e a área que o respectivo sinal wifi da antena alcançaria."
    
    # Since we have test cases, let's use them to understand.
    
    # First test case:
    # 4 rectangles:
    # A: 5 19 8 17
    # B: 5 15 15 5
    # C: 0 20 20 0   <-- this is the outer one
    # D: 8 10 10 8
    
    # So C contains all.
    # B is inside C, A is inside B? Let's see coordinates.
    # C: x 0-20, y 0-20 (note Y1=20 > Y2=0)
    # B: x 5-15, y 5-15
    # A: x 5-8, y 17-19  --> this is in the top part of B? B goes up to y=15, A is from y=17 to 19, so A is inside C but not inside B.
    # D: x 8-10, y 8-10, clearly inside B.
    
    # So nesting:
    # C contains A, B, D
    # B contains D
    # A and D are leaves.
    
    # Output is 2.
    
    # If we place one antenna in the outermost room C, since it's inside C, signal can go out, but there's no "out" of the museum. But can it cover the inner rooms? According to the rule, from inside C it should be able to go into... wait the rule is about crossing walls from inside to outside.
    
    # The walls block signal from outside to inside, but allow from inside to outside.
    
    # So if antenna is in the outermost room (between C and B), the signal is inside C but outside B. To reach inside B, it would have to cross B's wall from outside to inside, which is blocked.
    
    # So antenna in outer region cannot cover inner rooms.
    
    # If I place antenna inside an inner room, say inside B, then it can cover all of B, and since it can go out of B into the outer region (C - B), and from there it can cover the outer area.
    
    # So an antenna placed in a room covers that room and ALL outer regions, but not sibling rooms or other branches.
    
    # In other words, an antenna placed in a leaf room will cover the entire path from that leaf to the outermost room.
    
    # This sounds like covering a tree where we need to cover all nodes, and placing an antenna at a node covers the path from that node to the root.
    
    # Yes, this is a classic "minimum number of nodes to select so that every node is covered by at least one selected node on its path to root".
    
    # In tree terms, it's the minimum number of vertices such that every vertex has a selected vertex in its subtree or on the path to root? Let's formalize.
    
    # Each room corresponds to a node in the containment tree.
    # The outermost room is the root.
    # Placing an antenna in a room u covers u and all its ancestors (outer rooms).
    
    # We need to cover all rooms.
    
    # So we need to select a set of nodes such that for every node v, there is a selected node in the subtree of v (including v).
    
    # Yes! Because if I select a descendant of v (or v itself), then that antenna is inside v or deeper, so it can propagate out through v.
    
    # If I select an ancestor of v, that antenna is outside v, so it cannot enter v.
    
    # Therefore, to cover v, we must have at least one antenna in the subtree rooted at v (including v).
    
    # And we want the minimum number of such antennas.
    
    # This is exactly the minimum number of nodes to select in a tree such that every subtree has at least one selected node in it? No.
    
    # The condition is: for every node v, the subtree of v must contain at least one selected node.
    
    # Yes, that's exactly it.
    
    # This is a well-known problem: it's equivalent to finding the minimum number of nodes to select so that there is no "empty" subtree.
    
    # Actually, there's a simple greedy way: we can do a DFS and count how many "necessary" placements we need.
    
    # A standard way is to realize that we should place an antenna only at nodes that are not covered by any descendant.
    
    # We can traverse bottom-up.
    # For each subtree, we need to ensure it has at least one antenna.
    # The optimal is to place as deep as possible.
    
    # Let's define for each subtree u:
    # We must place at least one antenna in u's subtree.
    # To minimize total, we can decide whether to place at u or not.
    
    # But a better observation: this is equivalent to finding the number of nodes that have no selected descendant, but we need global minimum.
    
    # Actually there is a simple formula: the minimum number is the number of "maximal" rooms that are not contained in any other selected... but let's think differently.
    
    # Notice that if I select a node, it satisfies the condition for all its ancestors.
    # So selecting a leaf satisfies its entire path to root.
    
    # The condition "every subtree must contain at least one selected node" means that there cannot be any node with no selected nodes in its subtree.
    
    # This is equivalent to saying that the selected nodes form a "vertex cover" of the tree in a certain way, but actually there is a standard DP.
    
    # Let’s define two states:
    # Let’s do DFS and compute for each subtree:
    
    # We will compute the minimum number of antennas in the subtree of u, with the guarantee that u's subtree will have at least one.
    
    # But since every subtree must have one, it's the same for all.
    
    # For a leaf u: we must place one antenna in it. So cost = 1.
    
    # For a non-leaf u: we have options:
    # 1. Place an antenna at u. Then all subtrees of children are satisfied (because u is in their ancestor's subtree? No.
    # Wait, if I place at u, then for a child v, the subtree of v does NOT contain u. u is outside v.
    # So placing at u does NOT help any of the children's subtrees.
    # So if I place at u, I still need to cover each child's subtree independently.
    # So cost = 1 + sum over children of cost(child)
    
    # 2. Don't place at u. Then to satisfy u's subtree, at least one child subtree must... no, to satisfy u, we need at least one antenna in u's subtree, which would have to be in one of the children's subtrees.
    # But since every child subtree must have its own antenna anyway (by induction), this is automatically satisfied.
    # So if I don't place at u, the cost is just sum over children of cost(child).
    
    # So the minimum is always the sum over children, without placing at u.
    # That would mean we only place at leaves, and the answer is the number of leaves.
    
    # Let's check with sample.
    # In first sample:
    # Root C has children: A and B (since A is not inside B)
    # B has child D.
    # So leaves are A and D.
    # Number of leaves = 2, and sample output is 2. Good.
    
    # Second sample: 1 rectangle, answer 1. It's a leaf (and root). Good.
    
    # Third sample: 7 rectangles.
    # Let's assume output is 3, so probably 3 leaves in the containment tree.
    
    # Is the answer always the number of leaves in the containment tree?
    
    # Let's see if this makes sense.
    # If I place an antenna in every leaf room, then for any room, since every room that has no children is a leaf and has an antenna, and for internal nodes, they contain leaves, so there is an antenna in their subtree. Perfect.
    
    # Can we do with fewer? If I don't place in one leaf, then that leaf room itself has no antenna in its subtree (since it's a leaf), so it won't be covered. So we must place at least one in every leaf's subtree, which means exactly one per leaf subtree, and since they are disjoint, we need at least the number of leaves.
    
    # So yes, the minimum is exactly the number of leaves in the tree!
    
    # But is the tree a forest? No, there is one outermost.
    
    # In the containment, since one contains all, it's a tree.
    
    # But is it always a tree? The problem says "Não há nenhum tipo de interseção entre os retângulos que definem as salas." and one contains all others.
    
    # But rectangles can be nested in more complex ways, but since no intersections, the containment forms a tree (laminar family).
    
    # Yes, because if two rectangles both contain a third, but neither contains the other, that would be ok as long as they don't intersect improperly, but in axis-aligned without crossing, it should be laminar.
    
    # The problem says "as paredes das salas não se tocam", so no touching, so strict containment.
    
    # So yes, the containment relation forms a tree.
    
    # Therefore, the answer is the number of leaf nodes in this tree.
    
    # In the first sample, leaves are the smallest ones: A and D, yes 2.
    
    # In single room, 1 leaf.
    
    # Perfect.
    
    # So we just need to build the tree and count how many nodes have no children.
    
    # But we must be careful: the root is a leaf only if there are no other rooms.
    
    # Now, since N<=1e5, we need an efficient way to build the containment tree.
    
    # The naive way above is O(N^2) which is too slow.
    
    # We need an efficient way to find for each rectangle its parent (the smallest rectangle that contains it).
    
    # Since it's laminar and axis-aligned, we can use sorting and sweep line or use a stack or discretize.
    
    # A standard way for nested rectangles is to sort by increasing x1, then by decreasing x2, or something.
    
    # Since one contains all, we can think of the rectangles as intervals in 2D.
    
    # A good way is to sort all rectangles by their left edge (x1) ascending, and if tie by right edge (x2) descending (so larger ones come first).
    
    # We can use a set or a stack to keep track of active rectangles.
    
    # But perhaps the simplest efficient way for 1e5 is to realize we only need the parent of each, and count nodes with no children.
    
    # We can sort the rectangles in order of increasing size (by area? no).
    
    # Better: sort by x1 ascending, then by y1 descending (top), then by x2 ascending, etc. It's tricky.
    
    # A proven way for nested axis-aligned rectangles with no intersections is to sort them by their left x-coordinate.
    
    # Let's implement a O(N log N) way using sorting and a map or something.
    
    # Since we only need the number of leaves, we can find all rectangles that are not parent of anyone.
    
    # But to count leaves, a node is a leaf if no other rectangle is strictly contained in it.
    
    # Yes! We don't need to build the full tree.
    # A rectangle is a leaf if there is no other rectangle strictly inside it.
    
    # Then the answer is the number of such rectangles that have no rectangles inside them.
    
    # But is that correct? In the sample, A has nothing inside, D has nothing inside, B has D inside so not leaf, C has others.
    # Yes, leaves = 2. Perfect.
    
    # And for the root, if nothing inside, it's the only one.
    
    # So the problem reduces to, for each rectangle, check if there exists at least one other rectangle strictly contained in it.
    
    # If not, it's a leaf.
    
    # But with N=1e5, we cannot check naively.
    
    # We need an efficient way to count how many rectangles have no other rectangle inside them.
    
    # This is a classic problem: count the number of minimal rectangles under containment.
    
    # To do this efficiently, we can sort the rectangles in order of increasing x1, decreasing x2 (so from largest to smallest in x-direction), and use a data structure for y-intervals.
    
    # We will process rectangles from outermost to innermost likely.
    
    # Let's sort all rectangles by increasing X1, then by decreasing X2 (so for same X1, larger ones first).
    # Also need to handle Y.
    
    # A standard algorithm for this is to use a segment tree or fenwick to keep track of "covered" y-regions by active inner rectangles.
    
    # But perhaps a simpler way: since we only need to know if a rectangle contains any other, we can find for each rectangle the "immediate" contained ones.
    
    # But let's search for "minimum number of wifi antennas nested rectangles" or just implement the tree building efficiently.
    
    # Since N=1e5, we need O(N log N).
    
    # Let's compress all coordinates.
    # There are 2N distinct x coords and 2N y coords.
    
    # But perhaps we can model it as 2D partial order.
    
    # A rectangle A contains rectangle B if:
    # X1A <= X1B, X2A >= X2B, Y1A >= Y1B, Y2A <= Y2B.
    
    # And since no intersections and strict (because walls don't touch), we have strict inequalities.
    
    # To count for how many rectangles there exists no B != A such that A contains B.
    
    # I.e., number of rectangles that are minimal under the containment partial order.
    
    # To compute the number of such minimal elements.
    
    # One way is to find all rectangles that are not contained by any other? No, we want those that do not contain any other.
    
    # So the minimal ones in the poset (where higher = contains).
    
    # To count how many have no elements below them.
    
    # A good way is to sort the rectangles by increasing (X1), then by decreasing (X2), then by increasing (Y2), then by decreasing (Y1) or similar.
    
    # Then we can use a Fenwick tree or segment tree on the y-coordinates to query if there is any rectangle already processed that is contained.
    
    # Let's define the order: we process potential inner rectangles first.
    
    # So we want to process smaller rectangles before larger ones.
    
    # Sort by decreasing area? Not safe.
    
    # Sort by increasing width (X2-X1), then increasing height.
    
    # But may have same sizes.
    
    # A correct way is:
    # Sort the rectangles in increasing order of X1.
    # If X1 equal, process the one with smaller X2 first (inner ones have larger X1 or smaller X2).
    
    # Let's look for a standard technique for nested rectangles.
    
    # We can use a stack-based approach if we sort properly, but since it's 2D it's harder.
    
    # Since it's a tree, we can find the parent for each rectangle efficiently by keeping active candidates.
    
    # Here's a standard O(N log N) method using coordinate compression and segment tree:
    # We will associate each rectangle with its inner y-range.
    # We sort all rectangles by their X1 from left to right (increasing X1).
    # We will maintain a segment tree on the Y coordinates that stores the "most recent" (smallest X2) active rectangle that covers that y-range.
    
    # But it might be complicated.
    
    # Since N=1e5 and time limit is usually 2s for python, perhaps we can use a simpler method.
    
    # Let's observe that because walls don't touch and no intersections, the containments are strict and laminar.
    
    # A reliable method is to sort by X1 ascending.
    # Use a set of active rectangles sorted by their Y1 or something.
    
    # Let's implement the following algorithm:
    # - Sort rectangles in order of increasing X1, if tie by increasing X2.
    # - Use a data structure that keeps track of currently "open" rectangles (those whose X1 has been seen but not yet "closed" by their X2).
    # But it's getting complex.
    
    # Since we only need the number of leaves, we can count how many rectangles are "directly" contained in some parent, i.e. count the number of rectangles that have a parent.
    # Then answer = N - number of rectangles that are children of someone.
    
    # No: every non-root has a parent, so number of leaves is not that.
    # Number of leaves = total nodes - number of nodes with children.
    
    # So if I can count how many rectangles contain at least one other rectangle, then answer = N - that_count.
    
    # Yes.
    
    # So I need to count the number of rectangles that contain at least one other rectangle.
    
    # To do that, I can for each possible inner rectangle, mark its parent as "has_child".
    
    # So if I can find for each rectangle its immediate parent, I can mark the parents.
    
    # So the problem reduces to finding the parent of each rectangle efficiently.
    
    # How to find the immediate container for each rectangle.
    
    # A standard way is to use a segment tree where each node represents a y-interval and stores the candidate container with smallest area or most nested.
    
    # Let's implement it.
    
    # First, collect all Y coordinates for compression.
    all_y = []
    for x1,y1,x2,y2 in rects:
        all_y.append(y1)
        all_y.append(y2)
    all_y = sorted(set(all_y))
    y_to_idx = {y: i+1 for i, y in enumerate(all_y)}  # 1-based
    Y = len(all_y)
    
    # We will sort the rectangles by X1 ascending, then by X2 descending (larger first)
    events = []
    for i in range(N):
        x1, y1, x2, y2 = rects[i]
        events.append((x1, 0, i))   # 0 for open
        events.append((x2, 1, i))   # 1 for close
    
    # But we need to process in a certain order.
    
    # A better known method for this problem (this seems to be a known problem, perhaps from ICPC or OBI) is to realize that the answer is the number of rooms that have no rooms inside them.
    
    # Let's try to find a way.
    
    # We can use union-find like structure but with care.
    
    # Here's a method that works in O(N log N):
    # We will process the rectangles sorted by their left edge X1 increasing.
    # We will maintain a set of "active" y-intervals in a way that we keep the current innermost rectangle for each y.
    
    # We use a segment tree where each leaf is a y-coordinate (compressed), and we store in each node the rectangle that "covers" that y-range with the current innermost container.
    
    # When we encounter a new rectangle (when we reach its X1), we query the segment tree in its [Y2, Y1] range to see what is the current covering rectangle. That would be its parent.
    # Then we update the range [Y2, Y1] with this new rectangle as the new innermost for that y-range.
    
    # But we have to handle the X2 as well.
    
    # Actually, because rectangles don't intersect, when we process by increasing X1, the active ones are nested properly.
    
    # The standard algorithm for building the containment tree for axis-aligned rectangles with no intersections is as follows:
    
    # 1. Sort all rectangles in increasing order of X1.
    # 2. Use a segment tree on Y that can handle range updates and queries for the "current parent".
    # 3. Also need to "remove" a rectangle when we pass its X2, but since we sort by X1, it's not straightforward.
    
    # Let's change the event approach.
    
    # Create events for left and right sides.
    # Sort events by x coordinate.
    # When we meet a left side of a rectangle, we query who is covering its y-range, that is its parent.
    # Then we update the y-range with this rectangle id as the current covering rectangle.
    # When we meet the right side, we need to revert the update.
    
    # But to revert, we need a way to "undo" or keep stack of updates.
    
    # This requires a segment tree that supports range update with "timestamp" or just set the current owner.
    
    # Since the rectangles are nested or disjoint, when we encounter a left wall, the current state in that y-range should be the parent.
    
    # And because no touching, it should be unique.
    
    # To handle removal at right wall, we need the segment tree to support updating a range to a certain value, and be able to revert when the rectangle ends.
    
    # One way is to use a segment tree with lazy propagation for range set updates, and also keep track of the "depth" or just process in order.
    
    # Since they are strictly nested, the active rectangles form a stack (nested).
    
    # But because it's 2D, at a given x, the active y-intervals are nested or disjoint.
    
    # So we can maintain a set of active intervals in a balanced tree (like sorted by Y).
    
    # But in Python, it might be slow but with 1e5, we need care.
    
    # Let's implement a simple method that should work.
    
    # Since Python is allowed and N=1e5, but with log^2 it might pass if constant is small.
    
    # Let's use the following approach that is known to work for this:
    
    # We will consider all rectangles.
    # We will find for each rectangle if it has a child.
    # To do it efficiently, we can use 4 sorting passes or something, but perhaps overkill.
    
    # Let's look at the constraints again: N <= 10^5, so we need O(N log N).
    
    # After thinking, the DP we had earlier can be simplified.
    # From earlier reasoning, since placing at u does not help its children (because children are inside), and not placing at u is always better or equal, the optimal is to never place at non-leaves, only at leaves.
    # And we must place exactly at all leaves.
    # So answer = number of leaf rectangles (rectangles that contain no other rectangles inside them).
    
    # So now we need to count how many rectangles have zero rectangles strictly inside them.
    
    # To compute this, we can use a Fenwick tree or segment tree to count how many rectangles are contained in each.
    
    # But to count if >0 or not.
    
    # One efficient way:
    # - Sort all rectangles by X1 ascending, X2 descending (larger ones have smaller X2? No.
    # If we sort by X1 ascending, and for same X1 by X2 ascending (smaller inner first).
    
    # Let's try this:
    # We will process from smallest to largest in terms of X-range.
    
    # Sort the rectangles in decreasing order of (X2 - X1), so larger ones first.
    # Then for each, we can query if its area has been "marked" by inner ones.
    
    # We can use a 2D structure.
    
    # Let's compress all X and Y.
    
    # But perhaps the easiest is to use a technique similar to offline containment counting.
    
    # We can use a Fenwick tree on Y for "inner most" .
    
    # Let's code a method that works.
    
    # Method:
    # 1. Sort the rectangles in increasing order of X1.
    # 2. We will use a segment tree that stores the minimum X2 of rectangles that cover a certain y-range (active).
    # 3. Also store the id.
    
    # When processing a rectangle from left to right:
    # - Before adding it, we query the maximum "inner" X2 in its y-range. If there is a rectangle with X2 <= current X2, then it is contained.
    
    # It's getting complicated.
    
    # Let's look for the problem name. The problem is called "Wifi" and seems from Brazilian OBI or ICPC regional.
    
    # Upon thinking, I recall that in such problems, the answer is the number of rooms that are "odd" in some sense, but no.
    
    # From our earlier reasoning, since the logic holds, and sample matches, we just need to count leaves.
    
    # To compute number of rectangles that do not contain any other, we can do the following:
    # For each possible parent, check if it contains any.
    # To do it fast, we can use sweeping.
    
    # Let's implement a sweep line by x.
    
    # But to make it simple and since time is limited, let's assume we build the tree using a stack per possible nesting.
    
    # Another idea: since all rectangles have unique containment (because no touching), we can sort them by their center or by size.
    
    # Let's sort the rectangles by increasing X1, then decreasing Y1, then increasing X2, then decreasing Y2 or find a total order that respects containment.
    
    # A standard way that works is:
    # Sort the rectangles so that if A contains B then A appears before B in the list.
    # This can be done by sorting by X1 ascending, then by X2 descending, then by Y1 descending, then by Y2 ascending.
    
    # Let's try with sample.
    
    # Rect 0: 5 19 8 17   -> x1=5, y1=19, x2=8, y2=17
    # Rect 1: 5 15 15 5    -> x1=5, y1=15, x2=15, y2=5
    # Rect 2: 0 20 20 0    -> x1=0, y1=20, x2=20, y2=0
    # Rect 3: 8 10 10 8    -> x1=8, y1=10, x2=10, y2=8
    
    # Sort by x1 asc, then x2 desc, then y1 desc, then y2 asc.
    # So first rect2: x1=0
    # Then rect0 and rect1 have x1=5, rect1 has x2=15 > rect0 x2=8, so if we sort by x2 descending, rect1 comes before rect0.
    # Then rect3 x1=8.
    # So order: 2, 1, 0, 3.
    
    # Now if we process in this order, we can add them to a data structure.
    
    # We can have a set of "potential parents".
    
    # But let's use a segment tree with min id or something.
    
    # Let's implement a segment tree that can update a y-range with a rectangle id (meaning this is the current innermost rectangle for that y).
    # We process in order of increasing x1.
    # When we process a rectangle, we query the current id in its y-range. If there is one with larger x1 and smaller x2, it is contained.
    # But to make it work, we need to process left to right and only add when appropriate.
    
    # Let's code it.
    
    # We will create a list of rectangles sorted by x1 ascending.
    rect_list = sorted(range(N), key=lambda i: (rects[i][0], -rects[i][2], -rects[i][1], rects[i][3]))
    
    # This sorting tries to put outer ones first.
    # For sample: rect2 has smallest x1, then between rect0 and rect1, both x1=5, -x2: rect1 has -15, rect0 has -8, so -15 < -8 so rect1 comes before rect0? No.
    # key = (x1, -x2, -y1, y2)
    # For rect1: (5, -15, -15, 5)
    # For rect0: (5, -8, -19, 17)
    # At second component -x2: -15 < -8, so rect1 comes before rect0. But rect1 is not outer than rect0.
    # rect0 is not inside rect1.
    
    # So not perfect.
    
    # Let's try a different sorting: sort by x1 ascending, then by x2 descending (so larger x2 first, i.e. outer).
    # So key = (x1, -x2)
    # Then for x1=5, rect1 has x2=15, rect0 has x2=8, so -15 < -8, so rect1 comes first then rect0.
    # Still same.
    
    # But in reality rect0 and rect1 are both directly in root.
    
    # For the segment tree approach, the standard "sweep from left to right, add on left, remove on right" with segment tree for active y coverage can be used to detect containment.
    
    # But to detect if a rectangle contains others, we can count how many times a rectangle is "entered" by other rectangles' left sides while it is active.
    
    # This is getting too long.
    
    # Let's think differently.
    
    # Since the containment forms a tree, and we only need the number of leaves, and from DP, dp[u] = sum dp[v] for children v, and for leaf dp[u] = 1.
    # So answer is number of leaves.
    
    # To compute it, we can find all rectangles that are contained by some other, and count unique "parents".
    
    # No.
    
    # We can use a map or dict to count how many direct children each has, but we need to find them.
    
    # With N=1e5, we need log N.
    
    # Let's implement the segment tree with range update.
    
    # We will compress all y coordinates.
    ys = sorted(set([r[1] for r in rects] + [r[3] for r in rects]))
    yrank = {y: i for i, y in enumerate(ys)}
    m = len(ys)
    
    # We will create events for left and right.
    # Event: (x, type, rect_id)
    # type = 0: left side (open)
    # type = 1: right side (close)
    # We sort by x ascending, if tie, process opens before closes? We need to be careful.
    
    events = []
    for i in range(N):
        x1, y1, x2, y2 = rects[i]
        events.append((x1, 0, i, y1, y2))  # open
        events.append((x2, 1, i, y1, y2))  # close
    
    events.sort(key=lambda e: (e[0], e[1], -e[2] if e[1]==0 else e[2]))  # arbitrary
    
    # We will have a segment tree that for each y-segment stores the current "active" rectangle that is covering it (the innermost one).
    # Each node will store the id of the rectangle that is currently the active one for that entire range.
    
    class SegmentTree:
        def __init__(self, n):
            self.n = n
            self.tree = [-1] * (4 * n)
            self.lazy = [-1] * (4 * n)
        
        def propagate(self, node, start, end):
            if self.lazy[node] != -1:
                self.tree[node] = self.lazy[node]
                if start != end:
                    self.lazy[2*node] = self.lazy[node]
                    self.lazy[2*node+1] = self.lazy[node]
                self.lazy[node] = -1
        
        def update_range(self, node, start, end, l, r, val):
            self.propagate(node, start, end)
            if start > end or start > r or end < l:
                return
            if l <= start and end <= r:
                self.lazy[node] = val
                self.propagate(node, start, end)
                return
            mid = (start + end) // 2
            self.update_range(2*node, start, mid, l, r, val)
            self.update_range(2*node+1, mid+1, end, l, r, val)
            # Since it's set update, no need to combine tree[node]
            if self.tree[2*node] == self.tree[2*node+1] and self.tree[2*node] != -1:
                self.tree[node] = self.tree[2*node]
            else:
                self.tree[node] = -2  # mixed
        
        def query(self, node, start, end, l, r):
            self.propagate(node, start, end)
            if start > end or start > r or end < l:
                return -1
            if l <= start and end <= r:
                return self.tree[node]
            mid = (start + end) // 2
            left = self.query(2*node, start, mid, l, r)
            right = self.query(2*node+1, mid+1, end, l, r)
            if left == right:
                return left
            if left == -1:
                return right
            if right == -1:
                return left
            return -2  # multiple
    
    st = SegmentTree(m)
    
    has_child = [False] * N
    parent = [-1] * N
    
    active = {}
    
    for event in events:
        x, typ, idx, y1, y2 = event[0], event[1], event[2], event[3], event[4]
        ly = yrank[y2]
        ry = yrank[y1] - 1   # since y1 > y2, the range is from y2 to y1
        
        if typ == 0:  # open
            # Query who is currently covering this range
            curr_parent = st.query(1, 0, m-1, ly, ry)
            if curr_parent != -1 and curr_parent != -2:
                parent[idx] = curr_parent
                has_child[curr_parent] = True
            # Now add this rectangle as the new cover for this y range
            st.update_range(1, 0, m-1, ly, ry, idx)
            active[idx] = (ly, ry)
        else:  # close
            # Remove this rectangle, revert to previous
            # But to revert, we need to know what was before.
            # This is the problem with this approach: we need stack or previous value.
            # So this simple lazy segment tree cannot easily revert.
    
    # So this approach has a flaw for removal.
    
    # To fix this, one common way is to process all events sorted by x, and use a different structure that keeps all active rectangles in a tree of y-intervals.
    
    # We can use a set of active y-intervals with the corresponding rectangle.
    
    # But in Python, we can use a sorted dict or just since it's laminar, we can use a tree.
    
    # Since N=1e5, and Python is slow, but perhaps we can use a different insight.
    
    # Let's notice that because no two rectangles touch or intersect, their y-ranges are either disjoint, or nested, or one contains the other in y when x overlaps.
    
    # A working method is to use union-find on the y-compressed grid, but it may be overkill.
    
    # Let's look at the test cases to see if there is a pattern.
    
    # In all test cases, the output is small (2,1,3), consistent with number of leaves.
    
    # Let's assume we need to count leaves.
    
    # To compute it efficiently, we can find all rectangles that are the "innermost" for some area.
    
    # Another idea: we can consider all the "atomic" regions (the faces in the planar map).
    # The number of antennas needed is the number of atomic faces, because each atomic region needs its own antenna? No, because one antenna in the innermost covers all outer.
    # No, according to our earlier logic, it's the number of innermost rooms.
    
    # The atomic rooms are the leaves.
    
    # Yes.
    
    # To count the number of rectangles that have no rectangle inside them, we can use a O(N log N) method using sort and Fenwick tree to count contained rectangles.
    
    # Let's do this:
    # We will count for each rectangle how many rectangles it contains.
    # If the count is 0, then it's a leaf.
    
    # To count the number of rectangles contained in each, we can use offline 2D counting.
    
    # A rectangle B is contained in A if X1A <= X1B and X2B <= X2A and Y2A <= Y2B and Y1B <= Y1A.
    
    # So it's a 4-dimensional partial order counting.
    
    # To count for each A the number of B such that X1A <= X1B, X2B <= X2A, Y2A <= Y2B, Y1B <= Y1A.
    
    # This is standard 4D dominance counting, which can be done in O(N log^3 N) with heavy constants, not good for Python.
    
    # But since the rectangles are guaranteed to have laminar containment (no crossing), we can use a simpler sweep.
    
    # Let's implement a sweep line that moves from left to right.
    # We maintain the active segments in y, and since they are nested, we can keep a stack or a tree of active rectangles.
    
    # We will use a set to keep the active y endpoints.
    
    # But let's use a Fenwick tree or segment tree that keeps the "open" rectangles.
    
    # Here's a method that should work and is simpler:
    # We will sort all left and right edges.
    # But instead of updating range, we will discretize y and use a segment tree that stores whether a y-range is "occupied" by an inner rectangle.
    
    # When we encounter a left side of a rectangle R, we query if in its [y2, y1] there is already any "marked" point (meaning an inner rectangle has been completely inside).
    # If yes, then R has a child.
    # Then when we encounter the right side of a rectangle, we mark the y-range as "has inner" if it had no child? It's complicated.
    
    # Let's try to search for solution of this problem.
    
    # The problem is from OBI 2018 or something, called "Wifi".
    
    # Upon thinking, I recall that in such problems the minimum number of antennas is the number of "odd depth" rooms or something, but in our case from logic it's the number of leaves.
    
    # Let's verify with the third sample.
    # 7 rectangles:
    # 0: 50 80 90 75
    # 1: 45 30 50 20
    # 2: 5 98 6 97
    # 3: 0 100 100 0   <-- outer
    # 4: 20 60 98 5
    # 5: 25 50 70 10
    # 6: 30 45 65 15
    
    # Let's see containments.
    # Outer is 3: 0,100 to 100,0
    
    # Rect2: 5,98 to 6,97 : very thin on top left, likely direct child of outer.
    # Rect0: 50,80 to 90,75 : inside outer.
    # Rect4: 20,60 to 98,5 : large inside outer, contains others.
    # Rect5: 25,50 to 70,10 : inside rect4.
    # Rect6: 30,45 to 65,15 : inside rect5 or rect4.
    # Rect1: 45,30 to 50,20 : seems inside rect4.
    
    # So likely the leaves are: rect2, rect0, rect1, rect6? But output is 3.
    # So perhaps some are nested further.
    
    # Let's see if rect6 is inside rect5: rect5 x25-70, y10-50. rect6 x30-65, y15-45. Yes, 25<30<65<70 and 10<15<45<50, yes.
    # Rect1: x45-50, y20-30. Is it inside rect5? rect5 y up to 50, down to 10, yes 10<20<30<50, x25<45<50<70 yes. So inside rect5.
    # Rect0 is in top, x50-90 y75-80, rect4 goes up to y60, so not inside rect4, so direct in outer.
    # Rect2 is direct in outer.
    # So leaves are: rect2, rect0, and the innermost in the bottom branch.
    # If rect6 contains nothing, rect1 contains nothing, but if both are inside rect5, then leaves are rect2, rect0, rect1, rect6 -> 4, but sample output is 3.
    # The output for test 3 is 3.
    # So my assumption must be wrong.
    
    # This means that the answer is not the number of leaves.
    
    # My initial logic is flawed.
    
    # Let's go back.
    
    # In the third sample, if there are 4 leaves, but answer is 3, then we can cover with 3 antennas.
    
    # So sometimes we can place an antenna in an internal node to cover multiple leaves? But earlier I thought that placing in internal does not cover the inner rooms.
    
    # Let's re-read the problem carefully.
    
    # "o sinal wifi é capaz de atravessar as paredes quando vem de dentro para fora, mas estranhamente não atravessa as paredes quando vem de fora para dentro das salas!"
    
    # So signal can cross walls from inside to outside, but not from outside to inside.
    
    # If I place an antenna inside a room, the signal can go to the outside of that room (crossing the wall from inside to outside).
    # But to go to an inner room, the inner room is "inside", so from the current room to the inner room, the signal would be going from outside the inner room to inside the inner room, which is blocked.
    
    # So yes, antenna in a room covers the room itself and all outer areas, but not the inner rooms.
    
    # So to cover an inner room, you need an antenna inside it or in its descendants.
    
    # So for a leaf, you must place an antenna in it.
    # So in the third sample, if there are 4 leaves, it should require 4, but sample says 3, so either there are only 3 leaves or my understanding of nesting is wrong.
    
    # Let's check if rect1 is inside rect5.
    # rect5: X1=25, Y1=50, X2=70, Y2=10
    # rect1: X1=45, Y1=30, X2=50, Y2=20
    # Is 25 <= 45 and 50 <= 70 ? Yes.
    # Is Y2=10 <= Y2 of rect1=20 ? The condition for rect5 contains rect1:
    # For containment: the inner should have larger or equal Y2? No.
    # Recall:
    # Rectangle A contains B if:
    # A's left <= B's left, A's right >= B's right,
    # A's bottom <= B's bottom, A's top >= B's top.
    
    # In the input, it's given as X1,Y1,X2,Y2 where (X1,Y1) is upper left, (X2,Y2) is lower right, and Y1 > Y2.
    
    # So top = Y1, bottom = Y2.
    # So A contains B if:
    # X1A <= X1B and X2A >= X2B and Y2A <= Y2B and Y1A >= Y1B.
    
    # For rect5 (25,50,70,10) and rect1 (45,30,50,20):
    # X: 25<=45 and 70>=50 yes.
    # Y: Y2A=10 <= Y2B=20 ? 10 <= 20 yes.
    # Y1A=50 >= Y1B=30 ? 50 >= 30 yes.
    # Yes, so rect5 contains rect1.
    
    # Similarly for rect6 (30,45,65,15):
    # X 25<=30<=65<=70
    # Y: 10 <= 15 and 50 >= 45 yes.
    # So rect5 contains both rect1 and rect6.
    
    # So leaves: rect0, rect2, rect1, rect6. 4 leaves.
    # But sample output is 3.
    # This contradicts.
    
    # So my understanding of "leaf" or the covering is wrong.
    
    # Let's re-read the signal propagation.
    
    # "o sinal wifi é capaz de atravessar as paredes quando vem de dentro para fora, mas estranhamente não atravessa as paredes quando vem de fora para dentro das salas"
    
    # "from inside to outside" can cross, "from outside to inside" cannot.
    
    # Now, what is "dentro" and "fora" for a wall.
    # For a given wall of a room, "dentro" is the interior of that room, "fora" is the exterior.
    
    # So if antenna is in the interior of a room, signal can cross its own walls to the exterior.
    # If antenna is in the exterior, it cannot cross into the interior.
    
    # For an inner room, its "exterior" is the interior of its parent room.
    
    # So if I place antenna in the parent room (exterior to the child), it cannot cross into the child room.
    
    # If I place in the child room, it can cross out to the parent room.
    
    # So yes, seems correct.
    
    # But then why is the sample 3 if there are 4 leaves?
    
    # Let's check if rect1 is really inside rect5.
    # rect1 Y1=30, Y2=20
    # rect5 Y1=50, Y2=10
    # Is the entire rect1 inside rect5?
    # rect1's top is at 30, rect5's bottom is at 10, but is 30 > 10? Yes.
    # The y for rect1 is from 20 to 30, rect5 is from 10 to 50, so yes 10 < 20 < 30 < 50, so yes inside.
    
    # Let's list all containments:
    # Outer (3) contains all others.
    # rect4 (20,60,98,5) : x20-98, y5-60
    # Contains rect5 (25,50,70,10): yes.
    # Contains rect6 (30,45,65,15): 20<30<65<98, 5<15<45<60 yes.
    # Contains rect1 (45,30,50,20): 20<45<50<98, 5<20<30<60 yes.
    # Contains rect0? rect0 (50,80,90,75): y75-80. rect4 only goes up to 60, 80 > 60, so no.
    # rect2 is at y97-98, no.
    
    # rect5 contains rect6 and rect1?
    # rect5 y10-50, rect6 y15-45, yes.
    # rect1 y20-30, yes inside rect5.
    # So rect5 contains rect1 and rect6.
    # So the tree is:
    # Root 3
    # - 2 (leaf)
    # - 0 (leaf)
    # - 4
    #   - 5
    #     - 1 (leaf)
    #     - 6 (leaf)
    # So leaves: 2,0,1,6 -> 4 leaves.
    # But sample output is 3.
    # This means either one of them is not a leaf or the logic is wrong.
    
    # Let's check if rect6 is contained in rect1 or vice versa.
    # rect1: x45-50, y20-30
    # rect6: x30-65, y15-45
    # Does rect1 contain rect6? x45 <=30 ? No.
    # Does rect6 contain rect1? x30<=45<=50<=65 yes, y15<=20<=30<=45 yes.
    # Oh! rect6 contains rect1 !
    # Y for rect6 is 15 to 45, rect1 is 20 to 30, yes.
    # X 30 to 65 contains 45 to 50.
    # Yes! So rect6 contains rect1.
    
    # So correction:
    # rect4 contains rect5 and rect6? Wait, rect6 is contained in rect5 or not?
    # rect5: x25-70 y10-50
    # rect6: x30-65 y15-45 : yes, contained in rect5.
    # And rect6 contains rect1.
    
    # So tree:
    # 3 (root)
    #   - 0 (leaf)
    #   - 2 (leaf)
    #   - 4
    #     - 5
    #       - 6
    #         - 1 (leaf)
    # So leaves are 0, 2, 1. Exactly 3. Perfect!
    
    # My mistake in nesting.
    # Yes, now it matches. Answer is indeed the number of leaves in the containment tree.
    
    # Great.
    
    # So now we can proceed with confidence.
    
    # To solve, we need to build the containment tree and count how many nodes have no children.
    
    # With N=1e5 we need an efficient way.
    
    # We will use the segment tree with lazy propagation for range assign, but to handle the closing, we can process the events in a specific order and use a "version" or just use a different approach.
    
    # A standard way for building nesting tree for rectangles is to use a stack, but for that we need to process in a certain order.
    
    # Since it's laminar, we can use the following method that is O(N log N):
    
    # We will sort the rectangles in order of increasing X1, decreasing X2.
    # This tends to put outer rectangles before inner ones when they share the same left.
    
    # Then we will use a Fenwick or segment tree that stores the "last" rectangle that covers a y point.
    
    # Let's implement a working solution.
    
    # After some thought, here is a method that works:
    # We will associate each rectangle with its y-interval.
    # We sort all rectangles by their X1 ascending.
    # We will maintain a set of active rectangles' y-intervals, but since Python set is not enough, we use a segment tree that stores the deepest (most recently added) rectangle id for each y.
    
    # When we start a new rectangle (at its X1), we query the segment tree for the minimum or the id in its y-range. Since all active have smaller X1, the one with largest X2 that contains it would be the parent.
    
    # But to make it the immediate parent, we need the one with smallest area or the one that is the tightest.
    
    # If we process in order of increasing X1 and for same X1 by decreasing X2 (outer first), then when we add a rectangle, we can update.
    
    # Let's code it.
    
    # We will not use events for right, because if we sort by X1, and assume that when we process a rectangle, all possible containers have smaller X1, so they are already processed.
    
    # But the parent must have smaller X1 and larger X2.
    
    # So if we process from left to right, when we reach a rectangle, its parent must have been processed already.
    
    # So we can query the "current innermost" rectangle that covers the y-range of this new rectangle.
    
    # Then that innermost one that contains it in y and has larger X2 (we need to check) is the parent.
    
    # To make it work, the segment tree should store in each y the active rectangle with the smallest X2 that still contains the y (the innermost).
    
    # So we need to update ranges with a value if the new rectangle is smaller.
    
    # Let's define.
    
    # We will have a segment tree on y (compressed).
    # Each position in the segment tree will store the id of the current innermost rectangle covering that y-point.
    
    # We process rectangles in order of increasing X1.
    # For each new rectangle i:
    #   - Query the segment tree in the range of its y-interval. Get the current ids.
    #   - Among the ids returned, we need to find which one actually contains it (has X2 >= our X2 and Y contains).
    #   - Since we process by increasing X1, and no intersections, the current covering one should be the parent.
    #   - Then we update the entire y-range of this rectangle with id = i, because now it is the innermost for that range.
    
    # Yes, this works because when a rectangle is added, it becomes the new innermost for its y-range until a even inner one is added.
    
    # And since we only query when we open a new one, and the current value is the parent.
    
    # We don't need to remove because we never "close" in this sweep; the inner ones just overwrite the range.
    
    # This works because of the laminar property and no touching: the y-ranges don't partially overlap.
    
    # Let's test with the first sample.
    
    # Rects:
    # 0: x1=5 y1=19 x2=8 y2=17
    # 1: x1=5 y1=15 x2=15 y2=5
    # 2: x1=0 y1=20 x2=20 y2=0
    # 3: x1=8 y1=10 x2=10 y2=8
    
    # Sort by increasing X1: rect2 (0), then rect0 (5), rect1 (5), then rect3 (8).
    # For same x1=5, we should decide order. Let's say we sort by x1, then by -x2 (larger x2 first), so for x1=5, rect1 has x2=15 > rect0 x2=8, so rect1 then rect0? Or reverse.
    # Let's assume we sort by x1 asc, then x2 asc (smaller first, more inner first?).
    
    # Let's simulate with sort by x1 asc, then x2 asc.
    # Order: 2 (x1=0), then rect0 (x1=5,x2=8), then rect1 (x1=5,x2=15), then rect3 (x1=8).
    
    # Start with empty segment tree (value -1).
    
    # Process rect2 (outer):
    # Query its y range [0,20], gets -1, so no parent (it's root).
    # Update y [0,20] with id=2.
    
    # Process rect0 (5,19,8,17): y from 17 to 19.
    # Query y[17,19], currently covered by 2.
    # So parent[0] = 2.
    # Update y[17,19] with id=0.
    
    # Process rect1 (5,15,15,5): y from 5 to 15.
    # Query y[5,15], currently covered by 2 (since we only updated 17-19).
    # So parent[1] = 2.
    # Update y[5,15] with id=1.
    
    # Process rect3 (8,10,10,8): y from 8 to 10.
    # Query y[8,10]: this is inside [5,15], so should return id=1.
    # So parent[3] = 1. Correct!
    # Then update y[8,10] with 3.
    
    # Perfect.
    
    # Now has_child: 2 has children 0 and 1, 1 has child 3, 0 and 3 have no children.
    # Leaves: 0 and 3. Correct.
    
    # Now let's see if the third sample would work.
    # It should, because when we add an inner one, it updates its range, so when we add even inner, it queries the current innermost.
    
    # Yes.
    
    # Order matters: we processed the one with smaller x2 first at x1=5, and it worked.
    
    # If we had processed rect1 before rect0, let's see:
    # After root, process rect1 first (if sorted by x2 desc).
    # Process rect1: query -> parent=2, update [5,15] with 1.
    # Then rect0: query [17,19] -> still 2, parent=2, update [17,19] with 0.
    # Then rect3 at [8,10] queries and gets 1. Still correct.
    
    # Good.
    
    # So the order of processing at same x1 doesn't matter much as long as consistent.
    
    # Let's choose sort by x1 ascending, then by x2 ascending (smaller x2 first).
    
    # Now, to implement the segment tree, since we only need to query if there is a uniform id in the range or get any id (since due to laminar, the whole range should be covered by the same parent).
    
    # In the example, when querying [8,10] it was all covered by 1, yes.
    # Because of no touching and laminar, when you query a full rectangle's y-range, it should be covered by a single parent id.
    
    # So in segment tree, we can have each node store the id if the entire range has the same id, else -2.
    
    # In the update, we do range set update (lazy).
    
    # In query, if the range is not uniform, we may need to check, but in practice for this problem it should be uniform.
    
    # Let's implement it.
    
    # We need to map y to discrete values carefully.
    # Since we update [y2, y1], and y are discrete, we need to compress all y values and map the intervals to indices.
    
    ys = sorted(set(y for rect in rects for y in (rect[1], rect[3])))
    yrank = {y: i for i, y in enumerate(ys)}
    m = len(ys)
    
    # The segment tree will be on 0 to m-2, since intervals are between consecutive ys.
    # But to make it simple, since we only care about coverage, we can use the ranks of the y values.
    # The range for a rect from y2 to y1 corresponds to rank[y2] to rank[y1]-1.
    
    class SegTree:
        def __init__(self, n):
            self.n = n
            self.tree = [-1] * (4*n)
            self.lazy = [-1] * (4*n)
        
        def _push(self, node, s, e):
            if self.lazy[node] != -1:
                self.tree[node] = self.lazy[node]
                if s != e:
                    self.lazy[node*2] = self.lazy[node]
                    self.lazy[node*2+1] = self.lazy[node]
                self.lazy[node] = -1
        
        def update(self, node, s, e, l, r, val):
            self._push(node, s, e)
            if s > r or e < l:
                return
            if l <= s and e <= r:
                self.lazy[node] = val
                self._push(node, s, e)
                return
            mid = (s + e) // 2
            self.update(node*2, s, mid, l, r, val)
            self.update(node*2+1, mid+1, e, l, r, val)
            if self.tree[node*2] == self.tree[node*2+1] and self.tree[node*2] != -1:
                self.tree[node] = self.tree[node*2]
            else:
                self.tree[node] = -2
        
        def query(self, node, s, e, l, r):
            self._push(node, s, e)
            if s > r or e < l:
                return -1
            if l <= s and e <= r:
                return self.tree[node]
            mid = (s + e) // 2
            left = self.query(node*2, s, mid, l, r)
            right = self.query(node*2+1, mid+1, e, l, r)
            if left == right:
                return left
            if left == -1: return right
            if right == -1: return left
            return -2
    
    st = SegTree(m)
    
    # Sort indices by x1 asc, then x2 asc
    order = sorted(range(N), key=lambda i: (rects[i][0], rects[i][2]))
    
    parent = [-1] * N
    has_child = [False] * N
    
    for i in order:
        x1, y1, x2, y2 = rects[i]
        l = yrank[y2]
        r = yrank[y1] - 1
        if l > r:
            continue  # degenerate, shouldn't happen
        p = st.query(1, 0, m-1, l, r)
        if p != -1 and p != -2:
            parent[i] = p
            has_child[p] = True
        # Update the range with current id
        st.update(1, 0, m-1, l, r, i)
    
    # Now count how many have no children
    leaf_count = sum(1 for x in has_child if not x)
    
    print(leaf_count)
    
    # Let's test with first sample.
    # order by x1, then x2: rect2 (0,20), then rect0 (5,8), then rect1(5,15), then rect3(8,10)
    # As in my simulation, it sets parent[0]=2, parent[1]=2, parent[3]=1, has_child[2]=True, has_child[1]=True, has_child[0]=False, has_child[3]=False.
    # leaf_count = 2 (indices 0 and 3). Correct.
    
    # For single rectangle, order has one, query -1, no parent, has_child all False, count=1. Correct.
    
    # Should work for third sample too.
    
    # Now, is the segment tree correct with the mixed state (-2)?
    # In query, if it returns -2, it means multiple different ids in the range, which should not happen due to problem guarantees (no partial overlap).
    # So in practice it should return a single id.
    
    # This should work.
    
    # Let's check the yrank.
    # For the first sample, ys = [0,5,8,10,15,17,19,20] sorted.
    # rank[0]=0, 5=1, 8=2, 10=3, 15=4, 17=5, 19=6, 20=7.
    # For outer: y2=0 rank0, y1=20 rank7, so l=0, r=6.
    # For rect0: y2=17 r=5, y1=19 r=6, l=5, r=5 (rank[17]=5, rank[19]=6, r=6-1=5)
    # Yes.
    # For rect1: y2=5 rank1, y1=15 rank4, l=1, r=3.
    # For rect3: y2=8 rank2, y1=10 rank3, l=2, r=2.
    # When updating outer: updates 0 to 6 with 2.
    # Then rect0: query 5 to 5 -> 2, update 5 to 5 with 0.
    # Then rect1: query 1 to 3 -> 2, update 1 to 3 with 1.
    # Then rect3: query 2 to 2 -> now 1, correct.
    
    # Perfect.
    
    # This solves the problem.
    
    # Now, we need to be careful with the case when r < l, but since Y1 > Y2 given, and distinct, should be fine.
    
    # Also constraints say Y2 < Y1, good.
    
    # For large coordinates, no issue since we compress.
    
    # For N=1e5, segment tree with 4*2e5 ~ 800k, fine.
    # Python recursion limit not issue since no recursion.
    
    # Should pass within time, as each update/query is O(log N), total O(N log N).
    
    # Yes.
    
    # One possible issue: if two rectangles have same y coordinates, but problem says walls don't touch, so y's may coincide? But constraints don't forbid same y, but "não se tocam" means they don't touch, so probably strict containment, no shared edges.
    # So if two have same y, but since not touching, maybe not happen.
    # But in compression it's fine.
    
    # If r < l after compression, it means the y-range has no "space", but since Y1 > Y2 and distinct points, if only two y's, r = rank[y1]-1 = rank[y2]+1 -1 = rank[y2], so l=rank[y2], r=rank[y2], ok.
    
    # Good.
    
    # So this is the solution.
    
print("import sys")
print("from collections import defaultdict")
print("input = sys.stdin.read")
print("data = input().split()")
print("N = int(data[0])")
print("rects = []")
print("index = 1")
print("for i in range(N):")
print("    x1 = int(data[index])")
print("    y1 = int(data[index+1])")
print("    x2 = int(data[index+2])")
print("    y2 = int(data[index+3])")
print("    rects.append((x1, y1, x2, y2))")
print("    index += 4")
print("")
print("if N == 0:")
print("    print(0)")
print("    sys.exit()")
print("")
print("ys = sorted(set(y for rect in rects for y in (rect[1], rect[3])))")
print("yrank = {y: i for i, y in enumerate(ys)}")
print("m = len(ys)")
print("")
print("class SegTree:")
print("    def __init__(self, n):")
print("        self.n = n")
print("        self.tree = [-1] * (4 * n)")
print("        self.lazy = [-1] * (4 * n)")
print("")
print("    def _push(self, node, s, e):")
print("        if self.lazy[node] != -1:")
print("            self.tree[node] = self.lazy[node]")
print("            if s != e:")
print("                self.lazy[node*2] = self.lazy[node]")
print("                self.lazy[node*2+1] = self.lazy[node]")
print("            self.lazy[node] = -1")
print("")
print("    def update(self, node, s, e, l, r, val):")
print("        self._push(node, s, e)")
print("        if s > r or e < l: return")
print("        if l <= s and e <= r:")
print("            self.lazy[node] = val")
print("            self._push(node, s, e)")
print("            return")
print("        mid = (s + e) // 2")
print("        self.update(node*2, s, mid, l, r, val)")
print("        self.update(node*2+1, mid+1, e, l, r, val)")
print("        if self.tree[node*2] == self.tree[node*2+1] and self.tree[node*2] != -1:")
print("            self.tree[node] = self.tree[node*2]")
print("        else:")
print("            self.tree[node] = -2")
print("")
print("    def query(self, node, s, e, l, r):")
print("        self._push(node, s, e)")
print("        if s > r or e < l: return -1")
print("        if l <= s and e <= r:")
print("            return self.tree[node]")
print("        mid = (s + e) // 2")
print("        left = self.query(node*2, s, mid, l, r)")
print("        right = self.query(node*2+1, mid+1, e, l, r)")
print("        if left == right: return left")
print("        if left == -1: return right")
print("        if right == -1: return left")
print("        return -2")
print("")
print("st = SegTree(m)")
print("order = sorted(range(N), key=lambda i: (rects[i][0], rects[i][2]))")
print("has_child = [False] * N")
print("")
print("for i in order:")
print("    x1, y1, x2, y2 = rects[i]")
print("    l = yrank[y2]")
print("    r = yrank[y1] - 1")
print("    if l <= r:")
print("        p = st.query(1, 0, m-1, l, r)")
print("        if p != -1 and p != -2:")
print("            has_child[p] = True")
print("        st.update(1, 0, m-1, l, r, i)")
print("")
print("leaf_count = sum(1 for has in has_child if not has)")
print("print(leaf_count)")
