
import sys
from collections import defaultdict, deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    records = []
    idx = 1
    for _ in range(n):
        record_type = data[idx]
        x = int(data[idx + 1])
        records.append((record_type, x))
        idx += 2
    
    current_time = 0
    pending_time = 0
    first_event = True
    
    received = defaultdict(deque)
    total_time = defaultdict(int)
    
    for record_type, x in records:
        if record_type in ('R', 'E'):
            if pending_time > 0:
                current_time += pending_time
                pending_time = 0
            elif not first_event:
                current_time += 1
            first_event = False
            
            if record_type == 'R':
                received[x].append(current_time)
            else:
                if received[x]:
                    receive_time = received[x].popleft()
                    total_time[x] += current_time - receive_time
        else:
            pending_time = x
    
    all_friends = set(received) | set(total_time)
    for friend in sorted(all_friends):
        if received[friend]:
            print(friend, -1)
        else:
            print(friend, total_time[friend])

solve()
