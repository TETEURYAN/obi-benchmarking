import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    strings = []
    for i in range(1, n + 1):
        strings.append(data[i])
    
    # For each string sk (index k), check if it's a substring of Sa+Sb
    # where a < k and b < k (1-indexed), a can equal b
    # Each string has length 10, so concatenation has length 20
    # sk has length 10, so we need to check all pairs (a, b) from previous strings
    
    # For k-th string (0-indexed: k), previous strings are strings[0..k-1]
    # We need to check if strings[k] is substring of strings[a] + strings[b]
    # for any a in [0, k-1] and b in [0, k-1]
    
    # Naive: O(N^2 * 10) per string = O(N^3 * 10) total
    # N=10000, so N^2 = 10^8 which might be too slow
    # But each string is length 10, concatenation is length 20
    # substring check of length 10 in string of length 20 is O(10)
    # Total: N * N^2 * 10 = 10^9 * 10 for N=10000 -> too slow
    
    # Better approach:
    # strings[k] is substring of strings[a]+strings[b]
    # Since all strings have length 10, strings[k] (len 10) can appear in strings[a]+strings[b] (len 20)
    # at positions 0..10 (11 positions)
    # Position 0..9: entirely in strings[a] -> strings[k] == strings[a] (only at pos 0)
    # Actually position i means strings[k] == (strings[a]+strings[b])[i:i+10]
    # For i=0: strings[k] == strings[a] (since len=10)
    # For i=1..9: strings[k] == strings[a][i:] + strings[b][:10-i]
    # For i=10: strings[k] == strings[b]
    
    # So strings[k] is substring of strings[a]+strings[b] iff:
    # 1. strings[k] == strings[a] (for any a < k)
    # 2. strings[k] == strings[b] (for any b < k)  [same as 1]
    # 3. For some split point p in 1..9: strings[k][:10-p] is a suffix of strings[a] AND strings[k][10-p:] is a prefix of strings[b]
    #    (where a < k and b < k)
    
    # So we can precompute:
    # - set of previous strings (for exact match)
    # - for each possible suffix of length 1..9: set of strings[a] that end with that suffix
    # - for each possible prefix of length 1..9: set of strings[b] that start with that prefix
    
    prev_set = set()
    # suffix_set[l] = set of suffixes of length l seen so far
    suffix_set = [set() for _ in range(11)]  # index 1..9
    prefix_set = [set() for _ in range(11)]  # index 1..9
    
    for k in range(n):
        sk = strings[k]
        
        if k >= 1:
            # Check if sk is in prev_set (exact match with some previous string)
            if sk in prev_set:
                print(sk)
                return
            
            # Check split points p=1..9
            # p is the number of characters taken from strings[b] (prefix length from b)
            # strings[k][10-p:] is prefix of strings[b] of length p
            # strings[k][:10-p] is suffix of strings[a] of length 10-p
            found = False
            for p in range(1, 10):
                suffix_len = 10 - p  # length of suffix needed from strings[a]
                prefix_len = p       # length of prefix needed from strings[b]
                needed_suffix = sk[:suffix_len]  # this should be suffix of some strings[a]
                needed_prefix = sk[suffix_len:]  # this should be prefix of some strings[b]
                
                if needed_suffix in suffix_set[suffix_len] and needed_prefix in prefix_set[prefix_len]:
                    found = True
                    break
            
            if found:
                print(sk)
                return
        
        # Add sk to prev structures
        prev_set.add(sk)
        for l in range(1, 10):
            suffix_set[l].add(sk[10-l:])
            prefix_set[l].add(sk[:l])
    
    print("ok")

solve()