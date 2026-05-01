A = int(input())
B = int(input())
C = int(input())

# Check if all 3 fit in 1 trip
# All three in one box: A inside B inside C, or A and B side by side inside C
# Case 1: A < B < C (all nested)
# Case 2: A and B side by side inside C: (A + B) < C, and we need A < C and B < C (implied)
# Actually the configurations for 1 trip:
# - A inside B inside C: A < B and B < C
# - A and B side by side inside C: (A + B) < C

if (A < B and B < C) or (A + B) < C:
    print(1)
elif A < B and B < C:
    print(1)
else:
    # Check if 2 trips possible
    # Trip 1: A inside B (A < B), Trip 2: C alone
    # Trip 1: A inside C (A < C), Trip 2: B alone
    # Trip 1: B inside C (B < C), Trip 2: A alone
    # Trip 1: A and B inside C ((A+B) < C) - already checked above
    # Trip 1: A inside C, B inside C side by side - same as above
    # For 2 trips: we need to pack all 3 into 2 groups
    # Possible groupings:
    # {A, B} and {C}: A inside B (A < B) -> 2 trips
    # {A, C} and {B}: A inside C (A < C) -> 2 trips  
    # {B, C} and {A}: B inside C (B < C) -> 2 trips
    # {A, B, C} - already checked (1 trip)
    
    # Can we do 2 trips?
    # Option 1: A fits in B
    if A < B:
        print(2)
    # Option 2: A fits in C
    elif A < C:
        print(2)
    # Option 3: B fits in C
    elif B < C:
        print(2)
    else:
        print(3)