
import sys
sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index]); index += 1
    M = int(data[index]); index += 1
    I = int(data[index]); index += 1
    
    age = [0] * (N + 1)
    for i in range(1, N + 1):
        age[i] = int(data[index]); index += 1
    
    adj = [[] for _ in range(N + 1)]
    parent = [0] * (N + 1)
    for _ in range(M):
        X = int(data[index]); index += 1
        Y = int(data[index]); index += 1
        adj[X].append(Y)
        parent[Y] = X
    
    # Find roots
    roots = set(range(1, N + 1))
    for i in range(1, N + 1):
        if parent[i]:
            roots.discard(i)
    
    # For each tree, compute subtree and build euler tour + rmq prep
    # We will have one big structure for all trees
    first = [-1] * (N + 1)
    depth = [0] * (N + 1)
    euler = []
    euler_age = []
    euler_node = []
    pos = 0
    
    def dfs(u, d):
        nonlocal pos
        first[u] = pos
        depth[u] = d
        euler.append(pos)
        euler_age.append(age[u])
        euler_node.append(u)
        pos += 1
        for v in adj[u]:
            dfs(v, d + 1)
            euler.append(first[u])
            euler_age.append(age[u])
            euler_node.append(u)
            pos += 1
    
    for root in roots:
        dfs(root, 0)
    
    # Build sparse table for RMQ on euler_age (minimum age in range)
    if not euler_age:
        euler_age = [0]
    n_euler = len(euler_age)
    logn = 0
    while (1 << logn) <= n_euler:
        logn += 1
    st = [[0] * logn for _ in range(n_euler)]
    for i in range(n_euler):
        st[i][0] = i  # store index of minimum
    
    for j in range(1, logn):
        for i in range(n_euler):
            if i + (1 << j) - 1 >= n_euler:
                break
            left = st[i][j - 1]
            right = st[i + (1 << (j - 1))][j - 1]
            if euler_age[left] <= euler_age[right]:
                st[i][j] = left
            else:
                st[i][j] = right
    
    def rmq_min(L, R):
        if L > R:
            L, R = R, L
        length = R - L + 1
        k = 0
        while (1 << (k + 1)) <= length:
            k += 1
        left = st[L][k]
        right = st[R - (1 << k) + 1][k]
        if euler_age[left] <= euler_age[right]:
            return left
        return right
    
    def get_min_age(u):
        if first[u] == -1:
            return -1  # shouldn't happen
        # Find the highest ancestor: the one with minimal depth in the path from root to u
        # In euler tour, the first occurrence of the subtree is the entry, but to get manager we need ancestors
        # Actually, since managers are ancestors, the managers of u are all nodes from root to parent of u
        # In the euler tour technique for LCA, the min depth between first[root] and first[u] gives LCA, but here we need min age among all ancestors.
        # So we need to precompute for each node the min age in its path from root.
    
    # The above approach with one dfs per tree and euler for LCA is not directly giving min on path from root.
    # Let's change strategy.
    # Since N<=500, we can afford O(N^2) preprocessing per "version", but with M=60k updates it's too much.
    # Updates are swaps of positions.
    # Swapping two employees A and B means they exchange their places in the hierarchy.
    # That is, their incoming and outgoing edges are swapped in a specific way.
    # This is a tree (forest), and swapping two nodes' positions.
    
    # Because N=500, we can maintain the current parent array and for each query do a DFS or BFS from the employee upwards, keeping track of min age.
    # But with I<=500 and N=500, if every query we traverse up the tree, worst case tree is a chain, 500*500=250k operations per test? But there are multiple tests? No, single test.
    # The input has only one test case.
    # I up to 500, N=500, if every query walks 500, total time is 250000 operations, perfectly fine.
    # But there are T operations mixed with P.
    # The constraint is I <= 500, yes!
    # Look back: 1 ≤ I ≤ 500
    # Yes! I is number of instructions, up to 500.
    # And N<=500, M<=60k but M is initial edges.
    # So with I=500, N=500, we can afford to, for each P query, walk from E up to the root, collecting the minimum age of all managers (all ancestors).
    # That would be at most 500*500 = 250k operations, which is acceptable in Python.
    
    # We need to maintain the current hierarchy, i.e., the parent of each node.
    # When we do a swap T A B, we need to swap the positions of A and B.
    # What does "trocarem suas posições na cadeia de comando" mean exactly?
    # From the example, it means that A and B exchange their roles: the subordinates of A now report to B, and vice versa, and their managers also swap.
    # In other words, the entire subtree and the parent link are swapped.
    # Looking at the sample:
    
    # Initial:
    # Ages: 1:21, 2:33, 3:33, 4:18, 5:42, 6:22, 7:26
    # Edges:
    # 1->2, 1->3, 2->5, 3->5, 3->6, 4->6, 4->7, 6->7
    # So forest with root 1 and root 4.
    # Tree1: 1 (21) -> 2(33) ->5(42)
    #       \-> 3(33) ->5(42)
    #             \->6(22)->7(26)
    # Tree2: 4(18) ->6(22)->7(26)
    #           \->7(26)
    # Note there are multiple parents? 5 has two managers? 2 and 3 both manage 5.
    # 6 has 3 and 4, 7 has 4 and 6.
    # It's not a tree! It's a DAG! Multiple parents allowed.
    # "cadeia de comando", but from description, a person can have multiple managers.
    # In the problem statement: "uma pessoa pode gerenciar outras pessoas, e pode ser gerenciada por outras pessoas"
    # So it's a general DAG, not necessarily a tree.
    # That changes things.
    # With N=500, M=60k, it's dense.
    # For queries, "o mais jovem gerente (direto ou indireto) de A"
    # So all ancestors in the DAG, find the one with minimal age.
    # And if no manager, print *
    # Updates: swap positions of A and B.
    # This is tricky in a DAG.
    # What does swapping positions mean in a DAG?
    # It means that all incoming edges to A now go to B, all outgoing from A now from B, and same for B.
    # In other words, A and B swap their identities in the graph.
    # But ages stay with the person.
    # The example will tell us.
    
    # Let's look at first sample.
    # Initial graph:
    # Managers of 7: from edges 4->7, 6->7 so parents of 7 are 4 and 6.
    # P 7 -> min age of managers of 7, which are 4(18),6(22), and their managers.
    # Managers of 4? none in list. Managers of 6: 3 and 4.
    # So ancestors of 7: 4,6,3,1 (since 3->6,1->3),2? no.
    # Ages: 4:18, 6:22, 3:33, 1:21. So youngest is 18. Matches first output 18.
    # Then T 4 2 : swap 4 and 2.
    # After swap, what happens.
    # Second query P 7 -> 21
    # So after swap, the youngest manager of 7 is 21.
    
    # When we swap positions of 4 and 2, it means the node "4" and node "2" exchange their places, so all edges that pointed to 4 now point to 2, edges from 4 now from 2, etc.
    # Let's see parents.
    # Originally:
    # parent lists (incoming):
    # 2: [1]
    # 3: [1]
    # 5: [2,3]
    # 6: [3,4]
    # 7: [4,6]
    # 4: []
    # 1: []
    # Outgoing:
    # 1: [2,3]
    # 2: [5]
    # 3: [5,6]
    # 4: [6,7]
    # 6: [7]
    
    # After swapping 4 and 2, the nodes swap identities in the structure.
    # So the new node at position 2 has what 4 had, and vice versa.
    # But people have fixed ids and ages.
    # The swap is swapping the employees A and B, so their positions in the company hierarchy are exchanged.
    # That means the person who was at "slot" of 4 is now at slot of 2 and vice versa.
    # But it's easier to think that we swap the ages and we swap the adjacency.
    # No, because when we swap David(4) and George(2), the figure (b) shows that now the person with age 33 is where 18 was and vice versa.
    # The ages move with the person.
    # So when two people swap positions, their ages move to the new position, and the management relations are based on positions.
    # So the graph structure (who manages who) stays the same in terms of slots, but the people (with their ages) are swapped.
    # So to implement, we can have an array person[slot] = employee_id, and age_at_slot[slot].
    # But the queries are given by employee id.
    # So we need to know where each employee is currently located.
    
    # Let's define that the graph is on positions 1 to N.
    # The edges are fixed? No, when people swap, the edges stay with the positions.
    # The input gives "X gerencia Y diretamente" meaning person X manages person Y.
    # But when they swap, the management relations change because people moved.
    # The problem says "dois empregados A e B trocarem suas posições na cadeia de comando".
    # So the positions have fixed management relations, and employees move between positions.
    # So the graph is on positions, and each position has an employee.
    # When A and B swap, we swap which employee is at which position, thus swapping their ages at those positions, and the management is by position.
    # Then, a query for employee E is: find the position of E, then find all positions that manage that position (ancestors), then among the employees currently at those ancestor positions, what is the minimal age.
    # That makes sense.
    # And since the graph is fixed, we can precompute for each position what is the min age among its ancestors, but since employees move, ages at positions change, so we need dynamic min on ancestors.
    # With swaps being employee swaps, it's like the values (ages) are permuted.
    # With N=500, we can maintain the current age at each node (position).
    # The graph is given by initial X Y meaning position X manages position Y.
    # Employees are initially at their own id position.
    # When we swap employees A and B, we swap the ages at their current positions? No.
    # Employees have fixed ages, they move to new positions.
    # So we need to track where each employee is.
    # Let's say we have pos[employee] = current_position
    # Initially pos[i] = i for all i.
    # age_at_position[i] = age[i] initially.
    # When we do T A B, we swap the positions of employee A and B:
    # posA = pos[A]; posB = pos[B]
    # pos[A] = posB; pos[B] = posA
    # age_at_position[posA] = age[B]  wait no.
    # Since age is fixed to employee, age_at_position[new_pos_of_A] = age[A]
    # So after swap:
    # temp = age_at_position[posA]
    # age_at_position[posA] = age_at_position[posB]
    # age_at_position[posB] = temp
    # But since age_at_position[posX] should be age of the employee currently at posX.
    # Yes, and since we swap the employees, we swap the ages at those positions.
    # Yes.
    # And for query P E, we need the position where E is currently, say p = pos[E]
    # Then find all ancestors of p (positions that manage p directly or indirectly), look at the current age_at_position of those ancestors, and take the min.
    # If no ancestors, *
    
    # This matches.
    # Now, is the graph a DAG? Yes, assumed no cycles I hope.
    # With N=500, for each query, if we traverse the ancestor graph, it could be expensive if dense.
    # M=60*1000 = 60k edges, N=500, so graph can be dense.
    # If we do naive DFS for each query, with 500 queries, and each can visit all nodes, 500*500=250k, but with edge count 60k, if we traverse edges it could be up to 500*60k which is 30M, might be acceptable but tight in python and if not memoized.
    # We need to only traverse ancestors, so we should build the reverse graph (from child to parents).
    # To find all ancestors, we can do DFS or BFS from the node going up the parent links, using a set to avoid revisiting.
    # Since N=500, even 500*500 = 250k is fine.
    # We can precompute the transitive closure, but since the graph is static (only values change), yes!
    # The graph structure (who manages who) is fixed! Only the ages at positions change with swaps.
    # So we can precompute for each position, the list of all its ancestors, or even better, since we only need the min age among them, but because ages change, we cannot precompute the min.
    # With swaps, ages move around.
    # Since N=500, we can precompute a bool matrix is_ancestor[500][500], then for a query on position p, we iterate all possible ancestors a=1 to N, if is_ancestor[a][p] then take min of current_age[a].
    # Precomputing transitive closure with floyd warshall on DAG is possible.
    # Since N=500, floyd is 500^3 = 125M, a bit slow but might pass (python can do ~10^8 per sec, 125M is borderline but for bit matrix we can optimize).
    # We can do DFS from each node to find all reachable ancestors, since M=60k, N=500, doing DFS from each with memoization (bitsets) is good.
    # Using bitsets in python is possible with integers but with 500 bits we need array of int.
    # Since I=500, and for each P query we can run a DFS/BFS upwards with visited array of size 500, total time is acceptable as long as we don't have too many edges.
    # Total operations roughly I * (N + M_ancestors), but worst case if DAG is dense, M~N^2/2 ~ 125k, then 500*125k ~ 60M, too slow for python.
    # So we need a better way.
    # We need fast way to query min age on all ancestors of a node, with updates being swaps of ages at two nodes.
    # This is dynamic ancestor min queries on a DAG with value swaps.
    # Since it's a static DAG, we can do topological order.
    # If we process in reverse topological order (from leaves to roots?).
    # For each node, the min manager age is the min of its direct managers' ages and their min manager ages.
    # So min_ancestor[u] = min over parents p of ( age[p], min_ancestor[p] )
    # Yes!
    # If we can maintain this, when we swap two ages, we need to update the affected nodes.
    # But swaps can affect many nodes.
    # Since N=500, we can just, after each swap, recompute the min_ancestor for ALL nodes by processing in topological order.
    # That would be perfect.
    # We need a topological order of the DAG.
    # Assuming it's a DAG (no cycles, as it's a command hierarchy).
    # We can compute topo order once.
    # Then, we maintain current_age[1..N], initially current_age[i] = Ki
    # We also need the parents list for each node.
    # Then, for each swap T A B:
    #   We swap the employees? Wait, since queries are by employee id, but if ages are tied to employees, and employees move to different positions.
    # Let's clarify with sample.
    
    # In sample 1:
    # Ages given: 21 33 33 18 42 22 26 for employees 1 to 7.
    # After T 4 2, then P 7 outputs 21.
    # Before swap, min was 18 which is age of 4.
    # After swapping 4 and 2, if 4 and 2 swapped positions, then the position that had age 18 now has age 33 (age of 2), and position that had 33 (employee 2) now has 18.
    # Then the managers of 7 were positions 4 and 6.
    # So if position 4 now has age 33 (from employee 2), position 6 has 22.
    # Then ancestors positions: 4(now33), 6(22), parents of 6 which are 3(33) and 4(33 now?), 1(21).
    # So ages of managers: 33,22,33,21. Min is 21. Yes! Matches the sample output 21.
    # Perfect.
    # Next P 5 -> 18
    # Managers of 5: 2 and 3.
    # After swap, position 2 now has the employee who was at 4, i.e. age 18.
    # Position 3 has 33.
    # So min of 18 and 33 and their managers: managers of 2 is 1(21), managers of 3 is 1(21). So 18,33,21. Min 18. Yes.
    # Then T 1 4
    # Now swap employees 1 and 4.
    # Currently after first swap, positions have employees: pos1=1, pos2=4, pos3=3, pos4=2, etc.
    # But anyway, we don't need to track employees if we only care about ages at positions.
    # For query P E, E is the employee id.
    # So we DO need to know at which position employee E is currently located.
    # So we need to maintain the current position of each employee.
    # Initially, employee i is at position i, age_at[i] = K_i
    # When we swap employees A and B, we swap their positions:
    # pa = position[A]
    # pb = position[B]
    # position[A] = pb
    # position[B] = pa
    # Then, since they moved, the age at position pa becomes age[B], age at pb becomes age[A].
    # But since age is fixed per employee, we can have an array current_age[1..N] where current_age[pos] = age[ employee_at_pos ]
    # So we also need employee_at[ pos ] array.
    # Initially employee_at[i] = i, current_age[i] = age[i], position[i] = i
    # For swap A and B:
    # pa = position[A]; pb = position[B]
    # employee_at[pa] = B; employee_at[pb] = A
    # position[A] = pb; position[B] = pa
    # current_age[pa] = age[B]
    # current_age[pb] = age[A]
    # Yes.
    # Then for query P E:
    # p = position[E]
    # Then we need min current_age[x] for all x that are ancestors of p (x manages p directly or indirectly).
    # If none, *
    
    # Since the graph on positions is fixed, we can build the parent lists (incoming edges).
    # To compute min ancestor age for a position, we can use DP in reverse topo order.
    # First, compute topological order of positions.
    # Since it's a hierarchy, should be DAG.
    # To get topo, we can use Kahn or DFS.
    # Then, to compute for all nodes the min ancestor age, we can iterate in reverse topological order (from roots to leaves?).
    # If topo is roots first, then for a node, after processing all its parents, we can compute.
    # Yes.
    # So if we have topo list where if u manages v then u appears before v in topo.
    # Then we iterate from start of topo to end, for each node u, its min_ancestor_age[u] = min over its parents p of min( current_age[p], min_ancestor_age[p] )
    # For roots, min_ancestor_age[root] = infinity or flag.
    # Yes.
    # Since I=500, and N=500, if after each T we recompute the DP for all nodes, time is 500 * (I/2) * N ~ 500*250*500 ~ 60M, too slow? No, for each DP we need to traverse all edges.
    # If we have parent list, for each node we look at its parents.
    # So cost per full DP is O(N + M), with M=60k, N=500, I=500, about 250 swaps max, 250 * 60k ~ 15M operations, perfectly fine in python.
    # Yes!
    # So plan:
    # - Read N, M, I
    # - Read age[1..N]  (fixed employee ages)
    # - Build adj_out: from manager to subordinates  (but we need parents for going up)
    # - Build parents: list of direct managers for each node. parents[v].append(u) when u manages v.
    # - Also build children if needed for topo.
    # - Initially position = [0] + list(range(1,N+1))
    # - employee_at = [0] + list(range(1,N+1))
    # - current_age = [0] + age[1:]   wait index from 1.
    # age = [0]*(N+1); for i in 1 to N: age[i]=...
    # current_age = [0] + [age[i] for i in range(1,N+1)]
    
    # Compute topological order.
    # We will use Kahn's algorithm.
    # Compute indegree from parents.
    # indegree = [len(parents[i]) for i in range(N+1)]
    # Then queue with nodes with indegree 0 (roots, no managers)
    # Then build topo list.
    # If len(topo) != N, cycle, but assume no.
    
    # Then, we will have a array min_anc[1..N], where min_anc[u] = min age of ancestors of u, or a large number if none.
    
    # Function to recompute():
    #   for u in topo:   # topo has roots first
    #       if not parents[u]:   # no managers
    #           min_anc[u] = 10**9
    #       else:
    #           res = 10**9
    #           for p in parents[u]:
    #               res = min(res, current_age[p], min_anc[p])
    #           min_anc[u] = res
    # Yes! Because when we process u, all its parents p have already been processed (since topo).
    # Perfect.
    
    # Then, for each instruction:
    #   if T A B:
    #       pa = position[A]
    #       pb = position[B]
    #       # swap employees
    #       employee_at[pa] = B
    #       employee_at[pb] = A
    #       position[A] = pb
    #       position[B] = pa
    #       # swap current ages
    #       current_age[pa], current_age[pb] = current_age[pb], current_age[pa]
    #       # then recompute all min_anc
    #       recompute()
    #   elif P E:
    #       p = position[E]
    #       val = min_anc[p]
    #       if val == 10**9:
    #           print('*')
    #       else:
    #           print(val)
    
    # We need to call recompute() also at the beginning, before any instructions.
    # Yes.
    # And the last instruction is always P.
    
    # Now, let's verify with sample 2.
    # 6 5 6
    # ages 10 20 30 40 50 60
    # edges:
    # 1->5, 1->4, 3->6, 2->5, 4->5
    # So parents:
    # 4: [1]
    # 5: [1,2,4]
    # 6: [3]
    # 1,2,3: []
    # P 1 -> no manager -> *
    # P 5 -> managers 1(10),2(20),4(40 and its manager 1:10). So min 10. Yes.
    # P 6 -> manager 3(30). min 30.
    # Then T 1 6 : swap employees 1 and 6.
    # So position of 1 was 1, of 6 was 6.
    # After: employee_at[1]=6 (age 60), employee_at[6]=1 (age 10)
    # current_age[1]=60, current_age[6]=10, others same.
    # Now P 1: employee 1 is now at position 6.
    # Position 6 has managers? parents[6]=[3], age at 3 is 30.
    # So min manager age for pos 6 is 30. Output 30.
    # P 4: employee 4 at pos 4, parents of 4 is [1], current_age[1]=60 now.
    # So min is 60. Yes, matches sample output.
    # Perfect!
    
    # Now implement.
    # We need to build parents list.
    # Also for topo, we need outgoing? For Kahn we need indegree which is number of parents, and when processing a node we reduce indegree of its children.
    # So we also need children list (adj).
    
    # Let's code.
    
    from collections import deque
    
    # Read all input
    # Already have data list from beginning? In my first thought I had input read, but now let's do it cleanly.
    
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    I_ = int(data[idx]); idx += 1  # I is keyword
    
    age = [0] * (N+1)
    for i in range(1, N+1):
        age[i] = int(data[idx]); idx += 1
    
    parents = [[] for _ in range(N+1)]
    children = [[] for _ in range(N+1)]
    for _ in range(M):
        X = int(data[idx]); idx += 1
        Y = int(data[idx]); idx += 1
        parents[Y].append(X)
        children[X].append(Y)
    
    position = list(range(N+1))
    employee_at = list(range(N+1))
    current_age = [0] + [age[i] for i in range(1, N+1)]
    
    # Topological order using Kahn
    indeg = [len(parents[i]) for i in range(N+1)]
    q = deque()
    for i in range(1, N+1):
        if indeg[i] == 0:
            q.append(i)
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in children[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    # Assume no cycle, len(topo) == N
    
    min_anc = [10**9] * (N+1)
    
    def recompute():
        for u in topo:
            if not parents[u]:
                min_anc[u] = 10**9
            else:
                res = 10**9
                for p in parents[u]:
                    res = min(res, current_age[p], min_anc[p])
                min_anc[u] = res
    
    recompute()
    
    answers = []
    for _ in range(I_):
        typ = data[idx]; idx += 1
        if typ == 'T':
            A = int(data[idx]); idx += 1
            B = int(data[idx]); idx += 1
            pa = position[A]
            pb = position[B]
            # swap
            employee_at[pa] = B
            employee_at[pb] = A
            position[A] = pb
            position[B] = pa
            current_age[pa], current_age[pb] = current_age[pb], current_age[pa]
            recompute()
        else:  # P
            E = int(data[idx]); idx += 1
            p = position[E]
            val = min_anc[p]
            if val == 10**9:
                answers.append('*')
            else:
                answers.append(str(val))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
``` 

Wait, there is a bug: in the input reading, I used `data = input().split()` but at top I have `import sys` etc.

Also in the code above I assumed `data` is defined, but in the main I have to read it.

Let me correct the full code.

Also, in the first sample, after several swaps, last P 6 outputs 26, P 2 outputs * I think from sample.

The output is:
18
21
18
18
*
26

Corresponding to the 6 P queries.

Yes.

This should work.

One issue: in Kahn's algorithm, if there are multiple components it's fine.

If there is cycle, topo will be incomplete, but assume input is valid.

In recompute, when min_anc[p] == 10**9 it means p has no managers, so min(current_age[p], 10**9) = current_age[p], which is correct.

Yes.

For a node with managers, it takes min of all those.

Yes.

Perfect.

Now, to make it complete, we need to put the input reading inside main correctly.

In the code I have `data = input().split()` but it's sys.stdin.read().

Yes. Here is the final co