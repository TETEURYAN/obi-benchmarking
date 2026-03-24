import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
records = input_data[1:]

time = 0
last_was_event = False

total_time = {}
pending_time = {}

idx = 0
for _ in range(n):
    type_ = records[idx]
    x = int(records[idx+1])
    idx += 2
    
    if type_ == 'R':
        if last_was_event:
            time += 1
        if x not in total_time:
            total_time[x] = 0
        pending_time[x] = time
        last_was_event = True
    elif type_ == 'E':
        if last_was_event:
            time += 1
        if x not in total_time:
            total_time[x] = 0
        if x in pending_time and pending_time[x] != -1:
            total_time[x] += time - pending_time[x]
            pending_time[x] = -1
        last_was_event = True
    elif type_ == 'T':
        time += x
        last_was_event = False

for x in sorted(total_time.keys()):
    if x in pending_time and pending_time[x] != -1:
        print(f"{x} -1")
    else:
        print(f"{x} {total_time[x]}")