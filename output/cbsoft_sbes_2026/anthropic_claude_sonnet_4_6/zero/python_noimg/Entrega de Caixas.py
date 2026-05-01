A = int(input())
B = int(input())
C = int(input())

# Check if all 3 fit in 1 trip
# All three in one box: A and B side by side inside C: (A+B) < C
# Or A inside B inside C: A < B < C
# Or A inside C and B inside C side by side: already covered by (A+B)<C
# Actually let's think about configurations for 1 trip:
# - All inside C: either A<C and B<C and (A+B)<C (two boxes side by side inside C)
# - A inside B, then B inside C: A<B and B<C
# - A inside C, B inside C side by side: (A+B)<C
# Wait, let me reconsider based on the figure description

# 1 trip possibilities:
# 1. A inside B, B inside C: A < B and B < C
# 2. A and B side by side inside C: (A+B) < C
# 3. A inside C, B inside C (but B must fit alone): B < C and A < C - but this is just B<C since A<=B<=C
#    Actually two boxes inside C side by side means (A+B)<C
#    One box inside another inside C: A<B<C

# Let me think about all 1-trip scenarios:
# All 3 boxes transported in 1 trip means they all fit together somehow
# - nest all: A<B<C (strict)
# - two side by side in C: (A+B)<C (A and B fit side by side in C)
# - A inside B, both inside C: A<B and B<C

# 2 trip possibilities:
# - 1 trip carries 2 boxes, 1 trip carries 1 box
# - A inside B (A<B), C alone: 2 trips
# - A inside C (A<C), B alone: 2 trips  
# - B inside C (B<C), A alone: 2 trips
# - A and B side by side in C: already 1 trip
# - A inside C, B inside C side by side: (A+B)<C -> 1 trip

# Check 1 trip
one_trip = False

# All nested: A < B < C (strict inequalities since A<=B<=C given)
if A < B and B < C:
    one_trip = True

# A and B side by side inside C
if (A + B) < C:
    one_trip = True

# A inside B, and B inside C (same as nested)
# A inside C, B inside C side by side: (A+B)<C already covered

# What about A inside B, then A+B... no, once A is inside B, the outer size is B
# So A inside B gives size B, then B inside C: B<C
# That's the nested case

if one_trip:
    print(1)
else:
    # Check 2 trips
    two_trip = False
    
    # A inside B, C separate
    if A < B:
        two_trip = True
    
    # B inside C, A separate
    if B < C:
        two_trip = True
    
    # A inside C, B separate
    if A < C:
        two_trip = True
    
    # A and B side by side... wait that would need a container
    # Actually for 2 trips: one trip carries 2 boxes nested or side by side in third
    # but if side by side in C, that's 1 trip with all 3
    
    if two_trip:
        print(2)
    else:
        print(3)