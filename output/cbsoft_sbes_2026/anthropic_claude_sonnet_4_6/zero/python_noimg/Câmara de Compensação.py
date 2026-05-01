
```python
import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    M = int(input_data[idx]); idx += 1
    N = int(input_data[idx]); idx += 1
    
    # Calculate net balance for each person
    balance = [0] * (N + 1)
    
    total_original = 0
    for _ in range(M):
        X = int(input_data[idx]); idx += 1
        V = int(input_data[idx]); idx += 1
        Y = int(input_data[idx]); idx += 1
        balance[Y] += V
        balance[X] -= V
        total_original += V
    
    # The minimum total is achieved by finding the minimum number of transactions
    # to settle all debts. This is equivalent to: given creditors and debtors,
    # find minimum transactions.
    # 
    # The minimum total value of checks in an equivalent list:
    # We need to find the minimum sum of transactions to settle all net balances.
    # 
    # The key insight: the minimum total is achieved when we optimally match
    # creditors with debtors. The minimum sum equals sum of positive balances
    # (= sum of negative balances in absolute value), but we need to find
    # the minimum number of transactions weighted by values.
    #
    # Actually, the minimum total VALUE (not count) of transactions:
    # The sum of all positive balances equals sum of all negative balances (absolute).
    # The minimum total is exactly sum of positive balances = sum of negative balances abs.
    # Because any equivalent list must transfer exactly the net amounts.
    # 
    # Wait, let me reconsider. The minimum total is sum of positive balances.
    # Because we need to move money from debtors to creditors, and the minimum
    # total flow equals the sum of positive balances (creditors' total).
    
    positives = []
    negatives = []
    
    for i in range(1, N + 1):
        if balance[i] > 0:
            positives.append(balance[i])
        elif balance[i] < 0:
            negatives.append(-balance[i])
    
    min_total = sum(positives)  # = sum(negatives)
    
    # Subtask A: can we reduce total?
    if total_original > min_total:
        print("S")
    else:
        print("N")
    
    print(min_total)

solve()
```