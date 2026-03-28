import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    M = int(data[idx]); idx += 1
    N = int(data[idx]); idx += 1
    
    # balance[i] = net balance of person i (positive = receives, negative = pays)
    balance = [0] * (N + 1)
    
    total_original = 0
    
    for _ in range(M):
        X = int(data[idx]); idx += 1
        V = int(data[idx]); idx += 1
        Y = int(data[idx]); idx += 1
        balance[X] -= V
        balance[Y] += V
        total_original += V
    
    # The minimum total compensated is achieved by finding the minimum number of transactions
    # that settle all balances. This is equivalent to a min-cost flow / greedy settlement problem.
    # 
    # The minimum total value compensated: we need to find a set of transactions that
    # settles all net balances with minimum sum of transaction values.
    #
    # Key insight: The minimum sum of values in an equivalent list equals
    # sum of positive balances (= sum of negative balances in absolute value).
    # Because any equivalent list must transfer exactly the net positive amount
    # from debtors to creditors.
    # Wait - but that's not right either. Let me think more carefully.
    #
    # Actually the minimum total compensated is the sum of all positive balances
    # (which equals sum of absolute values of negative balances).
    # Because in any equivalent list, each unit of money that needs to go from
    # net debtors to net creditors must be "moved" at least once.
    # The minimum is achieved when we can route money directly without cycles.
    #
    # The minimum possible total = sum of positive balances
    # (since we need to transfer that amount from debtors to creditors)
    
    min_total = sum(b for b in balance if b > 0)
    
    # Subtask A: can we reduce total?
    # Original total > min_total means we can reduce
    if total_original > min_total:
        print("S")
    else:
        print("N")
    
    print(min_total)

solve()