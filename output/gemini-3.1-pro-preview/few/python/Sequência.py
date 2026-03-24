import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    L = int(input_data[1])
    H = int(input_data[2])
    
    S = [int(x) for x in input_data[3:N+3]]
    M = [int(x) for x in input_data[N+3:2*N+3]]
    
    INF = 10**15
    min_pref = [INF] * (N + 1)
    min_pref[0] = 0
    
    ans = 0 if L == 0 else -INF
    
    curr_sum = 0
    curr_marks = 0
    
    for i in range(N):
        curr_sum += S[i]
        curr_marks += M[i]
        
        low = curr_marks - H
        if low < 0:
            low = 0
        high = curr_marks - L
        
        if high >= 0:
            m_val = min_pref[low]
            for k in range(low + 1, high + 1):
                if min_pref[k] < m_val:
                    m_val = min_pref[k]
            
            cand = curr_sum - m_val
            if cand > ans:
                ans = cand
                
        if curr_sum < min_pref[curr_marks]:
            min_pref[curr_marks] = curr_sum

    print(ans)

if __name__ == '__main__':
    solve()