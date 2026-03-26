import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    M = int(data[1])
    
    # We need at least M//2 distinct words, and total words between N and M
    # Strategy: generate M//2 distinct words, then use N total words (>= N, <= M)
    # We'll use exactly max(N, M//2) words if possible, but must be <= M
    
    min_distinct = M // 2
    
    # Generate min_distinct distinct words using simple patterns
    # Use single letters a-z (26), then two-letter combos, etc.
    # We need up to 10000 distinct words, each max 10 letters
    
    distinct_words = []
    
    # Single letters: 26
    import string
    letters = string.ascii_lowercase
    
    for c in letters:
        distinct_words.append(c)
        if len(distinct_words) == min_distinct:
            break
    
    if len(distinct_words) < min_distinct:
        # Two letter combos: 26*26 = 676
        for c1 in letters:
            for c2 in letters:
                distinct_words.append(c1 + c2)
                if len(distinct_words) == min_distinct:
                    break
            if len(distinct_words) == min_distinct:
                break
    
    if len(distinct_words) < min_distinct:
        # Three letter combos
        for c1 in letters:
            for c2 in letters:
                for c3 in letters:
                    distinct_words.append(c1 + c2 + c3)
                    if len(distinct_words) == min_distinct:
                        break
                if len(distinct_words) == min_distinct:
                    break
            if len(distinct_words) == min_distinct:
                break
    
    if len(distinct_words) < min_distinct:
        # Four letter combos: 26^4 = 456976, more than enough
        for c1 in letters:
            for c2 in letters:
                for c3 in letters:
                    for c4 in letters:
                        distinct_words.append(c1 + c2 + c3 + c4)
                        if len(distinct_words) == min_distinct:
                            break
                    if len(distinct_words) == min_distinct:
                        break
                if len(distinct_words) == min_distinct:
                    break
            if len(distinct_words) == min_distinct:
                break
    
    # Now we have min_distinct distinct words
    # Total words needed: between N and M
    # We have min_distinct words already
    # If min_distinct >= N, we're done (use min_distinct words, which is <= M since min_distinct = M//2 <= M)
    # If min_distinct < N, we need more words (can repeat), total must be <= M
    
    total_needed = max(N, min_distinct)
    # total_needed <= M? 
    # min_distinct = M//2 <= M, N <= M, so max(N, M//2) <= M. Yes.
    
    words = list(distinct_words)  # already min_distinct words
    
    if total_needed > min_distinct:
        # Need to add (total_needed - min_distinct) more words, can repeat
        extra = total_needed - min_distinct
        # repeat first word
        words.extend([distinct_words[0]] * extra)
    
    print(' '.join(words))

solve()