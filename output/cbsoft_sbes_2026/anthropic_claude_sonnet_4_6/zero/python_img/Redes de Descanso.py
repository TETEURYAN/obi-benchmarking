I need to find the maximum number of non-crossing hammocks where each hammock connects two trees of the same height, and each tree is used at most once.

Let me think about this problem:
- Hammocks connect pairs of trees with the same height
- Hammocks of the same height cannot intersect (one must be completely to the left of the other)
- Each tree used at most once
- Maximize number of hammocks

This is essentially: given trees with heights, pair up trees of the same height such that:
1. Each tree used at most once
2. No two pairs of the same height cross (nested is ok? Wait - "completely to the left" means no nesting either for same height)

Wait, re-reading: "Two redes penduradas em árvores de mesma altura não devem se intersectar – ou seja, se duas redes estão penduradas na mesma altura, então uma delas precisa estar completamente à esquerda da outra."

So same-height hammocks cannot intersect (and since they're at the same height, they also can't be nested - they must be non-overlapping intervals). Different height hammocks can cross freely.

So for each height h, we have a set of trees with height h, and we need to pair them into non-overlapping intervals, maximizing total pairs across all heights.

For a given height h with positions p1 < p2 < ... < pk, the maximum non-overlapping pairs is floor(k/2) - we just greedily pair (p1,p2), (p3,p4), etc.

Wait, but trees are shared across heights - each tree can only be used once! So if tree i has height h, using it for a height-h hammock means it can't be used for any other hammock (but it only has one height anyway). So actually each tree has exactly one height, so there's no conflict between heights.

Wait - each tree has a fixed height. A hammock must connect two trees of the SAME height. So tree i can only participate in a hammock with another tree of the same height. Since each tree has exactly one height, there's no cross-height conflict.

So the answer is simply: for each height h, count how many trees have that height (call it c_h), and add floor(c_h / 2) to the answer.

Let me verify with examples:
- Example 1: `4 2 2 6 4 10 6 10 4 2 3 2`
  - Height 4: positions 1,5,9 → count=3 → floor(3/2)=1
  - Height 2: positions 2,3,10,12 → count=4 → floor(4/2)=2
  - Height 6: positions 4,7 → count=2 → floor(2/2)=1
  - Height 10: positions 6,8 → count=2 → floor(2/2)=1
  - Height 3: positions 11 → count=1 → 0
  - Total: 1+2+1+1=5 ✓

- Example 2: `1 1 1 1 1 1 1` → count=7 → floor(7/2)=3 ✓

- Example 3: `7 2 1 3 2 3 5 5 7 6`
  - Height 7: 2 → 1
  - Height 2: 2 → 1
  - Height 1: 1 → 0
  - Height 3: 2 → 1
  - Height 5: 2 → 1
  - Height 6: 1 → 0
  - Total: 4 ✓

The solution is simply counting frequencies and summing floor(count/2).

from collections import Counter

n = int(input())
a = list(map(int, input().split()))
freq = Counter(a)
print(sum(v // 2 for v in freq.values()))