
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
E = int(data[1])

indians = []
index = 2
for i in range(E):
    V = int(data[index])
    D = int(data[index + 1])
    indians.append((V - 1, D))  # 0-based position
    index += 2

# Simulate until back to initial positions (ignoring directions)
initial_pos = sorted([p for p, d in indians])

# Use a set of (pos, dir) but since we need to detect cycle on positions only
# We simulate the configuration of positions (sorted) and find when it repeats initial

# But directions matter for movement, we need full state for simulation
# Since N up to 1e6 but E<=1000, we can simulate with map or list of size E

# Represent each indian as position and direction
# But to detect when positions match initial (regardless of who and directions)

from collections import defaultdict

def simulate_step(pos_dir):
    # pos_dir: list of (pos, dir)
    new_pos_dir = []
    events = defaultdict(list)  # pos -> list of (incoming_dir, original_index or just info)
    
    for p, d in pos_dir:
        next_p = (p + d) % N
        events[next_p].append((d, p, d))  # incoming dir, original pos, original dir
    
    for target_pos in range(N):
        arrivals = events.get(target_pos, [])
        if not arrivals:
            continue
        if len(arrivals) >= 2:
            # collision: all reverse direction, stay at original? No.
            # The rule is about two jumping to same or adjacent about to collide
            # We need to process all possible interactions carefully.
    
    # Better way: since E<=1000, N<=1e6, but we need O(E log E) per step or better
    
    # The key is that indians move independently until interactions.
    # Interactions are:
    # 1. Two indians land on same spot (from opposite directions)
    # 2. Two indians in adjacent toras moving towards each other
    
    # So let's model current state as dict pos -> direction
    # Since no two on same initially and we maintain that? No, they can collide.
    
    # From description: when two jump to same, they BOTH stay? "ambos permanecem nas toras"
    # "permanecem nas toras" but which toras? The one they jumped to or original?
    # The description says "caem na mesma tora ao mesmo tempo. Nesse caso, ambos permanecem nas toras"
    # It's ambiguous but probably they both end up on that tora? But then two on same tora.
    # But initial condition says at most one per tora at start, but during dance it can happen?
    # But the end condition is "as toras ocupadas por um índio são exatamente as mesmas toras ocupadas no início"
    # implying we care about set of occupied toras.
    
    # Let's look at sample.
    
    # First sample:
    # N=6 E=4
    # positions 2,3,5,6 (1-based) all direction 1 (clockwise)
    # So positions 1,2,4,5 (0-based)
    
    # All moving +1.
    # Next positions would be 2,3,5,0
    # No two to same, no adjacent moving towards each other (since all same direction, no).
    # So new positions 0,2,3,5
    
    # Next step: from 0,2,3,5 all +1 -> 1,3,4,0
    # sorted 0,1,3,4
    
    # Next: from 0(+1),1(+1),3(+1),4(+1) -> 1,2,4,5
    # sorted 1,2,4,5 which is initial (1,2,4,5)
    # And output is 3. Yes matches.
    
    # Second sample: N=3 E=1 pos 2 (1-based so 1), dir -1
    # So position 1, dir=-1. Next: 1-1=0
    # Then from 0, -1 -> 0-1 = 2 (mod 3)
    # Then from 2, -1 -> 2-1=1
    # Back to start after 3 steps. Output 3.
    
    # Third sample matches the figure, output 4.
    
    # Now about collisions.
    # In first sample no collision happened.
    # Let's think of a case with collision.
    
    # Suppose two adjacent, moving towards each other.
    # Say N=5, indians at 0 dir=1, at 1 dir=-1.
    # They are consecutive, moving towards each other (0->1, 1->0).
    # So according to rule, they don't jump, and reverse direction.
    # So after step: still at 0 and 1, but directions become -1 and +1 respectively.
    
    # Another case: two moving to same spot.
    # Say at 0 dir=1, at 2 dir=-1. N=4.
    # Next: 0->1, 2->1. So both jump to 1.
    # Then "caem na mesma tora", "ambos permanecem nas toras, mas passam a pular na direção contrária"
    # So both end at position 1? But two at same position.
    # But the end condition talks about "toras ocupadas", so set of positions.
    # But if two at same, occupied is one tora.
    # The problem says "a tora onde o índio inicia", and "no início da dança uma tora terá no máximo um índio".
    # But during it might allow multiple?
    # But in output we only care when the set of occupied positions returns to initial set.
    
    # But if two occupy same, then number of occupied decreases.
    # Is that allowed?
    
    # The note: "Note que se o índio não pula e inverte seu sentido, mas ao mesmo tempo um outro índio cair na mesma tora no sentido contrário, caimos no primeiro caso, e ambos os índios na tora invertem seus sentidos (assim, o índio que estava na tora anteriormente inverte seu sentido novamente)."
    
    # This note suggests that an indian can stay (not jump) and another can jump into his tora.
    # So multiple indians can be at same tora.
    
    # So we must allow multiple indians per tora.
    
    # So state is multiset of positions? No, since indians are indistinguishable for end condition, only the set? No, if two at same position, it's still one position occupied but with multiplicity? But the end is "as toras ocupadas por um índio são exatamente as mesmas"
    # "as toras ocupadas por um índio são exatamente as mesmas toras ocupadas no início da dança"
    # It says "toras ocupadas", so the set of toras that have at least one indian.
    # Not counting multiplicity.
    
    # But if two at same, the set has size less than E.
    # Is that possible in the dance? Probably yes.
    
    # But to detect end, we need when the set of positions with at least one indian is the same as initial set.
    # And "não importando qual índio está em cada tora e nem os sentidos"
    # Yes, so only the set of occupied positions matters for termination.
    
    # Now for simulation, since indians have individual directions, we need to track each indian's position and direction.
    # Indians are distinguishable only by their state (pos, dir).
    # Since E<=1000, we can simulate each step by moving all indians according to rules.
    
    # But the rules are a bit tricky to implement because interactions are between pairs.
    
    # Let's formalize the rules.
    
    # Each indian attempts to jump to next tora in his direction.
    # But there are two types of interactions:
    
    # Type 1: if two indians are jumping to the SAME tora (must be from opposite sides), then they both land there and both reverse direction for next time.
    
    # Type 2: if two indians are in consecutive toras and are jumping TOWARDS each other, then they both stay put and both reverse direction.
    
    # Note that these can interact in complex ways if more than two indians.
    # Also the note says if one is staying (due to type 2) and another jumps into him, then it becomes type 1.
    
    # So perhaps it's better to think in terms of what happens at each tora.
    
    # This seems complicated. Maybe we need to process all possible "would be" moves and resolve conflicts.
    
    # Since it's a circle and movement is only +1 or -1, we can think of indians as particles on a circle with velocities +1 or -1.
    # The interactions are like elastic collisions where they bounce (reverse direction).
    
    # In fact, this looks a lot like particles colliding and reversing direction, which is equivalent to them passing through each other without interaction.
    
    # Let's see.
    
    # Case 1: two moving towards each other on adjacent positions: they "bounce" i.e. reverse directions and stay. But if they passed through, the one that was going right would continue to the left guy's position +1, but since they stay and reverse, the effect is that the identities swap in terms of velocity.
    # After collision, the one on left now has velocity -1 (was +1, reversed), one on right has +1 (was -1, reversed).
    # If they passed through, the left one would have continued with +1 to next, but that's not matching.
    # No.
    
    # Let's say positions 0 and 1, left at 0 vel=+1, right at 1 vel=-1.
    # After "don't jump, reverse": left stays at 0 with vel=-1, right stays at 1 with vel=+1.
    # If they passed through without changing vel: left would go to 1 with +1, right would go to 0 with -1.
    # So final: position 0 has vel=-1, position 1 has vel=+1.
    # Which is the same configuration as the "stay and reverse".
    # The only difference is which indian is which, but since they are indistinguishable except for velocity, the state is the same.
    
    # Now, for two jumping into same spot from opposite.
    # Say positions 0 vel +1, position 2 vel -1, N>3, no others.
    # They both move to position 1.
    # According to rule, both remain at 1 (I assume both at position 1), and both reverse direction.
    # So at position 1 we have two indians: one with vel=-1 (was +1), one with vel =+1 (was -1).
    
    # If they passed through: the +1 from 0 would go to 1 then continue? But in one step, from 0 to 1 with +1, from 2 to 1 with -1.
    # If pass through, they would swap and continue but in one discrete step it's both at 1 with their velocities unchanged: so at 1: vel+1 and vel-1.
    # Which matches exactly the "both at 1, reverse direction" because reversing +1 becomes -1, reversing -1 becomes +1, so same as keeping original directions.
    # Again, same final state.
    
    # So in both types of "collision", the effect on the configuration (positions and directions present) is the same as if the indians passed through each other without interacting, keeping their directions.
    
    # And the note about combined case also fits because it's like multiple pass throughs.
    
    # Therefore, the overall dynamics is equivalent to each indian moving independently with constant velocity, passing through others, and the occupied positions at any time are just the positions of all these independent movers.
    
    # And since the termination condition depends only on the set of occupied positions (not who or directions), we can simulate each indian independently moving at constant speed, and after T steps, each indian i is at (initial_pos_i + T * dir_i) mod N.
    # Then the set of these positions should equal the initial set of positions.
    
    # We need the smallest T >=1 such that the set {(p + T * d) mod N for each indian} == initial set of positions.
    
    # Yes!
    
    # And since indians can overlap, the set size might be smaller, but when it matches the initial set, it stops.
    
    # This matches the samples:
    # First sample: positions [1,2,4,5] (0-based), all d=1
    # After T steps: [1+T,2+T,4+T,5+T] mod 6
    # We need set of these == {1,2,4,5} mod 6.
    # For T=3: 1+3=4, 2+3=5, 4+3=7%6=1, 5+3=8%6=2 → {4,5,1,2} yes same.
    # Perfect.
    
    # Second: one indian at 1, d=-1.
    # After T: (1 - T) mod 3
    # Set has one element. Initial set {1}.
    # When (1-T)%3 ==1 ⇒ -T %3 ==0 ⇒ T%3==0. Smallest T=3.
    # Yes.
    
    # For the figure, presumably it works.
    
    # If there are opposite directions, it should still work due to the equivalence.
    
    # Great! So now we can implement this efficiently.
    
    # Since E<=1000, N<=1e6, we cannot simulate step by step up to potentially large T (could be up to N).
    # What is the max possible T? Since it's cyclic, the period divides something like lcm of periods, but worst case T can be up to N I think.
    # But N=1e6, if we simulate T up to 1e6, and each step compute set of E positions, it would be 1e6 * 1000 = 1e9 ops, way too slow.
    
    # Need smarter way.
    
    # We need smallest T>0 such that the set S_T = {(p_i + T * d_i) mod N for i=1 to E} equals S_0 = {p_1, ..., p_E}
    
    # Since indians are moving independently on the circle.
    
    # One way is to notice that this is equivalent to the multiset of positions returning, but since we use set, it's when all the positions are a permutation of the initial ones, allowing for overlaps only if initial had overlaps but initial doesn't.
    
    # Initial has unique positions.
    
    # But during, if two land on same, then |S_T| < E, so cannot equal S_0 which has E distinct.
    # So we only need cases where all E positions are distinct and exactly match the initial E positions.
    
    # So it's when the map i -> (p_i + T*d_i) mod N is a permutation of the initial positions.
    
    # To find minimal T.
    
    # Since E is small (1000), but N large (1e6), we need to be careful.
    
    # One standard way for these "when does the set of points return" with constant velocities is to consider the relative movements.
    
    # But perhaps a better observation: because it's a circle, each particle returns to its starting point after a period depending on gcd.
    
    # But since directions are +1 or -1, moving at speed 1.
    
    # The configuration of positions returns when each position is occupied by some particle.
    
    # Since particles don't really interact (in effective model), it's like labels moving.
    # But we don't care about labels.
    
    # To compute minimal T, we can simulate the movement but since N large we cannot loop T=1,2,... checking each time.
    
    # Checking each time would be too slow anyway.
    
    # We need to find the period of the entire system.
    
    # The state is fully determined by the positions of all E indians (since directions are constant in the effective model!).
    
    # In the effective "pass through" model, directions never change! Each keeps its own d forever.
    
    # Yes.
    
    # So each has fixed velocity.
    
    # The set of positions at time T is { (p + T * d) % N | for each (p,d) in indians }
    
    # We need minimal T > 0 s.t. this set equals the initial set.
    
    # Since E<=1000, we can consider that for the sets to be equal, every final position must be one of the initial positions.
    
    # But to find the minimal such T efficiently.
    
    # Note that T can be up to lcm of individual periods, but individual period for a particle is N / gcd(N,1) =N, so up to N.
    # We cannot check all T.
    
    # We need a smarter approach.
    
    # Since all speeds are \pm 1, we can separate two groups: clockwise and counterclockwise.
    
    # Let CW be the indians with d=1, their positions at T: (p + T) mod N
    # CCW with d=-1: (p - T) mod N
    
    # So the occupied positions at time T: { (p + T) % N for p in CW_pos } union { (q - T) % N for q in CCW_pos }
    
    # This must equal initial_positions set.
    
    # Let S be the initial set of positions (0 to N-1).
    
    # Then S = { (x + T) mod N | x in S_cw } U { (y - T) mod N | y in S_ccw }  where S_cw is initial pos of cw indians, etc.
    
    # But since the groups are fixed.
    
    # Let A be list of initial positions of +1 movers.
    # B be list of initial positions of -1 movers.
    
    # Then at time t, positions = [(a + t) % N for a in A] + [(b - t) % N for b in B]
    # The set of these must == initial S = set(A+B)
    
    # Since |A| + |B| = E <=1000, to find min t>0.
    
    # One way that works in time is to note that the configuration repeats every 2N steps at latest, because +t and -t mod N, period 2N for the pair.
    # But 2N = 2e6, with E=1000, if we loop t from 1 to 2*N, and for each t compute the set (which is O(E) to build set), total time is 2e6 * 1000 ~ 2e9 operations, too slow for python.
    
    # Need faster.
    
    # We need to check for each possible t if the generated positions land exactly on the initial S, with no duplicates outside or missing.
    
    # Since it's a set equality, all generated positions must be in S, and there must be exactly E distinct (no overlaps in the landed positions).
    
    # Since |S|=E (initially distinct), we need the E computed positions to be all distinct and all inside S.
    
    # To speed up, perhaps we can use the fact that each moving point must land on some initial position.
    
    # But maybe we can model it as each initial position must be "hit" by exactly one mover.
    
    # A position x in S at time t is occupied if there exists an initial a in A s.t. (a + t) % N == x, i.e. a == (x - t) % N and that a was in A
    # or there exists b in B s.t. (b - t)%N ==x i.e. b == (x + t) % N and b in B.
    
    # So for every x in S, the number of ways it can be reached: whether (x - t)%N is in A or (x + t)%N is in B. Exactly one of them should be true (since exactly one occupant).
    
    # But since we require exactly the set S occupied, and E positions generated, if there are no two landing on same then if all landed in S then it must cover all because |S|=E.
    
    # So condition is: all the E landing positions are distinct AND all are in S.
    
    # To find minimal t, since N large but E small, perhaps we can consider for each possible "target".
    
    # Each mover must map to a unique position in S.
    
    # But perhaps it's like matching.
    
    # Since E<=1000, we can simulate the positions but jump to next interesting event.
    # But what are events? When two particles land on same position.
    
    # But since we have the pass-through model, overlaps happen when two particles cross.
    
    # But for our purpose we need when the set returns.
    
    # Let's consider that the entire configuration of positions is periodic with period dividing N for all +1 or all -1, but mixed it's lcm(N, N)=N but as above.
    
    # If all have same direction, say all +1, then the set shifts by t each time, so it returns when t % N ==0, but only if the gaps are preserved, no: the set returns when shifting the set by t gives back same set.
    # I.e. S + t ≡ S mod N, meaning S is union of cycles or something.
    # In first sample, S={1,2,4,5}, S+3 = {4,5,7%6=1,8%6=2} = same set. Even though t=3 not multiple of N.
    
    # So it's when t is such that adding t mod N permutes the set S.
    
    # But we have two groups.
    
    # Let S be the initial positions set.
    # But the movers are partitioned into two types: those that will be at s + t, those at s - t.
    
    # The ones that started in A (cw) will be at A+t, the B-t.
    
    # So it's not that any in S can go to any.
    
    # The "labels" of velocity are attached.
    
    # The positions in S have associated "which velocity group they belong to"? No, because when they "collide and reverse" it's like exchanging velocities.
    
    # In the effective model, the velocities stay with the "soul" that keeps moving.
    # But for the set, it's just positions.
    
    # To compute efficiently, since E<=1000, we can use a map from position to list of velocities, but.
    
    # Notice that because of the equivalence, the positions at time t are exactly the same as if no interactions, each keeps moving.
    # To find min t>0 s.t. the set of positions at t equals set at 0.
    
    # To find this fast, we can consider all the individual motions.
    # Each particle i has position p_i(t) = (init_p_i + t * d_i) % N
    
    # We need {p_1(t), p_2(t), ..., p_E(t)} == {p_1(0), ..., p_E(0)} as sets.
    
    # Since N is large, but number of distinct p(t) over time is limited per particle but not helpful.
    
    # One efficient way: the time when the configuration can possibly return must be a multiple of the cycle time for each "component".
    
    # But perhaps better: note that for the set to be the same, each p_i(t) must equal some p_j(0).
    
    # So for each particle i, there must be some j such that (p_i + t * d_i) % N == p_j
    
    # But with all distinct.
    
    # This is like the permutation induced.
    
    # But with E=1000 it's hard to check many t.
    
    # What is the possible range of T? In worst case it can be N, but we need O(E^2 log N) or better.
    
    # Let's think differently.
    # Since all move at speed 1, the relative position between two +1 is fixed, between two -1 is fixed, between +1 and -1 changes at rate 2.
    
    # The set S(t) = (A + t) U (B - t) mod N
    
    # We want S(t) = S(0) = A U B
    
    # So (A + t) U (B - t) ≡ A U B mod N
    
    # This means that every point in A+t must be in A or B, and every in B-t in A or B, and no duplicates outside.
    
    # For every a in A, (a + t) % N must be in S
    # For every b in B, (b - t) % N must be in S
    # And all these E values must be distinct.
    
    # Since S has E elements, equivalent to the map being injective on the positions.
    
    # To find smallest t, we can consider that t must satisfy that for every mover, its new pos is in S.
    
    # So for each cw mover a, (a + t) % N in S  ⇒  t % N in (s - a) % N for some s in S
    # So for each a, t must be congruent to one of the (s - a) for s in S.
    
    # But since many, it's per particle constraint.
    
    # But with E=1000, too many.
    
    # Since it's modular, perhaps we can use BFS to find the minimal time where the occupied set returns, but with state being the set? 2^1000 impossible.
    
    # No.
    
    # The positions are on circle of size 1e6, can't use bitsets.
    
    # We need another insight.
    
    # Since the particles are effectively passing through, the positions occupied at time t are the initial positions "plus" the displacement of their "velocity".
    # But let's assign to each initial position its "effective" velocity? But it changes upon collision.
    
    # In the pass through model, the positions that are occupied are the same as the positions where there is a "soul" passing.
    # The set S(t) is union over all initial (pos, vel) of pos + vel*t.
    
    # To have S(t) = S(0).
    
    # Let's consider the difference.
    # A position x is occupied at time 0 if x in S.
    # At time t, x is occupied if there is some initial y in S such that y + d*y * t ≡ x mod N, where d*y is the direction of the indian that started at y.
    # So it depends on which direction was at which starting position.
    
    # So we do have to keep the pairing of position and its direction.
    
    # Let me create two sets:
    pos_cw = set()
    pos_ccw = set()
    all_pos = set()
    
    for p, d in indians:
        all_pos.add(p)
        if d == 1:
            pos_cw.add(p)
        else:
            pos_ccw.add(p)
    
    # Now, at time t, the occupied positions are:
    # for each original cw: (p + t) % N
    # for each original ccw: (p - t) % N
    
    # So occupied = set( (p + t) % N for p in pos_cw ) | set( (p - t) % N for p in pos_ccw )
    
    # We need this occupied == all_pos, and also that there are no collisions i.e. the size of the union must be E (no two land on same spot).
    
    # Yes.
    
    # To find the smallest t >= 1 satisfying that.
    
    # Since E<=1000, we can loop over possible t in a smart way.
    
    # Notice that for there to be no overlap in the landed positions, and all land in all_pos.
    
    # But to make it fast, observe that if there is any overlap or landing outside, it's invalid.
    
    # But how to find the min t without checking all?
    
    # The period is at most 2*N because (t + 2N) = t mod N for both + and - since - (t+2N) = -t -2N ≡ -t mod N.
    # So the configuration repeats every 2N.
    # So the answer is at most 2N <= 2e6.
    
    # If we can check each t in O(E / 32) or faster using some trick, but in python hard.
    
    # But E=1000, 2e6 * 1000 = 2e9 too slow.
    # We need to reduce the time per t.
    
    # We cannot afford to rebuild the set every time.
    
    # We need a way to only check candidate t's.
    
    # Let's consider what t makes all the moved positions land inside S.
    
    # For a fixed t, for every p in pos_cw, (p+t)%N must be in all_pos
    # for every p in pos_ccw, (p-t)%N must be in all_pos
    
    # So t must satisfy for every cw p: (p+t) %N in S  ⇒ t % N in (s - p) %N for some s in S
    
    # But to satisfy for all p simultaneously.
    
    # This is like t must be in the intersection of certain arithmetic progressions or possible shifts for each.
    
    # But with 1000, hard.
    
    # Since N<=1e6, we can precompute for each possible position whether it is in S.
    # Use a boolean array is_occupied = [False]*N but N=1e6 ok for memory.
    
    # Then, to find min t, we still need to check for each t=1 to 2*N if the condition holds.
    
    # But to check fast, for each t we would need to verify E positions are in S and no duplicates.
    
    # Verifying E=1000 for 2e6 times is 2e9, too slow (~20 seconds in pypy maybe, but likely TLE).
    
    # We need faster verification.
    
    # One way is to notice that overlaps happen only when two specific particles meet.
    
    # We can find all possible times where a collision (overlap) happens, and only check the t's that are not collision times, but still too many t to check.
    
    # We need when the set equals initial, which is rare.
    
    # How many times does it happen? Probably the answer is small? But constraints don't say, answer can be up to 2e6 I guess, but we need to output the number.
    
    # Let's see constraints again.
    # N <= 1.000.000, E<=1000.
    # Time limit not specified but in OBI usually 1 or 2 seconds.
    # In python we can do ~1e8 operations per second roughly.
    # So 2e9 is too much.
    
    # Need O(N) or O(E^2 + N) at worst but N=1e6 ok if small constant.
    
    # Let's think of it as the positions of cw group are rotating one way, ccw the other.
    
    # The occupied set changes when one of the particles moves to a position that was not occupied or leaves.
    # But still.
    
    # Since S is fixed, we can think of each position in S must be "covered" by exactly one "source" at time t.
    
    # A position x is covered by a cw source if there is p in pos_cw s.t. p + t ≡ x => p = x - t, so if (x - t) % N in pos_cw
    # Covered by a ccw source if (x + t) % N in pos_ccw.
    
    # For the configuration to have exactly the positions in S occupied with exactly one each (no overlap means no position covered twice, and no extra but since only E movers, if no double cover then no extra).
    
    # So we need that for every x in S, the number of coverings = 1. I.e. exactly one of the two: either (x-t)%N in pos_cw or (x+t)%N in pos_ccw, but not both.
    
    # For positions not in S, they should have zero coverings, but if a mover lands outside S, then that landing position (not in S) would have a cover, but also some x in S would have zero. So if every x in S has exactly 1, then total covers = E, so no covers outside.
    
    # Perfect. So condition is: for ALL x in initial S, exactly one of the following is true:
    # 1. (x - t) % N is in pos_cw
    # 2. (x + t) % N is in pos_ccw
    
    # Not both.
    
    # This is useful because now we can iterate over all x in S (only 1000 of them), but still for each t we check 1000, same problem.
    
    # But now, we can see that this must hold for all x.
    
    # To make it fast, perhaps we can use that t is the same for all.
    
    # Let's consider for each position x in S, depending on t, which "origin" it comes from.
    
    # But maybe we can assign for each possible t mod something.
    
    # Since N<=1e6, we can actually simulate all particles' positions but we don't loop on t, instead we can find the cycle length by simulating until repeat but with smart structure.
    
    # Since the state is the assignment of directions to the positions? But no.
    
    # In the effective model directions are fixed to the "particles".
    # The full state that repeats is the positions of all cw particles and all ccw.
    # Since they all move rigidly, the relative positions within cw group are fixed, same for ccw.
    
    # The cw particles are always separated by the same differences.
    # The set A + t mod N is just the whole set A rotated by t.
    
    # Same for B - t.
    
    # To have (A + t mod N) union (B - t mod N) == S
    
    # And |union| == |A| + |B| i.e. (A+t) and (B-t) are disjoint.
    
    # Yes.
    
    # Since E small, perhaps we can consider the possible t that make A + t subset of S, but A+t is E/2 points, still hard.
    
    # Let's see the constraints again.
    # There is "Em um conjunto de casos de teste que totaliza 40 pontos, N ≤ 100 e E ≤ 100."
    # So there are subtasks.
    # Probably there are cases with small N and large N.
    # For full points we need efficient solution.
    
    # For N<=100 we can simulate easily.
    # But we need for N=1e6, E=1000.
    
    # Let's think about what the answer represents.
    # It's the order of the transformation in the group.
    
    # The operation is rotating the cw group by +1, ccw group by -1 each step.
    
    # We want the smallest t >0 such that rotating A by t and B by -t gives back sets whose union is S and they don't overlap.
    
    # To find min t, we can consider that for the cw particles, their positions at t must be in S, so for each a in A, a+t mod N in S.
    # So t ≡ s - a mod N for some s in S.
    # But since this must hold simultaneously for all a in A with distinct s.
    # It means that the shift t must map the set A to some subset of S via +t, and B to the complement via -t.
    
    # That is, there is a subset X of S such that X = (A + t) mod N, and S - X = (B - t) mod N.
    
    # Yes.
    
    # Since E<=1000, but choosing subset is impossible.
    
    # Notice that if I add t to both sides or something.
    
    # Let's consider a particular point.
    
    # Let's consider the sum of all positions.
    
    # Initial sum_S = sum of all_pos
    
    # At time t, sum of positions = sum(A + t) + sum(B - t) = sum(A) + sum(B) + t * |A| - t * |B| = sum_S + t*(|A| - |B|)
    # mod N? But since it's positions on circle, sum mod N might be useful.
    
    # The actual sum is not mod, but the positions are mod N so the representative sum differs by multiple of N when wrapping.
    # So if a particle crosses 0 it subtracts N in the 0..N-1 representative.
    # So the sum can change by arbitrary multiples, not very helpful.
    
    # Let's try to find when a collision happens i.e. when two particles occupy same spot.
    # For two cw: (a1 + t) == (a2 + t) mod N never unless a1==a2.
    # Two ccw never.
    # One cw and one ccw: a + t ≡ b - t mod N ⇒ 2t ≡ b - a mod N ⇒ t ≡ (b-a)* inv(2) mod N/gcd(2,N)
    # So possible collision times can be calculated, there are |A|*|B| possible collision times mod N/gcd(2,N).
    # With E=1000, |A|*|B| ~ 2.5e5, so about 250k possible collision times.
    # But we need not only no collision but also that all positions are in S.
    
    # For the positions to be in S, for a cw particle at a, a+t must be in S.
    # So for each cw a, the possible t for which a+t in S are t = (s - a) % N for each s in S, so E possibilities per a, total E*E/2 ~ 5e5 possible t per group.
    # Then the t that satisfy for all cw and all ccw that their landing is in S would be the t that are in the possible for every particle.
    # That seems hard to compute intersection.
    
    # Perhaps we can use brute force on possible t from the possible shifts.
    
    # Since for the cw set, the possible t that make all (A + t) subset of S.
    # Because the relative distances in A are fixed, the number of possible t where the entire pattern of A fits inside S is small.
    
    # Specifically, for a fixed set A and S, the possible shifts t where (A + t) mod N is subset of S.
    # Since it's modular, but because N is large and E small, but to find all such t, one way is to pick one reference a0 in A, for each possible s in S, assume a0 maps to s, then t = (s - a0) % N, then check if for this t all other a in A, (a + t)%N is in S. This takes O(E * E) time = 10^6, acceptable!
    
    # Yes! Since E=1000, E^2 = 1e6, perfectly fine.
    
    # Similarly we have to consider the B as well.
    
    # So, the possible t's that make all cw particles land in S are at most E (one for each possible image of a reference particle), and we can collect all t where the whole A+t subset S, in O(E^2) time.
    
    # Likewise for B: possible t where all (B - t) subset of S, again by picking reference b0, for each possible target s in S, t = (b0 - s) % N  (because b0 - t ≡ s => t ≡ b0 - s), then check if all other b, (b - t)%N in S. Again O(E^2).
    
    # Then, the possible t that satisfy BOTH all cw land in S and all ccw land in S are the intersection of these two lists of possible t's.
    
    # Since each list has at most E candidates (usually much less), we can collect set or sorted list of possible t from cw, from ccw, take intersection, also remove t=0.
    
    # Then, for each such candidate t (at most 1000), we need to check if there are no overlaps between the (A+t) and (B-t), i.e. the two sets are disjoint.
    # Since if both subsets of S, |A|+|B|=E=|S|, then if disjoint, their union will be exactly S.
    # Perfect!
    
    # So we only need to check for each candidate t in the intersection whether set(A+t) and set(B-t) are disjoint.
    
    # To do that, we can for each candidate, generate the positions for one group and put in a set, then check the other group doesn't intersect it. Since per t it's O(E), and 1000 candidates *1000 =1e6 again fine.
    
    # But actually number of candidates in intersection is likely very small, but worst case if many overlaps in possible t it's ok, 1e6 fine.
    
    # We also need the smallest t>0, but since t is mod N, the actual smallest positive is the min among all such t % N, but wait, t we computed is between 0 and N-1.
    
    # But the configuration has period 2N, because for t and t+N, + (t+N) = +t +N ≡ +t, but -(t+N) = -t -N ≡ -t, so same.
    # No: (p + (t+N)) %N = p+t +N %N = p+t, same for - too. So actually period is N!
    # -(t + N) % N = (-t -N) % N = (-t) % N, yes same.
    # So the positions at t and t+N are exactly the same.
    # So we only need to consider t = 0 to N-1.
    
    # In our candidate generation, when we do (s - a) % N we get all possible in 0..N-1.
    
    # Is t=0 always a solution? Yes, but we want minimal >0.
    
    # If there is a smaller t>0, good.
    
    # What if the only solution is t multiple of N, then answer is N? But in second sample N=3, answer=3.
    # Yes.
    
    # In first sample N=6 answer=3.
    
    # Perfect.
    
    # Now, one issue: if |A|+|B| < E? No.
    # If some t makes two in A+t land on same? But since all a distinct, a1 +t == a2 +t iff a1==a2, impossible.
    # Same for B-t.
    # Only possible overlap is between a cw and a ccw landing on same.
    
    # Yes.
    
    # Also if S has duplicates? But problem says at most one per tora initially, so |S|=E.
    
    # Perfect.
    
    # So now let's implement this.
    
    # We will:
    # - Read N, E, the list of (p, d), p 0-based.
    # - Collect list_A = [p for p,d in indians if d==1]
    # - list_B = [p for p,d in indians if d==-1]
    # - S = set(list_A + list_B)
    # - If len(S) != E: but shouldn't happen.
    
    # Then, if E==0, but E>=1? No E>=1.
    
    # To get possible t for CW:
    # if not list_A:
    #   possible_cw = set(range(N)) but that's not practical. If no cw, then always "satisfied" for cw.
    # We need to handle cases where A or B empty.
    
    # If A empty, then possible_cw_t = all t, but we cannot list all.
    # Similarly for B.
    # So we need to handle separately.
    
    # Cases:
    # 1. Both A and B non-empty: then generate possible_t_cw (list or set), possible_t_ccw, then intersection.
    # 2. Only A (all cw): then possible t are those where (A + t) %N subset S. Since |A|=E=|S|, it means A + t == S as sets. So it's when shifting the whole set by t gives back itself.
    # 3. Only B similar.
    
    # But in our method, if A empty, then the condition for cw is always true, so possible_t = the possible from ccw only.
    # And since |B|=E, B-t subset S and | |=E means B-t == S, and no overlap issue since no A.
    # Yes.
    
    # So to make code handle empty, we can:
    # possible_ts = None
    # if list_A:
    #     possible_cw = set()
    #     a0 = list_A[0]
    #     for s in S:   # S is set of int
    #         t = (s - a0) % N
    #         # check if all of A map into S
    #         good = True
    #         for a in list_A:
    #             if (a + t) % N not in S:
    #                 good = False
    #                 break
    #         if good:
    #             possible_cw.add(t)
    #     possible_ts = possible_cw
    # if list_B:
    #     possible_ccw = set()
    #     b0 = list_B[0]
    #     for s in S:
    #         t = (b0 - s) % N
    #         good = True
    #         for b in list_B:
    #             if (b - t) % N not in S:
    #                 good = False
    #                 break
    #         if good:
    #             possible_ccw.add(t)
    #     if possible_ts is None:
    #         possible_ts = possible_ccw
    #     else:
    #         possible_ts = possible_ts & possible_ccw
    # if possible_ts is None:  # no indians, but not possible
    #     pass
    
    # Then, candidates = [t for t in possible_ts if t != 0]
    # if not candidates:
    #     # only t=0, then it must return at t=N ? But since period N, if only 0 then answer N?
    #     # In all moving same direction, like sample 2, let's see.
    #     # Sample 2: one indian d=-1, so A=[], B=[1], S={1}, N=3
    #     # Since A empty, possible_ts = possible from B.
    #     # b0=1, for s in {1}, t = (1 - 1)%3 =0
    #     # check for b=1, (1 - 0)%3=1 in S yes.
    #     # So possible_ts = {0}, no other.
    #     # But we know at t=3 it returns, but 3%3=0, so indeed the next is N=3.
    #     # So if 0 is the only possible mod N, then the smallest positive is N.
    
    # Yes!
    
    # So after getting possible_ts (which are all t mod N that work for the landing in S),
    # Then we need to filter those where the two groups don't overlap.
    # For t in possible_ts:
    #   if t==0: continue  # we will handle later
    #   Compute positions from A+t and B-t, see if any common.
    #   Since we already have that A+t all in S, B-t all in S, and |A|+|B|=E=|S|, then if no intersection between (A+t) and (B-t), then union exactly S.
    #   If there is intersection, then union has size <E, so some other position in S not covered, but we don't need to check further.
    
    # So in code:
    
    # ans = N  # at latest it should return at N? Wait is it always true that at t=N it returns?
    # At t=N, p + N %N =p, p -N %N =p, so yes every particle back to start, so S(N)=S(0), so N is always a valid answer.
    # So we can set ans = N
    # Then for each valid t in 1..N-1 that satisfies, take min.
    
    # So in the possible_ts, they are all t in 0..N-1 that make all land positions in S.
    # Then among them, we need to check the disjoint condition, and take the minimal t>0, or N if none.
    
    # For t=0, the disjoint is true (since initial no two on same, and A and B partition S).
    # If there is a t in 1 to N-1 in possible_ts that has disjoint A+t and B-t, then it's a candidate.
    
    # If the only one is 0, then ans=N.
    
    # Is N the smallest? In the single particle case yes, since it goes around the circle.
    # If all particles have same direction, say all cw, then at t=N all back.
    # But there may be smaller t where the set is rotated but coincides with original set.
    # Like if equally spaced, e.g. every position occupied, then any t works.
    # But if E=N, then S is all positions, any t the set is all, so answer would be 1.
    # Let's check if our code handles.
    # If E=N, S = all 0..N-1, then for any t, A+t will be in S always.
    # In our generation, since for a0, for every s there is t=s-a0, and since S is full, the check will always pass, so possible_cw will have all N values.
    # Then possible_ts will be all 0..N-1.
    # Then we need to check for each t=1 to N-1 whether A+t and B-t disjoint.
    # But if E=N, then |A|+|B|=N, S has N, so to have disjoint and union S means no overlap between the two groups' positions.
    # But since they fill all, it means the positions of A+t and B-t must cover everything without overlap, which is always true if they don't overlap.
    # But if for some t a cw and ccw land on same, then overlap, size would be <N, but since total N movers on N spots, if overlap then some spot empty, but wait.
    # Anyway, but in our code if N=1e6, E=1e6, but constraint E<=1000, so E<=1000, N>=E, N=1e6 but E=1000 so |S|=1000, looping over 1000 is fine, but if S full only when E=N but N<=1000 then since constraint for 40pts N<=100 but anyway, since E<=1000 always in constraints, our O(E^2) =1e6 is always fine. Never have to list all N.
    
    # Because when S is not full, the number of possible t for cw is at most E (number of possible images for a0), so possible_cw has size <=E.
    # Same for ccw. Intersection <=1000.
    # Perfect.
    
    # Now, if one group is empty, say no B, all in A, then possible_ts = possible_cw, which are the t where A + t subset S, but since sizes equal, A + t == S as set.
    # Then since no B, no overlap to check, so all such t are valid.
    # Then we take the min t >0 in possible_ts, or if only 0 then N.
    
    # Yes, for example if all have same direction, the t's are the periods where shifting the set A by t gives back the same set A (since S=A).
    # Yes, exactly the rotational symmetries of the set.
    # In first sample all d=1, A={1,2,4,5}, B-empty.
    # Then possible t: those where {1+t,2+t,4+t,5+t} %6 == {1,2,4,5}
    # As we saw t=3 works, also t=0, and t=6%6=0.
    # Does our code find t=3?
    # a0=1 (assume sorted but doesn't matter), S={1,2,4,5}
    # For s=1, t=(1-1)%6=0, then check A+0 = same, yes.
    # s=2, t=(2-1)%6=1, then A+1={2,3,5,0}, is {0,2,3,5} == {1,2,4,5}? No, and in check: for a=4, 4+1=5 in S yes; a=5:5+1=6%6=0 in S? 0 not in S, so good=False. Not added.
    # s=4, t=(4-1)%6=3, A+3 = {1+3=4,2+3=5,4+3=7%6=1,5+3=8%6=2} = {4,5,1,2} all in S yes. So t=3 added.
    # s=5, t=(5-1)%6=4, A+4={5,6%6=0,8%6=2,9%6=3}={5,0,2,3} , 0 not in S, rejected.
    # So possible_ts = {0,3}, then candidates 3, min=3. Perfect.
    
    # Another sample 2: as above, only {0}, so ans = 3. Perfect.
    
    # Now for mixed directions.
    # Let's see the third sample.
    # N=8 E=6
    # indians:
    # 2 -1 → pos1 d=-1
    # 3 1 →2, +1
    # 4 -1 →3,-1
    # 6 1 →5,+1
    # 7 -1 →6,-1
    # 8 1 →7,+1
    # So A (cw +1): 2,5,7
    # B (ccw -1): 1,3,6
    # S = {1,2,3,5,6,7}
    # Output 4.
    
    # At t=4, cw: 2+4=6, 5+4=9%8=1, 7+4=11%8=3 → {6,1,3}
    # ccw: 1-4=-3%8=5, 3-4=-1%8=7, 6-4=2 → {5,7,2}
    # Union {6,1,3,5,7,2} = {1,2,3,5,6,7} yes.
    # And disjoint yes.
    
    # Our code should find t=4 among others maybe 0.
    
    # Perfect.
    
    # Now, if N even, inv of 2 exists? But we don't need.
    
    # Now implement carefully with % N.
    
    # Also if E=1, works.
    
    # If all positions, but E<=1000, if N=3 E=3, all positions occupied, then for any t, since S={0,1,2}, any landing is in S, so possible t all 0,1,2.
    # Then if there are both cw and ccw, we need to check for t=1,2 if the landed from cw and ccw don't overlap.
    # Since 3 positions,  if |A|=2,|B|=1 say, then if they land on different, ok.
    # Since full, as long as no two land on same spot, which since 3 movers on 3 spots, equivalent to no overlap.
    # The dance would stop at t=1 if after one step the occupied are still all 3 (which they are).
    # Yes makes sense.
    
    # Now, one more: the problem says the dance ends when the toras occupied are the same, NOT considering the directions.
    # And in our model it matches.
    
    # Also in the collision, as we argued, the positions are the same as pass-through.
    # But is there a case where multiple on same tora?
    # Yes if a cw and ccw land on same, then in real they collide and reverse, but in positions, two on same tora.
    # In that case the occupied set has size <E, so different from initial unless initial had multiples but it doesn't.
    # In our check, when they overlap we discard that t, which is correct because set would have size <E.
    # In the real physics, when two collide on same, they both stay there (according to description), so yes two on one tora, set size decreases.
    # Yes.
    
    # The second rule about not jumping if adjacent towards each other: in pass through it also matches as we saw earlier.
    
    # The note also matches.
    
    # So this is correct.
    
    # Great!
    
    # Now code it.
    # We need to find the MINIMAL positive t.
    # So we collect all valid t in 1 to N-1 that work, take min, if none then N.
    
    # Since possible_ts has only few, we can iterate.
    
    # But t= N is equivalent to t=0.
    # So if no other, answer N.
    
    # Is it possible that there is no smaller and N is the answer, yes.
    # Is it possible answer >N? No, because at N it returns.
    
    # Yes.
    
    # Let's implement.
    
    # To avoid large sets if N small, but since we use %N and sets of size 1000 ok.
    
    # S as set for O(1) lookup.
    
    # list_A and list_B as lists.
    
    # If list_A and list_B both empty, not happen.
    
    # If one empty, as above, the possible_ts will be set by the non-empty one, and since no other group, we don't intersect, and for overlap check, if one is empty then no overlap possible.
    
    # So in code for checking overlap, if one list empty, always disjoint.
    
    # Yes.
    
    # Let's write the code.
    
S = set()
A = []
B = []

# after reading
for p, d in indians:
    if d == 1:
        A.append(p)
    else:
        B.append(p)
    S.add(p)

# now
possible = None
if A:
    poss_a = set()
    if A:  # redundant
        a0 = A[0]
        for s in S:
            t = (s - a0) % N
            good = True
            for a in A:
                if ((a + t) % N) not in S:
                    good = False
                    break
            if good:
                poss_a.add(t)
    possible = poss_a

if B:
    poss_b = set()
    b0 = B[0]
    for s in S:
        t = (b0 - s) % N
        good = True
        for b in B:
            if ((b - t) % N) not in S:
                good = False
                break
        if good:
            poss_b.add(t)
    if possible is None:
        possible = poss_b
    else:
        possible = possible.intersection(poss_b)

if possible is None:
    # no indians
    print(0)
    sys.exit()

# now possible has all t mod N where all land in S
# find the smallest t > 0 that also has no overlap between A+t and B-t

ans = N
for t in possible:
    if t == 0:
        continue
    # check if A+t and B-t disjoint
    positions_a = {(a + t) % N for a in A}
    overlap = False
    for b in B:
        pos = (b - t) % N
        if pos in positions_a:
            overlap = True
            break
    if not overlap:
        ans = min(ans, t)

print(ans)

# Yes! This should work.
# In the all cw case, it works as shown.
# If both groups, for t=4 in sample 3, it should be found because when we map one from A or from B it will discover t=4 as possible for both groups.
# For example, take a0=2, s=6, t=(6-2)%8=4, then check other A: 5+4=9%8=1 in S, 7+4=11%8=3 in S yes. So 4 in poss_a.
# For B, b0=1, for s=5, t=(1-5)%8 = (-4)%8=4, then check other b: for b=3, 3-4=-1%8=7 in S yes; b=6:6-4=2 in S yes. So 4 in poss_b.
# Thus 4 in intersection. Then when checking overlap, positions_a at t=4: {6,1,3}, then B-t:5,7,2 none in {1,3,6}, good. So ans=min(N,4)=4.
# Perfect.
# If there were a smaller t, it would take it.
# If only 0, ans remains N.
# Excellent.
# Time: O(E^2) for generating possible (2 * E * E = about 2e6), then for checking candidates <=E times, each O(E) so another 1e6, total fine for python even with N=1e6.
# Memory fine.
# Edge case: E=1, works.
# E=N=3 all filled with mixed dir, will find smallest t=1 if no overlap at t=1.
# If at t=1 there is overlap between a cw and ccw, then that t=1 would be in possible (since S full), but overlap=True so discarded, then maybe t=2 etc.
# Yes correct, because if two land on same at t=1, then occupied positions <3.
# Yes.
# Another edge: N=3, E=2.
# Suppose positions 1 and 2, dirs 1 and -1.
# S={0,1} wait 0-based pos 0 and 1.
# Then A=[0], B=[1]
# possible for A: a0=0, for s=0 t=0, for s=1 t=1.
# For t=0: ok.
# For t=1: A+1={1}, 1 in S yes.
# For B: b0=1, for s=0: t=(1-0)%3=1, then B-t=1-1=0 in S yes.
# for s=1: t=(1-1)%3=0, B-t for t=0:1 in S.
# So possible = {0,1} intersection.
# Now for t=1: positions_a = (0+1)%3=1
# B-t=(1-1)%3=0
# {1} and {0}, disjoint? yes.
# So ans=1.
# What happens physically: indian at 0 going +1 (to 1), indian at 1 going -1 (to 0).
# They are consecutive and moving towards each other, so according to rule 2, they both stay, reverse directions.
# After one step: still at 0 and 1, but directions reversed.
# So occupied toras same! Yes, so dance ends after 1 batida. Correct.
# In our model: at t=1 positions would be 0+1=1, 1-1=0, same positions. Yes.
# Perfect.
# Another case where they collide in middle: N=4, A at 0 d=1, B at 2 d=-1. S={0,2}
# Then possible t:
# For A a0=0, s=0 t=0; s=2 t=2.
# t=0: ok.
# t=2: 0+2=2 in S yes.
# For B b0=2, s=0: t=(2-0)%4=2, then for b=2, 2-2=0 in S yes.
# s=2 t=(2-2)=0, ok.
# So possible {0,2}
# For t=2: A+2={2}, B-2={2-2=0}, so positions 2 and 0, which is S, disjoint yes.
# So ans=2.
# Physically: at t=1, from 0->1, from 2->1, both go to 1, collide, both at 1, reverse dir, so now two at position 1, occupied={1} != {0,2}.
# At t=2, each at 1, now directions reversed so the one that was cw now ccw, from 1 goes to 0, the one that was ccw now cw goes to 2. So end at 0 and 2. Yes back.
# Our model directly at t=2: 0+2=2, 2-2=0, same.
# Perfect.
# So the model works even when there are intermediate collisions.
# Awesome.
# This is the way.
# Now write the code cleanly.

import sys

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1
E = int(data[index])
index += 1

indians = []
for i in range(E):
    V = int(data[index])
    index += 1
    D = int(data[index])
    index += 1
    indians.append((V-1, D))

A = []
B = []
S = set()

for p, d in indians:
    S.add(p)
    if d == 1:
        A.append(p)
    else:
        B.append(p)

possible = None
if A:
    poss_a = set()
    a0 = A[0]
    for s in list(S):
        t = (s - a0) % N
        good = True
        for a in A:
            if (a + t) % N not in S:
                good = False
                break
        if good:
            poss_a.add(t)
    possible = poss_a

if B:
    poss_b = set()
    b0 = B[0]
    for s in list(S):
        t = (b0 - s) % N
        good = True
        for b_pos in B:
            if (b_pos - t) % N not in S:
                good = False
                break
        if good:
            poss_b.add(t)
    if possible is None:
        possible = poss_b
    else:
        possible = possible & poss_b

if not possible:
    print(N)
    sys.exit(0)

ans = N
for t in possible:
    if t == 0:
        continue
    # check overlap
    pos_a = {(a + t) % N for a in A}
    overlap = any(((b - t) % N in pos_a) for b in B)
    if not overlap:
        if t < ans:
            ans = t

print(ans)
