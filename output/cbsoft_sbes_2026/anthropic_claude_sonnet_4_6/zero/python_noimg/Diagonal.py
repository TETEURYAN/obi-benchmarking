import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    n = int(input_data[0])
    A = [int(x) for x in input_data[1:n+1]]
    
    # For apartment i in building j (1-indexed), sound is heard at apartment a in building b
    # if b < j and a - i = j - b, i.e., a = i + (j - b)
    # The diagonal is defined by: a - j = i - j + j - b + b... wait
    # a - i = j - b => a + b = i + j
    # So the diagonal key is i + j (apartment number + building number)
    
    # For a given diagonal d = i + j, we need to count apartments on that diagonal
    # An apartment (i, j) is on diagonal d if i + j = d
    # For building j, the apartments on diagonal d are at floor i = d - j
    # This floor must satisfy 1 <= i <= A[j], so 1 <= d - j <= A[j]
    # => d - A[j] <= j <= d - 1
    
    # We want to find the diagonal d that maximizes the count of valid (i, j) pairs
    # where 1 <= i <= A[j] and i + j = d, i.e., 1 <= d - j <= A[j]
    
    # For each building j (1-indexed), it contributes to diagonals d where:
    # d = j + i, 1 <= i <= A[j]
    # So d ranges from j+1 to j+A[j]
    
    # We need to find the diagonal d with maximum count of buildings contributing to it
    # This is equivalent to: for each building j with A[j] > 0, add 1 to range [j+1, j+A[j]]
    # Find the maximum value in this range array
    
    # With N up to 300,000 and A[i] up to 1e9, we need coordinate compression or 
    # a sweep line approach
    
    # Sweep line: events
    # For building j (1-indexed), if A[j] > 0:
    #   +1 at d = j+1
    #   -1 at d = j+A[j]+1
    
    if n == 0:
        print(0)
        return
    
    events = []
    for j in range(1, n+1):
        aj = A[j-1]
        if aj > 0:
            events.append((j + 1, 1))
            events.append((j + aj + 1, -1))
    
    if not events:
        print(0)
        return
    
    events.sort()
    
    max_count = 0
    current = 0
    prev_d = None
    
    i = 0
    while i < len(events):
        d = events[i][0]
        # Process all events at this d
        while i < len(events) and events[i][0] == d:
            current += events[i][1]
            i += 1
        if current > max_count:
            max_count = current
    
    # Wait, we need to track the maximum BEFORE applying the -1 events
    # Let me redo: we want max count in any interval
    # The count changes at event points, we want max between events
    
    events.sort()
    
    max_count = 0
    current = 0
    
    i = 0
    while i < len(events):
        d = events[i][0]
        # Before processing events at d, current is the count for [prev_d, d)
        # But we want max count at any point
        # Actually we should check current before applying events at d
        # The count is 'current' for all d in [last_event_d, this_event_d)
        if current > max_count:
            max_count = current
        while i < len(events) and events[i][0] == d:
            current += events[i][1]
            i += 1
    
    if current > max_count:
        max_count = current
    
    print(max_count)

solve()