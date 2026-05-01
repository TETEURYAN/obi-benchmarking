import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    E = int(data[idx]); idx+=1
    I = int(data[idx]); idx+=1
    V = int(data[idx]); idx+=1
    
    # implications: A -> B means if A occurred, B occurred
    # reverse: for each event B, store its causes (parents in implication graph)
    # forward: A -> B
    
    forward = [[] for _ in range(E+1)]  # forward[A] = list of B where A->B
    reverse = [[] for _ in range(E+1)]  # reverse[B] = list of A where A->B
    
    for _ in range(I):
        A = int(data[idx]); idx+=1
        B = int(data[idx]); idx+=1
        forward[A].append(B)
        reverse[B].append(A)
    
    initial = []
    for _ in range(V):
        initial.append(int(data[idx])); idx+=1
    
    # We need to find all events that certainly occurred.
    # Rules:
    # 1. If event X is true, then all consequences of X (forward) are also true.
    # 2. If event X is true and X has causes (reverse[X] is non-empty), 
    #    then at least one cause must be true. But if ALL causes lead to the same 
    #    certain conclusion, we can deduce more.
    #    Specifically: if X is true and reverse[X] = {A1, A2, ...}, 
    #    then at least one Ai is true. If there's only ONE cause, that cause must be true.
    #    If multiple causes exist, we can't be certain which one.
    
    # Algorithm:
    # - Start with known true events
    # - Forward propagation: if A is true, all B in forward[A] are true
    # - Backward propagation: if B is true and |reverse[B]| == 1, then reverse[B][0] is true
    # - Repeat until no new events are added
    
    certain = set(initial)
    queue = deque(initial)
    
    while queue:
        event = queue.popleft()
        
        # Forward: event -> all consequences
        for B in forward[event]:
            if B not in certain:
                certain.add(B)
                queue.append(B)
        
        # Backward: if event is true and has exactly one cause, that cause is certain
        if len(reverse[event]) == 1:
            A = reverse[event][0]
            if A not in certain:
                certain.add(A)
                queue.append(A)
    
    result = sorted(certain)
    print(*result)

solve()