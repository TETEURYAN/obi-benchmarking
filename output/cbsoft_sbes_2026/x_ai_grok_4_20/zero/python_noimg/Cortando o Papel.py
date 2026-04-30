
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

if N == 1:
    print(1)
    sys.exit()

max_pieces = 2

# Encontra todos os mínimos locais (incluindo bordas)
local_mins = []
if A[0] < A[1]:
    local_mins.append(A[0])
if A[-1] < A[-2]:
    local_mins.append(A[-1])

for i in range(1, N-1):
    if A[i] < A[i-1] and A[i] < A[i+1]:
        local_mins.append(A[i])
    elif A[i] == A[i-1] and A[i] < A[i+1]:
        j = i
        while j > 0 and A[j] == A[j-1]:
            j -= 1
        if j == 0 or A[j-1] > A[i]:
            local_mins.append(A[i])

# Conta quantos mínimos locais distintos existem
if local_mins:
    local_mins.sort()
    unique = 1
    for i in range(1, len(local_mins)):
        if local_mins[i] != local_mins[i-1]:
            unique += 1
    max_pieces = max(max_pieces, unique + 1)

# Verifica cortes em todas as alturas únicas
heights = sorted(set(A))
for h in heights:
    pieces = 0
    i = 0
    while i < N:
        if A[i] > h:
            pieces += 1
            while i < N and A[i] > h:
                i += 1
        else:
            i += 1
    max_pieces = max(max_pieces, pieces)

print(max_pieces)
