import sys

def solve():
    n = int(sys.stdin.read().strip())
    
    if n == 1:
        print(1)
        return
    
    if n == 2:
        print(-1)
        return
    
    # Strategy: construct a fantastic square
    # For odd n: use consecutive numbers 1..n*n arranged in rows
    # Each row i (0-indexed): i*n+1, i*n+2, ..., i*n+n
    # Row mean = i*n + (n+1)/2, which is in the row (middle element)
    # Column j: j+1, j+1+n, j+1+2n, ..., j+1+(n-1)*n
    # Column mean = j+1 + n*(n-1)/2, which must be in the column
    # Column elements: j+1+k*n for k=0..n-1
    # Mean = j+1 + n*(n-1)/2
    # For this to be in column: j+1 + k*n = j+1 + n*(n-1)/2 => k = (n-1)/2
    # This works when n is odd!
    
    if n % 2 == 1:
        grid = []
        for i in range(n):
            row = [i*n + j + 1 for j in range(n)]
            grid.append(row)
        for row in grid:
            print(*row)
        return
    
    # For even n >= 4:
    # We need a different construction.
    # Idea: For each row, have n numbers where the mean is one of them.
    # Simple approach: use arithmetic progressions.
    # 
    # Construction for even n:
    # Use blocks. For n even, n >= 4.
    # 
    # Let's use the following: 
    # Row i: start with base_i, then base_i+1, ..., base_i+(n-2), base_i + (n-2) + (n-1)
    # i.e., last element = base_i + 2*(n-1) - 1... let me think differently.
    #
    # For each row: [a, a+1, a+2, ..., a+(n-2), a+(n-2)+(n-1)] = [a..a+n-2, a+2n-3]
    # Mean = (sum of a..a+n-2 + a+2n-3) / n
    # sum = (n-1)*a + (0+1+...+n-2) + a+2n-3 = n*a + (n-1)(n-2)/2 + 2n-3
    # mean = a + (n-1)(n-2)/(2n) + (2n-3)/n
    # This gets complicated.
    #
    # Better: For even n, use rows of form: [b, b+d, b+2d, ..., b+(n-1)*d]
    # arithmetic progression with common difference d.
    # Mean = b + (n-1)*d/2, must be integer => (n-1)*d even
    # For even n, n-1 is odd, so d must be even.
    # Mean = b + (n-1)*d/2, which is the middle... but n is even so no exact middle.
    # Mean must be IN the row: b + k*d = b + (n-1)*d/2 => k = (n-1)/2, not integer for even n.
    # So pure AP rows don't work for even n.
    #
    # Use the test case 4 pattern as inspiration:
    # Rows: [1,2,3,6], [7,8,9,12], [13,14,15,18], [31,32,33,36]
    # Each row: [a, a+1, a+2, a+5] -> mean = (4a+8)/4 = a+2, which is in row. 
    # Columns: 1,7,13,31 -> mean=13, in col. 2,8,14,32->mean=14. 3,9,15,33->mean=15. 6,12,18,36->mean=18.
    # Col differences: 6,6,18 for first col. Not AP.
    # 
    # General pattern for n=4k or n=4k+2?
    # Row pattern: [a, a+1, ..., a+n-2, a+n-2+(n-1)] = [a..a+n-2, a+2n-3]
    # For n=4: [a,a+1,a+2,a+5], mean=(4a+8)/4=a+2 ✓
    # For general even n: sum = (a+a+1+...+a+n-2) + (a+2n-3)
    # = (n-1)*a+(n-2)(n-1)/2 + a+2n-3 = n*a + (n-1)(n-2)/2+2n-3
    # mean = a + [(n-1)(n-2)/2+2n-3]/n = a + [(n^2-3n+2+4n-6)/(2n)] = a+(n^2+n-4)/(2n)
    # For n=4: a+(16+4-4)/8=a+16/8=a+2 ✓
    # Need (n^2+n-4)/(2n) to be integer and = some offset k in {0,1,...,n-2} or n-2+(n-1)=2n-3... wait mean=a+2 which is offset 2 from a, so it's the element a+2 in the row.
    # mean - a = (n^2+n-4)/(2n), need this to be integer in {0,1,...,n-2}.
    # For n=4: 2 ✓ (in {0,1,2})
    # For n=6: (36+6-4)/12=38/12 not integer. ✗
    
    # Let me just use a verified construction.
    # For even n, construct rows where each row is [a, a+1, ..., a+n-2, a+n-2+S]
    # where S chosen so mean is a+(n-2)/2... 
    # Actually let me try: rows of [a, a+1, ..., a+n-1] but shift last element.
    # Mean of [a..a+n-1] = a+(n-1)/2, not integer for even n.
    # Replace last element x with x': mean = (sum - (a+n-1) + x')/n = integer in row
    # sum of a..a+n-1 = n*a+n(n-1)/2
    # new sum = n*a+n(n-1)/2 - (a+n-1) + x' = (n-1)*a + n(n-1)/2-(n-1)+x' = (n-1)(a+(n-2)/2)+x'... 
    # Hmm let me just hardcode a working construction.
    
    # WORKING CONSTRUCTION for any n:
    # If n is odd: consecutive numbers work.
    # If n is even: 
    #   Use n odd-sized blocks? No.
    #   
    # Key insight from n=4 example:
    # Row i (0-indexed, i=0..n-1): 
    #   first n-1 elements: i*(n+1)+1, i*(n+1)+2, ..., i*(n+1)+(n-1)  [consecutive]
    #   last element: i*(n+1)+(n-1)+(n) = i*(n+1)+2n-1... 
    # For n=4, i=0: 1,2,3,6 -> gaps: 1,1,3. i*(n+1)=0, so 1,2,3 then 3+3=6. 
    # i=1: 5,6,7,10? But example has 7,8,9,12.
    # With step n+1=5: i=0->0, i=1->5, i=2->10, i=3->15
    # Row 0: 1,2,3,6; Row1: 6,7,8,11 - overlap!
    
    # Let me re-examine n=4 example more carefully:
    # Row 0: 1,2,3,6   (base=1, last=6=1+5)
    # Row 1: 7,8,9,12  (base=7, last=12=7+5)
    # Row 2: 13,14,15,18 (base=13, last=18=13+5)
    # Row 3: 31,32,33,36 (base=31, last=36=31+5)
    # Bases: 1,7,13,31. Diffs: 6,6,18.
    # Columns 0-2: 1,7,13,31 / 2,8,14,32 / 3,9,15,33
    # Col 0 mean = (1+7+13+31)/4=52/4=13 ✓ (in col)
    # Col 1 mean = (2+8+14+32)/4=56/4=14 ✓
    # Col 2 mean = (3+9+15+33)/4=60/4=15 ✓  
    # Col 3: 6,12,18,36 mean=72/4=18 ✓
    # 
    # Cols 0-2 are AP with d=6 (except last: 31 instead of 19)
    # Col 3: 6,12,18,36 - AP with d=6 except last=36 instead of 24.
    # 
    # So the pattern: first n-1 rows form AP with common difference n+2 (for n=4: 6=4+2)
    # Last row has a jump.
    # 
    # For cols 0..n-2: elements in rows 0..n-2 are i*(n+2)+j+1 for row i, col j
    # Mean of col j in rows 0..n-2 = [j+1 + j+1+(n+2) + ... + j+1+(n-2)(n+2)] / (n-1)... 
    # but we need mean over ALL n rows.
    
    # Let me think of a cleaner construction.
    # 
    # CONSTRUCTION: 
    # For even n, let's build it as follows.
    # Each row will be an arithmetic sequence with common difference 2, 
    # centered at an odd number (so mean = center = middle element... but n even has no middle).
    # 
    # Alternative: For even n, use rows of length n where:
    # Row = [c - (n-2), c-(n-4), ..., c-2, c, c+2, ..., c+(n-2), c+n]
    # Wait that's n+1 elements.
    #
    # Let me try yet another approach.
    # For even n >= 2:
    # Each row: n-1 consecutive numbers starting at a, plus one extra number equal to mean.
    # [a, a+1, ..., a+n-2, M] where M = mean of all n numbers.
    # Sum = (n-1)*a + (n-2)(n-1)/2 + M = n*M
    # => (n-1)*a + (n-2)(n-1)/2 = (n-1)*M
    # => a + (n-2)/2 = M  (dividing by n-1, valid since n>=2)
    # For n even: (n-2)/2 = (n-2)/2, integer only if n even ✓
    # So M = a + (n-2)/2
    # But M must be in the row. Row = [a, a+1, ..., a+n-2, M=a+(n-2)/2]
    # Is a+(n-2)/2 in [a, a+1, ..., a+n-2]? Yes! It's a + (n-2)/2 which is between a and a+n-2.
    # So the row is [a, a+1, ..., a+n-2, a+(n-2)/2] but a+(n-2)/2 is already in the sequence!
    # That means we have a duplicate. ✗
    
    # Hmm. So we need M NOT in [a..a+n-2] but still in the row.
    # Row = [a, a+1, ..., a+n-2, M] with M != a+k for k=0..n-2, but M = a+(n-2)/2 which IS in that range.
    # Contradiction. So this approach fails.
    
    # Let me think differently.
    # Row = [a, a+1, ..., a+n-2, X] where X is chosen so:
    # 1. Mean is integer
    # 2. Mean is in the row
    # 3. X not in [a..a+n-2]
    # 
    # Mean = (sum(a..a+n-2) + X) / n = ((n-1)*a + (n-1)(n-2)/2 + X) / n
    # For mean to be integer: (n-1)*a + (n-1)(n-2)/2 + X ≡ 0 (mod n)
    # (n-1) ≡ -1 (mod n), so: -a - (n-2)/2... this gets messy.
    # 
    # Let's say mean = a + k for some k in {0, 1, ..., n-2} (mean is one of first n-1 elements)
    # Then: (n-1)*a + (n-1)(n-2)/2 + X = n*(a+k)
    # X = n*(a+k) - (n-1)*a - (n-1)(n-2)/2
    # X = a + n*k - (n-1)(n-2)/2
    # For X to not be in [a..a+n-2]: X < a or X > a+n-2
    # X = a + n*k - (n-1)(n-2)/2
    # X - a = n*k - (n-1)(n-2)/2
    # For k = (n-2)/2 (middle of first n-1): X-a = n*(n-2)/2 - (n-1)(n-2)/2 = (n-2)/2 * (n-(n-1)) = (n-2)/2
    # So X = a+(n-2)/2, which is in [a..a+n-2]. ✗
    # 
    # For k = n-2 (last of first n-1 elements, i.e., mean = a+n-2):
    # X = a + n*(n-2) - (n-1)(n-2)/2 = a + (n-2)*(n - (n-1)/2) = a + (n-2)*(n+1)/2
    # For n=4: X = a + 2*5/2 = a+5. Row = [a,a+1,a+2,a+5], mean=(4a+8)/4=a+2. But mean should be a+2=a+k=a+2 ✓
    # Wait k=n-2=2 for n=4, mean=a+2 ✓, X=a+5 ✓ (not in [a,a+1,a+2])
    # This matches the n=4 example!
    
    # For general even n, use k = n-2:
    # Row = [a, a+1, ..., a+n-2, a+(n-2)*(n+1)/2]
    # Mean = a + (n-2)
    # Need (n-2)*(n+1)/2 to be integer: (n-2)*(n+1) even.
    # n even => n-2 even => (n-2)*(n+1) even ✓
    # Need X = a+(n-2)*(n+1)/2 > a+n-2 (to avoid duplicate):
    # (n-2)*(n+1)/2 > n-2 => (n+1)/2 > 1 => n > 1 ✓ for n>=4
    # 
    # So for even n>=4, each row: [a, a+1, ..., a+n-2, a+(n-2)*(n+1)/2]
    # Mean = a+n-2 (the second-to-last of the consecutive part)
    # 
    # Now for columns to also satisfy the condition, we need to choose the bases a_i carefully.
    # 
    # Let D = (n-2)*(n+1)/2 (the offset for last element)
    # For n=4: D=5
    # 
    # Row i: [a_i, a_i+1, ..., a_i+n-2, a_i+D]
    # Col j (j=0..n-2): elements are a_0+j, a_1+j, ..., a_{n-1}+j
    # Col n-1: elements are a_0+D, a_1+D, ..., a_{n-1}+D
    # 
    # For col j (j=0..n-2): mean = (sum of a_i+j) / n = (sum(a_i))/n + j
    # For mean to be integer: sum(a_i) ≡ 0 (mod n)
    # For mean to be in col j: mean = a_k + j for some k, i.e., mean - j = a_k for some k.
    # So (sum(a_i))/n must equal some a_k.
    # 
    # For col n-1: mean = (sum(a_i+D))/n = (sum(a_i))/n + D
    # Same condition: sum(a_i)/n must be some a_k, and mean = a_k + D must be in col n-1.
    # Col n-1 elements: a_0+D, ..., a_{n-1}+D. Mean = a_k+D ✓ (it's in col n-1).
    # 
    # So we need: sum(a_i) divisible by n, and sum(a_i)/n = a_k for some k.
    # i.e., the mean of the bases is one of the bases.
    # 
    # This is exactly the same problem recursively! We need the bases a_0,...,a_{n-1} 
    # to form a sequence where their mean is one of them.
    # 
    # Simple solution: make a_0,...,a_{n-1} an arithmetic sequence with odd number of terms... 
    # but n is even. 
    # 
    # For n even: use a_i = base + i*step for i=0..n-1, mean = base+(n-1)*step/2.
    # For mean to be integer: (n-1)*step even, n-1 odd so step must be even.
    # For mean to be in sequence: base+k*step = base+(n-1)*step/2 => k=(n-1)/2, not integer. ✗
    # 
    # Alternative: use a_0,...,a_{n-2} as AP, and a_{n-1} chosen so mean is a_{n-2}.
    # a_i = base + i*step for i=0..n-2, a_{n-1} = ?
    # mean of all = (sum(a_0..a_{n-2}) + a_{n-1})/n = a_{n-2} = base+(n-2)*step
    # sum(a_0..a_{n-2}) = (n-1)*base + step*(n-2)(n-1)/2
    # a_{n-1} = n*(base+(n-2)*step) - (n-1)*base - step*(n-2)(n-1)/2
    #          = base + n*(n-2)*step - (n-1)*(n-2)*step/2... wait
    #          = base*(n-(n-1)) + step*(n*(n-2) - (n-2)(n-1)/2)
    #          = base + step*(n-2)*(n - (n-1)/2)
    #          = base + step*(n-2)*(n+1)/2
    # 
    # So a_{n-1} = base + step*(n-2)*(n+1)/2 = base + step*D (where D=(n-2)*(n+1)/2 same as before!)
    # 
    # So the bases follow the SAME pattern as the rows!
    # a_i = base + i*step for i=0..n-2, a_{n-1} = base + step*D
    # 
    # Now we need all elements to be distinct positive integers <= 1000000.
    # 
    # Let's set step = n (so rows don't overlap in the first n-1 columns):
    # a_i = base + i*n for i=0..n-2, a_{n-1} = base + n*D
    # 
    # Row i (i=0..n-2): [base+i*n, base+i*n+1, ..., base+i*n+n-2, base+i*n+D]
    # Row n-1: [base+n*D, base+n*D+1, ..., base+n*D+n-2, base+n*D+D]
    # 
    # Need all elements distinct. Let's check for n=4, D=5, step=4, base=1:
    # a_0=1, a_1=5, a_2=9, a_3=1+4*5=21
    # Row 0: 1,2,3,6
    # Row 1: 5,6,7,10 -- 6 appears in row 0! ✗
    # 
    # Need to choose step and base more carefully.
    # 
    # For rows 0..n-2 with a_i = base+i*step:
    # Row i elements: base+i*step, base+i*step+1, ..., base+i*step+n-2, base+i*step+D
    # Row i occupies: [base+i*step, base+i*step+n-2] ∪ {base+i*step+D}
    # 
    # For no overlap between consecutive rows i and i+1 in the consecutive part:
    # base+(i+1)*step > base+i*step+n-2 => step > n-2 => step >= n-1
    # Also need base+i*step+D not in row i+1's range:
    # base+i*step+D < base+(i+1)*step or base+i*step+D > base+(i+1)*step+n-2
    # i.e., D < step or D > step+n-2
    # D = (n-2)*(n+1)/2
    # For n=4: D=5, step>=3. If step=6: D=5<6 ✓
    # 
    # Let's use step = D+1 = (n-2)*(n+1)/2 + 1? That might be large.
    # Or step = n*(n-1)/2 + 1? 
    # 
    # Actually, let me just use step large enough.
    # For rows not to overlap: need step >= n (to separate consecutive parts) and D < step.
    # D = (n-2)*(n+1)/2. For n=4: D=5. Use step=6.
    # For n=6: D=4*7/2=14. Use step=15.
    # For n=8: D=6*9/2=27. Use step=28.
    # General: step = D+1 = (n-2)*(n+1)/2+1
    # 
    # But also need row n-1 (with base a_{n-1}=base+step*D) not to overlap with others.
    # a_{n-1} = base + step*D
    # Row n-1 consecutive part: [base+step*D, base+step*D+n-2]
    # Row n-2 consecutive part: [base+(n-2)*step, base+(n-2)*step+n-2]
    # Row n-2 extra: base+(n-2)*step+D
    # 
    # Need base+step*D > base+(n-2)*step+n-2+D (all of row n-2 is below row n-1):
    # step*D > (n-2)*step+n-2+D
    # step*(D-n+2) > n-2+D
    # step > (n-2+D)/(D-n+2) [if D>n-2]
    # D = (n-2)(n+1)/2, D-n+2 = (n-2)(n+1)/2-(n-2) = (n-2)*((n+1)/2-1) = (n-2)*(n-1)/2
    # (n-2+D)/(D-n+2) = (n-2+(n-2)(n+1)/2) / ((n-2)(n-1)/2)
    #                  = (n-2)*(1+(n+1)/2) / ((n-2)(n-1)/2)
    #                  = (1+(n+1)/2) / ((n-1)/2)
    #                  = (2+n+1)/(n-1) = (n+3)/(n-1)
    # For n>=4: (n+3)/(n-1) <= 7/3 < 3. So step >= 3 suffices for this condition!
    # But we also need step >= D+1 for D < step. D = (n-2)(n+1)/2.
    # For n=40: D = 38*41/2 = 779. step = 780.
    # 
    # Max element: base + step*D + D = base + D*(step+1) = 1 + 779*780 + 779 ≈ 608,000 < 1,000,000 ✓
    # Wait: base + step*D + D = base + D*(step+1). With step=D+1: D*(D+2) = 779*781 = 608,399. ✓
    # 
    # But wait, I also need to verify no overlaps between row n-1 and rows 0..n-2.
    # Row n-1 starts at base+step*D. Row n-2 ends at max(base+(n-2)*step+n-2, base+(n-2)*step+D).
    # = base+(n-2)*step+D (since D>n-2 for n>=4).
    # Need base+step*D > base+(n-2)*step+D:
    # step*D > (n-2)*step+D
    # step*(D-n+2) > D
    # step > D/(D-n+2) = D/((n-2)(n-1)/2)
    # For n=4: D=5, (n-2)(n-1)/2=3, D/3=5/3<2. step>=2 suffices. ✓
    # For n=40: D=779, (n-2)(n-1)/2=38*39/2=741, D/741≈1.05. step>=2 suffices. ✓
    # 
    # Great! So with step=D+1, all rows are non-overlapping.
    # But I also need to check that the extra element of row i (base+a_i+D) doesn't 
    # fall in the consecutive range of row i+1 or any other row.
    # 
    # Extra element of row i: a_i + D = base + i*step + D
    # Consecutive range of row j: [base+j*step, base+j*step+n-2]
    # Is base+i*step+D in [base+j*step, base+j*step+n-2]?
    # i*step+D in [j*step, j*step+n-2]?
    # (i-j)*step + D in [0, n-2]?
    # If i=j: D in [0,n-2]? D=(n-2)(n+1)/2 > n-2 for n>=4. ✗ (not in range, good)
    # If i<j: (i-j)*step+D = D-(j-i)*step. With step=D+1: D-(j-i)*(D+1) = D*(1-(j-i))-(j-i).
    #   For j-i=1: D-D-1=-1 < 0. ✗ (not in [0,n-2], good)
    #   For j-i>=1: even more negative. Good.
    # If i>j: (i-j)*step+D = (i-j)*(D+1)+D = (i-j+1)*D+(i-j) >= 2D+1 > n-2. Good.
    # 
    # Also check extra element of row i vs extra element of row j (i≠j):
    # a_i+D vs a_j+D: a_i≠a_j so a_i+D≠a_j+D. ✓
    # 
    # Check extra element of row i vs consecutive range of row n-1:
    # Row n-1 consecutive: [base+step*D, base+step*D+n-2]
    # Extra of row i (i<n-1): base+i*step+D
    # Is i*step+D in [step*D, step*D+n-2]?
    # For i<n-1: i*step+D < (n-1)*step+D <= step*D (need (n-1)*step <= step*D, i.e., n-1<=D)
    # D=(n-2)(n+1)/2. For n=4: D=5>=3=n-1 ✓. For n>=4: D=(n-2)(n+1)/2 >= n-1 iff (n-2)(n+1)>=2(n-1) iff n^2-n-2>=2n-2 iff n^2-3n>=0 iff n>=3. ✓
    # So extra of row i < step*D <= row n-1 consecutive start. ✓
    # 
    # Check extra element of row n-1: base+step*D+D = base+D*(step+1) = base+D*(D+2)
    # vs consecutive ranges of rows 0..n-2: max end = base+(n-2)*step+n-2 < base+(n-1)*step < base+step*D (shown above). ✓
    # vs extra elements of rows 0..n-2: base+i*step+D < base+(n-1)*step <= base+step*D < base+D*(D+2). ✓
    # 
    # So with step=D+1 and base=1, all elements are distinct! ✓
    # 
    # Now verify column conditions:
    # Col j (j=0..n-2): elements = a_0+j, a_1+j, ..., a_{n-1}+j
    # = base+j, base+step+j, ..., base+(n-2)*step+j, base+step*D+j
    # This is the same structure as the rows! (with base'=base+j, step'=step)
    # Mean = (sum of a_i)/n + j = a_{n-2}+j (by construction of bases)
    # = base+(n-2)*step+j, which is the (n-1)-th element (0-indexed: n-2) of col j. ✓
    # 
    # Col n-1: elements = a_0+D, a_1+D, ..., a_{n-1}+D
    # = base+D, base+step+D, ..., base+(n-2)*step+D, base+step*D+D
    # Mean = (sum of a_i)/n + D = a_{n-2}+D = base+(n-2)*step+D, which is in col n-1. ✓
    # 
    # PERFECT! The construction works recursively.
    # 
    # Summary for even n>=4:
    # D = (n-2)*(n+1)//2
    # step = D+1
    # base = 1
    # a_i = base + i*step for i=0..n-2
    # a_{n-1} = base + step*D
    # Row i: [a_i, a_i+1, ..., a_i+n-2, a_i+D]
    
    D = (n-2)*(n+1)//2
    step = D + 1
    base = 1
    
    a = [base + i*step for i in range(n-1)] + [base + step*D]
    
    grid = []
    for i in range(n):
        row = list(range(a[i], a[i]+n-1)) + [a[i]+D]
        grid.append(row)
    
    # Verify (optional, remove for speed):
    # for row in grid: print(*row)
    
    for row in grid:
        print(*row)

solve()