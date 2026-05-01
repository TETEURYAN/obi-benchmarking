import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    energies = sorted(int(data[i+1]) for i in range(n))
    
    # The minimum dissonance is achieved by arranging songs in sorted order
    # and then connecting them in a way that minimizes total variation.
    # 
    # Key insight: When songs are sorted, the optimal arrangement is to
    # place them in a "zigzag" or interleaved pattern.
    # 
    # Actually, the classic result: for a cyclic arrangement minimizing
    # sum of |a[i] - a[i+1]|, the optimal is to sort and then interleave
    # (place even-indexed elements first, then odd-indexed in reverse, or similar).
    # 
    # But let's think more carefully. With sorted array, if we arrange them
    # in sorted order cyclically: cost = 2*(max - min) since we go up and come back.
    # Wait no: sorted order gives cost = (e[n-1] - e[0]) going up + (e[n-1] - e[0]) coming back
    # = 2*(e[n-1] - e[0]).
    # 
    # Actually for sorted array a[0] <= a[1] <= ... <= a[n-1]:
    # cyclic sum = sum|a[i]-a[i+1]| for i=0..n-2 + |a[n-1]-a[0]|
    # = (a[n-1]-a[0]) + (a[n-1]-a[0]) = 2*(a[n-1]-a[0])
    # 
    # Can we do better? The minimum possible dissonance for a cyclic arrangement
    # of sorted values is 2*(max - min). This is because in any cyclic arrangement,
    # the sum of absolute differences >= 2*(max - min) (since we must go from min to max
    # and back at least once).
    # 
    # Wait, but test case 1: energies = [15, 20, 20, 60, 80]
    # 2*(80-15) = 130. Output is 130. Correct!
    # 
    # Test case 2: energies = [20, 30, 95]
    # 2*(95-20) = 150. Output is 150. Correct!
    # 
    # Test case 3: energies = [0,0,0,0,0,1,1,1,1] (five 0s and four 1s)
    # 2*(1-0) = 2. Output is 2. Correct!
    # 
    # So the answer is simply 2*(max - min).
    
    print(2 * (energies[-1] - energies[0]))

solve()