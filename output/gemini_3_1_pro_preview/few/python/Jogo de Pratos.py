import sys
from functools import cmp_to_key
from bisect import bisect_right

def compare_meals(m1, m2):
    a1, b1 = m1
    a2, b2 = m2
    val1 = b1 * (a2 - 1)
    val2 = b2 * (a1 - 1)
    if val1 > val2:
        return -1
    elif val1 < val2:
        return 1
    else:
        return 0

def start_x(L1, L2):
    a1, b1 = L1
    a2, b2 = L2
    return (b1 - b2) // (a2 - a1) + 1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    K = int(input_data[2])
    
    idx = 3
    a = [int(x) for x in input_data[idx : idx+N]]
    idx += N
    b = [int(x) for x in input_data[idx : idx+N]]
    idx += N
    
    spells = list(zip(a, b))
    
    a_prime = [int(x) for x in input_data[idx : idx+M]]
    idx += M
    b_prime = [int(x) for x in input_data[idx : idx+M]]
    idx += M
    
    meals = list(zip(a_prime, b_prime))
    
    Q = int(input_data[idx])
    idx += 1
    queries = [int(x) for x in input_data[idx : idx+Q]]
    
    MOD = 10**9 + 7
    
    meals.sort(key=cmp_to_key(compare_meals))
    A_meal = 1
    B_meal = 0
    for am, bm in meals:
        A_meal = (A_meal * am) % MOD
        B_meal = (am * B_meal + bm) % MOD
        
    spells.sort(key=lambda x: (x[0], x[1]))
    
    stack = []
    for a_s, b_s in spells:
        if stack and stack[-1][0] == a_s:
            stack.pop()
        
        while len(stack) >= 1:
            if len(stack) >= 2:
                L1 = stack[-2]
                L2 = stack[-1]
                L3 = (a_s, b_s)
                if start_x(L2, L3) <= start_x(L1, L2):
                    stack.pop()
                    continue
            
            L2 = stack[-1]
            L3 = (a_s, b_s)
            if start_x(L2, L3) <= 1:
                stack.pop()
                continue
            
            break
        stack.append((a_s, b_s))
        
    starts = [1]
    for i in range(1, len(stack)):
        starts.append(start_x(stack[i-1], stack[i]))
        
    out = []
    for x in queries:
        rem_K = K
        curr_x = x
        
        while rem_K > 0:
            pos = bisect_right(starts, curr_x) - 1
            if pos == len(stack) - 1:
                break
            a_s, b_s = stack[pos]
            curr_x = a_s * curr_x + b_s
            rem_K -= 1
            
        if rem_K > 0:
            a_s, b_s = stack[-1]
            curr_x %= MOD
            if a_s == 1:
                curr_x = (curr_x + rem_K * b_s) % MOD
            else:
                pow_a = pow(a_s, rem_K, MOD)
                term1 = (pow_a * curr_x) % MOD
                term2 = (b_s * (pow_a - 1) % MOD * pow(a_s - 1, MOD - 2, MOD)) % MOD
                curr_x = (term1 + term2) % MOD
        else:
            curr_x %= MOD
            
        curr_x = (A_meal * curr_x + B_meal) % MOD
        out.append(str(curr_x))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()