import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    K = int(input_data[idx]); idx += 1
    U = int(input_data[idx]); idx += 1
    
    cartelas = []
    for i in range(N):
        nums = set()
        for j in range(K):
            nums.add(int(input_data[idx])); idx += 1
        cartelas.append(nums)
    
    sequence = []
    for i in range(U):
        sequence.append(int(input_data[idx])); idx += 1
    
    # For each card, find when it gets completed
    # completion_round[i] = the index (1-based) of the draw that completes card i
    
    # Build position map: number -> draw position (1-based)
    pos = {}
    for i, num in enumerate(sequence):
        pos[num] = i + 1
    
    completion = []
    for i, cartela in enumerate(cartelas):
        # The card is completed when the last of its numbers is drawn
        last_draw = max(pos[num] for num in cartela)
        completion.append((last_draw, i + 1))
    
    min_draw = min(c[0] for c in completion)
    winners = [c[1] for c in completion if c[0] == min_draw]
    winners.sort()
    
    print(' '.join(map(str, winners)))

main()