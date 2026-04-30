
import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    F = [0] * (N + 1)
    for i in range(1, N + 1):
        F[i] = int(data[index])
        index += 1
    Q = int(data[index])
    index += 1
    queries = []
    for _ in range(Q):
        A = int(data[index])
        B = int(data[index + 1])
        queries.append((A, B))
        index += 2
    
    # Build reverse graph
    rev = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        rev[F[i]].append(i)
    
    # Find the cycle
    vis = [0] * (N + 1)  # 0 not, 1 visiting, 2 done
    cycle = []
    cycle_id = [-1] * (N + 1)
    in_cycle = [False] * (N + 1)
    cycle_start = -1
    
    def dfs_cycle(u, path):
        nonlocal cycle_start
        vis[u] = 1
        path.append(u)
        v = F[u]
        if vis[v] == 0:
            dfs_cycle(v, path)
        elif vis[v] == 1:
            # cycle found
            idx = path.index(v)
            cycle_start = idx
        path.pop()
        vis[u] = 2
    
    for i in range(1, N + 1):
        if vis[i] == 0:
            path = []
            dfs_cycle(i, path)
            if cycle_start != -1:
                cycle = path[cycle_start:]
                break
    
    C = len(cycle)
    for i in range(C):
        cid = cycle[i]
        in_cycle[cid] = True
        cycle_id[cid] = i
    
    # Build tree structure: from cycle outwards (reverse edges)
    # We will compute depth and parent for every node
    depth = [0] * (N + 1)
    parent = [0] * (N + 1)
    tree = [[] for _ in range(N + 1)]  # children in tree (out from cycle)
    
    # BFS from cycle nodes using reverse edges, but only non-cycle incoming
    from collections import deque
    q = deque()
    for i in range(1, N + 1):
        if in_cycle[i]:
            depth[i] = 0
            parent[i] = i  # self for cycle
            q.append(i)
    
    while q:
        u = q.popleft()
        for prev in rev[u]:
            if in_cycle[prev]:
                continue  # cycle edge already handled
            if depth[prev] == 0 and not in_cycle[prev]:  # not visited
                depth[prev] = depth[u] + 1
                parent[prev] = u
                tree[u].append(prev)
                q.append(prev)
    
    # For each cycle node, compute the "entry" points from paths
    # But we need distances along the functional graph (forward)
    
    # Precompute for each node the distance to its cycle entry point
    dist_to_cycle = [0] * (N + 1)
    entry = [0] * (N + 1)  # which cycle node it enters
    
    for i in range(1, N + 1):
        if in_cycle[i]:
            dist_to_cycle[i] = 0
            entry[i] = i
        else:
            # follow parents until cycle
            cur = i
            d = 0
            while not in_cycle[cur]:
                cur = parent[cur]
                d += 1
            dist_to_cycle[i] = d
            entry[i] = cur
    
    # Now, for two nodes A and B, we need min meeting time
    # Meeting point can be on cycle or on some path
    # But since paths are trees pointing inward, meeting on path only if one is ancestor of other
    
    def dist(u, v):
        # distance following edges from u to v, if v is reachable from u
        if u == v:
            return 0
        d = 0
        cur = u
        while cur != v:
            cur = F[cur]
            d += 1
            if d > N:  # safety
                return -1
        return d
    
    # But we need efficient way for many queries
    
    # Key observation: the only places where paths meet are on the cycle.
    # Any two paths eventually lead to the cycle.
    # So possible meeting points are:
    # 1. On the path from A to cycle (if B can reach it)
    # 2. On the path from B to cycle (if A can reach it)
    # 3. On the cycle
    
    # Since movement is only forward, the reachable set from a node is the path to cycle and then the whole cycle.
    
    # The time to meet at a city X is max(timeA to X, timeB to X) if both can reach X.
    # We want the min over all possible X of that max.
    
    # Since graph is functional, from any node there is exactly one path.
    # So the nodes reachable from a city X are exactly the nodes on the unique path from X following F.
    
    # So for two starting cities A and B, the possible meeting points X are the intersection of the two paths from A and from B.
    # The intersection will be a suffix of both paths (after they merge).
    
    # The first common node on both paths is the merge point, and then everything after.
    # So the possible X are from the merge point onwards (including the cycle loop).
    
    # To minimize max(dist(A,X), dist(B,X)).
    # Since after merge, the path is the same, let M be the first merge point.
    # Then for X on the common path, let da = dist(A,M), db = dist(B,M)
    # For a point X that is k steps after M, time = max(da + k, db + k)
    # Which is max(da,db) + k. So minimum is when k=0 i.e. at M: max(da, db)
    # But if they go around the cycle, it might be possible to meet earlier? No, because going further increases both by same amount.
    
    # But if one is already on cycle and other enters later, or if they are on cycle.
    
    # Actually, once on cycle, you can keep looping, but since it's a cycle, the meeting point can be any point on cycle, and you can choose how many laps.
    
    # But because both move simultaneously, it's more subtle on cycle.
    
    # Let's classify.
    
    # First, find the entry point of A and B to the cycle.
    # Let EA = entry[A], distA = dist_to_cycle[A]
    # EB = entry[B], distB = dist_to_cycle[B]
    
    # If the path from A and B merge before cycle, then the merge point M is the first common node.
    # If one path is completely on the path of the other, then one can reach the other's position.
    
    # Case 1: if one node is reachable from the other.
    # That is, if following from one we hit the other.
    # Then they can meet at the later one, time = distance between them.
    # Since the other can stay or move? No, both can move, but if one is upstream, the downstream one must move forward while the upstream catches up.
    # If A can reach B by following edges, then dist(A,B) = d, then A can go to B in d steps, B can go forward and come back? But since it's functional, once B leaves, to meet at some point, it's complicated.
    
    # Let's think again.
    
    # Since both move at speed 1 or can they stay? The problem says "ambas podem se deslocar simultaneamente", but I think they must move or can they stay? No, the problem is to meet at a city, and each edge takes 1 time, but they can choose paths.
    # But since only one outgoing, they have no choice, they can only follow the unique path.
    # But they can choose when to start? No.
    # The problem is they move simultaneously, each step they both traverse one edge or ? The problem says "considerando que cada estrada é percorrida em uma unidade de tempo".
    # But since only one way, the position at time t for a person starting at X is F^t(X).
    # So at time t, person from A is at iterate F t times from A, person from B at iterate from B.
    # They meet at time t if F^t(A) == F^t(B).
    # We want the minimal such t >= 0.
    # That's the correct interpretation!
    # Because there is no choice of path, only one outgoing edge from each city.
    # So they both follow their unique path, and we want the smallest t where their positions coincide.
    
    # Yes, that makes sense with the sample.
    # In sample:
    # F = [-,2,6,1,6,2,5] so 1->2, 2->6, 3->1, 4->6, 5->2, 6->5
    # Cycle is 2->6->5->2
    # For 4 and 3:
    # 4 ->6 ->5 ->2 ->6 ->5...
    # 3 ->1 ->2 ->6 ->5 ->2...
    # At t=0: 4 and 3
    # t=1: 6 and 1
    # t=2: 5 and 2
    # t=3: 2 and 6
    # t=4: 6 and 5
    # t=5: 5 and 2
    # They never at same at same time? But sample says 3 for 4 3.
    # The sample output first is 3.
    # But according to this at t=3: 2 and 6 different.
    # So my interpretation is wrong.
    
    # The problem says "ambas podem se deslocar simultaneamente para chegar ao ponto de encontro."
    # "the point of meeting can be different from initial cities"
    # So they can choose to stop at some city? Or what?
    # No, but in functional graph with outdegree 1, if they keep moving they loop.
    # But the sample says people in 4 and 3 can meet at 2 or 6 in time 3.
    # From 4 to 2: 4->6->5->2 : 3 steps
    # From 3 to 6: 3->1->2->6 : 3 steps
    # Yes, so they arrive at different points at time 3.
    # So they don't have to be at same position at same time following blindly.
    # They can choose where to stop? But the graph has only one outgoing, but perhaps they can stay in a city?
    # The problem is about moving along edges, but to meet at a city, meaning both reach that city, and the time is the max of the times they take to reach it, since they move simultaneously.
    # Yes, that matches.
    # "o tempo mínimo em que elas podem se encontrar", "ambas podem se deslocar simultaneamente"
    # So it's the min over all cities X of max( dist(A,X), dist(B,X) ), where dist is the length of the path from start to X if exists, else inf.
    # Yes, and since they move at same speed, the time to meet at X is the max of their individual travel times to X.
    # And we take the min such over all possible X that both can reach.
    
    # Yes, and in sample:
    # For 4 and 3:
    # From 4 path: 4,6,5,2,6,5,2... so can reach 4,6,5,2
    # From 3 path: 3,1,2,6,5,2,6... so 3,1,2,6,5
    # Common reachable: 6,5,2
    # dist(4,6)=1, dist(3,6)=3, max=3
    # dist(4,5)=2, dist(3,5)=4, max=4
    # dist(4,2)=3, dist(3,2)=2, max=3
    # So min max is 3. Yes.
    # For 1 and 3:
    # 1 path: 1->2->6->5->2...
    # 3 path: 3->1->2->6...
    # Common: 1,2,6,5
    # dist(1,1)=0, dist(3,1)=1, max=1
    # Yes, meet at 1 in time 1 (3 goes to 1, 1 stays).
    # Is staying allowed? Apparently yes, time 0 to stay at own city.
    # For 6 and 3:
    # 6 path: 6->5->2->6...
    # 3: 3->1->2->6->5...
    # Common: 2,6,5
    # dist(6,2)=2 (6-5-2), dist(3,2)=2 (3-1-2), max=2
    # dist(6,6)=0, dist(3,6)=3, max=3
    # So min 2. Matches sample.
    # Perfect.
    
    # So now, we need for many queries, given A B, find min over all X reachable from both A and B of max( dist(A,X), dist(B,X) )
    
    # Since the structure is paths leading to a single cycle, the reachable from a node is the chain from it to the cycle, then the entire cycle.
    
    # So, first, if A and B are such that one's path passes through the other, then we can meet at the downstream one with max(dist,0).
    
    # To compute efficiently.
    
    # First, let's assign each node its "chain" or depth from cycle as above.
    # We have dist_to_cycle[u]: steps to reach the cycle.
    # entry[u]: the cycle city it reaches first.
    
    # The cycle cities have positions 0 to C-1.
    # Let's number cycle as cycle[0], cycle[1], ..., cycle[C-1], where F[cycle[i]] = cycle[(i+1)%C]
    
    # dist on cycle from cycle[i] to cycle[j] is (j - i) mod C.
    
    # Now, for a node u not on cycle, the path is u -> ... -> entry[u], then follows cycle.
    # The nodes on its path before cycle are unique to its "tail".
    
    # To find common reachable nodes.
    # The common reachable are:
    # - If one tail contains the other (one is on the path of the other), then the downstream part.
    # - The cycle is always common after they both enter.
    
    # So, cases:
    
    # 1. If A is on the path from B to cycle (i.e. B can reach A), then A is reachable from B, and from A everything after A is reachable from both.
    #    Then possible X = from A onwards (including cycle).
    #    Then the min max time is 0 if we meet at A (B takes dist(B,A), A takes 0).
    #    Wait, max(dist(B,A), 0) = dist(B,A)
    #    But we can also meet later on cycle perhaps with smaller max? No, because later would be at least that.
    #    No, max would be at least dist(B,A) since B has to travel at least that to reach A or later.
    #    So time = dist(B,A)
    
    # Similarly if B on path from A.
    
    # 2. If neither is on the other's path, then the tails don't overlap, so common reachable only on the cycle.
    #    So we need to find best meeting point on the cycle.
    
    # For meeting on cycle:
    # Let EA = entry[A], DA = dist_to_cycle[A]
    # EB = entry[B], DB = dist_to_cycle[B]
    # To reach a cycle city X, from A: time = DA + dist_on_cycle(EA, X)
    # from B: DB + dist_on_cycle(EB, X)
    # We want min over X on cycle of max( DA + d(EA,X), DB + d(EB,X) )
    # Where d(u,v) is steps on cycle from u to v (only forward).
    
    # Since it's a cycle, we can compute this efficiently.
    
    # Also, for the case where paths merge on cycle, it's included.
    
    # If the two tails merge before cycle? In this graph, since in_degree <=1 for non-cycle, the tails are disjoint until cycle.
    # The constraint: "A cada cidade pertencente a um caminho periférico chega no máximo uma estrada"
    # "to each city not on cycle at most one incoming"
    # So the peripheral paths are trees? No, since outdegree=1, indegree<=1 for non-cycle, so they are disjoint paths leading into cycle.
    # No branching inward.
    # So tails are just paths, no merging before cycle.
    # Therefore, no node on two different tails.
    # So, only if one node is on the path of the other, which can only happen if they are on the SAME tail/path.
    # I.e., one is ancestor of the other in the chain to the cycle.
    
    # To check if A and B are on same chain: if entry[A] == entry[B] and then see depths.
    
    # Since it's a path, the one with larger depth is further out.
    # If entry same, then the one with bigger dist_to_cycle is upstream.
    # Say if DA > DB, then if following from A exactly DA-DB steps reaches B, then yes B is downstream from A.
    # But since no branching, and same entry, yes all on one path are linearly ordered by depth.
    # Since indegree <=1, from one entry point, there is at most one path coming in.
    # But multiple paths can enter at different cycle nodes.
    # For same entry point, there is only one direct predecessor, so it's a single chain per entry point.
    # Yes.
    # So if entry[A]==entry[B], let’s say u = the one with larger depth, v = smaller depth.
    # Then since linear, v is reachable from u, dist(u,v) = depth[u]-depth[v]
    # Then, they can meet at v with time = depth[u]-depth[v]  (u travels that, v stays)
    # They can also meet further on cycle, but that would require u to travel more than that, so max at least that, so the min is exactly that difference.
    
    # If they have different entries, then cannot reach each other's tail, so only meet on cycle.
    
    # If one is on cycle and other not, if entry of other is the one on cycle? If A on cycle, DA=0, EA=A.
    # If B has entry[A], then if A is on the path? Since A on cycle, only if B's path enters at A, then the entry is A, so same entry, and since DA=0 < DB, then time = DB - 0 = DB, i.e. B goes to A, A stays. Yes correct.
    
    # Now, if different entries or not on same chain, then only cycle.
    
    # So now, we need a way to compute for two points on cycle EA, EB, with offsets DA, DB,
    # the min_X max(DA + d(EA,X), DB + d(EB,X)) over all X on cycle.
    
    # Since C can be up to 1e5, but N=1e5, Q=1e5, we need O(1) or O(log) per query after preprocess.
    
    # Let's represent cycle positions as 0 to C-1.
    # Let pos[city] = cycle_id[city]
    # So let pa = cycle_id[EA], pb = cycle_id[EB]
    # d from a to x: if x >= a: x-a else x-a + C
    # No, since directed cycle.
    # From position i, after k steps: (i + k) % C
    # So distance from i to j is (j - i) mod C.
    
    # Let da(x) = DA + ((x - pa) % C)
    # db(x) = DB + ((x - pb) % C)
    # We want min over x=0..C-1 of max( da(x), db(x) )
    
    # This is a classic problem, can be solved by considering the points where da(x)=db(x), or using ternary search since it's unimodal? 
    # Actually, as x increases, both da and db increase by 1 each step, but when wrapping, it jumps.
    # No, (x - p % C) increases by 1 mod C, but the value increases by 1 until wrap then jumps down? No.
    # As x goes 0 to C-1 sequentially in cycle order, but to evaluate for each.
    # But since it's circular.
    
    # One way is to notice that the function f(x) = max(DA + d(pa,x), DB + d(pb,x))
    # d(pa,x) = (x - pa) mod C
    # To find min max.
    
    # A standard way for this is to consider the latest entry time.
    # Both will reach the cycle at time DA and DB, but at different points.
    # Then they continue moving on cycle.
    # But since we can choose any meeting point, it's like one may wait by looping extra laps.
    # But since looping extra lap costs C time for both? No.
    # Since they arrive at their entry at time = their DA/DB, then from there they can move further on cycle.
    # So the time to reach a point X is as above.
    
    # To compute min max without O(C):
    # Let's assume wlog DA >= DB. No.
    # Let’s consider the relative position.
    # Let diff = (pa - pb) % C
    # We can iterate over possible "extra laps" but since C large not good.
    
    # Notice that f(x) = max( DA + d(pa,x), DB + d(pb,x) )
    # Let d1(x) = (x - pa) % C
    # d2(x) = (x - pb) % C
    # f(x) = max(DA + d1(x), DB + d2(x))
    # As x increases, both d1 and d2 increase by 1 every step, until one laps but since we take % it's sawtooth but actually since we consider all x, but to find min max.
    
    # There is a way: the optimal meeting point will be such that the max is achieved by both or one just after the other.
    # We can consider for each possible "target" relative.
    
    # Let's think the time t must be at least max(DA, DB), because to reach cycle.
    # But if they meet on tail, we already handled.
    # For cycle meeting, t >= max(DA, DB)
    # For a given t, can they both reach some common X by time <=t ?
    # But since Q large, better closed form.
    
    # From a fixed starting on cycle, the positions one can be at time t is only one: after (t - D) steps from entry.
    # No, wait: since they can only move forward or... wait.
    # In the problem, do they have to keep moving? Or can they stop at a city?
    # From the sample, when meeting at 1 for persons at 1 and 3, the one at 1 stays, doesn't move.
    # So yes, they can stop. So once they reach a city, they can stay there forever.
    # That's important.
    # So, the time to reach X is the exact steps if X is on the path, and once reached, they can wait.
    # So dist(A,X) is the exact number of steps to first reach X, and then they can wait so any time >= that they can be at X.
    # Therefore, to meet at X, the time needed is max( timeA_to_X, timeB_to_X ), yes.
    # And since after reaching cycle, because it's a cycle, from the entry, you can reach any city on cycle by going enough steps, and since you can wait, but wait where?
    # If you can stop at any city, then once you reach the cycle, you can go to any point on cycle and stop there.
    # Yes.
    # So time for A to reach a cycle city X is DA + d(EA, X), and then can stay.
    # Yes, same as before.
    
    # Now, to find min t = min over X max( tA(X), tB(X) )
    
    # Since on tails, only if on same chain.
    
    # For cycle part, since you can reach any X on cycle from any entry.
    # Yes.
    
    # To compute that min over cycle.
    # Because you can lap around as many times as you want, but since you can stop, lapping would only make you take longer to reach a point, so optimal is without full laps, i.e. d is between 0 and C-1.
    # So X ranges over the C cities, d=(posX - posEntry) mod C , yes 0 to C-1.
    # So we have to consider all C possibilities, but C=1e5, Q=1e5, cannot loop per query.
    
    # We need O(1) or amortized fast way.
    
    # Let's find a formula for min over x max( DA + ((x-pa)%C) , DB + ((x-pb)%C) )
    
    # Let’s denote offset1 = DA - pa
    # offset2 = DB - pb
    # Then DA + (x - pa)%C = (DA - pa) + (x % C) but % is tricky.
    # Let’s fix the positions 0 to C-1.
    # Without loss of generality, we can assume pa = 0 by rotating.
    # Let’s set pa = 0, then we have pb' = (pb - pa) % C
    # Let d = (pb - pa) % C
    # Then f(x) = max( DA + (x % C), DB + ((x - d) % C) )  wait x from 0 to C-1, (x - pa)%C = x since pa=0.
    # d(pb, x) = (x - pb) % C = (x - (pa + d)) %C = (x - d) % C
    # Yes.
    # So min over x=0 to C-1 of max( DA + x , DB + (x - d mod C) ) where x here is distance from pa.
    # Let k = x, from 0 to C-1, costA = DA + k
    # costB = DB + ((k - d + C) % C)   wait (x - d) % C
    
    # (k - d) mod C.
    # Now, the function costA(k) = DA + k   increasing
    # costB(k) = DB + (k - d) mod C   which is increasing with jumps down by C when crossing.
    
    # To find where they intersect etc.
    # The max of two functions, one increasing linear, other is increasing but resets every cycle but since only one cycle range.
    # Since k from 0 to C-1, (k - d mod C) = k-d if k>=d else k-d+C
    
    # So, if we split the range at k = d.
    
    # For k = 0 to d-1: (k-d +C) = k + (C-d)
    # costB = DB + k + (C - d)
    # costA = DA + k
    # So max(DA+k, DB + C - d + k )
    # Which is k + max(DA, DB + C - d)
    # So in this range, it's increasing, min in this range is at k=0: max(DA, DB+C-d)
    
    # For k = d to C-1:
    # (k - d) mod = k-d
    # costB = DB + k - d
    # costA = DA + k
    # max( DA+k , DB - d + k ) = k + max(DA, DB - d)
    # Again linear increasing.
    # So min in this segment at k=d: d + max(DA, DB-d)
    
    # Therefore, the possible candidates for minimum are only two points: at k=0 and at k=d.
    # The min f is the min of :
    # max(DA, DB + C - d)     # at k=0
    # and  d + max(DA, DB - d)   # at k = d
    
    # Is that all? Since in both segments f(k) = k + constant, so yes increasing in each, so minima at the beginning of each segment.
    # The segments are 0 to d-1 and d to C-1, so yes, check at k=0 and k=d.
    # But is there the wrap around? Since we only go one cycle, but because if you go more than C it would be DA+k with k>=C which is larger than DA+k-C +C = same as going less but since can stop, no need to go more.
    # Yes.
    
    # Let's verify with sample.
    # Take A=4, B=3
    # 4: path 4->6, so entry=6, DA=1 (dist_to_cycle[4]=1)
    # 3: 3->1->2, entry=2? From 3->1->2, and 2 is on cycle, dist=2
    # Cycle: from figure, cycle 2->6->5->2, so cycle[0]=2,1=6,2=5 ?
    # F[2]=6, F[6]=5, F[5]=2.
    # So positions: let’s say pos[2]=0, pos[6]=1, pos[5]=2.
    # EA=6, pa=1, DA=1
    # EB=2, pb=0, DB=2
    # d = (pb - pa) % 3 = (0 - 1)%3 = 2
    # In my earlier, I set pa=0, but let's use general.
    # In formula I set pa=0, d=(pb-pa)%C =2
    # Then min of :
    # max(DA, DB + C - d) = max(1, 2 + 3 -2) = max(1,3)=3
    # and d + max(DA , DB - d) = 2 + max(1, 2-2)=2 + max(1,0)=2+1=3
    # Yes, min=3. Correct.
    
    # Another: A=6, B=3
    # A=6 on cycle, DA=0, EA=6 pa=1
    # B=3, EB=2 pb=0, DB=2
    # Same as above but DA=0 now.
    # max(0, 2+3-2)=max(0,3)=3
    # 2 + max(0,2-2)=2+max(0,0)=2
    # min=2. Yes matches.
    
    # Another: 1 and 3.
    # But 1 is not on cycle. 1->2, so entry of 1 is 2, dist_to_cycle[1]=1
    # B=3, entry=2, dist=2
    # Same entry! So this is the chain case.
    # entry same=2, dist1=1, dist3=2 >1, so the upstream is 3, downstream 1, time = 2-1 =1. Yes matches sample.
    # If we had used cycle formula wrongly: EA=2 pa=0, DA=1 for1
    # EB=2 pb=0 DB=2 for3
    # d=(0-0)%3=0
    # Then max(1,2+3-0)=max(1,5)=5
    # 0 + max(1,2-0)= max(1,2)=2
    # min=2 , but actual is 1, which is better, by meeting at 1 before cycle. Yes, so we must handle the same chain case first.
    
    # Another sample: 5 and 2.
    # 5 on cycle, DA=0, entry=5 pos=2
    # 2 on cycle, entry=2 pos=0, DB=0
    # Different "entries" but both on cycle.
    # d=(0 - 2)%3 = ( -2 %3)=1
    # max(0,0+3-1)=max(0,2)=2
    # 1 + max(0,0-1)=1 + max(0,-1)=1+0=1
    # min=1. And sample output 1. Yes.
    # What does it mean? Meeting at ? With t=1.
    # From 5 at t=1 goes to 2, from 2 at t=0 stays? But if d=1, k=d=1, which is from pa=2 (pos5=2), k=1 reaches (2+1)%3=0 which is pos 2. Yes, 5 goes to 2 in 1 step, 2 stays at 2. max(1,0)=1.
    # Perfect.
    
    # Last sample 2 2: 0.
    
    # Great.
    
    # Now, if d=0 and DA,DB, if same position on cycle, then min of max(DA,DB +C)= big, and 0 + max(DA,DB)=max(DA,DB)
    # Yes, which is correct, meet at that city, time max(DA,DB).
    
    # Excellent. So only these two candidates.
    
    # So in general, for any pa,pb,DA,DB,C:
    # Let delta = (pb - pa) % C
    # Then the two options:
    # opt1 = max(DA, DB + C - delta)
    # opt2 = delta + max(DA, DB - delta)
    # Then min(opt1, opt2)
    # In above when pa=1 pb=0, delta=(0-1)%3=2, as above worked.
    # When pa=2 pb=0, delta=(0-2)%3=1, worked.
    # When same pa=pb=0, delta=0,
    # opt1 = max(DA,DB+C-0)=max(DA,DB+C)
    # opt2 = 0 + max(DA, DB -0 ) = max(DA,DB)
    # Yes, takes the min which is max(DA,DB). Perfect.
    
    # Is this always the min?
    # Suppose C=5, DA=0, DB=0, pa=0, pb=2, delta=2
    # opt1 = max(0,0+5-2)=3
    # opt2 =2 + max(0,0-2)=2+0=2
    # So 2.
    # Is there better? At k=0: max(0+0,0+(0-2)%5=3 )=max(0,3)=3
    # At k=2: max(0+2, 0+(2-2)%5=0)=max(2,0)=2
    # At k=3: max(3,1)=3
    # At k=4:4,2 ->4
    # At k=1:1, (1-2)%5=4, max(1,4)=4
    # Yes min is 2. Good.
    
    # Another example, suppose DA=5, DB=1, pa=0, pb=0, delta=0
    # Then since same entry, but if on cycle DA=5? If on cycle dist=0.
    # But if different, wait.
    # Suppose pa=0, pb=1, delta=1, DA=0, DB=0, C=5
    # opt1=max(0,0+5-1)=4
    # opt2=1+max(0,0-1)=1+0=1
    # Yes, meet at pb, time 1: from pa=0 go 1 step to pos1, from pb stay. Yes.
    
    # Seems correct.
    
    # Is there case where the min is not at these?
    # Suppose the increasing parts, since in each piece it's increasing with slope 1, the min must be at the start of a piece, which are k=0 (from pa) and k=delta (from pb?).
    # k=0 is at EA, k=delta is at EB, because from pa, after delta steps: pa + delta = pb, since delta = pb-pa mod.
    # Yes! So the two candidates are simply:
    # - Meet at EA: time = max(DA + 0, DB + dist(EB, EA) )
    # - Meet at EB: time = max(DA + dist(EA, EB), DB + 0 )
    # And since after that, if you go further, the max can only stay or increase.
    # But is the global min always at one of the two entry points??
    # In previous examples yes.
    # In first, EA=6, EB=2
    # Meet at 6: max(1+0, 2 + dist(2 to 6))
    # From 2->6 is 1 step (2->6), so max(1, 2+1)=3
    # Meet at 2: max(1 + dist(6 to 2), 2+0)
    # From 6->5->2 : 2 steps, max(1+2,2)=3
    # Yes.
    # For 6 and 3: EA=6 DA=0, EB=2 DB=2
    # Meet at 6: max(0, 2 + dist(2,6)=1 ) = max(0,3)=3
    # Meet at 2: max(0 + dist(6,2)=2 , 2 ) = max(2,2)=2
    # Yes.
    # For 5 and 2: EA=5 pos2 DA0, EB=2 pos0 DB0
    # dist(5 to 2): from 5->2 :1 step (5->2), max(0+1,0)=1
    # dist(2 to 5): 2->6->5 :2 steps, max(0+2,0)=2
    # min(1,2)=1. Yes.
    # Perfect! So even simpler: when meeting on cycle, the optimal is always to meet at one of the two entry points!
    # Because the max will be smallest at one of them.
    # If you meet further, both have to travel more, so max increases or stays but not smaller.
    # Yes.
    
    # So, in code, for cycle meeting: min(
    #   max(DA, DB + cycle_dist(EB, EA) ),
    #   max(DA + cycle_dist(EA, EB), DB )
    # )
    # Where cycle_dist(u,v) = (pos[v] - pos[u] + C) % C
    
    # Yes.
    
    # Now, for the chain case: if same_entry and not on cycle or whatever.
    # If entryA == entryB:
    #   Let depA = dist_to_cycle[A]
    #   depB = dist_to_cycle[B]
    #   if depA > depB:
    #       time_chain = depA - depB   # A goes to B's position
    #   elif depB > depA:
    #       time_chain = depB - depA
    #   else:
    #       time_chain = 0
    #   Then, this is a possible, and we take min( time_chain, the cycle_meet_time )
    #   But if they are on same chain, meeting before cycle at the downstream one gives smaller or equal.
    #   In the example of 1 and 3: dep1=1, dep3=2, same entry 2.
    #   time_chain = 2-1=1
    #   cycle meet as above would be max(1,2)=2 at entry, so min(1,2)=1 correct.
    #   If both on cycle, dep=0 same, time_chain=0, which is correct.
    #   If one on cycle one on its tail: say A on entry, depA=0, B on tail depB=5, time_chain=5, cycle would be max(0,5 + dist(EB,EA)=0 since EB=EA)=5, same.
    
    # If different entries, then only the cycle one.
    
    # Also if A==B, time=0.
    
    # Now, one more: can they meet on the tail of one if the other enters the cycle and loops around to come back? No, because from cycle you cannot go to the peripheral paths, since peripherals are incoming to cycle, not outgoing.
    # The paths are one way into the cycle, from cycle you stay in cycle.
    # So cannot reach the tail from cycle. So only if on same tail.
    
    # Perfect.
    
    # So now, to detect if on same chain: if entry[A] == entry[B], then yes.
    # Because each entry has only one incoming path.
    
    # Yes, due to indegree <=1.
    
    # Now, we need to compute for nodes not on cycle their entry and depth.
    # We already have in earlier code.
    
    # For nodes on cycle, entry[u]=u, depth=0.
    
    # Also for cycle_dist.
    
    # Now, let's implement.
    
    # First, find the cycle properly.
    # In the beginning I had a dfs to find cycle, but since N=1e5, recursion may fail, although setrecursionlimit.
    # Better use iterative.
    
    # Standard way to find cycle in functional graph.
    
    # Since exactly one cycle.
    
    vis = [0] * (N+1)
    cycle = []
    for i in range(1,N+1):
        if vis[i]: continue
        path = []
        x = i
        while not vis[x]:
            vis[x] = 1
            path.append(x)
            x = F[x]
        # now x is visited
        if not in_cycle[x] and x in path:  # wait better mark after.
    # Better standard:
    
    vis = [0] * (N+1) # 0 not, 1 in path, 2 done
    cycle_nodes = set()
    for i in range(1, N+1):
        if vis[i] != 0: continue
        x = i
        path = []
        seen_in_path = {}
        while vis[x] == 0:
            vis[x] = 1
            path.append(x)
            seen_in_path[x] = len(path)-1
            x = F[x]
        if vis[x] == 1:  # cycle
            if x in seen_in_path:
                idx = seen_in_path[x]
                for node in path[idx:]:
                    cycle_nodes.add(node)
                    in_cycle[node] = True
        # now set done
        for node in path:
            vis[node] = 2
    
    # Now cycle_nodes has the cycle.
    # But we need ordered cycle.
    # Pick any on cycle, follow until back.
    if not cycle_nodes:
        # shouldn't happen
        pass
    start = next(iter(cycle_nodes))
    cycle = []
    x = start
    while True:
        cycle.append(x)
        x = F[x]
        if x == start: break
    C = len(cycle)
    cycle_id = [-1] * (N+1)
    for i in range(C):
        cycle_id[ cycle[i] ] = i
        in_cycle[ cycle[i] ] = True
    
    # Now build the incoming tree, but since indegree 1, it's chains.
    # Compute for every node the entry and dist_to_cycle.
    # Since no recursion needed, we can go backwards from cycle.
    # But since we have rev graph.
    
    dist_to_cycle = [0] * (N+1)
    entry_point = list(range(N+1))  # default self
    for i in range(1,N+1):
        if in_cycle[i]:
            entry_point[i] = i
            dist_to_cycle[i] = 0
    
    # Now, process nodes in topological reverse, i.e. from cycle out.
    # Since it's chains, we can start from nodes whose F points to processed.
    processed = [False] * (N+1)
    for i in range(1,N+1):
        if in_cycle[i]:
            processed[i] = True
    
    q = deque([i for i in range(1,N+1) if in_cycle[i]])
    while q:
        u = q.popleft()
        for pre in rev[u]:  # nodes that point to u
            if processed[pre]: continue
            # then pre -> u
            if not in_cycle[pre]:
                entry_point[pre] = entry_point[u]
                dist_to_cycle[pre] = dist_to_cycle[u] + 1
                processed[pre] = True
                q.append(pre)
    
    # Now all should be processed since connected to cycle? There is at least one peripheral.
    # But constraint says there is exactly one cycle, at least one not on cycle.
    
    # Now, for cycle dist
    def cdist(p1, p2):
        # dist from p1 to p2 on cycle
        return (cycle_id[p2] - cycle_id[p1] + C) % C
    
    # Now, for each query
    answers = []
    for a, b in queries:
        if a == b:
            answers.append(0)
            continue
        ea = entry_point[a]
        eb = entry_point[b]
        da = dist_to_cycle[a]
        db = dist_to_cycle[b]
        if ea == eb:
            # same chain
            time_chain = abs(da - db)
            # also cycle but will be >= 
            t1 = max(da, db + cdist(eb, ea))
            t2 = max(da + cdist(ea, eb), db)
            t_cycle = min(t1, t2)
            ans = min(time_chain, t_cycle)
            answers.append(ans)
        else:
            # only cycle
            t1 = max(da, db + cdist(eb, ea))
            t2 = max(da + cdist(ea, eb), db)
            ans = min(t1, t2)
            answers.append(ans)
    
    for ans in answers:
        print(ans)

if __name__ == "__main__":
    main()
