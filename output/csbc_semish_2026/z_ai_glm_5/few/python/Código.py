import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    # The sequence elements are strings '0' or '1'
    sequence = input_data[1:n+1]
    
    count = 0
    
    # We need to find the pattern "100"
    # Since the input is space-separated, we can just check triplets
    # The constraint N <= 10^4 allows O(N) iteration easily.
    
    # Iterate up to n-3 (inclusive), so range(n - 2)
    # Check indices i, i+1, i+2
    
    # Optimization: Join into a string and use count?
    # string.count(sub) counts non-overlapping occurrences.
    # Does the problem allow overlapping?
    # Pattern "100" has length 3.
    # If we have "100100", occurrences are at 0 and 3. They don't overlap.
    # If we had pattern "111" and string "1111", occurrences at 0 and 1 overlap.
    # For "100", can it overlap with another "100"?
    # Pattern P = "100".
    # Next occurrence starts at i+k.
    # If they overlap, then suffix of P must be prefix of P.
    # Prefixes of "100": "1", "10".
    # Suffixes of "100": "0", "00".
    # No overlap is possible between two "100" patterns because the suffixes don't match prefixes.
    # Therefore, overlapping is impossible for this specific pattern.
    # So s.count("100") is safe and efficient.
    
    s = "".join(sequence)
    print(s.count("100"))

if __name__ == "__main__":
    solve()