import sys

data = sys.stdin.read().split()
idx = 0
A = int(data[idx]); idx+=1
N = int(data[idx]); idx+=1
M = int(data[idx]); idx+=1

rows = []
for i in range(N):
    row = [int(data[idx+j]) for j in range(M)]
    idx += M
    rows.append(row)

# rows[0] is row N (farthest), rows[N-1] is row 1 (closest)
# We want the closest row (smallest row number = index N-1 in rows list)
# Check from row 1 (index N-1) to row N (index 0)

def has_contiguous(row, A):
    count = 0
    for seat in row:
        if seat == 0:
            count += 1
            if count >= A:
                return True
        else:
            count = 0
    return False

for i in range(N-1, -1, -1):
    row_number = N - i  # row 1 is index N-1, row N is index 0
    if has_contiguous(rows[i], A):
        answer = row_number

# Find the best (smallest row number = closest to stage)
answer = -1
for i in range(N-1, -1, -1):
    row_number = N - i
    if has_contiguous(rows[i], A):
        answer = row_number

print(answer)