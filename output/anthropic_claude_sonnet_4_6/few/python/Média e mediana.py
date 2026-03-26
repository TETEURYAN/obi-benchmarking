import sys
a, b = map(int, sys.stdin.read().split())
# mean = median means C must equal the mean, and C must be the median
# mean = (A + B + C) / 3, median = C (when C is between A and B or equals mean)
# For mean == median == C: (A + B + C)/3 = C => A + B + C = 3C => A + B = 2C => C = (A+B)/2
# But C must be integer and be the median (A <= C <= B or C <= A <= B with C as median... wait)
# Actually median is middle value when sorted. If C is the median, then C is between A and B.
# C = (A+B)/2 must be integer. If A+B is even, C = (A+B)/2 which is between A and B (since A < B).
# If A+B is odd, C can't be exactly (A+B)/2 as integer while being median between A and B.
# Wait, let's reconsider: mean = (A+B+C)/3, median could be A, B, or C depending on ordering.
# Case 1: C is median => A <= C <= B (since A < B)
#   mean = C => C = (A+B)/2, must be integer
# Case 2: A is median => C <= A <= B
#   mean = A => A+B+C = 3A => C = 2A - B
#   Check: C <= A: 2A-B <= A => A <= B ✓ (since A < B, C < A, so A is indeed median)
# Case 3: B is median => A <= B <= C
#   mean = B => C = 2B - A
#   This gives C >= B > A, so B is median. But we want smallest C, so this is larger.
# 
# So candidates: 
#   - C = (A+B)/2 if (A+B) even (Case 1)
#   - C = 2A - B (Case 2, always valid)
# We want the smallest C.
# 
# Case 2 gives C = 2A - B. Since A < B, this is negative or less than A.
# Case 1 gives C = (A+B)/2 which is between A and B, so larger than 2A-B.
# 
# So the answer is always C = 2A - B? Let's verify with examples:
# Test 1: A=1, B=2 => C = 2*1-2 = 0. Sorted: 0,1,2. Median=1=A. Mean=(0+1+2)/3=1. ✓
# Test 2: A=6, B=10 => C = 2*6-10 = 2. Sorted: 2,6,10. Median=6=A. Mean=(2+6+10)/3=6. ✓
# Test 3: A=1, B=1000000000 => C = 2*1-1000000000 = -999999998. ✓
# 
# But wait, could Case 1 give smaller C? No, (A+B)/2 > 2A-B when A < B.
# What if we consider C < 2A-B? Then sorted order is C <= ... but mean would need to equal median.
# If C < A, median is A, mean = (A+B+C)/3 = A => C = 2A-B. That's the minimum for this case.
# So answer is always 2A - B.

print(2 * a - b)