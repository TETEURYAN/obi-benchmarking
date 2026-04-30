
import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    M = int(data[index])
    index += 1
    
    graph = [[] for _ in range(N+1)]
    rev_graph = [[] for _ in range(N+1)]
    edges = set()
    
    for _ in range(M):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        graph[x].append(y)
        rev_graph[y].append(x)
        edges.add((x, y))
    
    # Find SCCs using Kosaraju
    visited = [False] * (N+1)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(1, N+1):
        if not visited[i]:
            dfs1(i)
    
    visited = [False] * (N+1)
    scc = [-1] * (N+1)
    component_count = 0
    component_nodes = []
    
    def dfs2(u, comp):
        visited[u] = True
        scc[u] = comp
        component_nodes[-1].append(u)
        for v in rev_graph[u]:
            if not visited[v]:
                dfs2(v, comp)
    
    while order:
        u = order.pop()
        if not visited[u]:
            component_nodes.append([])
            dfs2(u, component_count)
            component_count += 1
    
    # Build condensation graph
    cond_graph = [set() for _ in range(component_count)]
    for u in range(1, N+1):
        cu = scc[u]
        for v in graph[u]:
            cv = scc[v]
            if cu != cv:
                cond_graph[cu].add(cv)
    
    # Compute reachable counts in condensation DAG
    out_count = [0] * component_count
    in_count = [0] * component_count
    
    def dfs_out(u, vis):
        vis[u] = True
        cnt = 0
        for v in cond_graph[u]:
            if not vis[v]:
                cnt += dfs_out(v, vis)
            cnt += 1
        out_count[u] = cnt
        return cnt + 1  # including self for size calc, but we adjust later
    
    # We need number of reachable nodes from each component (excluding self)
    vis = [False] * component_count
    for i in range(component_count):
        if not vis[i]:
            dfs_out(i, vis)
    
    # For in_count, we need reverse condensation
    rev_cond = [set() for _ in range(component_count)]
    for u in range(component_count):
        for v in cond_graph[u]:
            rev_cond[v].add(u)
    
    def dfs_in(u, vis):
        vis[u] = True
        cnt = 0
        for v in rev_cond[u]:
            if not vis[v]:
                cnt += dfs_in(v, vis)
            cnt += 1
        in_count[u] = cnt
        return cnt + 1
    
    vis = [False] * component_count
    for i in range(component_count):
        if not vis[i]:
            dfs_in(i, vis)
    
    # Compute current connectivity
    total_connectivity = 0
    comp_size = [len(component_nodes[i]) for i in range(component_count)]
    
    for i in range(component_count):
        # nodes reachable from i (excluding own component)
        reachable = out_count[i]
        total_connectivity += comp_size[i] * reachable
        # nodes that can reach i (excluding own)
        reaching = in_count[i]
        total_connectivity += comp_size[i] * reaching
        # within component is already handled? No, within SCC all are mutually reachable but since x!=y
        # In SCC, every pair (x,y) x!=y is reachable both ways
        total_connectivity += comp_size[i] * (comp_size[i] - 1)
    
    # The current connectivity is total_connectivity
    # Now we need to check for each possible edge (A,B) if adding it increases connectivity
    
    # But N=2e5, we can't check all possible edges
    # We need smart way
    
    # Adding edge (A,B) where A in compX, B in compY, X != Y
    # If there is already path from X to Y in condensation, then no new reachability
    # Otherwise, it will add new paths from all nodes that reach X to all nodes reachable from Y
    
    # More precisely:
    # The increase happens for pairs (u,v) where u can reach A (incl A), v is reachable from B (incl B),
    # and there was no path from u to v before.
    
    # But since it's DAG of SCCs, the only way it increases is if there was no path from compA to compB.
    
    # To have no increase, adding (A,B) must not create any new reachable pair.
    # That means that for every u that can reach A, and every v reachable from B, there must already be path u->v.
    
    # In terms of SCCs, this is only possible if there is already a path from compA to compB in the condensation graph.
    # If there is already path from compA to compB, then adding edge from A to B doesn't create new reachabilities between components.
    # Within components it's already fully connected.
    
    # If compA == compB, then adding edge inside SCC doesn't change anything since already strongly connected.
    # But the problem says A != B and no existing edge (A,B).
    # If they are in same SCC, adding edge inside doesn't change connectivity value, because it's already possible to go from any to any in SCC.
    
    # So two cases where adding (A,B) doesn't change connectivity:
    # 1. scc[A] == scc[B] and (A,B) not already an edge
    # 2. scc[A] != scc[B] and there is already a path from scc[A] to scc[B] in condensation DAG
    
    # If there is path from sccA to sccB, then yes, all nodes reaching sccA can already reach all nodes in sccB.
    
    # Now, the task is to find if there is any such (A,B) that is not already an edge.
    
    # If the graph is strongly connected (one SCC), then any missing edge (A,B) with A!=B is valid, since connectivity is already N*(N-1).
    
    # If there are multiple SCCs, we need to find either:
    # - An SCC with at least 2 nodes that is not complete (has missing edge)
    # - Or an edge between different SCCs where there is already path from source SCC to target SCC, and that specific edge doesn't exist.
    
    # But we need to output any such pair or -1 if none exists.
    
    # When would none exist?
    # Only if every possible pair is either:
    # - already connected by an edge, or
    # - adding it would create new connectivity.
    
    # That means the graph is such that the condensation is a DAG where we cannot add any edge without creating new path.
    # I.e., the condensation DAG has no "redundant" possible edges.
    
    # To solve efficiently:
    # First, if there is any SCC with size >=2, then since N<=2e5, M<=4e5, if a component has size S>=2, it can have at most S*(S-1) edges, but usually not complete.
    # But checking if an SCC is complete (tournament or full) is expensive.
    # We don't need to check if it's complete. We can just look for any two nodes in same SCC without direct edge.
    # But with N=2e5, we need O(N+M) solution.
    
    # Strategy:
    # 1. If there is any SCC with >= 2 nodes, pick the largest one or any with size>=2.
    #    Then, since it's strongly connected, there must be cycles, but to find a missing edge:
    #    We can pick any node in the component, and see if there is another node not directly connected.
    #    But to do it efficiently, perhaps we can just try to find if the component has less edges than S*(S-1).
    #    But counting edges inside each SCC.
    
    # Let's compute for each SCC how many internal edges it has.
    
    internal_edges = [0] * component_count
    for u in range(1, N+1):
        cu = scc[u]
        for v in graph[u]:
            if scc[v] == cu:
                internal_edges[cu] += 1
    
    for i in range(component_count):
        S = comp_size[i]
        max_possible = S * (S - 1)
        if internal_edges[i] < max_possible:
            # There is at least one missing edge inside this SCC
            # Now we need to find one such pair
            # To find it efficiently, we can look at nodes in this component
            nodes = component_nodes[i]
            if S >= 2:
                # We can use a set for outgoing in this component
                # But since N large, we need care
                # Since we just need any, we can pick first two nodes and check if edge exists between them in either direction? No, we need specific direction.
                # We need (A,B) with no existing (A,B)
                # Since it's SCC with S>=2, there are at least two nodes u,v with path u->v and v->u.
                # But to find missing direct edge.
                # Simple way: for each node in component, if it doesn't have outdegree == S-1 inside component, then there is some node not directly connected.
                # To find it, we can build adj sets for large components? But memory and time tight.
                
                # Better approach: we will iterate through all nodes in the component and check their out-neighbors within component.
                # But if component is large, say 2e5, and we do it naively it's too slow.
                # We need a way that is O(N+M) total.
                
                # We can, for each component, pick one node u in it.
                # Since it's strongly connected and S>=2, there is at least one node v such that there is edge u->v or v->u.
                # But we need a pair without direct edge.
                # A simple way that works in practice and is efficient: we can look at the node with minimum out-degree inside the component.
                # But let's think differently.
                
                # Actually, since we can output ANY valid pair, we can first check if there is any SCC with size >=2 that has internal_edges < S*(S-1).
                # Then to find a concrete missing edge, we can loop over all given edges and mark them, but per component it's expensive.
                
                # Here's an efficient way:
                # We will create for each component a list of nodes.
                # If a component has size 1, skip.
                # If size >=2, we can take the first node A = nodes[0]
                # Then we create a set of its out-neighbors within the component.
                # If len(out) < S-1, then there is some B in component, B != A, not in out-neighbors.
                # To find such B, we can loop through all nodes in component until we find one not in the set and not A.
                # But if component is very large and the first node has full out-degree, we may need to try another node.
                # In worst case if all but one have full degree, it could be slow? No, because if internal_edges < S*(S-1), there must be at least one node with outdegree < S-1 inside.
                # So we can loop over all nodes in the component and for each compute its internal outdegree by counting how many neighbors are in same component.
                # But that is O(M) total if we do it for all, but we can do it only for one component.
                # Since we only need one pair, we can choose the smallest component with size >=2.
                # But to make it simple and efficient, let's first find if there is any component with size >=2 and internal_edges < max.
                # Then for that component, we will build a set of nodes for fast lookup.
                # Then for each node in the component, we can count how many internal neighbors it has by iterating its adj list.
                # Since sum of degrees is M=4e5, if I do it only for nodes in one component, the time is sum of degrees of those nodes, which is acceptable.
                # Yes!
                
                # So plan:
                # Find a candidate component that has size >=2 and internal_edges < S*(S-1)
                # Then, for that component, we build a set of its nodes for O(1) lookup.
                # Then, we iterate through each u in the component:
                #    internal_out = 0
                #    neighbors = []
                #    for v in graph[u]:
                #        if v in component_set:
                #            internal_out += 1
                #            neighbors.append(v)
                #    if internal_out < S - 1:
                #        # find a B not in neighbors and B != u
                #        for b in component_nodes[i]:
                #            if b != u and b not in neighbors:  # but neighbors is list, slow
                # We need set.
                # So for each u we would need to build set of internal neighbors.
                # If component is large, and many u have full degree, it could be time consuming if not careful.
                # But in practice with python it might TLE if S=1e5 and we loop a lot.
                
                # Better way: pick two arbitrary nodes u, v in the component with u != v.
                # Check if there is already edge u->v. If not, then (u,v) is a valid pair.
                # If yes, check if there is edge v->u. If not, output (v,u).
                # If both edges exist, pick another node w, and check against u and v.
                # Since it's strongly connected, it's unlikely all pairs have both directions, because that would require many edges.
                # But to guarantee efficiency, we can do the following:
                # Take the list of nodes in the component.
                # We will check for i in range(min(100, len(nodes))):
                #     for j in range(i+1, min(100, len(nodes))):
                #         a = nodes[i]
                #         b = nodes[j]
                #         if (a, b) not in edges:
                #             return a, b
                #         if (b, a) not in edges:
                #             return b, a
                # This is 100*50 = 5k checks, very fast.
                # Is it possible that in a strongly connected component all pairs among first 100 nodes have both directions? Yes, but then we can fall back to another strategy.
                # But if the component has >=2 nodes and not all possible edges, there must be a missing one.
                # To make it 100% efficient and simple, we can use the fact that if internal_edges < S*(S-1), then there is a missing directed edge.
                # We can iterate over ALL edges in the graph once, and for each component that needs a missing edge, we can have a map or something.
                # Perhaps a different approach.
                
                # Let's change strategy.
                # We will look for a valid pair in this priority:
                # 1. Find if there is any SCC with size >= 2. Then we will find a missing edge inside it by checking pairs of nodes.
                # To do it safely, we can select the SCC with smallest size >=2.
                # Since smallest size is small, we can easily find a missing edge.
                # Yes! Perfect.
                
                # Find the smallest SCC with size >=2. If none, then all SCCs are size 1.
                # If all SCCs are size 1, then we need to find an edge (A,B) where there is already a path from A to B in the DAG.
                # That is, we can add an edge from a component to another that is already reachable.
                
    # Let's implement step by step.
    
    # First, find all components with size >=2, and among them the one with smallest size.
    min_size = N + 1
    candidate_comp = -1
    for i in range(component_count):
        if comp_size[i] >= 2 and comp_size[i] < min_size:
            min_size = comp_size[i]
            candidate_comp = i
    
    if candidate_comp != -1:
        # Find a missing edge in this component
        nodes = component_nodes[candidate_comp]
        node_set = set(nodes)
        # Since size is smallest, and if size=2, very easy
        # We will check all pairs until we find one without direct edge.
        # Since it's smallest, even if size=300, C(300,2)=~45k is acceptable.
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i == j:
                    continue
                a = nodes[i]
                b = nodes[j]
                if (a, b) not in edges:
                    print(a, b)
                    return
        # If we reached here, it means the component is fully connected with all directed edges.
        # But then internal_edges would be S*(S-1), contradiction with our earlier check.
        # We didn't check internal_edges, but if we reached here it means it is complete.
        # So we should have checked internal_edges first.
        
    # Let's reorganize.
    
    # Compute internal_edges
    internal_edges = [0] * component_count
    for u in range(1, N+1):
        cu = scc[u]
        for v in graph[u]:
            if scc[v] == cu:
                internal_edges[cu] += 1
    
    # Find candidate for internal missing edge
    candidate_comp = -1
    for i in range(component_count):
        S = comp_size[i]
        if S >= 2 and internal_edges[i] < S * (S - 1):
            candidate_comp = i
            break
    
    if candidate_comp != -1:
        nodes = component_nodes[candidate_comp]
        S = len(nodes)
        node_set = set(nodes)
        # Now find a pair without direct edge
        # To do it fast, we pick nodes one by one and look for missing out edge
        for idx in range(S):
            u = nodes[idx]
            internal_out_set = set()
            for v in graph[u]:
                if v in node_set:
                    internal_out_set.add(v)
            if len(internal_out_set) < S - 1:
                for b in nodes:
                    if b != u and b not in internal_out_set:
                        print(u, b)
                        return
        # If we didn't find, something is wrong, but shouldn't happen
    
    # If no internal missing edges in any SCC, that means every SCC with >=2 nodes is a complete digraph (has all possible directed edges).
    # Now we need to look for cross edges that are redundant, i.e., from compX to compY where X can already reach Y.
    # That is, there is a path from X to Y in the condensation DAG, with length >=1 (since if length=0, it's same component, already handled).
    # So, if the condensation DAG has any edge that is not a "bridge" in terms of reachability, meaning if there is a pair of components X, Y where X can reach Y in more than one way or through longer path.
    # To find if there is any possible (A,B) with scc[A] != scc[B], no direct edge, but scc[A] can reach scc[B].
    
    # To find such a pair efficiently.
    # One way is to find if the condensation DAG is such that its transitive closure has more pairs than the number of direct edges.
    # But we need a concrete pair.
    
    # Notice that if the condensation DAG has a component with outdegree >=2 or indegree >=2 or has a path of length >=2, then there are redundant edges possible.
    # For example, if there is path X -> Z -> Y, then we can add edge X->Y if it doesn't exist, and it won't change reachability.
    
    # So, to find such, we can look for any two components where one can reach the other through a path of length >=2, and then pick any A in source, B in target, if the direct edge doesn't exist.
    # If all such have the direct edge, then it's like the DAG is transitively closed.
    # The case where no such pair exists is when the condensation is a linear chain: 1->2->3->...->K, and there are no extra edges.
    # In that case, you cannot add any edge without either creating a cycle or skipping, which would not change? Wait, adding 1->3 when 1->2->3 exists does not change reachability, because 1 could already reach 3.
    # So in a chain, you can always add an edge from i to j where j > i+1.
    # The only case where you cannot add any edge is when the DAG has only one component, or when it is such that every possible pair of components that have a path already have the direct edge? But that can't be for long chains.
    # When is it impossible to add any edge without increasing connectivity?
    # It is when there is no pair of distinct components X, Y such that X can reach Y.
    # That is, the condensation DAG has no paths of length >=1, meaning it is composed of isolated nodes, i.e. no edges between components.
    # No, if there is an edge X->Y, then X can reach Y, so we can add another edge from a node in X to a node in Y only if there is no direct edge between those specific nodes.
    # The condition is not about components having path, but whether we can find specific A in X, B in Y where path from X to Y exists, and (A,B) not in original edges.
    # Since M<=4e5, and N=2e5, it's likely there are many missing edges.
    # The only time when it's impossible is when for every pair of components X,Y where X can reach Y (including direct), all possible pairs (a in X, b in Y) already have an edge a->b.
    # That is very rare and only possible if the sizes are small or if there are no such reachable pairs.
    # If there is any reachable pair X to Y with X != Y, and (sizeX * sizeY > number of existing edges from X to Y), then there is a missing one.
    # To compute that, we would need to count edges between every pair of components, which is possible but heavy.
    # Since we have the test cases, let's look at them.
    
    # Test 1:
    # 4 3
    # 1 2
    # 2 4
    # 1 4
    # So cities 1,2,4 are connected, 3 is isolated?
    # From 1 we can reach 2 and 4.
    # From 2 to 4.
    # From 3 nowhere.
    # From 4 nowhere.
    # Can we go back? No.
    # SCCs are {1}, {2}, {3}, {4} I think, since no cycles.
    # Is there cycle? No.
    # Connectivity: (1,2),(1,4),(2,4)
    # So 3 pairs.
    # If we add any edge, for example 4 to 1, that would create cycle, allowing more paths like 1 to 4 to 1, but also from 2 to 4 to 1, etc, increasing connectivity.
    # Similarly, adding 4 to 3 would allow 1,2,4 to reach 3, increasing.
    # Adding 3 to 1 would allow 3 to reach 1,2,4.
    # So indeed -1.
    
    # Test 2:
    # 4 4
    # 1 2
    # 2 4
    # 1 4
    # 4 3
    # Now we have 4->3.
    # So from 1 we can reach 2,4,3.
    # From 2 to 4,3.
    # From 4 to 3.
    # From 3 nowhere.
    # SCCs still all separate.
    # Output is 2 3.
    # Is there already path from 2 to 3? Yes, 2->4->3.
    # Adding 2->3 doesn't create new reachability because 2 could already reach 3, and no one reaches 2 except 1, and 1 could already reach 3.
    # Perfect.
    
    # So in this case, since there is a path of length 2, we can add a shortcut.
    
    # To generalize, if the condensation DAG is not a single path without possible shortcuts, but actually as long as there is either:
    # - An SCC with >=2 nodes not fully connected (almost always)
    # - Or there is a path of length >=2 in the condensation DAG, then we can add an edge from a node in the source to a node in the target of that path.
    # - Or if there is a component with multiple out edges or in edges, we might be able to add parallel edges but since it's between components, if there is already one edge from component X to Y, we can add another from different A to B.
    
    # To make it simple and efficient, we can do the following:
    # We will compute the topological order of the condensation DAG.
    # Then, we can find if there is any possible redundant edge.
    # But perhaps a simple way that works:
    # We can find the sources and sinks in the condensation.
    # If there is more than 1 source or more than 1 sink, then we can connect them in certain ways but that might increase connectivity.
    # The problem is to find if there is a redundant edge, i.e. one that doesn't increase the number of reachable pairs.
    
    # Let's think what makes an added edge redundant.
    # Adding (u, v) is redundant if and only if there is already a path from u to v in the original graph.
    # Because if there is already a path from u to v, then adding direct edge doesn't allow any new pairs, because anything that could reach u could already reach v through that path, and anything reachable from v was already reachable from u.
    # Is that true?
    # Yes! Exactly.
    # If there is already a directed path from u to v, then adding (u,v) does not change the reachability relation at all.
    # If there is no path from u to v, then adding it will make u reach v, and all that reach u will reach all that v reaches, which were not reachable before, so connectivity increases (unless the sets are trivial).
    # So the condition simplifies to:
    # Find A != B, no direct edge (A,B), BUT there is already a directed path from A to B (of length >=2).
    # If no such pair exists, output -1.
    
    # This is much simpler to understand.
    # The task is to find if there is any pair of nodes that are connected by a path of length at least 2, but have no direct edge.
    # If yes, output one such pair. Else -1.
    
    # In test 1, all reachable pairs have direct edges: 1->2, 1->4, 2->4. No pair has path length >=2.
    # In test 2, 2->4->3, so path from 2 to 3 of length 2, and no direct 2->3, so output 2 3.
    # Perfect.
    # Also, if there is a cycle, say A->B->A, then there is path A to B (direct), but also B to A. But for direct edges, if both directions are there, then for example if there is longer cycle, we can find other pairs.
    # If two nodes with only one direction, but cycle through others, then there is path back.
    
    # So now, how to find if there is any pair u,v such that u can reach v, there is no direct edge u->v, and u != v.
    # With N=2e5, M=4e5, we need an efficient way.
    # One way is to compute all reachability, but impossible.
    # We need to find if the graph's transitive closure has any pair not in the direct edges.
    # I.e., if the graph is transitively closed (for the reachability), meaning it is a DAG of cliques or something.
    # But to find one such pair, we can use the SCCs again.
    # If there is any SCC with more than 1 node, then since it's strongly connected and has cycle, there is path from a node to another of length >=2 (around the cycle), so if there is no direct edge between some pair in the cycle, we can use that.
    # In a strongly connected component of size >=2, there is always a cycle, so for any two nodes on the cycle, there is path in both directions of length >=2 if the direct edge is not there, or if the cycle is longer than 2.
    # If the SCC is just two nodes with edges both ways, then path of length 2 exists (A->B->A), but for the pair (A,B), there is direct edge, so we cannot use (A,B) as the redundant edge because the condition is no existing rodovia (A,B).
    # But since both directions are present, there is no missing direct edge, so we cannot use them.
    # But if the SCC has 3 nodes in a cycle A->B->C->A, then for example from A to C there is direct? If not, then A to C has path A->B->C of length 2, so (A,C) is a valid pair if no direct edge.
    # If the graph has all 6 edges, then it's complete, and there is no missing edge, so no redundant to add inside.
    # So back to square one.
    
    # To find a pair with path length >=2 without direct edge.
    # One standard way in competitive programming for this kind of "find if there is a redundant edge" or "find a edge that can be added without changing reachability" is to use the topological order of the SCCs.
    # Since we have the condensation DAG, which is a DAG.
    # Within an SCC, if it's not a complete digraph, then there is a missing direct edge, and since they are strongly connected, there is path (actually many).
    # So first, we look for an SCC that is not complete.
    # To find a missing edge in it, since we have smallest such, or we can pick one with size 2.
    # If size 2, and internal_edges < 2, then it must have only one directed edge, say A->B but not B->A.
    # Then since it's SCC, there must be path from B to A, so there is path B to A of length >=2 (through other nodes? If size=2 and only one edge, it cannot be strongly connected.
    # Contradiction.
    # If two nodes with only one edge, they are not in same SCC.
    # So for size=2 SCC, it must have both directed edges A<->B.
    # Then internal_edges = 2, S*(S-1)=2, so it is "complete", so we won't pick it as candidate for missing internal edge.
    # For size=3, to be strongly connected, minimum is cycle of 3, so 3 edges, but S*(S-1)=6, so 3 < 6, so there is missing edge.
    # So we can find it.
    # So our earlier code with finding smallest component with internal_edges < S*(S-1) will work for size>=3.
    # For size=2, it will have exactly 2 edges, so =, so not selected.
    # For size=1, 0 = 0.
    # So only when there is an SCC with size >=3 that is not complete (which is almost always, unless it has all 6+ edges).
    # If all SCCs are of size 1 or 2, and the size 2 are complete (both edges), then we need to find cross-component redundant edges.
    # That is, pairs in different SCCs where there is a path from one to the other of length >=2.
    # To find such a pair, we can do a DFS or BFS from each component in the condensation, and see if we can reach a component at distance >=2, and then pick a node from source and a node from target.
    # Since component_count can be up to 2e5, we need to be careful.
    # But we can start from components that have out edges, and see if any of their successors have out edges, then we can go two steps.
    # To make it concrete, we can compute for each component the list of reachable components in exactly 1 step and in >=2 steps.
    # But to find one concrete example, we can pick a component that has a path of length >=2 from it.
    # We can do a topological sort of the condensation components.
    # Then, we can compute for each component the set of reachable components, but too slow.
    # Since we only need one pair, we can start from nodes with outdegree >0, and do a DFS or BFS but limit the depth or something.
    # A very simple and efficient way in practice is to do DFS from each node but with memoization (dynamic programming on DAG of SCCs).
    # But perhaps the following works:
    # We will iterate over all existing edges, and for each edge u->v, we can see if v has any out-neighbor w, such that there is no direct edge u->w.
    # If yes, then (u, w) is a pair with path u->v->w of length 2, and no direct u->w.
    # This finds a pair with path of length exactly 2.
    # This is very efficient.
    # We can loop over all edges u->v, then for each neighbor w of v, if w != u and (u, w) not in edges, then output u w.
    # This finds many such redundant edges.
    # Is it complete? It finds only length 2 paths.
    # But in the test 2, from 1->2, then 2->4, so for u=1, v=2, w=4, is there direct 1->4? Yes, in the input there is 1 4, so it would not output 1 4.
    # Then for u=1, v=4, w=3, is there direct 1->3? No, so it would output 1 3.
    # Also good.
    # For u=2, v=4, w=3, no direct 2->3, output 2 3, which is the sample.
    # Perfect.
    # Now, is there a case where there is a path of length >=3 but no length 2 path that has a missing direct edge?
    # For example, suppose A->B->C->D, and all possible shortcuts are already present: A->C, A->D, B->D.
    # Then for length 2: A->B->C but A->C exists, B->C->D but B->D exists, A->C->D but A->D exists.
    # So this method would not find any.
    # But there is path A to D of length 3, and if A->D exists, then it is covered.
    # So in this case, all possible pairs that have path already have direct edge.
    # So the method is correct in not finding, because all are covered by direct edges.
    # Is there a case where there is a long path but all length 2 are covered by direct, but some longer is not?
    # In a DAG, if all length 2 have direct edges, then by transitivity, longer paths would also have direct edges? No, not necessarily if it's not complete.
    # Suppose A->B->C->D, with edges A->C, B->D, but no A->D.
    # Then for length 2:
    # A->B->C: has A->C
    # B->C->D: has B->D
    # A->C->D: has no A->D ! So when we process edge A->C, v=C, w=D, check if (A,D) exists, if not, we output A D.
    # So it finds it.
    # Is it always the case that if there is a path of length >=2 without direct edge, there is some length 2 subpath where the shortcut is missing?
    # No. Suppose we have A->B->C->D, with A->C, A->D, B->D, but wait then all are covered.
    # If A->D exists, then the pair A D has direct edge.
    # So when would there be a missing direct for a long path but all length 2 shortcuts are present?
    # It seems that if all consecutive length 2 have the shortcut, then by induction, longer ones also have.
    # Yes, it seems this method covers all cases.
    # Suppose a more complex graph with branches.
    # It seems that this method of looking for u -> v -> w with no u -> w is a standard way to find a redundant edge for this exact purpose.
    # And if no such triple exists, then the graph is transitively reduced, meaning no redundant edges can be added without changing reachability.
    # Yes.
    # So this is perfect and very efficient: O(M * average outdegree of v) which since sum outdegrees = M, total time is O(M).
    # We just need to be careful not to output if u == w, but since no self-loops, ok.
    
    # So let's implement this.
    # We will also handle the case inside SCCs by this method, because if there is a cycle, there will be u->v->w where w can reach u etc, but since we only need one, it's fine.
    # But if there is a large SCC that is not complete, this method may or may not find a missing edge inside, but since we have the length 2, it should find if there is any triangle or something.
    # To be safe, we can first check for internal missing in SCCs with size >=3 as before, but since this method is simple, let's see if it works for cycles.
    # Suppose a cycle of 3: 1->2->3->1, no other edges.
    # Then check:
    # u=1,v=2,w=3: is there 1->3? No, so output 1 3. Perfect, and there is path 1->2->3.
    # Similarly for others.
    # If we have complete bidirected, then for every u v w, the direct u->w exists, so no output from this, which is correct because all direct edges exist, adding any would be duplicate but since no duplicate allowed, and all are present, no pair to add.
    # Perfect.
    # Another case: two nodes A<->B. Then possible triples? u=A v=B w=? B has only edge to A, so w=A, then u=A w=A, self, skip.
    # Similarly other way. So no output, correct, because the only possible pairs are (A,B) and (B,A) which already have edges.
    # Perfect!
    
    # So this method works for everything.
    # Now, what if there is a longer path without any length 2 missing shortcut? As we saw, it seems it would imply all are connected directly.
    # So this should be correct.
    # And for the first test case:
    # Edges: 1->2, 2->4, 1->4.
    # Check triples:
    # u=1 v=2 w=4: is there 1->4? Yes, so skip.
    # u=2 v=4 w=? 4 has no out, skip.
    # u=1 v=4 w=? no out.
    # No triple found, output -1. Perfect.
    
    # Another case: suppose isolated nodes, no edges, then no triples, -1 correct, because adding any edge increases connectivity from 0 to 1.
    
    # Great.
    
    # So now we can implement this.
    # We need to be careful with multiple edges or self but problem says no.
    # We will use set of edges for fast lookup, but with M=4e5, in python set of tuples is acceptable.
    # Since N=2e5, we can use a list of sets for adjacency.
    
    # Let's use adj list as list of sets for fast check.
    
    adj = [set() for _ in range(N+1)]
    for _ in range(M):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        adj[x].add(y)
    
    # Now, we need to iterate over all possible length 2 paths.
    # To do it, we loop over all u that have neighbors.
    for u in range(1, N+1):
        for v in adj[u]:
            for w in adj[v]:
                if w != u and w not in adj[u]:
                    print(u, w)
                    return
    # If no such found, then -1
    print(-1)

if __name__ == "__main__":
    main()
```

Wait, there was a bug: I redefined adj after the first part. Let's correct and make a clean version.

Here is the final clean co