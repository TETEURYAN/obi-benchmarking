Looking at this problem, I need to find the smallest A such that there exists a B ≥ A where writing all integers from A to B consecutively (digit by digit) produces exactly the given sequence.

Key observations:
- N ≤ 1000, so the sequence is short
- A and B can be up to 10^1000, so they're big integers
- I need to find the smallest possible A

Approach:
- Try all possible starting positions and lengths for A (the first number)
- For each candidate A (extracted from some prefix of the digit sequence), simulate writing A, A+1, A+2, ... and check if it matches the entire digit sequence
- Among all valid A values, output the smallest

Since N ≤ 1000, A has at most 1000 digits. I'll try each possible length for A (1 to N digits), and for each length, extract A from the beginning of the sequence. Then simulate and verify.

But A could start with leading zeros? No - A ≥ 1, so A doesn't have leading zeros. Also intermediate numbers don't have leading zeros.

For each possible length `la` (1 to N):
- Extract candidate A = digits[0:la] as a number (skip if leading zero and la > 1)
- Simulate: write A, A+1, ... consuming digits, check if we consume exactly N digits

The simulation: given A and the digit string, greedily match numbers starting from A. Each number A+k has a known number of digits. Check that those digits match the sequence.

Since N ≤ 1000 and la ≤ 1000, and for each A we simulate O(N) digits with big integer arithmetic... the number of steps in simulation is at most N (since each number has ≥ 1 digit). Big integer increment is O(digits) = O(1000). Total: O(N * N * N) = O(10^9)... might be tight.

Actually la ranges 1..N, so N candidates. For each, simulation is at most N steps (numbers written), each step: increment big int O(la+log N) and compare digits O(la+log N). So O(N * N * N) worst case with N=1000 → 10^9, too slow.

But in practice, numbers grow slowly. Let me think: for la=1, numbers are 1-digit, so we write at most 1000 numbers. For la=500, each number has ~500 digits, so at most 2 numbers fit. The total work across all candidates is manageable.

Also, I want the **smallest** A, so I should collect all valid A values and return the minimum.

```python
import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    digits = [int(x) for x in data[1:n+1]]
    s = ''.join(map(str, digits))
    
    valid_A = []
    
    for la in range(1, n + 1):
        # Extract candidate A from first la digits
        prefix = s[:la]
        if la > 1 and prefix[0] == '0':
            continue
        if prefix[0] == '0' and la == 1:
            continue  # A >= 1
        
        A = int(prefix)
        if A == 0:
            continue
        
        # Simulate
        pos = 0
        cur = A
        ok = True
        while pos < n:
            cs = str(cur)
            lc = len(cs)
            if pos + lc > n:
                ok = False
                break
            if s[pos:pos+lc] != cs:
                ok = False
                break
            pos += lc
            cur += 1
        
        if ok and pos == n:
            valid_A.append(A)
    
    if valid_A:
        print(min(valid_A))

solve()
```

Wait, but A can be up to 10^1000, and `int(prefix)` with prefix of length 1000 is fine in Python. And `str(cur)` for big integers is fine too. The simulation for large A will terminate quickly (few numbers fit). This should work within time limits.

```python
import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    digits = [int(x) for x in data[1:n+1]]
    s = ''.join(map(str, digits))
    
    valid_A = []
    
    for la in range(1, n + 1):
        prefix = s[:la]
        if prefix[0] == '0':
            continue
        
        A = int(prefix)
        
        pos = 0
        cur = A
        ok = True
        while pos < n:
            cs = str(cur)
            lc = len(cs)
            if pos + lc > n:
                ok = False
                break
            if s[pos:pos+lc] != cs:
                ok = False
                break
            pos += lc
            cur += 1
        
        if ok and pos == n:
            valid_A.append(A)
    
    if valid_A:
        print(min(valid_A))

solve()
```