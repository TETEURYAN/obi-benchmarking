import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M1 = int(input_data[1])
    A = [int(x) for x in input_data[2:2+M1]]
    
    idx = 2 + M1
    M2 = int(input_data[idx])
    B = [int(x) for x in input_data[idx+1:idx+1+M2]]
    
    K_min = max(0, M1 + M2 - N)
    
    cost = [[a * b for b in B] for a in A]
    
    low = 0
    high = 200000
    best_ans = -float('inf')
    
    while low <= high:
        mid = (low + high) // 2
        
        dp_score = [0] * (M2 + 1)
        dp_k = [0] * (M2 + 1)
        
        for i in range(1, M1 + 1):
            cost_i = cost[i-1]
            new_dp_score = [0] * (M2 + 1)
            new_dp_k = [0] * (M2 + 1)
            
            prev_score = dp_score[0]
            prev_k = dp_k[0]
            
            for j, c_val in enumerate(cost_i, 1):
                best_s = dp_score[j]
                best_k = dp_k[j]
                
                s2 = new_dp_score[j-1]
                k2 = new_dp_k[j-1]
                
                if s2 > best_s or (s2 == best_s and k2 > best_k):
                    best_s = s2
                    best_k = k2
                    
                s3 = prev_score + c_val + mid
                k3 = prev_k + 1
                
                if s3 > best_s or (s3 == best_s and k3 > best_k):
                    best_s = s3
                    best_k = k3
                    
                new_dp_score[j] = best_s
                new_dp_k[j] = best_k
                
                prev_score = dp_score[j]
                prev_k = dp_k[j]
                
            dp_score = new_dp_score
            dp_k = new_dp_k
            
        max_score = dp_score[M2]
        max_k = dp_k[M2]
        
        if max_k >= K_min:
            best_ans = max_score - mid * K_min
            high = mid - 1
        else:
            low = mid + 1
            
    print(best_ans)

if __name__ == '__main__':
    solve()