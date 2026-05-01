import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    T = [int(data[idx+i]) for i in range(N)]
    idx += N
    F = [int(data[idx+i]) for i in range(M)]
    idx += M
    
    # Sort cars in descending order (largest first assigned first = less waiting)
    T.sort(reverse=True)
    # Sort mechanics by factor ascending (fastest mechanics get more cars)
    F.sort()
    
    # If M >= N, assign one car per mechanic, all wait times = 0
    if M >= N:
        print(0)
        return
    
    # Key insight: 
    # For a single mechanic with factor f, if cars assigned in order t1, t2, ..., tk (sorted desc),
    # waiting times are: 0, t1*f, (t1+t2)*f, ...
    # Sum = f * (t1*(k-1) + t2*(k-2) + ... + t_{k-1}*1)
    # = f * sum_{i=1}^{k-1} t_i * (k-i)
    # 
    # The optimal strategy:
    # - Sort cars descending
    # - Sort mechanics ascending by factor
    # - Assign cars in round-robin: car 0 to mech 0, car 1 to mech 1, ..., car M-1 to mech M-1,
    #   car M to mech 0, car M+1 to mech 1, etc.
    # This is the classic scheduling problem to minimize weighted completion time.
    #
    # Actually the optimal assignment: 
    # Sort T descending, sort F ascending.
    # Assign cars to mechanics in round-robin fashion (car i goes to mechanic i % M).
    # Within each mechanic's queue, cars are already in descending order (which minimizes waiting).
    
    # Each mechanic j gets cars at positions j, j+M, j+2M, ... (0-indexed from sorted T desc)
    # The waiting time contribution for mechanic j with factor F[j]:
    # cars assigned: T[j], T[j+M], T[j+2M], ...
    # waiting times: 0, T[j]*F[j], (T[j]+T[j+M])*F[j], ...
    # sum = F[j] * (T[j]*(cnt-1) + T[j+M]*(cnt-2) + ...)
    # where cnt is number of cars for this mechanic
    
    total = 0
    for j in range(M):
        # cars for mechanic j: indices j, j+M, j+2M, ...
        cars = []
        idx2 = j
        while idx2 < N:
            cars.append(T[idx2])
            idx2 += M
        # cars is already sorted descending
        # waiting time sum for this mechanic
        # car[0]: wait=0, car[1]: wait=cars[0]*F[j], car[2]: wait=(cars[0]+cars[1])*F[j], ...
        prefix = 0
        for k in range(len(cars)):
            total += prefix * F[j]
            prefix += cars[k]
    
    print(total)

solve()